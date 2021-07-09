'''
Modified verification.py
This script reads and processes grib files containing SPC day 1 convective outlooks ending at 1200 UTC. File
types include wind, hail, torn, sigwind, sighail, sigtorn. Grid points are spaced every 5 km. The categorical
forecast values are:
2 = GEN-TSTM
3 = MARGINAL
4 = SLIGHT
5 = ENHANCED
6 = MODERATE
8 = HIGH
Note: MARGINAL and ENHANCED were not introduced until late 2014.

Forecast periods end at 1200 UTC. For example, the forecasts on the 22nd day of the month cover the following
periods:
220100-221200
221200-231200
221300-231200
221630-231200
222000-231200

Storm reports are derived from the data at http://www.spc.noaa.gov/wcm/#data. These reports may not match the
reports on the SPC Storm Reports page because of post-processing at the SPC. This is out of our control.

The goal of this script is to compare SPC forecasts with observed storm reports and to
produce summary statistics for use in forecast verification.

*** To run: Use ./runverif.py *ONLY* ***

G. A. Flynt
Nov 2020
'''

#******************
# USER MODIFICATION
#******************

fcst_times=['1200']				        #All of the SPC convective outlook forecast times
years=['2019']					#List of years to analyze
ftypes=['hail', 'torn', 'wind', 'sigwind']	#SPC convective outlook forecast types (CONTROLLED BY RUNVERIF.PY!!)
testrun=False														#True: Use only five SPC data files to test the code; False: Operational
ntestfiles=5														#Number of SPC files to read if testrun=True
verbose=False														#True: Print status messages and various data values; False: Operational
adjgrid=True														#True: Verify adjacent grid pts per SPC forecast definition; False: Verify only the nearest grid pt
adjpts=9															#Grid point distance in all directions verified by an adjacent observation
																	# (~9 for a 5-km grid and 25 mi (40.2336 km) from a point; checked by distance calc)
withindist=40.2336													#SPC forecast scale (in km; i.e., 25 miles of a point = 40.2336 km --> 80.5 km grid)

distdir=r'C:/Users/gaflynt/Anaconda3/THESIS/Utl/'									#The location of the Sodano distance calculator (Python)
#******************
#******************
#Define a function for finding the nearest lat/lon coordinates to a point on an irregular 2-D grid
def find_indices_original(points,lon,lat,tree=None):
	#This is used when calculating the binary decision tree repeatedly (which is REALLY slow!)
	if tree is None:
		lon,lat = lon.T,lat.T
		lonlat = np.column_stack((lon.ravel(),lat.ravel()))
		tree = sp.spatial.cKDTree(lonlat)
	dist,idx = tree.query(points,k=1)
	ind = np.column_stack(np.unravel_index(idx,lon.shape))
	return [(i,j) for i,j in ind]

def find_indices(points,lon,lat,tree):
	#This is used when using the binary decision tree from maketree(). This is MUCH faster!
	lon,lat = lon.T,lat.T
	dist,idx = tree.query(points,k=1)
	ind = np.column_stack(np.unravel_index(idx,lon.shape))
	return [(i,j) for i,j in ind]

def maketree(lon,lat):
	#Create a binary decision tree
	lon,lat = lon.T,lat.T
	lonlat = np.column_stack((lon.ravel(),lat.ravel()))
	tree = sp.spatial.cKDTree(lonlat)
	return tree

print ("IMPORTING PYTHON PACKAGES...")
import os, string, sys
import matplotlib							#Use matplotlib for drawing figures and using speedy arrays
import pygrib 
matplotlib.use('Agg')						#Prevent need for a X server
from pylab import *
from numpy import ma
import numpy as np							#Needed for NumPy array operations
import glob
import scipy as sp 
from scipy.interpolate import interp1d
from scipy.interpolate import interpolate  
import csv
import string 
import pytz
from datetime import datetime as dt, timedelta
import time
import gc

print("IMPORTING CUSTOM PACKAGES...")
sys.path.insert(0,distdir)
from sodano import *

'''
#Get the forecast type from runverif.py (the driver for this program)
allftypes=list(ftypes)
ftypes=[sys.argv[1]]
if ftypes[0] not in allftypes:
    print("ERROR 210: "+ftypes[0]+" is not a valid forecast type!")
    sys.exit()
print("ftypes: ",ftypes)
'''

