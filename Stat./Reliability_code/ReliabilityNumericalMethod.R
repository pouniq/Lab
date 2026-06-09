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


L <- c(2.4,3.2,3.8,4.2,5.0,5.0,
       6.2,7.6,8.4,8.4,8.8,8.8)

R <- c(2.6,3.4,4.0,4.4,5.2,5.2,
       6.4,7.8,8.6,8.6,Inf,Inf)

loglik <- function(par){
  
  lambda <- par[1]
  beta   <- par[2]
  
  if(lambda <= 0 || beta <= 0)
    return(1e20)
  
  S <- function(t)
    exp(-(lambda*t)^beta)
  
  ll <- 0
  
  for(i in seq_along(L)){
    
    if(is.infinite(R[i])){
      
      ll <- ll + log(S(L[i]))
      
    } else {
      
      ll <- ll + log(S(L[i]) - S(R[i]))
      
    }
  }
  
  -ll
}

fit <- optim(
  par = c(0.1,2),
  fn = loglik,
  method = "L-BFGS-B",
  lower = c(1e-8,1e-8)
)

fit$par




t0 <- c(2.4,3.2,3.8,4.2,5.0,6.2,7.6,8.4)
t1 <- c(2.6,3.4,4.0,4.4,5.2,6.4,7.8,8.6)

r  <- c(1,1,1,1,2,1,1,2)

tc <- 8.8      # زمان سانسور
m  <- 2        # تعداد سانسور شده‌ها


loglik <- function(par){
  
  lambda <- par[1]
  beta   <- par[2]
  
  if(lambda <= 0 || beta <= 0)
    return(-Inf)
  
  S <- function(t)
    exp(-(lambda*t)^beta)
  
  ll <- sum(
    r * log(S(t0) - S(t1))
  ) +
    m * log(S(tc))
  
  ll
}


fit <- optim(
  par = c(0.1,5),
  fn  = function(par) -loglik(par),
  method = "L-BFGS-B",
  lower = c(1e-10,1e-10)
)

fit$par


