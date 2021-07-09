#!/usr/bin/python2.7.13
######!/usr/local/epd-7.2-2-rh5-x86_64/bin/python

'''
runverif.py
This script drives verification.py with separate forecast types. This is
necessary because the memory required to analyze all forecast types together
overwhelms Blizzard. See verification.py for additional usage notes and
configuration options.

Run with:
./runverif.py &

C. Godfrey
20 August 2018
'''

import os

#******************
# USER MODIFICATION
#******************

#fcst_times=['0100','1200','1300','1630','2000']						#All of the SPC convective outlook forecast times
#years=['2011','2012','2013','2014','2015','2016']					#List of years to analyze
ftypes=['torn', 'hail', 'wind', 'sigwind', 'sighail', 'sigtorn']	#SPC convective outlook forecast types

#******************

#TEST BLOCK FOR SHORTENED USER MODS
#print "***  TESTING!!!  ***"
#ftypes=['torn', 'hail']	#SPC convective outlook forecast types
#years=['2011','2012']					#List of years to analyze

####################
#Run verification.py
####################
for ftype in ftypes:
	print "Analyzing "+ftype+" forecasts..."
	os.system("stdbuf -i0 -o0 -e0 ./verification.py "+ftype+" >& verif_"+ftype+".out")

print "Done with runverif.py"
