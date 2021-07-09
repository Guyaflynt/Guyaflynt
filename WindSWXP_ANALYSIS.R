#April 2021
#Guy Flynt
#This code is to find the percentile and more for Wind, and to find other goodies
#Code was used to test the data from my thesis looking verifing forecasts from the Storm Prediction Center 
#One-way ANOVA test and Tukey test 
#2D density plot 

#Wind overforecast
MCSMover= Windoverforecast85$`MCS Maintenance Probability 1 Hour max`
DCPover= Windoverforecast85$`DCP 1 Hour Max`
DCAPEover= Windoverforecast85$`DCAPE 1 Hour Max`
MUCAPEWover= Windoverforecast85$`MUCAPE 1 Hour Max`
SHR1over= Windoverforecast85$`SHR1 m/s 1 Hour Max`
SHR6Wover= Windoverforecast85$`SHR6 m/s 1 Hour Max`
SHR8over= Windoverforecast85$`SHR8 m/s 1 Hour Max`

#Quantile of the data
quantile(MCSMover)
quantile(DCPover)
quantile(DCAPEover)
quantile(MUCAPEWover)
quantile(SHR1over)
quantile(SHR6Wover)
quantile(SHR8over)


#Wind Good Skill
MCSMgood= Windgoodforecast8515$`MSC main mcsm`
DCPgood= Windgoodforecast8515$`DCP 1 hour max = decp`
DCAPEgood= Windgoodforecast8515$`DCAPE dncp`
MUCAPEWgood= Windgoodforecast8515$`MUCAPE mucp`
SHR1good= Windgoodforecast8515$`SHR1 m/s`
SHR6Wgood= Windgoodforecast8515$`SHR6 m/s`
SHR8good= Windgoodforecast8515$`SHR8 m/s`

#Quantiles of the data
quantile(MCSMgood)
quantile(DCPgood)
quantile(DCAPEgood)
quantile(MUCAPEWgood)
quantile(SHR1good)
quantile(SHR6Wgood)
quantile(SHR8good)



#Wind Poor Skill
MCSMpoor= WindPS15$`MSC Maintience 1 Hour Max`
DCPpoor= WindPS15$`DCP 1 Hour Max`
DCAPEpoor= WindPS15$`DCAPE 1 Hour Max`
MUCAPEWpoor= WindPS15$`MUCAPE 1 Hour Max`
SHR1poor= WindPS15$`SHR1 m/s 1 Hour Max`
SHR6Wpoor= WindPS15$`SHR6 m/s 1 Hour Max`
SHR8poor= WindPS15$`SHR8 m/s 1 Hour Max`

#Quantile of the data 
quantile(MCSMpoor)
quantile(DCPpoor)
quantile(DCAPEpoor)
quantile(MUCAPEWpoor)
quantile(SHR1poor)
quantile(SHR6Wpoor)
quantile(SHR8poor)

#One way ANOVA test code 
length(SHR8poor) <- 267
combine_groups= data.frame(cbind(SHR8over, SHR8good, SHR8poor))
combine_groups

stackedgroups= stack(combine_groups)
stackedgroups

combineoverandgood= data.frame(cbind(SHR8over, SHR8poor))
goodataframe= data.frame(SHR8good)
stackoverandgood= stack(combineoverandgood)
length(stackoverandgood) <- 325
length(goodataframe) <- 325

y= stackoverandgood$values
length(y) <- 325
x= goodataframe$SHR8good
length(x) <- 325
thettest= t.test(x,y, var.equal = TRUE); thettest
coxtest= wilcox.test(x,y); coxtest

anovatest= aov(values ~ ind, stackedgroups) #The test
summary(anovatest) #Summary, that gives the p-value
TukeyHSD(anovatest) #Post-hoc test to find 



#boxplots 
bxMCSM= expression(bold("MCSM Overforecast"))
bx1MCSM= expression(bold("MCSM Good Skill"))
bx2MCSM= expression(bold("MCSM Poor Skill"))
bysMCSM= expression(bold("MCSM (%)"))
boxplot(MCSMover, MCSMgood, MCSMpoor, ylab= bysMCSM, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxMCSM, bx1MCSM, bx2MCSM), main= "MCSM Category Comparison", boxwex = 0.5)

