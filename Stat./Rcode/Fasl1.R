
##### 
# practices:
# install.packages('maps')
# 1
library(maps)
map('world','iran')


# 2
a = 5
b = 7
c = a^2 + b^2
c <- sqrt(c)
c
# R: 8.602325


# 3
a <- 1
b <- -1
c <- 1
l <- b^2 - 4 * a * c

root <- (-b + sqrt(as.complex(l))) / (2*a)
roott <- (-b - sqrt(as.complex(l))) / (2*a)
cat(root, roott)


# 4
install.packages('polyroot')
?polyroot
polyroot(c(1,-1,1))
polyroot(c(1,-1,1))



# 5
cos(2*atan(1))
# 6.123234e-17

# 6
5 < 7 || 4 == 3
# گزاره های منطقی دوتایی فقط آیتم های اولی را باهم مقایسه می کند
# اما عامل های منطقی همه آیتم ها را یک به یک با هم مقایسه می کند

# 7
??aporpos
apropos('student')



dnorm(0,1)
dt(0,5)


# 8
qcauchy(0.025)
qcauchy(0.975)


