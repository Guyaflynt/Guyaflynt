#!/usr/local/epd-7.2-2-rh5-x86_64/bin/python

'''
Tornado Composite Parameter

This code is made for a simplefied way for anyone to interept the condidtions for the atmosphere. Each parameter is scaled so that it will add up to 100, or 100 perecent. The parameters being based mostly on pivotal weather. However, most of these parameters in this list can be found online, or they are alterations to the code. The tornado parameters are CAPE (J/kgK), LI (C), CIN, Shear, storm relative helicity, engergy helicity index, TT, K, lapse rates. 


Will later make a alteration to the code if the location is in the southeast. 

Mostly consists of what is question, the compare the values of the parameter that will then connect to a number. For example if the value
'''

#Import external modules
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


print "Welcome to the TCP number for the chance for tonradoes. Below you will enter your numbers and see the results, please go to pivotal weather for your numbers. "
EHI01= 0.0
EHI03= 0.0
EHI06= 0.0
MLCAPE= 0.0
MUCAPE= 0.0
SFCCAPE= 0.0
Lapse75= 0
shear01= 0
shear03= 0
shear06= 0
shear08= 0
SRH01= 0
SRH03= 0
BRS= 0
CINSFC= 0
CINML= 0
LISFC= 0
LIML= 0
Kindex= 0
TT= 0
SCP= 0
STP= 0




TCP= 0.0


#Use the number from pivotal and enter here, below will print out the number adding to 100 EHI01
print 'EHI = Energy-Helicity Index. The basic premise behind EHI is that storm rotation should be maximized when CAPE is large and SRH is large. 0-1 km EHI values greater than 1-2 have been associated with significant tornadoes in supercells (SPC).'

EHI01= float( raw_input( "what is the EHI 0-1 km that you found?: "))
#The range of numbers are based off some reaserach and combining the ranged values the spc and other sources have provided.Both EHI01 and EHI03 are worth 5%, with the highest possible value being 5.  
if EHI01 <= 0.8:	
	print "Low CAPE or storm relative helicity"
	EHI01= 0
elif 0.9 <= EHI01 <= 2.4:
	print 'Decent CAPE or storm relative helicity'
	EHI01= 1.0
elif 2.5 <= EHI01 <= 3.5:
	print 'Large CAPE or storm relative helicity'
	EHI01= 3.0
elif EHI01 >= 3.6:
	print "Major CAPE or storm relative helicity"
	EHI01 = 5.0
else:
	sys.exit
print EHI01

print 'EHI = Energy-Helicity Index. The basic premise behind EHI is that storm rotation should be maximized when CAPE is large and SRH is large. 0-1 km EHI values greater than 1-2 have been associated with significant tornadoes in supercells (SPC).'	
EHI03= float( raw_input( "what is the EHI 0-3 km that you found?: "))

if EHI03 <= 0.8:
	print "Low CAPE or storm relative helicity"
	EHI03= 0
elif 0.9 <= EHI03 <= 2.4:
	print 'Decent CAPE or storm relative helicity'
	EHI03= 1.0
elif 2.5 <= EHI03 <= 3.5:
	print 'Large CAPE or storm relative helicity'
	EHI03= 3.0
elif EHI03 >= 3.6:
	print "Major CAPE or storm relative helicity"
	EHI03 = 5.0
else:
	print "next"
print EHI03


# Mixed layer, most unstable, and surface convective aviable potential energy are all worth 7% out of 100. The reason they are worth this amount is due the need of the energy.  The following three question will provide a description of what each parameters are, and what the value of each parameter mean. 

print 'CAPE = Convective Available Potential Energy. CAPE is a measure of instability through the depth of the atmosphere, and is related to updraft strength in thunderstorms (SPC).'

print 'Mixed layer CAPE is the mean conditions in the lowest 100 milibars (SPC).'

MLCAPE= float( raw_input( "what is the MLCAPE that you found?: "))

if MLCAPE <= 200:
	MLCAPE= 0 
	print 'Tornadoes unlikely'
elif 201 <= MLCAPE <= 999.0:
	print 'CAPE is still to low regarding to climateology of tornadoes, but is till enough in certain regions.'
	MLCAPE= 2.0
