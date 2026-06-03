h <- scan()
h

##### 
# practices:
# 1
d <- c(81.8,69.3,76.4,61.7,76.9,76.5,74.8,68.9,62.7,76.5)
mean(d)
median(d)
sd(d)
cv <- max(d) - min(d)
cv

#2
x <- c(1,0.5,01)
mu <- c(0.25,-0.25,0)
sig <- matrix(c(9,0,-1,0,7,2,-1,2,5),nrow=3)

f <- function(x,mu,sig){
  1 / (sqrt((2*pi)^3 * det(sig))) * exp(-0.5 %*% t((x - mu)) %*% solve(sig) %*% (x-mu))
}
f(x,mu,sig)


# 3


X <- matrix(rnorm(100),ncol=5)

X %*% solve(t(X) %*% X) %*% t(X)


# 4
df_sorted <- airquality[order(airquality$Temp), ]
df_sorted



# 5
c()








