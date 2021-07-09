## Bacteria Growth Example

##############################################
## Fit long-term growth data to logistic model
k = seq(0:21)
y_data = c(0.02,0.021,0.028,0.031,0.04,0.05,0.05,0.06,0.067,0.07,0.071,0.076,0.08,0.081,0.08,0.081,0.08,0.08,0.081,0.081,0.081,0.082)

# Plot Data
plot(k,y_data,xlab="Time (hours)",ylab="Cell Density (cells/ml)",main="Cell Density versus Time")


# Assign vectors y_k and y_(k+1)
y_k = y_data[1:(length(y_data)-1)]
y_kp1 = y_data[2:length(y_data)]
PerCap_y = (y_kp1-y_k)/y_k

# Plot y_(k+1) versus y_k
plot(y_k,PerCap_y)


# Fit model (y_(k+1)=(1+r)*y_k) to data
fit = lm(PerCap_y~y_k)
fit
abline(fit)
int = fit$coefficients[[1]]
slope = fit$coefficients[[2]]
r = int
K = -r/slope


# Plot data along with model output
y_model = rep(0,length(k))
y_model[1] = y_data[1]
for (i in 1:(length(y_model)-1)){
  y_model[i+1] = y_model[i] + r*y_model[i]*(1-y_model[i]/K)
}
plot(k,y_data,pch=20,ylim=c(0.02,0.09),xlab="Time (hours)",ylab="Cell Density (cells/ml)")
points(k,y_model,pch=21)
legend(1, 0.09, c("Data", "Model"), col = c(1,1),pch = c(20,21))