elif 1000.0 <= MLCAPE <= 2999.0:
	print 'Atmosphere is unstable. Enough CAPE for tornadoes.'
	MLCAPE= 4.0
elif MLCAPE >= 3000.0:
	print 'Atmosphere is highly unstable,' 
	MLCAPE= 7.0
else:
	print 'next'
print MLCAPE

print 'Most unstable means the most unstable parcel found in the lowest 300 milibar of the atmosphere (SPC).'

MUCAPE= float( raw_input( "what is the MUCAPE that you found?: "))

if MUCAPE <= 200:
	MUCAPE= 0
	print 'Tornadoes unlikely'
elif 201 <= MUCAPE <= 999.0:
	print 'CAPE is still to low regarding to climateology of tornadoes, but is till enough in certain regions.'
	MUCAPE= 2.0
elif 1000.0 <= MUCAPE <= 2999.0:
	print 'Atmosphere is unstable. Enough CAPE for tornadoes.'
	MUCAPE= 4.0
elif MUCAPE >= 3000.0:
	print 'Atmosphere is highly unstable,' 
	MUCAPE= 7.0
else: 
	print 'next'
print MUCAPE

print 'Surface based'

SFCCAPE= float( raw_input( "what is the SFC CAPE that you found?: "))

if SFCCAPE <= 200:
	SFCCAPE= 0
	print 'Tornadoes unlikely'
elif 201 <= SFCCAPE <= 999.0:
	print 'CAPE is still to low regarding to climateology of tornadoes, but is till enough in certain regions.'
	SFCCAPE = 2.0
elif 1000.0 <= SFCCAPE <= 2999:
	print 'Atmosphere is unstable. Enough CAPE for tornadoes.'
	SFCCAPE= 4.0
elif SFCCAPE >= 3000.0:
	print 'Atmosphere is highly unstable,' 
	SFCCAPE= 7.0
else:
	print 'next'
print SFCCAPE


Lapse75= float( raw_input( "what is the 700-500 lapse rate that you found?: "))

if Lapse75 <= 5.9:
	Lapse75= 0
	print 'condtionally stable'
elif 6.0 <= Lapse75 <= 6.9:
	Lapse75= 1.0
elif 7.0 <= Lapse75 <= 7.9:
	Lapse75= 3.0
elif 8.0 <= Lapse75 <= 9.5:
	Lapse75= 5.0
else: 
	print 'next'
print Lapse75
shear01= float( raw_input( "what is the shear value between 0-1 km that you found?: "))

if shear01 <= 19:
	shear01= 0
	print 'low prob of tornadoes'
elif 20 <= shear01 <= 33:
	shear01= 1
elif 34 <= shear01 <= 49:
	shear01= 3
elif shear01 >= 50:
	shear01= 5
else:
	print 'next'
print shear01

shear03= float( raw_input( "what is the shear value between 0-3 km that you found?: "))

if shear03 <= 29:
	shear03= 0
	print 'low prob of tornadoes'
elif 30 <= shear03 <= 39:
	shear03= 1
elif 40 <= shear03 <= 54:
	shear03= 3
elif shear03 >= 55:
	shear03= 5
else:
	print 'next'
print shear03
shear06= float( raw_input( "what is the shear value between 0-6 km that you found?: "))

if shear06 <= 29:
	shear06= 0
	print 'low prob of tornadoes'
elif 30 <= shear06 <= 44:
	shear06= 1
elif 45 <= shear06 <= 59:
	shear06= 3
elif shear06 >= 60:
	shear06= 5
else:
	print 'next'
print shear06
shear08= float( raw_input( "what is the shear value between 0-8 km that you found?: "))

if shear08 <= 29:
	shear08=0
	print 'low prob of tornadoes'
elif 30 <= shear08 <= 39:
	shear08= 0.5
elif 40 <= shear08 <= 49:
	shear08= 1
elif shear08 >= 50:
	shear08= 2
else:
	print 'next'
print shear08
SRH01= float( raw_input( "what is the storm relative helicity value between 0-1 km that you found?: "))

if SRH01 <= 149:
	SRH01= 0
	print 'low prob of tornadoes'
elif 150 <= SRH01 <= 230:
	SRH01= 1
