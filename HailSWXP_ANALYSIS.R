#April 2021
#Guy Flynt
#This code is to find the percentile and more for Wind, and to find other goodies
#Code was used to test the data from my thesis looking verifing forecasts from the Storm Prediction Center 
#One-way ANOVA test and Tukey test 
#2D density plot 
#Hail 
#Hail Overforecast
LR75over= Hailoverforecast85$`Lapse Rate from 700 to 500 mb 1 Hour Max`
PWATover= Hailoverforecast85$`Precipitable water 1 Hour Max`
MUCAPEover= Hailoverforecast85$`Most unstable CAPE 1 Hour Max`
FMUCAPEover= Hailoverforecast85$`MUCAPE from -10C to -30C 1 Hour Max`
SSPover= Hailoverforecast85$`Craven-Brooks Sig Severe 1 Hour Max`
SSPV2over= Hailoverforecast85$`SSPV2 Using MUCP`
SHR6Hover= Hailoverforecast85$`SHR6 (m/s) 1 Hour Max`
MLCAPEHover= Hailoverforecast85$MLCAPE
  
#Overforecast Percentiles 
quantile(LR75over)
quantile(PWATover)
quantile(MUCAPEover)
quantile(FMUCAPEover)
quantile(SSPover)
quantile(SSPV2over)
quantile(SHR6Hover)
quantile(MLCAPEHover)


#Hail Good skill
LR75good= Hailgoodforecast8515$`Lapse Rate from 700 to 500 mb 1 Hour Max`
PWATgood= Hailgoodforecast8515$`Precipitable water 1 Hour Max`
MUCAPEgood= Hailgoodforecast8515$`Most unstable CAPE 1 Hour Max`
FMUCAPEgood= Hailgoodforecast8515$`MUCAPE from -10C to -30C 1 Hour Max`
SSPgood= Hailgoodforecast8515$`Craven-Brooks Sig Severe 1 Hour Max`
SSPV2good= Hailgoodforecast8515$`SSPV2 Using MUCP`
SHR6Hgood= Hailgoodforecast8515$`SHR6 (m/s) 1 Hour Max`
MLCAPEHgood= Hailgoodforecast8515$MLCAPE

#Good skill Percentiles 
quantile(SHR6Hgood)
quantile(MLCAPEHgood)


#Hail Poor Skill
LR75poor= HailPS15$`Lapse Rate from 700 to 500 mb hour max` <- 
PWATpoor= HailPS15$`Precipitable water 1 hour max`
MUCAPEpoor= HailPS15$`Most unstable CAPE  1 hour max`
FMUCAPEpoor= HailPS15$`MUCAPE from -10C to -30C  hour max`
SSPpoor= HailPS15$`Craven-Brooks Sig Severe 1 hour max`
SSPV2poor= HailPS15$SSPv2
SHR6Hpoor= HailPS15$`SHR6 m/s`
MLCAPEHpoor= HailPS15$MLCAPE

#Poor Skill Percentiles 
quantile(LR75poor)
quantile(PWATpoor)
quantile(MUCAPEpoor)
quantile(FMUCAPEpoor)
quantile(SSPpoor)
quantile(SSPV2poor)
quantile(SHR6Hpoor)
quantile(MLCAPEHpoor)

#Scatter SSP vs PWAT
plot(SSPover, PWATover, pch= 15, col= "red", main= "SSP vs PWAT Comparison", xlim= c(0,100000))
points(SSPgood, PWATgood, pch= 16, col="blue")
points(SSPpoor, PWATpoor, pch= 17, col= "gold2")

#One-way Anova Test with Tukey test 
length(SSPV2good) <- 270
length(stackoverandgood) <- 325
combine_groups= data.frame(cbind(SSPV2over, SSPV2good, SSPV2poor))
combine_groups
length(SSPV2poor) <- 270
combineoverandgood= data.frame(cbind(SSPV2over, SSPV2poor))
stackoverandgood= stack(combineoverandgood)
goodataframe= data.frame(SSPV2good)
length(SSPpoor) <- 55
length(stackoverandgood) <- 325
length(goodataframe) <- 325

stackedgroups= stack(combine_groups)
stackedgroups
y= stackoverandgood$values
length(y) <- 325
x= goodataframe$SSPV2good
length(x) <- 325
anovatest= aov(values~ ind, stackedgroups)
summary(anovatest)
TukeyHSD(anovatest)

thettest= t.test(x,y, var.equal = TRUE); thettest
coxtest= wilcox.test(x,y); coxtest

#Boxplots
#LR75 
bxshr6= expression(bold("SHR6 Overforecast"))
bx1shr6= expression(bold("SHR6 Good Skill"))
bx2shr6= expression(bold("SHR6 Poor Skill"))
byshr6= expression(bold("SHR6 (m/s)"))
boxplot(SHR6Hover, SHR6Hgood, SHR6Hpoor, ylab= byshr6, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxshr6, bx1shr6, bx2shr6), main= "SHR6 Category Comparison", boxwex = 0.5)

