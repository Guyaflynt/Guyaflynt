#April 2019
#Guy Flynt
#This code is to plot all years and time periods for wind data on relability charts
wd11axis= X0100_wind_real_diagrams$axis
wd0111= X0100_wind_real_diagrams$`2011`
wd0112= X0100_wind_real_diagrams$`2012`
wd0113= X0100_wind_real_diagrams$`2013`
wd0114= X0100_wind_real_diagrams$`2014`
wd0115= X0100_wind_real_diagrams$`2015`
wd0116= X0100_wind_real_diagrams$`2016`

library("plotrix")
par(pty="s")
par(mfrow = c(1,1 ))
plot(one, toone, type="l", xlab = "Forecast Probability", ylab = "Observed Relative Frequency", asp = 1, main= "Hypothetical Precipitation Reliability Diagram")
#Import the wind data for 0100 
forecastprob= c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
obsfreq= c(0.030716724,0.088607595,0.209876543,0.316326531,0.390625,0.5,0.58974359,0.692307692,0.80952381,0.857142857,0.9)
points(forecastprob,obsfreq, type = "b", pch=16, col="blue")
counts= c(293	,237	,162,	98,	64,	36,	39,	26,	21,	14,	10)
barplot(counts, forecastprob, space = 0, width = 1, xlab = "")
# Plotting the data of 0100 wind data
points(wd11axis, wd0111, type = "b", pch= 16, col= "blue")
points(wd11axis, wd0112, type = "b", pch= 16, col= "red")
points(wd11axis, wd0113, type = "b", pch= 16, col= "green")
points(wd11axis, wd0114, type = "b", pch= 16, col= "orange")
points(wd11axis, wd0115, type = "b", pch= 16, col= "black")
points(wd11axis, wd0116, type = "b", pch= 16, col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))


#Importing the data for 1200 wind data
wd12axis= X1200_wind_real_diagrams$axis
wd1211= X1200_wind_real_diagrams$`2011`
wd1212=X1200_wind_real_diagrams$`2012`
wd1213=X1200_wind_real_diagrams$`2013`
wd1214=X1200_wind_real_diagrams$`2014`
wd1215=X1200_wind_real_diagrams$`2015`
wd1216=X1200_wind_real_diagrams$`2016`

#Plotting the 1200 wind data
plot(one, toone, type="l",  xlab = "Forecast Probability", ylab = "Observed Relative Frequency", asp = 1)
points(wd12axis, wd1211, type= "b", pch= 16, col= "blue")
points(wd12axis, wd1212, type= "b", pch= 16, col= "red")
points(wd12axis, wd1213, type= "b", pch= 16, col= "green")
points(wd12axis, wd1214, type= "b", pch= 16, col= "orange")
points(wd12axis, wd1215, type= "b", pch= 16, col= "black")
points(wd12axis, wd1216, type= "b", pch= 16, col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

#Importing the 1300 wind data
wd13axis= X1300_wind_real_diagrams$axis
wd1311= X1300_wind_real_diagrams$`2011`
wd1312= X1300_wind_real_diagrams$`2012`
wd1313= X1300_wind_real_diagrams$`2013`
wd1314= X1300_wind_real_diagrams$`2014`
wd1315= X1300_wind_real_diagrams$`2015`
wd1316= X1300_wind_real_diagrams$`2016`

#Plotting the 1300 wind data
plot(one, toone, type="l",  xlab = "Forecast Probability", ylab = "Observed Relative Frequency", asp = 1)
points(wd13axis, wd1311, pch=16, type = "b", col= "blue")
points(wd13axis, wd1312, pch=16, type = "b", col= "red")
points(wd13axis, wd1313, pch=16, type = "b", col= "green")
points(wd13axis, wd1314, pch=16, type = "b", col= "orange")
points(wd13axis, wd1315, pch=16, type = "b", col= "black")
points(wd13axis, wd1316, pch=16, type = "b", col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))


#Importing the 1630 wind data
wd16axis= X1630_wind_real_diagram$axis
wd1611= X1630_wind_real_diagram$`2011`
wd1612= X1630_wind_real_diagram$`2012`
wd1613= X1630_wind_real_diagram$`2013`
wd1614= X1630_wind_real_diagram$`2014`
wd1615= X1630_wind_real_diagram$`2015`
wd1616= X1630_wind_real_diagram$`2016`

#Plotting the 1630 wind data
plot(one, toone, type="l",  xlab = "Forecast Probability", ylab = "Observed Relative Frequency", asp = 1)
points(wd16axis, wd1611, pch=16, type = "b", col= "blue")
points(wd16axis, wd1612, pch=16, type = "b", col= "red")
points(wd16axis, wd1613, pch=16, type = "b", col= "green")
points(wd16axis, wd1614, pch=16, type = "b", col= "orange")
points(wd16axis, wd1615, pch=16, type = "b", col= "black")
points(wd16axis, wd1616, pch=16, type = "b", col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

# Importing the 2000 wind data
wd20axis= X2000_wind_real_diagrams$axis
wd2011= X2000_wind_real_diagrams$`2011`
wd2012= X2000_wind_real_diagrams$`2012`
wd2013= X2000_wind_real_diagrams$`2013`
wd2014= X2000_wind_real_diagrams$`2014`
wd2015= X2000_wind_real_diagrams$`2015`
wd2016= X2000_wind_real_diagrams$`2016`

# Plotting the 2000 wind data
plot(one, toone, type="l",  xlab = "Forecast Probability", ylab = "Observed Relative Frequency", asp = 1)
points(wd20axis, wd2011, type= "b", pch=16, col= "blue")
points(wd20axis, wd2012, type= "b", pch=16, col= "red")
points(wd20axis, wd2013, type= "b", pch=16, col= "green")
points(wd20axis, wd2014, type= "b", pch=16, col= "orange")
points(wd20axis, wd2015, type= "b", pch=16, col= "black")
points(wd20axis, wd2016, type= "b", pch=16, col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))
mtext("Hail Reliability Diagrams", outer = TRUE, cex=2.0)

