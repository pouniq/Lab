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

## the second example ----
t(X) %*% X
t(X) %*% y



# example one ----
x1 <- c(7,1,11,11,7,11,3,1,2,21,1,11,10)
x2 <- c(26,29,56,31,52,55,71,31,54,47,40,66,68)
x3 <- c(6,15,8,8,6,9,17,22,18,4,23,9,8)
x4 <- c(60,52,20,47,33,22,6,44,22,26,34,12,12)
y <- c(78.5,74.3,104.3,87.6,95.9,109.2,102.7,72.5,93.1,115.9,83.8,113.3,109.4)

x <- cbind(x1,x2,x3,x4)
cor(x)
det(cor(x))
det(solve(t(x) %*% x))
# we have multicollinearity for sure
b <- solve(t(x) %*% x) %*% t(x) %*% y
e <- eigen(solve(t(x) %*% x))

# for finding out about kappa:
e$values[1] / e$values[4]

 



e$values[1] / sum(e$values)



(e$values[1] + e$values[2]) / sum(e$values)

# VIF ----
xx1 <- lm(x1 ~ x2 + x3 + x4)
summary(xx1)$r.squared
vi_1 <- 1 / (1 - summary(xx1)$r.squared)
vi_1



xx2 <- lm(x2 ~ x1 + x3 + x4)
summary(xx2)$r.squared
vi_2 <- 1 / (1 - summary(xx2)$r.squared)
vi_2


xx3 <- lm(x3 ~ x1 + x2 + x4)
summary(xx3)$r.squared
vi_3 <- 1 / (1 - summary(xx3)$r.squared)
vi_3


xx4 <- lm(x4 ~ x1 + x3 + x2)
summary(xx4)$r.squared
vi_4 <- 1 / (1 - summary(xx4)$r.squared)
vi_4

# ANOVA -----
anova(lm(y ~ x1 + x2 + x3 + x4))


# Ridge regression ----



install.packages("GLMsData")
library(GLMsData)
data(windmill)
head(windmill)
y <- windmill$DC
x <- windmill$Wind

fit0 <- lm(x ~ y)
summary(fit0)

plot(fit0,pch=19)

# transform on X:
w <- x*log(x)
fit_xt <- lm(y ~ x + w)
summary(fit_xt)

alpha0 <- 1
alpha1 <- fit_xt$coefficients[3] / fit0$coefficients[2] + alpha0

x.prime <- x^alpha1


fit_xtt <- lm(y ~ x.prime )

# Transformations ----


## first Transformations -----
# the best one by far.
x.star <- 1/x
fit1 <- lm(x.star ~ y)
summary(fit1)

plot(fit1)

## Second Transformations ----
x.star1 <- x^2
fit2 <- lm(x.star1 ~ y)
summary(fit2)


## Third Transformations ----
x.star2 <- x^3
fit3 <- lm(x.star2 ~ y)
summary(fit3)



## box-cox example:
install.packages('sp')
library(sp)
data(meuse)  
head(meuse)
attach(meuse)

y <- meuse$zinc
x1 <- meuse$elev
x2 <- meuse$dist
fit0 <- lm(y ~ x1 + x2)
summary(fit0)
plot(fit0)

bc <- boxcox(zinc ~ elev + dist , data = meuse)
(lambda <- bc$x[which.max(bc$y)])
zinc.bc<- (zinc^lambda-1)/lambda



fit1 <- lm(zinc.bc ~ x1 + x2)
summary(fit1)
plot(fit1)


par(mfrow=c(2,2))
plot(fit2)



## linearity ----
### goodness of fitness ----

### scatter plot ----
plot(windmill$Wind , windmill$DC)
### partial regression (added plots) when we have multiple variables ----
### Past expriences ---- 
## Normal Error ----
## Constant Variance ( Multicollinearity )  ----
## homoscedasticity ----






