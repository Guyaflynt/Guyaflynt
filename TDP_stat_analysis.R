# April 2021
# Author Guy Flynt
# This code is to find the correlation between various variables; between nests and landscape variables
# Topic: Analyze data related the relative distance between the Cerulean Warbler, an endangered bird spices located in Indiana. Project code was for a biology thesis, not mine. 
# Data file used is TDP_Datasets 
####
#Avg distance from nests analysis
Numnests= TDP_Datasets$`Number of nests`[1:7]; Numnests #Number of nests per unit
Roadavg= TDP_Datasets$`Average Distance Roads`[1:7] #Avg distance from a road
Streamavg= TDP_Datasets$`Average distance from a stream`[1:7] #Avg distance from a stream 
Trailavg= TDP_Datasets$`Average Distance from a trails`[1:7] #Avg distance from a trial 

#R2 value and correlation tests for number of nests and streams 
r2= lm(Numnests~Streamavg) #linear regression 
summary(r2)
cor.test(Numnests,Streamavg) #Pearson
cor.test(Numnests,Streamavg,method = "spearman")
cor.test(Numnests,Streamavg,method = "kendall")
plot(Numnests, Streamavg, pch= 16, col= "blue")

#R2 value and correlation tests for number of nests and roads
r2= lm(Numnests~Roadavg) #linear regression 
summary(r2)
cor.test(Numnests,Roadavg) #Pearson
cor.test(Numnests,Roadavg,method = "spearman")
cor.test(Numnests,Roadavg,method = "kendall")


#R2 value and correlation tests for number of nests and trail
r2= lm(Numnests~Trailavg)
summary(r2)
cor.test(Numnests,Trailavg) #Pearson
cor.test(Numnests,Trailavg,method = "spearman")
cor.test(Numnests,Trailavg,method = "kendall")
plot(Numnests, Trailavg, pch= 16, col= "lime green")

#Plot AVG Distance
plot(Numnests, Roadavg, pch= 16, col= "black", cex= 2, main= "Number of Nests vs Landscape Variables", xlab= "Number of nests", ylab= "Average Distance (m)")
points(Numnests, Streamavg, pch= 16, cex= 2, col= "light blue")
points(Numnests, Trailavg, pch= 16, cex= 2, col= "yellow")
legend("topright", legend = c("Average Road Distance (m)", "Average Stream Distance (m)", "Average Trail Disance (m)"), col = c("Black", "light blue", "yellow"), pch= 19, bty= "n", pt.cex = 2, cex = 1.2)


######
#Sum within analysis
Sumstreamavg= TDP_Datasets$`Summarized Steams length in METERS`
Sumroadavg= TDP_Datasets$`Summarized Roads length in METERS`
Sumtrailavg= TDP_Datasets$`Summarized Trail length in METERS`
Numnestsdata= c(0,0,16,8,13,31,6,91,14)
treatments= TDP_Datasets$Treatment

#R2 value and correlation tests for number of nests and sum area of streams per unit
r2= lm(Numnestsdata~Sumstreamavg) #linear regression 
summary(r2)
cor.test(Numnestsdata,Sumstreamavg) #Pearson
cor.test(Numnestsdata,Sumstreamavg,method = "spearman")
cor.test(Numnestsdata,Sumstreamavg,method = "kendall")
plot(Numnestsdata, Sumstreamavg, pch= 16, col= "blue")


#R2 value and correlation tests for number of nests and sum area of Roads per unit
r2= lm(Numnestsdata~Sumroadavg) #linear regression 
summary(r2)
cor.test(Numnestsdata,Sumroadavg) #Pearson
cor.test(Numnestsdata,Sumroadavg,method = "spearman")
cor.test(Numnestsdata,Sumroadavg,method = "kendall")
plot(Numnestsdata, Sumroadavg, pch= 16, col= "black")


#R2 value and correlation tests for number of nests and sum area of trails per unit
r2= lm(Numnestsdata~Sumtrailavg) #linear regression 
summary(r2)
cor.test(Numnestsdata,Sumtrailavg) #Pearson
cor.test(Numnestsdata,Sumtrailavg,method = "spearman")
cor.test(Numnestsdata,Sumtrailavg,method = "kendall")
plot(Numnestsdata, Sumtrailavg, pch= 16, col= "brown")

maxdataframe= data.frame(Sumstreamavg, Sumroadavg, Sumtrailavg)
cor(maxdataframe)


Sumstreamavg= TDP_Datasets$`Summarized Steams length in METERS`
Sumroadavg= TDP_Datasets$`Summarized Roads length in METERS`
Sumtrailavg= TDP_Datasets$`Summarized Trail length in METERS`
Numnestsdata= c(0,0,16,8,13,31,6,91,14)

plot(Numnestsdata, Sumroadavg, pch= 16, col= "black", cex= 2, main= "Number of Nests vs Sum Total of Landscape Variables", xlab= "Number of nests", ylab= "Summed total (m)")
points(Numnestsdata, Sumstreamavg, pch= 16, cex= 2, col= "light blue")
points(Numnestsdata, Sumtrailavg, pch= 16, cex= 2, col= "yellow")
legend("topright", legend = c("Sum Total Roads (m)", "Sum Total Streams (m)", "Sum total Trials (m)"), col = c("Black", "light blue", "yellow"), pch= 19, bty= "n", pt.cex = 2, cex = 1.2)