par(mfrow=c(1,1))
bxpwat= expression(bold("PWAT Overforecast"))
bx1pwat= expression(bold("PWAT Good Skill"))
bx2pwat= expression(bold("PWAT Poor Skill"))
bypwat= expression(bold("PWAT (inches)"))
boxplot(PWATover, PWATgood, PWATpoor, ylab= bypwat, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxpwat, bx1pwat, bx2pwat), main= "PWAT Category Comparison", boxwex = 0.5)


#boxplot(LR75over, LR75good, LR75poor, ylab= "LR75 (C/km)", col=c('Red', 'Blue', 'yellow'), names = c("LR75 Overforecast", "LR75 Good Skill Forecast", "LR75 Poor Skill"), main= "LR75 Category Comparison", boxwex = 0.5)
bxmuc= expression(bold("MUCAPE Overforecast"))
bx1muc= expression(bold("MUCAPE Good Skill"))
bx2muc= expression(bold("MUCAPE Poor Skill"))
bymuc= expression(bold("MUCAPE (J/kg)"))
boxplot(MUCAPEover, MUCAPEgood, MUCAPEpoor, ylab= bymuc, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxmuc, bx1muc, bx2muc), main= "MUCAPE Category Comparison", boxwex = 0.5)

bxFmuc= expression(bold("FMUCAPE Overforecast"))
bx1Fmuc= expression(bold("FMUCAPE Good Skill"))
bx2Fmuc= expression(bold("FMUCAPE Poor Skill"))
byFmuc= expression(bold("FMUCAPE (J/kg)"))
boxplot(FMUCAPEover, FMUCAPEgood, FMUCAPEpoor,ylab= byFmuc, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxFmuc, bx1Fmuc, bx2Fmuc), main= "FMUCAPE Category Comparison", boxwex = 0.5)

bxSSP= expression(bold("SSP Overforecast"))
bx1SSP= expression(bold("SSP Good Skill"))
bx2SSP= expression(bold("SSP Poor Skill"))
bySSP= expression(bold("SSP (m3/s3)"))
boxplot(SSPover, SSPgood, SSPpoor, ylab= bySSP, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxSSP, bx1SSP, bx2SSP), main= "SSP Category Comparison", boxwex = 0.5)

#boxplot(SSPV2over, SSPV2good, SSPV2poor, ylab= "SSPV2", col=c('Red', 'Blue', 'yellow'), names = c("SSPV2 Overforecast", "SSPV2 Good Skill Forecast", "SSPV2 Poor Skill"), main= "SSPV2 Comparison", boxwex = 0.6, ylim= c(0,450000))
bxML= expression(bold("MLCAPE Overforecast"))
bx1ML= expression(bold("MLCAPE Good Skill"))
bx2ML= expression(bold("MLCAPE Poor Skill"))
byML= expression(bold("MLCAPE (J/kg)"))
boxplot(MLCAPEHover, MLCAPEHgood, MLCAPEHpoor, ylab= byML, col=c('lightsalmon', 'lightblue', 'lightgoldenrodyellow'), names = c(bxML, bx1ML, bx2ML), main= "MLCAPE Category Comparison", boxwex = 0.5)


#Density Plots for all three cats
library(ggplot2)
library(RColorBrewer)
#display.brewer.all()
library(wesanderson)
pal <- wes_palette("Zissou1", type = "continuous")
#overforecast
paradataover <- data.frame(SSPover, PWATover, stringsAsFactors = TRUE)
bp <- ggplot(paradataover, aes(SSPover,PWATover))
h5 <- bp + stat_bin_2d(bins=10) + scale_fill_gradientn(colours = pal)+ scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + ggtitle("Overforecast: SSP vs PWAT")+ theme(plot.title = element_text(hjust = 0.5), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank()) +xlab("SSP (numeric)") + ylab("PWAT (inches)")
h5

#Good Skill
paradataover <- data.frame(SSPgood, PWATgood, stringsAsFactors = TRUE)
bp <- ggplot(paradataover, aes(SSPgood,PWATgood))
h5 <- bp + stat_bin_2d(bins=10) + scale_fill_gradientn(colours = pal)+ scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + ggtitle("Good Skill: SSP vs PWAT")+ theme(plot.title = element_text(hjust = 0.5), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank()) +xlab("SSP (numeric)") + ylab("PWAT (inches)")
h5

#Poor skill
paradataover <- data.frame(SSPpoor, PWATpoor, stringsAsFactors = TRUE)
bp <- ggplot(paradataover, aes(SSPpoor,PWATpoor))
h5 <- bp + stat_bin_2d(bins=10) + scale_fill_gradientn(colours = pal)+ scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) +scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + ggtitle("Poor Skill: SSP vs PWAT")+ theme(plot.title = element_text(hjust = 0.5), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank()) +xlab("SSP (numeric)") + ylab("PWAT (inches)")
h5
