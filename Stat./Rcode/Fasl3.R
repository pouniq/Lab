# داریم راجب نمودارها در فصل سوم صجبت می کنیم.


# histogram: / هیستوگرام

x<- rnorm(15,3,1)
y<- rnorm(15,3)

plot(x,y, xlab='Tree growth', ylab='Flower growth',
     sub='Tree Vs Flower Growth', col='purple', type='o', xlim=c(2,5),
     ylim = c(1,10), pch = '+', lty= 3, lwd=2, cex.axis = 2)  


# in type we have two s, S one of them go horizontal first then vertical and 
# the other one is doing vice Versa.

# lty: line type: when you put different numbers you get different line 
# types

# lwd: it change the stroke size of our plot

# cex: characther expression, you can combine this with different things in your
# plot

trees['Height']

trees$Height

plot(trees$Height,trees$Volume)
plot(Height~Volume, data=trees)
plot(trees)
pairs(trees)

library(MASS)


cement$y

?plot



# making sequences 

x <- seq(1,5,0.2)
y <- x*sin(x)

plot(x,y,type='l')
# adding layers to your plot

plot(Volume~Girth , data=trees,xlim=c(0,30),ylim=c(-40,40))
# points(c(12,16,19,20) , c(40,20,70,75), pch='$', col='red')
# lines(c(12,16,19,20) , c(40,20,70,75), col='blue')
# y = -30 + 5x
abline(c(-30,5), lty=2, col='purple')


# giving points, characters

plot(Volume~Girth , data=trees)
text(c(12,16,19), c(40,20,70),c('A','B','C'))
?text

# using mouse to select the points
# Interesting Trick
plot(Volume~Girth , data=trees)
text(locator(3),c('A','B','C'))



# Histograms
# distribution of variables
?hist

hist(trees$Height , breaks = 'sturges') # default value for breaks
length(trees$Height)


hist(trees$Height , breaks = seq(60,90,10)) # custom breaks
length(trees$Height)


# with probability set to True we get relative freq
hist(trees$Height , main = 'sturges', col='yellow', border='purple',
     probability = T, label=T, density = 5)

# when we plot=F then we get the detail
hist(trees$Height , plot=F)


# Q-QQ plot
  # Normality: we compare the theory and experimented values to find that
  # if the values are normal or not

qqnorm(trees$Height)
qqline(trees$Height)

  # when doing hypothesis testing we are assuming that our values 
  # are normal then we proceed to do testing, if we don't have 
  # normal then we go and do non-parametric things.


# one of the regression assumptions is that we have normally distributed 
# errors


# categorical vs. numerical 
# boxplot ro bbin
InsectSprays


# pie chart
# barplot
# boxplot
# vionelplot


# to use piechart we need to turn our data to frequency table
tis <- table(InsectSprays$spray)
pie(tis)


names <- c('Rasht', 'Anzali', 'Lahijan', 'Talesh')
pop <- c(1000, 400, 150, 200)

pie(pop,labels = names)

barplot(pop, names = names, col = 'blue', density = 20)



# تمرین -------
airquality
# 1
plot(airquality$Ozone,airquality$Temp)


# 2:
rg <- rgamma(1000,3,5)
hist(rg, probability = T , label=T)
lines(density(rg), lwd = 3, col = 'red')


# 3:

theta <- seq(0, 2*pi, length.out = 1000)

k <- 4  
a <- 1 

r <- a * cos(k * theta)

x <- r * cos(theta)
y <- r * sin(theta)

# رسم
plot(x, y, type = "l", col = "blue", lwd = 2,
     xlab = "X", ylab = "Y", 
     asp = 1)  s
polygon(x, y, col = rgb(1, 1, 0, 0.3))
abline(h = 0, v = 0, col = "gray", lty = 2)
abline(a = 0, b = 1, col = "red", lwd = 2)   # y = x (شیب 1)


# 4:
sleep
boxplot(sleep$extra[sleep$group == 1] , sleep$extra[sleep$group == 2] , 
        horizontal = T )
# the second one is more effective

# 5:
city = c("Kermanshah", "Eslamabad-e Gharb", "Javanrud", "Sonqor", 
         "Sarpol-e Zahab", "Paveh", "Gilan-e Gharb", "Qasr-e Shirin", 
         "Ravansar", "Dalahu", "Harsin", "Kangavar", "Sahneh", 
         "Salas-e Babajani", "Nowdeshah")
population = c(946651, 90440, 54354, 48498, 45281, 
               25868, 22331, 18340, 16816, 15973, 
               14867, 13241, 12800, 8500, 4200)

length(population)
M <- data.frame(city, population)
plot(1:15,M$population, type = 'h', lwd = 3, col = 'red',
     xlab = 'city', ylab = 'population')


plot(x, type="b", col="red", pch=19, lwd=2, main="Sales")

plot(trees$Volume , trees$Girth)
points(50, 15, col = 'blue')
abline(a = -10 , b= 5, col = 'red', lty = 2)
text(locator(1), 'outlier')
lines(c(20,80), c(20,10), col = 'green')


hist(trees$Volume, breaks = 8, probability = T)
hist(trees$Volume, breaks = 8, freq = F)

?hist
s <- 0 
for (i in 1:100){
  s <- s + i
}
s

sum(1:100)

function(n){
  for(i in n){
    
  }
}

f <- function(x){
  x^3 - 3*x +1
}

curve(f, -3, 3)
uniroot(f , c(-2,2))

integrate(f,0 , 2)
