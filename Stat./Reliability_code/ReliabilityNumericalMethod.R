library(MASS)

data <- cbind(c(1:20), 
              c(25,28,29,44,57,58,63,64,64,
                76,87,93,111,126,136,139,157,168,189,212))

colnames(data) <- c('i','t_i')
data[,2]


library(fitdistrplus)

fit <- fitdist(data[,2], "weibull")
summary(fit)
plot(fit) 

beta = 1

f <- sum(log(beta) + beta * log(lambda) + (beta - 1) * log(t) - (lambda * t_i)^beta)




loglik <- function(params, t){
  lambda <- params[1]
  beta <- params[2]
  n <- length(t)
  
  n*log(beta) + n*beta*log(lambda) +
    (beta - 1)*sum(log(t)) -
    sum((lambda * t)^beta)
}


neg_loglik <- function(params) - loglik(params, data[,2])

result <- optim(
  par    = c(0.01, 1.5),        # initial guess: lambda, beta
  fn     = neg_loglik,
  method = "L-BFGS-B",          # allows box constraints
  lower  = c(1e-10, 1e-10)      # keep both params positive
)

y <- data[,2]

f <- function(params, y){
  
  lambda <- params[1]
  beta <- params[2]
  n <- length(y)
  
  n*log(beta) + n*beta*log(lambda) + (beta - 1)*sum(log(y)) - 
    sum((lambda * y)^beta)
  
}

f(params = c(2,3), y)

initialval <- c(1,1)
optim(initialval, f,
      y = y,
      control = list(fnscale = -1),
      method = "BFGS",
      hessian = TRUE)








