#---- 
#geometric
# pmf
pmf_geo <- function(p,x) (1-p)^(x-1)*(p)
x <- 1:200000
p <- 0.3
plot(x , pmf_geo(p, x))

# expected value
sum(x * pmf_geo(p,x))

# variance
# why this one is wrong ?? 
# sum(x^2 * pmf_geo(p,x)) - sum(x * pmf_geo(p,x))


sample <- 1+rgeom(200000 , p)
hist(sample)
mean(sample)
var(sample)
#---- 
# poisson distribution
pmf_pois <- function(lambda , k )

#----
# nomal dist.
# turning uniform to bernoli and showing it is turning into normal

berno <- function(n,p) ifelse(runif(n) < 1-p , 0 ,1)
berno(100, 0.4)

var(runif(100000 , 2 , 5))

nsimul <- 10000
n <- 1000
p <- 0.3
res <- sapply(1:nsimul, function(i) mean(berno(n,p)))
head(res)


#---- 
# joint distribution
 
library(MASS)
library(plotly)

 