bxDCP= expression(bold("DCP Overforecast"))
bx1DCP= expression(bold("DCP Good Skill"))
bx2DCP= expression(bold("DCP Poor Skill"))
byDCP= expression(bold("DCP (numeric)"))
boxplot(DCPover, DCPgood, DCPpoor, ylab= byDCP, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxDCP, bx1DCP, bx2DCP), main= "DCP Category Comparison", boxwex = 0.5)

#boxplot(DCAPEover, DCAPEgood, DCAPEpoor, ylab= "DCAPE (J/kg)", col=c('Red', 'Blue', 'yellow'), names = c("DCAPE Overforecast", "DCAPE Good Skill Forecast", "DCAPE Poor Skill"), main= "DCAPE Category Comparison", boxwex = 0.5)

#boxplot(MUCAPEWover, MUCAPEWgood, MUCAPEWpoor, ylab= "MUCAPE (J/kg)", col=c('Red', 'Blue', 'yellow'), names = c("MUCAPE Overforecast", "MUCAPE Good Skill Forecast", "MUCAPE Poor Skill"), main= " MUCAPE Category Comparison", boxwex = 0.5)
bxshr1= expression(bold("SHR1 Overforecast"))
bx1shr1= expression(bold("SHR1 Good Skill"))
bx2shr1= expression(bold("SHR1 Poor Skill"))
byshr1= expression(bold("SHR1 (m/s)"))
boxplot(SHR1over, SHR1good, SHR1poor, ylab= byshr1, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxshr1, bx1shr1, bx2shr1), main= "SHR1 Category Comparison", boxwex = 0.5)
#boxplot(SHR6Wover, SHR6Wgood, SHR6Wpoor, ylab= "SHR6 (m/s)", col=c('Red', 'Blue', 'yellow'), names = c("SHR6 Overforecast", "SHR6 Good Skill Forecast", "SHR6 Poor Skill"), main= "SHR6 Category Comparison", boxwex = 0.5)
#boxplot(SHR8over, SHR8good, SHR8poor, ylab= "SHR8 (m/s)", col=c('Red', 'Blue', 'yellow'), names = c("SHR8 Overforecast", "SHR8 Good Skill Forecast", "SHR8 Poor Skill"), main= "SHR8 Category Comparison", boxwex = 0.5)

#Density Plots for all three classes
library(ggplot2)
library(RColorBrewer)
#display.brewer.all()
library(wesanderson)
pal <- wes_palette("Zissou1", type = "continuous")

#overforecast
paradataover <- data.frame(MUCAPEWover, SHR6Wover, stringsAsFactors = TRUE)
bp <- ggplot(paradataover, aes(MUCAPEWover,SHR6Wover))
h5 <- bp + stat_bin_2d(bins=10) + scale_fill_gradientn(colours = pal)+ scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + ggtitle("Overforecast: MUCAPE vs SHR6")+ theme(plot.title = element_text(hjust = 0.5), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank()) +xlab("MUCAPE (J/kg)") + ylab("SHR6 (m/s)")
h5

#Good Skill
paradataover <- data.frame(MUCAPEWgood, SHR6Wgood, stringsAsFactors = TRUE)
bp <- ggplot(paradataover, aes(MUCAPEWgood,SHR6Wgood))
h5 <- bp + stat_bin_2d(bins=10) + scale_fill_gradientn(colours = pal)+ scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + ggtitle("Good Skill: MUCAPE vs SHR6")+ theme(plot.title = element_text(hjust = 0.5), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank()) +xlab("MUCAPE (J/kg)") + ylab("SHR6 (m/s)")
h5

#Poor
paradataover <- data.frame(MUCAPEWpoor, SHR6Wpoor, stringsAsFactors = TRUE)
bp <- ggplot(paradataover, aes(MUCAPEWpoor,SHR6Wpoor))
h5 <- bp + stat_bin_2d(bins=10) + scale_fill_gradientn(colours = pal)+ scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + ggtitle("Poor Skill: MUCAPE vs SHR6")+ theme(plot.title = element_text(hjust = 0.5), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank()) +xlab("MUCAPE (J/kg)") + ylab("SHR6 (m/s)")
h5



