library(ggplot2)

ss <- 100000
X1 <- rnorm(ss)^2
X2 <- X1 + rnorm(ss)^2
X3 <- X2 + rnorm(ss)^2
X4 <- X3 + rnorm(ss)^2

d <- data.frame(X1 , X2 , X3 , X4)
head(d)




##### t-test ####
# One Sample
data <- c(20 , 25 , 32 , 19 , 17 , 18 , 15 , 24 , 31 , 23)
mean(data)
realMean <- 24

t.test(data)

tTest_stat <- function(data , realMean) (mean(data) - realMean)/(var(data)/sqrt(length(data)))


  
  
