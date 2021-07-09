#!/bin/bash
#
#$ -cwd
#$ -j y
'''
A. Flynt
Feb, 2021

This program is to read the SS data and to seperate data with a>0, b>0, and c>0 with reports, and a bias that is greater than 0. 
'''
import  os, string, sys, glob, csv
from pylab import *

#File names
#Hail1200_SS_20082019.csv
#Torn1200_SS_20082019.csv
#Wind1200_SS_20082019.csv

#Seperating into different files 
#Hail_reports10_SS.csv
#Torn_reports10_SS.csv
#Wind_reports10_SS.csv

#HSS and bias 85th percentile; This is used to find overforecast and well placed forecasts. 
#Hail HSS=0.241, B= 21.899
#Torn HSS=0.187, B= 39.067
#Wind HSS= 0.193, B= 31.367

#HSS and bias 15th percentile; these values are used to find poor skill misplcement forecasts 
# reports >= 10 and bias <= 15th percentile and HSS <= 15th percentile 
#Hail HSS= 0.034, B= 4.678
#Torn HSS= 0.013, B= 6.793
#Wind HSS= 0.013, B= 5.715

#Null dataset is 1 >= Bias <= 15th percentile and reports >= 10 and Hss >= 85th percentile
#Hail HSS=0.241, B= 4.678
#Torn HSS=0.187, B= 6.793
#Wind HSS= 0.193, B= 5.715

#Overforecast is bias > 90th percentile
#Null dataset forecst with good skill is bias greater than one bust less than the 10th bias percentile with HSS greater than the 90th percentile 
# Misplaced and poor skill forecast is bias less than the 10th percentile and HSS less than either the 10th or 15th HSS percentile. 

#Overforecast files DONE
#Hailoverforecast85.csv
#Tornoverforecast85.csv
#Windoverforecast85.csv

#Good skill or well placed forecasts
# Hailgoodforecast8515.csv
# Torngoodforecast8515.csv
# windgoodforecast8515.csv

#Poor skill and placed forecasts bias and HSS 15th percentile
# HailPS15.csv
# TornPS15.csv
# WindPS15.csv
#########################################################################################
#Data file names 10 Reports
#Hail1200_SS_20082019.csv
#Torn1200_SS_20082019.csv
#Wind1200_SS_20082019.csv

#Overforecast files 
#Hailoverforecast95reports10.csv
#Tornoverforecast95reports10.csv
#Windoverforecast95reports10.csv

#Good skill or well placed forecasts
# Hailgoodforecast595reports10.csv
# Torngoodforecast595reports10.csv
# windgoodforecast595reports10.csv

#Poor skill and placed forecasts bias and HSS 5th percentile
# HailPS5reports10.csv
# TornPS5reports10.csv
# WindPS5reports10.csv


ofile= open('WindPS5reports10.csv', 'w')
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
		countreports= string.atof(items[13])
		if countreports >= 10.0 and HSS <= 0.00 and Bias <= 3.275: #if countreports >= 10.0 and HSS >= 0.193 and 1 <= Bias <= 5.715:  
			print >> ofile, dates, ',', hazard, ',', timefcst, ',', a, ',', b, ',', c, ',', d, ',', Bias, ',', HSS, ',', CSI, ',', FOH, ',', dreport, ',', countreports
		else: 
			print "no"
ofile.close()

