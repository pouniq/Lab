###### Mean Estimator #####
n <- 10
sample <- lapply(1:10000 , function(i) rnorm(n , mean = 4 , sd = 11))
mean.estimator <- sapply(sample , function(x) mean(x))
hist(mean.estimator , breaks = 50 )

mean(mean.estimator)


###### Variance Estimator #####

n <- 10
V <- sapply(sample , function(x) ((x-mean(x))^2 / length(x))

                       
hist(mean.estimator , breaks = 50 )                