#SHR6 and MUCAPE MLCAPE comparison 
#Tornado
SRH6over= Tornoverforecast85$`SHR6 m/s 1 Hour Max`
MLCAPEover= Tornoverforecast85$`MLCAPE 1 Hour Max`
SRH6good= Torngoodforecast8515$`SHR6 m/s 1 Hour Max`
MLCAPEgood= Torngoodforecast8515$`MLCAPE 1 Hour Max`

#Hail
MUCAPEover= Hailoverforecast85$`Most unstable CAPE 1 Hour Max`
SHR6Hover= Hailoverforecast85$`SHR6 (m/s) 1 Hour Max`
MLCAPEHover= Hailoverforecast85$MLCAPE
MUCAPEgood= Hailgoodforecast8515$`Most unstable CAPE 1 Hour Max`
SHR6Hgood= Hailgoodforecast8515$`SHR6 (m/s) 1 Hour Max`
MLCAPEHgood= Hailgoodforecast8515$MLCAPE
MUCAPEpoor= HailPS15$`Most unstable CAPE  1 hour max`
SHR6Hpoor= HailPS15$`SHR6 m/s`
MLCAPEHpoor= HailPS15$MLCAPE

#Wind
MUCAPEWover= Windoverforecast85$`MUCAPE 1 Hour Max`
SHR6Wover= Windoverforecast85$`SHR6 m/s 1 Hour Max`
MUCAPEWgood= Windgoodforecast8515$`MUCAPE mucp`
SHR6Wgood= Windgoodforecast8515$`SHR6 m/s`
MUCAPEWpoor= WindPS15$`MUCAPE 1 Hour Max`
SHR6Wpoor= WindPS15$`SHR6 m/s 1 Hour Max`

#Overforecast box plot comparison 
boxplot(SRH6over, SHR6Hover, SHR6Wover, ylab= "SHR6 (m/s)", col=c('Red', 'green', 'blue'), names = c("SHR6 Tornado Overforecast", "SHR6 Hail Overforecast", "SHR6 Wind Overforecast"), main= "SHR6 Hazard Overforecast Comparison", boxwex = 0.5)
boxplot(MLCAPEover, MLCAPEHover, ylab= "MLCAPE (J/kg)", col=c('Red', 'green'), names = c("MLCAPE Tornado Overforecast", "MLCAPE Hail Overforecast"), main= "MLCAPE Hazard Overforecast Comparison", boxwex = 0.5)
boxplot(MUCAPEover, MUCAPEWover, ylab= "MUCAPE (J/kg)", col=c('green', 'blue'), names = c("MUCAPE Hail Overforecast", "MUCAPE Wind Overforecast"), main= "MUCAPE Hazard Overforecast Comparison", boxwex = 0.5)

#Good skill boxplot
boxplot(SRH6good, SHR6Hgood, SHR6Wgood, ylab= "SHR6 (m/s)", col=c('Red', 'green', 'blue'), names = c("SHR6 Tornado Good Skill", "SHR6 Hail Good Skill", "SHR6 Wind Good Skill"), main= "SHR6 Hazard Good Skill Comparison", boxwex = 0.5)
boxplot(MLCAPEgood, MLCAPEHgood, ylab= "MUCAPE (J/kg)", col=c('Red', 'green'), names = c("MLCAPE Tornado Good Skill", "MLCAPE Hail Good Skill"), main= "MLCAPE Hazard Good Skill Comparison", boxwex = 0.5)
boxplot(MUCAPEgood, MUCAPEWgood, ylab= "MUCAPE (J/kg)", col=c('green', 'blue'), names = c("MUCAPE Hail Good Skill", "MUCAPE Wind Good SKill"), main= "MUCAPE Hazard Good Skill Comparison", boxwex = 0.5)


#Poor boxplot
boxplot(SHR6Hpoor, SHR6Wpoor, ylab= "SHR6 (m/s)", col=c('green', 'blue'), names = c("SHR6 Hail Poor Skill", "SHR6 Wind Poor Skill"), main= "SHR6 Hazard Poor Skill Comparison", boxwex = 0.5)
boxplot(MUCAPEpoor, MUCAPEWpoor, ylab= "MUCAPE (J/kg)", col=c('green', 'blue'), names = c("MUCAPE Hail Poor Skill", "MUCAPE Wind Poor SKill"), main= "MUCAPE Hazard Poor Skill Comparison", boxwex = 0.5)

