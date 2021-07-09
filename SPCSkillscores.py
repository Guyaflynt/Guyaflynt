#!/bin/bash
#
#$ -cwd
#$ -j y
'''
A. Flynt
Feb, 2021

This program is to read and calculate skill scores using the 1200 outlook for all severe weather hazards from the SPC. The focus will be on POD, FOH, FAR, Bias, HSS, CSI, and TSS skill score. The data is wind, torn, and hail contingency data; using glob.glob
we will calculate the skill scores and send them to the approiate csv file. 
'''

import  os, string, sys, glob, csv
from pylab import *

# Hail path is Hailcont/*.dat
# Tornado path is Torncont/*.dat
# Wind path is Windcont/*.dat
#File name example is Hail1200_SS_20082019.csv

ofile = open('Wind1200_SS_20082019.csv', 'w')
print >> ofile, 'Date; Hazard Type; a; b; c; d; Bias; HSS; FOH; CSI; FAR'

files= glob.glob("Windcont/*.dat") #Location of the contigency data from 2008 march 26 to 2019
print files
for file in sorted(files): 
	print file
	with open(file) as csvfile:
		lines= csvfile.readlines()
		lines.pop(0) #removes header

		for line in lines:
			colms= line.split(';')
			date= colms[0]
			haz= colms[1]
			a= string.atof(colms[2])
			b= string.atof(colms[3])
			c= string.atof(colms[4])
			d= string.atof(colms[5])
			
			#print date, haz, a, b, c, d
			#STOP

			#####
			#skill scores finally
			####

			# Probability of flase detection equals false alarms divided by correct negatives plus flase alarms. What fraction of the observed no events incorrectly 				#forecast as yes. Sensitive to false alarms, ignores misses Can be influenced by fewwer yes forecasted to reduce the number of false alarms. Used for 					#probabilitic forecast. 
			#Range is 0 to 1, 0 being no skill and 1 being perfect.
			try: 
				Bias= ((a+b)/(a+c))
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				Bias= -999
			
			#Heidke skill Score (HSS) is proportion correct that would be achieved by random foreasts that are statistically indpendent of the obs. Where 0 is no skill, 			#and 1 is perfect score
			try: 
				HSS= (2*(a*d-b*c))/((a+c)*(c+d)+(a+b)*(b+d))
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				HSS= -999
			
			# Frequency of Hits equals hits divded by hits plus false alarms, might be called success ratio. How often were the forecast correct, meaning the frquency 				#forecast were correct. Sensitive to false alarms but ignores misses. 
			# Range is 0 to 1, with 0 being no skill and 1 being perfect
			try: 
				FOH= a/(a+b)
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				FOH= -999

			# Critical Success Index (CSI)= hits divided by hits plus misses plus false alarms, denoted by the equation below. Comparison of the forecast yes events to 			# the observed yes events. Characteristics of the skill score are it measures the fraction of observed and fore cast events that were correctly predicted. 				# Only concerned with a, b, and c elements of the contingency table. Not so good with rare events, tornadoes or floods. 
			# Range is from 0 to 1, with 0 being no skill and 1 being a perfect score. 
			try: 
				CSI= a/(a+b+c)
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				CSI= -999

			# Probability of Dectation (POD)= hits divided by hits plus misses. Described as what fraction of the observed hits, yes events, were observed 						# (cawcr.gov.au). Some characteristics are sensitive to hits, but ignores false alrms, b events. Relatively sensitive to frequently occuring evens, like hail 			# or wind. Widely used skill score. 
			# Range is from 0 to 1, as 0 would be no skill and 1 being perfect.
			try: 
				POD= a/(a+c)
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				POD= -999

			# False Alarms equals false alarms divded by hits plus false alarms. What fraction of the predicted yes events acctually did not occur. Characteristics 				# sensitive to false alamrs, but ignores misses. sensitive to climatological frequency of the event. 
			# Range is from 0 to 1, 0 score being no skill and 1 being a perfect score
			try: 
				FAR= b/(a+b)
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				FAR= -999
			
			#True Skill Statistic (TSS) is to let forecasters forecasat for rare events. Denominator is unbiased. 1 is perfect, 0 terrible. 
			try: 
				TSS= (a*d - b*c)/((a+c)*(b+d))
			except ZeroDivisionError as e:
				warn= e
				print "\tWarning: ",warn
				TSS= -999



			print >> ofile, date, ';', haz, ';', a, ';', b, ';', c, ';', d, ';', Bias, ';', HSS, ';', FOH, ';', CSI, ';', FAR
ofile.close()
		