#Create output file and write header (file name shows verification grid size)
contout=open("contingency_adjpts"+str(adjpts)+"_2019_"+ftypes[0]+".dat","w")	#Open output file for contingency table and other data for each forecast period
print ("YYYYMMDDHHMM ; type ; a; b; c; d", file= contout)

#Create output file for annual totals of forecasts/observations
#annver=open("annual_adjpts"+str(adjpts)+"_"+ftypes[0]+".verif","w")
#print ("YEAR; type; time; fprob : nfcst, nobs; [repeat last item for all forecast probabilities]", file= annver)

wrongcoords= open("wrongcordcat.dat", "w")
print("filename", file=wrongcoords)

gotlatlon=False
verif={}
verif_date={}

print ("READING OBSERVATIONS...")
reports={}
reports['torn']={}
reports['hail']={}
reports['wind']={}
#wheres the data file
files= glob.glob("2019reports/*.csv")
for file in files:
    #print(file)
    #stop
    with open(file, 'r') as excelfile:
        ftype= file[-8:-4]
        print(ftype)
        lines= excelfile.readlines()
        lines.pop(0)
        reporttime= []
        magn= []
        startlat= []
        startlon= []
        #numreports= []
        for line in lines: 
            colms= line.split(',')
            #print(colms)
            daymonyr=colms[4].split('/')
            #print(daymonyr)
            hms=colms[5].split(':')
            #print(hms)
            mon=int(daymonyr[0])
            #print(mon)
            day=int(daymonyr[1])
            yr=int(daymonyr[2])
            hour=int(hms[0])
            minute=int(hms[1])
            sec=int(hms[2])
            #print(yr, mon, day, hour, minute, sec)
            #stop
            d=datetime.datetime(yr,mon,day,hour,minute,sec) #The naive date/time
            #print(d)
            zone=colms[6]
            #stop
            #Dealing with time
            if zone.strip()=='?':
                print("ERROR 382: What's the time zone?")
                print(zone,d)
                sys.exit()
            else:
                zone=int(zone)
            if zone==9:
                #Time zone is GMT. Make no adjustment.
                local=pytz.timezone("UTC")
            elif zone==3:
                #Time zone is Central Standard Time. Convert to GMT.
                #tzoffset=6 #Offset is *always* 6 hours for CST
                #d=d+timedelta(hours=tzoffset) #Add tzoffset hours
                #local=pytz.timezone("UTC")
                central= pytz.timezone('US/Central')
            else:
                print ("ERROR 219: Unknown time zone: ",zone)
                sys.exit()
                
            #local_dt=local.localize(d,is_dst=None)
            #utc_dt=local_dt.astimezone (pytz.utc)
            cst_dt= central.localize(d)
                #if testrun and verbose: print "UTC date: ",utc_dt
            
            #Create the UTC date/time key
            fulldate=cst_dt.strftime('%Y%m%d%H%M') #Convert date to YYYYMMDDHHMM format
            
            #Break up the date/time and create data lists
            date=fulldate[0:8]
            #print(date)
            if not (date in reports[ftype]):
                rpttime=[]
                magn=[]
                strtlat=[]
                strtlon=[]
                #numreports= []
            rpttime.append(fulldate[8:12])
            #print(rpttime)
            magn.append(float(colms[10]))
            strtlat.append(float(colms[15]))
            strtlon.append(float(colms[16]))
            #numreports.append(float(colms[28]))
            #print(numreports)
            #print(date)
            reports[ftype][date]= [rpttime,magn,strtlat,strtlon]
            
            #print(reports[ftype][date][0])
            
#stop       
###########################################################################
#Read and verify forecasts
###########################################################################           
         
print("READING AND VERIFYING FORECASTS...")
path= r'C:/Users/gaflynt/Anaconda3/THESIS/2019_Grib2_files/'#Location of SPC convective outlook files
#dirs = os.listdir(path)
#files= dirs
for ftime in fcst_times:
    print(ftime)
    #fcast[ftime]={}
    for ftype in ftypes:
        #print ftype
        #fcast[ftime][ftype]={}
        if ftype=="torn": select='Tornado probability'
        elif ftype=="hail": select='Hail probability'
        elif ftype=="wind": select='Wind probability'
        elif ftype=="sigtorn": select= 'Significant Tornado probability'
        elif ftype=="sighail": select= 'Significant Hail probability'
        elif ftype=="sigwind": select= 'Significant Wind probability'
        else:
            print("ERROR 25: Unknown forecast type.")
            print(ftype)
            sys.exit()
