# Fasl 1 ----
choose(5,2)
## Derivative ----
D(expression(3*x^2) , 'x')

sample(1:5,1,prob = c(100,1,2,3,1))
?sample

## Distributions ----
# we have d,p,q,r:
# d: density function value (pdf)
# p: probability function (cdf)
# q: quantile values
# r: random number 
dnorm(1,0)
pnorm(1,0)
qnorm(0.25,1,0)
rnorm(10,0,1)
?qnorm
# Fasl 2 ----
letters
LETTERS

month.abb

rep(c(2,10,2,34), 5)
rep(c(2,10,2,34), each=5)

z <- c(30,10,20)
sort(z)
order(z) #  نشون میده که مثلا کوچکترین عدد در جایگاه دوم قرار داره، جواب سوال اینکه از کجا میتونم 
# اون عدد در اون جایگاه رو پیدا کنم آدرس میده یک طورایی
rank(z) # نشون میده که هر عدد در کدام جایگاه قرار میگیره

# Fasl 3 ----

## QQPLOT ----
sleep
boxplot(sleep$extra[sleep$group == 1] ,sleep$extra[sleep$group == 2] )

## building bar plot w/o using Barplot ----

barplot(table(InsectSprays$spray))
plot(InsectSprays$count, type = 'h', lwd=2)


## pie chart: ----

table(InsectSprays$spray)
pie(table(InsectSprays$spray))


# Fasl 4: functions ----
## first function ----
f <- function(x){
  cos(x) - x
}
f(2)
curve(f, -pi,pi)
integrate(f,lower=0,upper=pi)
uniroot(f,c(0,pi))
# uniroot(f,c(-pi,0))
# اروری که به ما میده به این دلیل هست که اگر اول و آخر بازه را در تابع قرار دهیم
# باید یکی مثبت و دیگری منفی باشد ولی اگر هر دو هم علامت باشند ما ارور میگیریم

## Median Function ----
y <- sort(x)
n <- length(y)
if (length(y) %% 2 == 0){
  m <- (y[n/2] + y[n/2 + 1]) / 2
} else {
  m <- y[(n+1) / 2]
}





