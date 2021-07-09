#!/bin/bash
#
#$ -cwd
#$ -j y
# -*- coding: utf-8 -*-
'''
A. Flynt
Sept. 2020

This file is to clean and get ride of unwanted data in file DC_JAN_2009_2019.csv, and make a new file called cleanfile.csv
'''

import  os, string, sys, glob, csv, re
ofile= open('cleanfile.csv', 'w')
print >> ofile, "Station, City, State, Month, Day, Year, Latititude, Longititude, Snow amount in inches, Avergae Temperature, Max Temp, Min Temp"
with open('DC_JAN_2009_2019.csv', 'rb') as datafile:
	lines= datafile.readlines()
	lines.pop(0)
	for line in lines:
		items= re.split(',|/', line)
		Station= items[0]
		City= items[1]
		State= items[2]
		Latititude= string.atof(items[3])
		Longititude= string.atof(items[4])
		months= string.atof(items[6])
		day= items[7]
		year= items[8]
		Snowamount= items[9]
		Snowdepth= items[10]
		TAVG= items[11]
		TMAX= items[12]
		TMIN= items[13]
		#print Station, City, State, months, day, year, Latititude, Longititude, Snowamount, TAVG, TMAX, TMIN
		if months == 1:
			print >> ofile, Station, ',', City, ',', State, ',', months, ',', day, ',', year, ',',  Latititude, ',', Longititude, ',', Snowamount, ',', TAVG, ',', TMAX, ',', TMIN 
		else:
			print "Not the month"

ofile.close()