#!/usr/bin/python2.7.13
######!/usr/local/epd-7.2-2-rh5-x86_64/bin/python

# Guy Flynt
# 7/9/2019
# This code is used to convert aqi to PPB 2016-2018

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


print "Here we go"

ofile= open("aqiconvert_2016_2018.dat", "w")
print >> ofile, "OBSAQI; PPB; Date; forecastor; Code Color; areaname"


with open('forcastdata_2016_2018.csv' , 'r') as file:
	lines= file.readlines()
	lines.pop(0)
	for line in lines:
		items= line.split(',')
		OBSAQI= string.atof(items[1])
		PPB= string.atof(items[2])
		date= items[3]
		fcst_color= items[4]
		forecastor= items[5]
		areaname= items[6]
		
		print" CODE GREEN RANGE"
		
		if OBSAQI == 0:
			PPB= 0
		else:
			print "nope"

		if OBSAQI == 1:
			PPB= 1
		else:
			print "nope"
	
		if OBSAQI == 2:
			PPB= 2
		else:
			print "nope"

		if OBSAQI == 3:
			PPB= 3
		else:
			print "nope"

		if OBSAQI == 4:
			PPB= 5
		else:
			print "nope"

		if OBSAQI == 5:
			PPB= 6
		else:
			print "nope"

		if OBSAQI == 6:
			PPB= 7
			print "also OBSAQI equals 6"
		else:
			print "nope"

		if OBSAQI == 7:
			PPB= 8.0
		else:
			print "nope"
		
		if OBSAQI == 8:
			PPB= 9.0
		else:
			print "nope"
		
		if OBSAQI == 9:
			PPB= 10.0
		else:
			print "nope"
		
		if OBSAQI == 10:
			PPB= 11.0
		else:
			print "nope"

		if OBSAQI == 11:
			PPB= 12.0
		else:
			print "nope"

		if OBSAQI == 12:
			PPB= 13.0
		else:
			print "nope"

		if OBSAQI == 13:
			PPB= 14
		else:
			print "nope"

		if OBSAQI == 14:
			PPB= 15.0
		else:
			print "nope"
		if OBSAQI == 15:
			PPB= 16
		else:
			print "nope"

		if OBSAQI == 16:
			PPB= 17.0
		else:
			print "nope"

		if OBSAQI == 17:
			PPB= 18.0
		else:
			print "nope"
	
		if OBSAQI == 18:
			PPB= 19.0
		else:
			print "nope"

		if OBSAQI == 19:
			PPB= 21.0
			print"also equals 20 OBSAQI"
		else:
			print "nope"

		if OBSAQI == 20:
			PPB= 22.0
		else:
			print "nope"

		if OBSAQI == 21:
			PPB= 23.0
		else:
			print "nope"

		if OBSAQI == 22:
			PPB= 24.0
		else:
			print "nope"

		if OBSAQI == 23:
			PPB= 25.0
		else:
			print "nope"

		if OBSAQI == 24:
			PPB= 26.0
		else:
			print "nope"

		if OBSAQI == 25:
			PPB= 27.0
		else:
			print "nope"

		if OBSAQI == 26:
			PPB= 28.0
		else:
			print "nope"

		if OBSAQI == 27:
			PPB= 29.0
		else:
			print "nope"

		if OBSAQI == 28:
			PPB= 30.0
		else:
			print "nope"

		if OBSAQI == 29:
			PPB= 31.0
		else:
			print "nope"

		if OBSAQI == 30.0:
			PPB= 32.0
		else:
			print "nope"

		if OBSAQI == 31:
			PPB= 34.0
			print"also equals 33"
		else:
			print "nope"

		if OBSAQI == 32:
			PPB= 35.0
		else:
			print "nope"

		if OBSAQI == 33:
			PPB= 36.0
		else:
			print "nope"

		if OBSAQI == 34:
			PPB= 37.0
		else:
			print "nope"

		if OBSAQI == 35:
			PPB= 38.0
		else:
			print "nope"

		if OBSAQI == 36:
			PPB= 39.0
		else:
			print "nope"

		if OBSAQI == 37:
			PPB= 40.0
		else:
			print "nope"

		if OBSAQI == 38:
			PPB= 41.0
		else:
			print "nope"

		if OBSAQI == 39:
			PPB= 42.0
		else:
			print "nope"

		if OBSAQI == 40:
			PPB= 43.0
		else:
			print "nope"

		if OBSAQI == 41:
			PPB= 44.0
		else:
			print "nope"

		if OBSAQI == 42:
			PPB= 45.0
		else:
			print "nope"

		if OBSAQI == 43:
			PPB= 46.0
		else:
			print "nope"

		if OBSAQI == 44:
			PPB= 47.0
		else:
			print "nope"

		if OBSAQI == 45:
			PPB= 48.0
		else:
			print "nope"

		if OBSAQI == 46:
			PPB= 49.0
		else:
			print "nope"

		if OBSAQI == 47:
			PPB= 50.0
		else:
			print "nope"

		if OBSAQI == 48:
			PPB= 51.0
			print"also equals 52 OBSAQI"
		else:
			print "nope"

		if OBSAQI == 49:
			PPB= 53.0
		else:
			print "nope"

		if OBSAQI == 50:
			PPB= 54.0
		else:
			print "nope"


		print"CODE YELLOW RANGE"

		if OBSAQI == 51:
			PPB= 55.0
		else:
			print "nope"

		if 52 <= OBSAQI <= 54:
			PPB= 56.0
		else:
			print "nope"

		if 55 <= OBSAQI <= 58:
			PPB= 57.0
		else:
			print "nope"

		if 59 <= OBSAQI <= 61:
			PPB= 58.0
		else:
			print "nope"

		if 62 <= OBSAQI <= 64:
			PPB= 59.0
		else:
			print "nope"

		if 65 <= OBSAQI <= 67:
			PPB= 60.0
		else:
			print "nope"

		if 68 <= OBSAQI <= 71:
			PPB= 61.0
		else:
			print "nope"

		if 72 <= OBSAQI <= 74:
			PPB= 62.0
		else:
			print "nope"

		if 75 <= OBSAQI <= 77:
			PPB= 63.0
		else:
			print "nope"

		if 78 <= OBSAQI <= 80:
			PPB= 64.0
		else:
			print "nope"

		if 81 <= OBSAQI <= 84:
			PPB= 65.0
		else:
			print "nope"

		if 85 <= OBSAQI <= 87:
			PPB= 66.0
		else:
			print "nope"

		if 88 <= OBSAQI <= 90:
			PPB= 67.0
		else:
			print "nope"

		if 91 <= OBSAQI <= 93:
			PPB= 68.0
		else:
			print "nope"

		if 94 <= OBSAQI <= 97:
			PPB= 69.0
		else:
			print "nope"

		if 98 <= OBSAQI <= 100:
			PPB= 70.0
		else:
			print "nope"


		print"CODE ORANGE now"

		if OBSAQI == 101:
			PPB= 71.0
		else:
			print "nope"

		if 102 <= OBSAQI <= 105:
			PPB= 72.0
		else:
			print "nope"

	
		if 106 <= OBSAQI <= 108:
			PPB= 73.0
		else:
			print "nope"

		if 109 <= OBSAQI <= 112:
			PPB= 74.0
		else:
			print "nope"

		if 113 <= OBSAQI <= 115:
			PPB= 75.0
		else:
			print "nope"

		if 116 <= OBSAQI <= 119:
			PPB= 76.0
		else:
			print "nope"

		if 120 <= OBSAQI <= 122:
			PPB= 77.0
		else:
			print "nope"

		if 123 <= OBSAQI <= 126:
			PPB= 78.0
		else:
			print "nope"

		if 127 <= OBSAQI <= 129:
			PPB= 79.0
		else:
			print "nope"

		if 130 <= OBSAQI <= 133:
			PPB= 80.0
		else:
			print "nope"

		if 134 <= OBSAQI <= 136:
			PPB= 81.0
		else:
			print "nope"

		if 137 <= OBSAQI <= 140:
			PPB= 82.0
		else:
			print "nope"

		if 141 <= OBSAQI <= 143:
			PPB= 83.0
		else:
			print "nope"

		if 144 <= OBSAQI <= 147:
			PPB= 84.0
		else:
			print "nope"

		if 148 <= OBSAQI <= 150:
			PPB= 85.0
		else:
			print "nope"


		print"CODE RED now"

		if OBSAQI == 151:
			PPB= 86.0
		else:
			print "nope"

		if 152 <= OBSAQI <= 154:
			PPB= 87.0
		else:
			print "nope"

		if 155 <= OBSAQI <= 156:
			PPB= 88.0
		else:
			print "nope"

		if 157 <= OBSAQI <= 159:
			PPB= 89.0
		else:
			print "nope"

		if 160 <= OBSAQI <= 161:
			PPB= 90.0
		else:
			print "nope"

		if 162 <= OBSAQI <= 164:
			PPB= 91.0
		else:
			print "nope"

		if 165 <= OBSAQI <= 166:
			PPB= 92.0
		else:
			print "nope"

		if 167 <= OBSAQI <= 169:
			PPB= 93.0
		else:
			print "nope"

		if 170 <= OBSAQI <= 172:
			PPB= 94.0
		else:
			print "nope"

		if 173 <= OBSAQI <= 174:
			PPB= 95.0
		else:
			print "nope"

		if 175 <= OBSAQI <= 177:
			PPB= 96.0
		else:
			print "nope"

		if 178 <= OBSAQI <= 179:
			PPB= 97.0
		else:
			print "nope"

		if 180 <= OBSAQI <= 182:
			PPB= 98.0
		else:
			print "nope"

		if 183 <= OBSAQI <= 185:
			PPB= 99.0
		else:
			print "nope"

		if 186 <= OBSAQI <= 187:
			PPB= 100.0
		else:
			print "nope"

		if 188 <= OBSAQI <= 190:
			PPB= 101.0
		else:
			print "nope"

		if 191 <= OBSAQI <= 192:
			PPB= 102.0
		else:
			print "nope"

		if 193 <= OBSAQI <= 195:
			PPB= 103.0
		else:
			print "nope"

		if 196 <= OBSAQI <= 197:
			PPB= 104.0
		else:
			print "nope"

		if 198 <= OBSAQI <= 200:
			PPB= 105.0
		else:
			print "nope"
		print >> ofile, PPB, ';', OBSAQI, ';', date, ';', forecastor, ';',  fcst_color, ';', areaname
ofile.close()
			
			
		

