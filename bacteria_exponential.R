## Bacteria Growth Example

##############################################
## Fit early growth data to exponential model

## Data
k = seq(0,5) # Time step (1 hour)
y_data = c(0.02,0.021,0.028,0.031,0.04,0.05)  # Cell Density (cells/ml)

# Plot Data
plot(k,y_data,xlab="Time (hours)",ylab="Cell Density (cells/ml)",main="Cell Density versus Time")

# Assign vectors y_k and y_(k+1)
y_k = y_data[1:(length(y_data)-1)]
y_kp1 = y_data[2:length(y_data)]

# Plot y_(k+1) versus y_k
plot(y_k,y_kp1)


# Fit model (y_(k+1)=(1+r)*y_k) to data
fit = lm(y_kp1~y_k+0)
fit
abline(fit)
slope = fit$coefficients
r = slope - 1


# Plot data along with model output
y_model = rep(0,length(k))
y_model[1] = y_data[1]
for (i in 1:(length(y_model)-1)){
  y_model[i+1] = (1+r)*y_model[i]
}
plot(k,y_data,pch=20,ylim=c(.02,0.06))
points(k,y_model,pch=21)
legend(0, 0.05, c("Data", "Model"), col = c(1,1),pch = c(20,21))