#year
        for year in years:
            try:
                obs.clear()		#Free up some memory
            except:
                pass
            obs={}
            gc.collect()
            
            #Read forecasts for the entire year for this ftype and ftime
            #print year
            #data files
            files=glob.glob(path+ftype+"_day1_grib2_"+ftime+"_"+year+"*")
            #print(path,ftype,ftime,year)
            #print(files)
            if testrun:
                files=files[0:ntestfiles]
                print(files)

#insert comment
            fname=[]
            i=-1
            for spcfile in files:
                #print(spcfile)
                i+=1
                #print(i,spcfile)
            
                if i==0: fname.append(spcfile) 
                    
                else:
                    thiscotime=dt.strptime(spcfile[-14:],'%Y%m%d%H%M%S') #Convert the date to a datetime object
                    lastcotime=dt.strptime(fname[i-1][-14:],'%Y%m%d%H%M%S') #Convert the date to a datetime object
                    tdiff=thiscotime - lastcotime
                    hourdiff=(tdiff.days)*24+(tdiff.seconds)/3600.
                    #print hourdiff

                    if hourdiff < 6:
                        #If the time difference between same-time outlooks is less than 6 hours, the
                        #second file is likely an amendment and should replace the first outlook. See
                        #torn_day1 20110113/20110114 as an example.
                        if verbose: print(spcfile+" is an amendment of "+fname[i-1]+". Replacing this outlook with the amendment.")
                        fname[i-1]=spcfile
                        i-=1
                        
                    elif hourdiff >= 6 and hourdiff <= 12:
                        print("ERROR 562: Time difference between successive same-time outlooks is between 6 and 12 hours. Uh...")
                        print (spcfile)
                        print (fname[-1])
                        sys.exit()
                        
                    else:
                        fname.append(spcfile) 
            files=list(fname)
            #print(files)
            #print(sorted(files))    
            
            #**********************************************
            #Verify the forecast in each convective outlook
            #**********************************************
            for file in sorted(files):
                #print("Opening ",file)
                grib=file
                #print(grib)
                grbs=pygrib.open(grib)
                #print(grbs)
                grb=grbs.select(name=select)[0]
                data=grb.values
                lat,lon=grb.latlons()
                #print(data,lat,lon)

                #Grab/save/check geographic coordinates
                if not gotlatlon:
                    #Save latlon coords
                    lats=lat
                    lons=lon
                    gotlatlon=True
  
                    #Make the binary tree for finding the nearest grid point to a specified point
                    #(see https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.html for refs)
                    print("Making the binary tree for the 2-D forecast grid. This may take a moment, but it's worth the wait...")
                    tree=maketree(lons,lats)        
                else:
                    #Check to make sure lat[X]==lats[X]; same for lon
                    #print "Shape of grid is: ",np.shape(lats)
                    examplex=234
                    exampley=123
                    if lats[examplex,exampley]!=lat[examplex,exampley] or lons[examplex,exampley]!=lon[examplex,exampley]:
                        print("ERROR 328: Geographic coordinates do not match!")
                        print("LATS: ",lats[examplex,exampley])
                        print("LAT: ",lat[examplex,exampley])
                        print("LONS: ",lons[examplex,exampley])
                        print("LON: ",lon[examplex,exampley])
                        #print(file, lats, lat, lons, lon)
                        print(file, file=wrongcoords)
                date=file[-14:-6]
                try:
                    fcast.clear()#Free up some memory rather than creating these dictionaries above and storing ALL the data
                except:
                    pass
                fcast={}
                gc.collect()
                fcast[ftime]={}
                fcast[ftime][ftype]={}
                fcast[ftime][ftype][year]={}
                fcast[ftime][ftype][year][date]=data
                
                #Create the observations dictionary for later
                if ftime not in obs:
                    obs[ftime]={}
                if ftype not in obs[ftime]:
                    obs[ftime][ftype]={}
                if year not in obs[ftime][ftype]:
                    obs[ftime][ftype][year]={}
                obs[ftime][ftype][year][date]=np.zeros(np.shape(lats)) #Makes array of zeros with same size as forecast grid

                
                #Create the verification dictionaries for later
                if ftype not in verif:
                    verif[ftype]={}
                if ftime not in verif[ftype]:
                    verif[ftype][ftime]={}

                if date not in verif_date:
                    verif_date[date]={}
                if ftype not in verif_date[date]:
                    verif_date[date][ftype]={}
                if ftime not in verif_date[date][ftype]:
                    verif_date[date][ftype][ftime]={}
                    
                ##################################################
                #Verify the forecasts
                ##################################################
                #For this forecast time, ftype, and year, count the number of hits and misses within the forecast period for each forecast value
                print("Verifying forecasts for ",date,ftype)
                
                nextdate=date #Initialize each forecast period to start and end on the same day
                
                #Check to see if there are reports at any time on the calendar days in the forecast period
                try:
                    nrpts=len(reports[ftype][date][0])
                    print(date, nrpts)
                    noreport=False
                    noreport_d1=False #Calendar day 1 reports
                except:
                    #There are no reports on this date...
                    noreport=True
                    noreport_d1=True #Calendar day 1 reports
                
                if ftime != '0100':
                    #The 0100 UTC forecasts end on the same calendar day, so we're good. Otherwise, get the next calendar day.
                    #newtime=dt.strptime(date,'%Y%m%d') #Convert the date to a datetime object
                    #newt=newtime+timedelta(days=1.0)  #Add a day
                    #nextdate=newt.strftime('%Y%m%d') #Convert new date to YYYYMMDD format
                    if verbose: print("Looking for the next date for the ",ftime,"UTC forecast time: ",nextdate)
                    
                    try:
                        nrpts=len(reports[ftype][date][0])
                        #print(nrpts,nextdate)
                        noreport=False
                        noreport_d1=False #Calendar day 2 reports
                        
                    except:
                        #...and there are no reports on the next calendar day.
                        noreport=True
                        noreport_d1=True #Calendar day 2 reports
                else:
                    #Reset switch for report existence on day 2 (otherwise, it's not set for 0100 UTC)
                    noreport_d2=False
                    
                if noreport:
                    #There are no storm reports for this forecast type during this forecast period.
                    if verbose: print("\tNo "+ftype+" observations on "+date+".") #No need to adjust anything else since the obs array is initialized with zeros.
                    #continue	#Continue the loop with the next forecast date..actually, don't. Continue on to print null dates.

                else:
                    #There is a report, so let's keep going.

                    ############
                    #NOTE: Your data are in fcst[ftime][ftype][year][date]
                    ############

                    #Determine the number of TOTAL reports on each calendar day in the forecast period
                
                    if date==nextdate:
                        #This applies to the 0100 UTC forecasts only
                        #nrpts=len(reports[ftype][date][0])
                        #print(nrpts)
                        print('cool')
                    else:
                        #This applies to all other forecast periods
                        #print "TESTING"
                        #print sorted(reports[ftype])
                        if not noreport_d1:
                            nrpts=len(reports[ftype][date][0])       #+len(reports[ftype][nextdate][0])
                            print(nrpts,date)
                            #print "There are ",len(reports[ftype][date][0]),ftype,"reports on this day and ",len(reports[ftype][nextdate][0],ftype,"reports on the next day."
                        elif noreport_d2:
                            #Count calendar day 1 reports only
                            nrpts=len(reports[ftype][date][0])
                        elif noreport_d1:
                            #Count calendar day 2 reports only
                            #nrpts=len(reports[ftype][date][0])
                            print("we just want the first day for ease")
                            
                        else:
                            print("ERROR 219: We shouldn't be here.")
                            print(date, nextdate, noreport_d1, noreport_d2)
                            sys.exit()
                            
                    #Here is the format of the reports dictionary: reports[ftype][date] = [rpttime,magn,strtlat,strtlon]
                    if verbose: print ("There are ",nrpts,ftype,"reports on the calendar days within the forecast period.")
                    try:
                        rptloc.clear() #Free up some memory rather than creating these dictionaries above and storing ALL the data
                    except:
                        pass
                    rptloc={}
                    gc.collect()

                    #Loop through each day in the forecast period
                    for rptdate in set([date,nextdate]): #Loops through unique date values only
                        
                        #Only consider a date if it has a report!
                        if rptdate==date and noreport_d1: continue
                        #if rptdate==nextdate and noreport_d2: continue

                        #Loop through all individual reports on each day
                        for r in range(len(reports[ftype][rptdate][0])):
                            #Grab individual report data for this date (the ith report)
                            rpttime=reports[ftype][rptdate][0][r]
                            #print(rpttime)
                            rptmag=reports[ftype][rptdate][1][r]
                            rptloc['lat']=reports[ftype][rptdate][2][r]
                            rptloc['lon']=reports[ftype][rptdate][3][r]
                            
                            #Find the nearest irregular 2-D grid point for the report location
                            indices=find_indices(np.asarray([rptloc['lon'],rptloc['lat']]),lons,lats,tree)
                            lat_idx=indices[0][1]
                            lon_idx=indices[0][0]

                            ##Only works with 1-D grid: Find the nearest latitude and longitude for report location
                            ##lat_idx = np.abs(lats - rptloc['lat']).argmin()
                            ##lon_idx = np.abs(lons - rptloc['lon']).argmin()
                            
                            #Testing
                            if testrun:
                                data=fcast[ftime][ftype][year][date] #Make shortened identifier for easier data access
                                print ("Report lat: ",rptloc['lat'])
                                print ("Report lon: ",rptloc['lon'])
                                print ("Indices: ",lat_idx, lon_idx)  #Lat/lon coordinate indices of nearest forecast grid point
                                print ("Grid coords: ",lats[lat_idx,lon_idx],lons[lat_idx,lon_idx]) #Coordinates of nearest forecast grid point
                                print ("Forecast: ",data[lat_idx,lon_idx]) #Value of forecast data at the nearest forecast grid point
                                print ("Shapes: ",np.shape(data),np.shape(lats),np.shape(lons)) #Shapes of arrays
                                #print "Date: ",date,"Nextdate: ",nextdate,"rptdate: ",rptdate
                                print

                            if testrun: print("REPORT TIME: ",rpttime,"DATE: ",rptdate,"\n----------------")
                            
                            #--------------------
                            #TEST: Verifies ~5-km grid spacing in entire NDFD CONUS 5-km domain
                            #print "Lat/lon grid size test:"
                            #print "original: ",lats[300,500],lons[300,500],"300,500"
                            #print "east: ",lats[300,501],lons[300,501],"501"
                            #print "west: ",lats[300,499],lons[300,499],"499"
                            #print "north: ",lats[301,500],lons[301,500],"301"
                            #print "south: ",lats[299,500],lons[299,500],"299"
                            #print "northeast: ",lats[301,501],lons[301,501],"301,501"

                            #print "original: ",lats[100,200],lons[100,200],"100,200"
                            #print "east: ",lats[100,201],lons[100,201],"201"
                            #print "west: ",lats[100,199],lons[100,199],"199"
                            #print "north: ",lats[101,500],lons[101,500],"101"
                            #print "south: ",lats[99,500],lons[99,500],"99"
                            #print "northeast: ",lats[101,201],lons[101,201],"101,201"
                            #--------------------
                            
                            
                            #Make sure that the report is within the forecast period (ending at 1200 UTC, exclusive). If so, count it.
                            countit=False
                            if ftime == "0100":
                                if (rptdate==date) and ((str(int(rpttime))) >= str(int(ftime))) and (str(int(rpttime) < 1200)):
                                    countit=True
                            else:
                                if ((rptdate==date) and ((str(int(rpttime))) >= str(int(ftime)))) or ((rptdate==nextdate) and (str(int(rpttime) < 1200))):
                                    countit=True
                            if verbose and not countit:
                                print("Excluding report on",rptdate,"at",rpttime,"because it falls outside the",ftime,"UTC forecast period on",date+".")

                            #Here are the i,j coordinates of the nearest grid point
                            i=lat_idx
                            j=lon_idx
                            
                            #Account for the more stringent criteria for significant events. Regular reports should NOT be counted in this case.
                            if countit:
                                if ftype=='sigtorn':
                                    #Magnitude values are -9 (unknown), 0, 1, 2, 3, 4, 5
                                    if string.int(rptmag) < 2:
                                        #Only count EF2 - EF5 tornadoes
                                        countit=False
                                if ftype=='sigwind':
                                    #Magnitude values are wind speed in knots
                                    if string.int(rptmag) < 65:
                                        #Only count winds of 65 kts or greater
                                        countit=False
                                if ftype=='sighail':
                                    #Magnitude values are hail size in inches
                                    if string.int(rptmag) < 2.0:
                                        #Only count hail with a diameter of 2 inches or greater
                                        countit=False
                                if verbose and not countit:
                                    print ("Excluding report on",rptdate,"at",rpttime,"from the "+ftype+" verification because it is not significant (magnitude="+rptmag+").")

                            if countit:
                                #Set the observed value for this grid point to unity
                                obs[ftime][ftype][year][date][i,j]=1
                                
                                
                                #NOTE: These cells only receive a single dichotomous value so that grid cells with
                                #multiple reports do not have more influence than a cell with a single report.
                                #This is similar to the analysis by Hitchens and Brooks (2012).
                                #if testrun: print "\tORIGINAL GRID COORDS: ",i,j
                                
                                if adjgrid:
                                    #Set adjacent 'adjpts' grid cells to unity if within 25 miles of the observation
                                    for igd in range(i-adjpts,i+adjpts+1):
                                        if igd < 1 or igd > len(lats)-1: continue
                                        for jgd in range(j-adjpts,j+adjpts+1):
                                            if jgd < 1 or jgd > len(lons)-1: continue
                                            
                                            #Check for the right grid distance tests at the selected SPC forecast scale (25 miles = 40.2336 km)
                                            if withindist > 40.234 or withindist < 40.233:
                                                print("*** WARNING: Distance tests assume a 5-km grid and SPC forecasts for")
                                                print(" within 25 miles of a point! withindist="+str(withindist)+"km")
                                                
                                            #The nearest 5x5 is always inside withindist (for 25 miles). Let's speed up the math!
                                            if abs(igd-i) <= 5 and abs(jgd-j) <= 5:
                                                obs[ftime][ftype][year][date][igd,jgd]=1
                                                #^This is redundant for the target grid point, but only if adjgrid==True
                                                #if testrun: print "\tINNER GRID COORDS: ",igd,jgd
                                            
                                            #The nearest 6x4 and 4x6 is also always inside withindist (for 25 miles).
                                            elif (abs(igd-i) <= 6 and abs(jgd-j) <= 4) or (abs(igd-i) <= 4 and abs(jgd-j) <= 6):
                                                obs[ftime][ftype][year][date][igd,jgd]=1
                                            
                                            else:
                                                #Calculate distance from the grid point to the observation (typically 25 mi/40.2336 km per the SPC) (in km)

                                                #Use the Python version of Sodano's inverse
                                                #Usage: dist,alpha12,alpha21=distance(ystart,yend,xstart,xend,3)
                                                #Note: The numpy.float64 data type has to be converted to a regular float with .item()
                                                #dist,alpha12,alpha21=distance(lats[igd,jgd].item(),lons[igd,jgd].item(),lats[i,j].item(),lons[i,j].item(),3)
                                                dist,alpha12,alpha21=distance(lats[igd,jgd],lats[i,j],lons[igd,jgd],lons[i,j],3)
                                            
                                                #Adjust obs array if grid cell is within appropriate distance
                                                if dist <= withindist:
                                                    obs[ftime][ftype][year][date][igd,jgd]=1

                                                    #if testrun: print "\tOUTER GRID COORDS: ",igd,jgd,dist
                                                #else:
                                                    #if testrun: print "\tEXCLUDED GRID COORDS: ",igd,jgd,dist
                                                    
                                                    
                ############################################################
                #***********************************************************
                #Define forecast/observation pair arrays on the lat/lon grid
                #***********************************************************
                #Probabilistic forecasts for this forecast time, forecast type, year, and date
                probs=fcast[ftime][ftype][year][date]

                #Observations (0=no, 1=yes) for this forecast time, forecast type, year, and date
                obsarr=obs[ftime][ftype][year][date] #This is defined at the completion of the previous loop
                #***********************************************************
                ############################################################
                
                try:
                    probset=np.unique(probs.compressed())	#Compressing removes the masked elements
                except:
                    probset=np.unique(probs)	#This must not be a masked array
                if testrun:
                    print("Here are the unique forecast probabilities for ",ftime,ftype,year,date)
                    print(probset)
                
                #Make sure we actually have a forecast for this date
                if len(probset)==0:
                    print("ERROR 913: The "+ftime+" UTC "+ftype+" forecast for "+date+" is completely missing!")
                    print ("\t We will need to account for storm reports on days with no forecasts. If we get")
                    print ("\t here, it means that there is no valid forecast on this day. In this case, there")
                    print ("\t are "+nrpts+" storm reports on "+date+". If there are zero storm reports as well,")
                    print ("\t then we will need to account for the valid set of no/no forecasts on this date in")
                    print ("\t the contingency table!")
                    sys.exit()
                           
                #Make an array of ones for counting
                ones=np.ones(np.shape(probs))

                for fprob in probset:
                    #For each forecast probability, count the number of forecasts
                    nfcst=np.sum(ones[(probs==fprob)])

                    #Testing
                    #for i in range(np.shape(lats)[0]):
                        #for j in range(np.shape(lats)[0]):
                    #if probs[i,j]==0.0:
                    #print "Hey! probs is equal to ",fprob,"! i,j=",i,j

                    #For each forecast probability, count the number of observations (conditional number of obs)
                    nobs=np.sum(obsarr[(probs==fprob)])
                           
                    if verbose:
                        print("There were ",nfcst,"forecasts with a ",fprob,"% probability.")
                        print("There were ",nobs,"observations with a ",fprob,"% forecast probability.")

                    #Create a new sub-dictionary if it's not already there
                    if fprob not in verif_date[date][ftype][ftime]:
                        verif_date[date][ftype][ftime][fprob]={}
                    if fprob not in verif[ftype][ftime]:
                        verif[ftype][ftime][fprob]={}
                    
                    #Save a two-item list of the number of forecasts and number of observations for each allowable forecast.
                    #We've got two here because we may or may not want to use the date.
                    verif_date[date][ftype][ftime][fprob]=[nfcst,nobs]
                    if not verif[ftype][ftime][fprob]:	#Empty dictionaries evaluate as false
                        verif[ftype][ftime][fprob]=[nfcst,nobs]	#Total nfcst,nobs for this type/time/prob (initial values)
                    else:
                        verif[ftype][ftime][fprob]=[verif[ftype][ftime][fprob][0]+nfcst,verif[ftype][ftime][fprob][1]+nobs]	#Total nfcst,nobs for this type/time/prob
                    
                #*****************************************************************************************************
                #Now add up contingency elements. Since we are considering probabilistic outlooks rather than
                #categorical outlooks, we will consider any non-zero forecast probability to be a 'yes' forecast.
                #*****************************************************************************************************

                #Make a forecast array of ones (yes) and zeros (no) from the probabilistic forecasts
                binfcst=np.zeros(np.shape(probs))
                binfcst[(probs > 0)]=1

                #a (fyes,oyes)
                a=np.sum(ones[(binfcst==1) & (obsarr==1)])

                #b (fyes,ono)
                b=np.sum(ones[(binfcst==1) & (obsarr==0)])

                #c (fno,oyes)
                c=np.sum(ones[(binfcst==0) & (obsarr==1)])

                #d (fno,ono)
                d=np.sum(ones[(binfcst==0) & (obsarr==0)])

                if testrun:
                    print("For",date,ftype,ftime,":")
                    print("\t\t a,b,c,d: ",a,b,c,d)

                #Print dates and contingency table values to file (as date+ftime;ftype;a b c d;...)
                # Old way of printing out data print >> contout, date+ftime,";",ftype,";",a,",",b,",",c,",",d,";",
                print(date+ftime,";",ftype,";",a,";",b,";",c,";",d, file= contout)
                #Print the number of forecast-observation pairs for each forecast (as ...fprob: nfcst,nobs)
                #for fprob in sorted(verif_date[date][ftype][ftime]):
                    # Old way of doing it print >> contout, fprob,":",verif_date[date][ftype][ftime][fprob][0],",",verif_date[date][ftype][ftime][fprob][1],";",
                 #   print(fprob,":",verif_date[date][ftype][ftime][fprob][0],",",verif_date[date][ftype][ftime][fprob][1],";", file= contout)
                # old way print >> contout
               

                #Do some garbage collection to free memory. Otherwise, Blizzard runs out of memory and kills the script!
                fcast.clear()
                verif_date.clear()
                obs.clear()
                fcast={}
                verif_date={}
                obs={}
                probs=-999
                obsarr=-999
                gc.collect()

            #Print annual totals
            # Old way of doing it print >> annver, year,";",ftype,";",ftime,";",
            #print(year,";",ftype,";",ftime,";", file= annver)
            #for fprob in sorted(verif[ftype][ftime]):
                # Old way of doing it print >> annver, fprob,":",verif[ftype][ftime][fprob][0],",",verif[ftype][ftime][fprob][1],";",
             #   print(fprob,":",verif[ftype][ftime][fprob][0],",",verif[ftype][ftime][fprob][1],";", file = annver)
            #Old way of doing it print >> annver
            #print(file= annver)

            #More garbage collection
            verif.clear()
            verif={}
            gc.collect()

print("...DONE...")    