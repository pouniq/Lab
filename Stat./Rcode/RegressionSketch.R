x<- rnorm(50,10,8)
e <- c()
fitt <- c()

for(i in 1:50){
  e[i] <- rnorm(1,0,0.4*abs(x[i]))
}
y <- 3 + 4 * x + e
fit <- lm(y~x)

summary(fit)
res <- residuals(fit)
fitt <- fitted(fit)
plot(fitt,res)



# Regression from scratch ----
X1 <- c(1,2,3)
X2 <- c(5,9,7)
oness <- c(1,1,1)
y <- c(10,12,15)
X <- cbind(oness, X1, X2)
betaCoef <- solve(t(X) %*% X) %*% t(X) %*% y
yhat <- X %*% betaCoef


