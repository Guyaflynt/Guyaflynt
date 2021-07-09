#!/bin/bash
#
#$ -cwd
#$ -j y
'''
A. Flynt
Feb, 2021

This program is to read the SS data and to seperate data with a>0, b>0, and c>0 with reports, and a bias = -999
'''

import  os, string, sys, glob, csv
from pylab import *

#File names
#Hail1200_SS_20082019.csv
#Torn1200_SS_20082019.csv
#Wind1200_SS_20082019.csv

#Seperating into different files 
#Bias_Hail_20082019_SS.csv
#Bias_Torn_20082019_SS.csv
#Bias_Wind_20082019_SS.csv

ofile= open('Bias_Wind_20082019_SS.csv', 'w')
print >> ofile, 'Date, Hazard Type, Fcst Time, a, b, c, d, Bias, HSS, CSI, FOH, Date of reports, Count of Reports'

with open('Wind1200_SS_20082019.csv', 'rb') as datafile: 
	lines= datafile.readlines()
	lines.pop(0) #Get rid of the headers
	for line in lines:
		items= line.split(',')
		dates= string.atof(items[0])
		hazard= items[1]
		timefcst= items[2]
		a=string.atof(items[3])
		b=string.atof(items[4])
		c=string.atof(items[5])
		d= string.atof(items[6])
		Bias= string.atof(items[7])
		HSS= string.atof(items[8])
		FOH= string.atof(items[9])
		CSI= string.atof(items[10])
		dreport= items[12]
		countreports= items[13]

		if Bias == -999.0 and b >= 1:
			print >> ofile, dates, ',', hazard, ',', timefcst, ',', a, ',', b, ',', c, ',', d, ',', Bias, ',', HSS, ',', CSI, ',', FOH, ',', dreport, ',', countreports
		else: 
			print "no"
ofile.close()

