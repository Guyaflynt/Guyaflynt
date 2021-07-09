#April 2019
#Guy Flynt
#This code is to graph the reliability diagrams for all time periods for tornadoes 
par(pty="s")
par(mfrow = c(1, 1))
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability")
#importing the torn data for 0100
t01axis= X0100_tornado_real_diagrams$axis
torn11= X0100_tornado_real_diagrams$`2011`
torn12= X0100_tornado_real_diagrams$`2012`
torn13= X0100_tornado_real_diagrams$`2013`
torn14= X0100_tornado_real_diagrams$`2014`
torn15= X0100_tornado_real_diagrams$`2015`
torn16= X0100_tornado_real_diagrams$`2016`
# Plotting the data for 0100
points(t01axis, torn11, type= "b", pch= 16, col= "blue")
points(t01axis, torn12, type= "b", pch=16 , col= "red")
points(t01axis, torn13, type= "b", pch= 16, col= "green")
points(t01axis, torn14, type= "b", pch= 16, col= "orange")
points(t01axis, torn15, type= "b", pch= 16, col= "black")
points(t01axis, torn16, type= "b", pch= 16, col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

# Importing the torn data for 1200
t12axis= X1200_torn_real_diagrams$axis
tn1211= X1200_torn_real_diagrams$`2011`
tn1212= X1200_torn_real_diagrams$`2012`
tn1213= X1200_torn_real_diagrams$`2013`
tn1214= X1200_torn_real_diagrams$`2014`
tn1215= X1200_torn_real_diagrams$`2015`
tn1216= X1200_torn_real_diagrams$`2016`
# Plotting the data for 1200
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability", main= "1200")
points(t12axis, tn1211, type="b", pch=16, col="blue")
points(t12axis, tn1212, type="b", pch=16, col="red")
points(t12axis, tn1213, type="b", pch=16, col="green")
points(t12axis, tn1214, type="b", pch=16, col="orange")
points(t12axis, tn1215, type="b", pch=16, col="black")
points(t12axis, tn1216, type="b", pch=16, col="purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

#Importing the torn data for 1300
t13axis= X1300_torn_real_diagrams$axis
tn1311= X1300_torn_real_diagrams$`2011`
tn1312= X1300_torn_real_diagrams$`2012`
tn1313= X1300_torn_real_diagrams$`2013`
tn1314= X1300_torn_real_diagrams$`2014`
tn1315= X1300_torn_real_diagrams$`2015`
tn1316= X1300_torn_real_diagrams$`2016`

#Plotting the data for 1300
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability", main= "1300")
points(t13axis, tn1311, type = "b", pch=16, col="blue")
points(t13axis, tn1312, type = "b", pch=16, col="red")
points(t13axis, tn1313, type = "b", pch=16, col=" green")
points(t13axis, tn1314, type = "b", pch=16, col="orange")
points(t13axis, tn1315, type = "b", pch=16, col="black")
points(t13axis, tn1316, type = "b", pch=16, col="purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

# Import the torn data for 1630
t16axis=X1630_torn_real_diagrams$axis
tn1611= X1630_torn_real_diagrams$`2011`
tn1612= X1630_torn_real_diagrams$`2012`
tn1613= X1630_torn_real_diagrams$`2013`
tn1614= X1630_torn_real_diagrams$`2014`
tn1615= X1630_torn_real_diagrams$`2015`
tn1616= X1630_torn_real_diagrams$`2016`
#Plotting the data for 1630
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability", main= "1630")
points(t16axis, tn1611, type="b", pch=16, col="blue")
points(t16axis, tn1612, type="b", pch=16, col="red")
points(t16axis, tn1613, type="b", pch=16, col="green")
points(t16axis, tn1614, type="b", pch=16, col="orange")
points(t16axis, tn1615, type="b", pch=16, col="black")
points(t16axis, tn1616, type="b", pch=16, col="purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

# Import torn data for 2000
t20axis= X2000_torn_real_diagrams$axis
tn2011= X2000_torn_real_diagrams$`2011`
tn2012= X2000_torn_real_diagrams$`2012`
tn2013= X2000_torn_real_diagrams$`2013`
tn2014= X2000_torn_real_diagrams$`2014`
tn2015= X2000_torn_real_diagrams$`2015`
tn2016= X2000_torn_real_diagrams$`2016`

#Plotting torn data for 2000
one= c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
toone= c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability", main="Tornado")
points(t20axis, tn2011, type= "b", pch= 16, col= "blue")
points(t20axis, tn2012, type= "b", pch= 16, col= "red")
points(t20axis, tn2013, type= "b", pch= 16, col= "green")
points(t20axis, tn2014, type= "b", pch= 16, col= "black")
points(t20axis, tn2015, type= "b", pch= 16, col= "orange")
points(t20axis, tn2016, type= "b", pch= 16, col= "purple")
legend("right", c("2011", "2012", "2013", "2014","2015","2016"),pch=c(16,16,16,16,16,16), col= c("blue", "red","green","orange","black","purple"))

#Fake TORNADO REAL PLOT
#0,2,5,10,15,30,45,60%
fakedatatorn= c(0.005,0.011, 0.035,0.149,0.17,0.28,0.47,0.66)

#axes for fake plot for tornado 
axistornado= c(0.00, 0.02,0.05,0.1,0.15,0.30,0.45,0.6)

toone= c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability", main="Tornado")
points(axistornado, fakedatatorn, type = "b", pch= 16, col= "blue")


#Fake wind real diagram 
fakedatatwind= c(0.05,0.17,0.35,0.45,0.60,0.8)

#axes for fake plot for wind
axiswind= c(0.00,0.05,0.15,0.30,0.45,0.6)

toone= c(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
plot(one, toone, type="l", asp = 1, ylab= "Observed Relative Frequency", xlab = "Forecast Probability", main="Wind")
points(axiswind, fakedatatwind, type = "b", pch= 16, col= "red")