elif 231 <= SRH01 <= 349:
	SRH01= 3
elif SRH01 >= 350:
	SRH01= 5
else: 
	print 'next'
print SRH01
SRH03= float( raw_input( "what is the storm relative helicity value between 0-3 km that you found?: "))

if SRH03 <= 149:
	SRH03= 0
	print 'low prob of tornadoes'
elif 150 <= SRH03 <= 299:
	SRH03= 1
elif 300 <= SRH03 <= 449:
	SRH03= 3
elif SRH03 >= 450:
	SRH03= 5
else: 
	print 'next'
print SRH03


BRS= float( raw_input( "what is the Bulk Richarson Shear value  that you found?: "))

if BRS > 45:
	BRS= 0
elif 20 <= BRS <= 45:
	BRS= 1
elif  10 <= BRS <= 19:
	BRS= 3
elif BRS <= 9:
	BRS= 2
else:
	sys.exit
print BRS


LISFC= float( raw_input( "what is the LI at the surface value that you found?: "))

if LISFC > 0:
	LISFC= 0
elif 0 >= LISFC >= -2.0:
	LISFC= 1
elif -3 >= LISFC >= -4:
	LISFC= 2
elif LISFC <= -5:
	LISFC= 3
else:
	sys.exit

print LISFC

LIML= float( raw_input( "what is the LI mixed layer value that you found?: "))

if LIML > 0:
	LIML= 0
elif 0 >= LIML >= -2.0:
	LIML= 1
elif -3 >= LIML >= -4:
	LIML= 2
elif LIML <= -5:
	LIML= 3
else:
	sys.exit

print LIML

CINSFC= float( raw_input( "what is the CIN value at the surface that you found?: "))

if CINSFC >= -9:
	CINSFC= 0
elif -10 >= CINSFC >= -89:
	CINSFC= 1
elif -90 >= CINSFC >= -190:
	CINSFC= 2
elif -191 >= CINSFC >= -350:
	CINSFC= 3
else:
	sys.exit
print CINSFC

CINML= float( raw_input( "what is the CIN mixed layer value that you found?: "))

if CINML >= -9:
	CINML= 0
elif -10 >= CINML >= -89:
	CINML= 1
elif -90 >= CINML >= -190:
	CINML= 2
elif -191 >= CINML >= -350:
	CINML= 3
else:
	sys.exit
print CINML

Kindex= float( raw_input( "what is K index that you found?: "))

if Kindex <= 19:
	Kindex= 0
elif 20 <= Kindex <= 25:
	Kindex= 0.5
elif 26 <= Kindex <= 30:
	Kindex= 1
elif 31 <= Kindex <= 35:
	Kindex= 2
elif Kindex >= 35:
	Kindex= 3
else:
	print 'next'
print Kindex

TT= float( raw_input( "what is the TT that you found?: "))

if TT < 44:
	TT= 0
if 44 <= TT <= 50:
	TT= 0.5
if 51 <= TT <= 52:
	TT= 1
if 53 <= TT < 56:
	TT= 2
if TT >= 56:
	TT= 3
else:
	print 'done'
print TT


SCP= float( raw_input( "what is the SCP value?:"))

if SCP < 3:
	SCP= 0
elif 3 <= SCP < 6:
	SCP= 2
elif 6 <= SCP < 10:
	SCP= 4
elif 10 <= SCP < 15:
	SCP= 6
elif SCP >= 15:
	SCP= 8
else:
	print 'stop'

print SCP

STP= float( raw_input( "what is the STP value?: "))

if STP < 0.5:
	STP= 0
elif 0.5 <= STP < 1.5:
	STP= 2
elif 1.5 <= STP < 2.5:
	STP= 4
elif 2.5 <= STP <= 3.5:
	STP= 6
elif STP >= 3.6:
	STP= 8
else:
	print 'stop'

print STP


TCP= EHI01 + EHI03 + MUCAPE + MLCAPE + SFCCAPE + Lapse75 + shear01 + shear03 + shear06 + shear08 + 	SRH01+ SRH03 + BRS + CINSFC + CINML + LISFC + LIML + Kindex + TT + SCP + STP
print TCP

