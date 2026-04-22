logFact <- function(x) sapply(x , function(y) ifelse(y==0 , 0 , sum(log(1:y))))
logComb <- function(n , r) logFact(n) - (logFact(n-r) + logFact(r))




