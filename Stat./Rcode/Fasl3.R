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
