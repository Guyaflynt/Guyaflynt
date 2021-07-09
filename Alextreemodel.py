#!/usr/bin/python2.7.13
######!/usr/local/epd-7.2-2-rh5-x86_64/bin/python
'''
This code will import tree data, read, and work a model. 
ALEX F. 

This directory contains digitized treefall data for all VORTEX-Southeast damage surveys.
The files are named after the nearest town.

FORMAT
Tag/tree number
Species (as an integer; see species file)
dbh (cm)
Damage (single character; see below)
Crown width (m)
Total height (m)
Height type (single character; see below)
Crown bottom (m) - use -999 if no data
Direction of fall (degrees clockwise from north)
x coordinate (use longitude to SIX decimal places; negative)
y coordinate (use latitude to SIX decimal places)
---------------------------------
Trunk defects/rot (text)
Root system defects/rot (text)
Comments on soil/waterlogging (text)
General comments (text)
Photos (comma-delimited image number list)
Photo comments (comma-delimited comments corresponding with each photo)
Distance to nearest point on structure (m)
Direction to nearest point on structure (degrees clockwise from north)
Part of structure at nearest point (side or corner); Use S or C
Plot (40 m x 40 m) - use -999 here for now
'''
'''
Damage has several categories:
I = "intact"
D = "defoliated #(does not apply to deciduous trees that haven't leafed out yet)"
N = bent
L = leaning
T = stubbed
K = debarked
S = trunk snapped
U = uprooted
B = branches broken (i.e., < half of crown gone)
C = crown broken (i.e., > half of crown gone) - not on our survey sheets
A = < 5 cm branches broken
B = > 5 cm branches broken
M = branches broken by debris
G = branches broken by impact with ground
X = cleanup already started
Note: If there are multiple conditions checked on the survey sheet, combine them into a character string.  For example, if the tree is debarked and cleanup has started, use KX.

Height type is C or M for calculated or measured.  Almost all of our trees should be directly measured, but for those that were not, we have a regression using dbh to estimate height.

Build the database in Excel.  We can export it as a semicolon-delimited file for use in our model.
'''
print "its a going"
