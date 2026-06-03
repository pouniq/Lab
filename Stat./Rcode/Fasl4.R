# Building Functions
# f(x) = x^2

f<- function(x){
  a<- x^2
  b<- x^3
  c(a,b)
}

f(50)

# we can write this function differently, but in any case
# it is all the same

# if we have just one line in our function then we can drop the {} too
# it would not return an error

# f(x) = x^2 + 2*x + 1
f <- function(x){
  r<- x^2 + 2*x+1
  r
}

f(9)


# f(x) = cos(x) - x

f <- function(x){
  cos(x) - x
}
f(pi)


z<- seq(0,pi,length=10)
f(z)
plot(z,f(z))
plot(z,f(z), type = 'l')


# curve function make plots for functions with limitation you provide
curve(f, -pi,pi)

# integral
# it uses numerical methods
integrate(f, lower = 0, upper = pi)

# f(x) = sqrt(x) + 2*x^2 -1

f<- function(x){
  sqrt(x) + 2*x^2 -1
}
integrate(f, lower = 0, upper = 20)
# we cannot put negative numbers when we have sqrt in our function


# Solving Equations or finding the root of the equation
# cos(x) - x = 0

uniroot(f, c(-pi , pi))
# output, root: the number when our equation is equal to zero
#, f.root: when we put the root in the function, in this case we are close to
# zero not absolutly zero
# iter: the number of iteration to get to our root, our find our root

f<- function(x){
  x^4 - 16
}
uniroot(f, c(0 , 5))

# if we solve it between -5 and 5
uniroot(f, c(-5 , 5))


# multi variate functions
# f(x,y) = x^2 + y^2
f <- function(x,y){
  z <- x^2 + y^2
  z
}


f <- function(x,y=6){
  z <- x^2 + y^2
  z
}

f(2)


##### if statements

x<- 10

if(x>5){
  y<- sin(x)/x
} else{y<- 5*cos(x)}



ifelse(x>5, y<- sin(x)/x, y<- 5*cos(x))


x <- c(1,2,3,4,5,6,10)
median((x))

y <- sort(x)
n <- length(x)
if(n %% 2 == 0){
  m <- (y[n/2] + y[n/2+1])/2
}else{
  m <- y[(n+1)/2]
}
m


x <- c(1,4,5,7,9)
y <- c(4,5,1,3)
R <- 10
f <- function(x,y, R){
  if(length(x) != length(y)){
    stop('the vectors are not in the same length')
  }
  else {
  sum(x^2+y^2 <=  R^2)
  }
}
f(x,y,R)


gammalik <- function(theta, x){
  alpha <- theta[1]
  beta <- theta[2]
  
  z <- (1/gamma(alpha)*beta^alpha)*x^(alpha - 1)*exp(-x/beta)
  y<- ifelse(x >= 0, z, 0)
  prod(y)
}


gammalik(c(3,1),x)

optim()


