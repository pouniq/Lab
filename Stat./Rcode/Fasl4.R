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



# ساخت تابع برای محاسبه محیط و مساحت
rect <- function(a,b){
  p = 2 * (a+b) # محیط مستطیل
  s = a * b # مساحت مستطیل
  c(Perimeter=p,Area=s)
}
rect(2,3)


# مساحت رویه و حجم مکعب را محاسبه کنیم.
cu <- function(x,y,z){
  v <- x * y * z # محاسبه حجم
  s <- (x*y+x*z+y*z)*2 # مساحت سطح
  c(volume = v, Surface_Area = s)
  
}
cu(2,4,2)


# اگر به آرگومان ها عدد بدهیم به آنها آرگومان اختیاری گفته میشود
# ولی اگر عددی ندهیم باید در زمان فراخوانی برای آن عدد تعریف کنیم



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

# تابع نشانگر 
# Indicator function
gammalik <- function(theta, x){
  alpha <- theta[1]
  beta <- theta[2]
  
  z <- (1/gamma(alpha)*beta^alpha)*x^(alpha - 1)*exp(-x/beta)
  y <- ifelse(x >= 0, z, 0)
  prod(y)
}
x <- c(2,3,5,6)
gammalik(c(2,5),x)
log(gammalik(c(2,5),x))

# if we minimum the -f, we actually maximize the f

obj <- function(theta){
  -log(gammalik(theta,x))
}
# distr
optim(c(2,1),obj)

# باید یک مقدار اولیه به آلفا و بتا بدیم تا همگرا شود.
# par: نشان دهنده مقدار برآورد شده آلفا و بتا است
# value: نشان دهنده مقدار تابع وقتی که آلفا و بتای می نیمم شده را در آن قرار می دهیم
# counts: چندبار الگوریتم تکرار شده تا به نتیجه برسه
# convergence: نشان دهنده این هست که آیا همگرا شده یا خیر که اگر صفر باشد همگرا نشده
# و اگر ۱ باشد همگرا شده است

 

# Dist. Detection -----
# ما یک بردار مشاهدات داریم میخوایم ببینیم که آیا از یک توزیع آمدند یا خیر
# استفاده از تابع چندک چندک
qqdist <- function(x, dist, ...){
  pois <- 
}

# function complete that.




# For Loop و حلقه ----
## For: برای تمام چیزهایی که داریم روش کار انجام میشه -- تعداد تکرارها ثابت باشه
## While: تا موقعی که اون شرطه درسته ادامه بده-- اگر تعداد تکرارها مشخص نباشه ولی نیازه که به یک شرطی برسیم
## repeat: مثل همون وایل هست ولی شرطو توی بدنه میزاریم نه همون اول



# Fibonacci ----

fib <- rep(1, 100)
for (i in 3:1000){
  fib[i] <- fib[i-1] + fib[i-2]
}
fib

# While Or Repeat:
# Taylor

s <- 0
n <- 0

while(abs(s-sqrt(3)/2) >= 1e-12){
  s <- s + ((-1)^n / factorial(2*n +1) * (pi/3)^(2*n+1))
  n <- n+1
}
s
n

## we can write that with repeat too !!!!!
# we just reverse the condition in repeat

s <- 0
n <- 0

repeat{
  s <- s + ((-1)^n / factorial(2*n +1) * (pi/3)^(2*n+1))
  n <- n+1
  
  if(abs(s-sqrt(3)/2) < 1e-12)
    break
}
s
n




# گشتاور ----
# گشتاورهای مرتبه ۱ تا آر رو می خوایم بنویسیم
mom <- function(x, r){
  m <- rep(0,1)
  for(k in 1:r){
    m[k] <- mean(x^k)
  }
  m
}
mom(x,5)


# برای گشتاور مرکزی
mom <- function(x, r){
  m <- rep(0,1)
  for(k in 1:r){
    m[k] <- mean((x-mean(x))^k)
  }
  m
}
mom(x,5)














# تمرین -------



