h <- scan()
h

##### 
# practices:
# 1
d <- c(81.8,69.3,76.4,61.7,76.9,76.5,74.8,68.9,62.7,76.5)
mean(d)
median(d)
sd(d)
cv <- max(d) - min(d)
cv

#2
x <- c(1,0.5,01)
mu <- c(0.25,-0.25,0)
sig <- matrix(c(9,0,-1,0,7,2,-1,2,5),nrow=3)

f <- function(x,mu,sig){
  1 / (sqrt((2*pi)^3 * det(sig))) * exp(-0.5 %*% t((x - mu)) %*% solve(sig) %*% (x-mu))
}
f(x,mu,sig)


# 3


X <- matrix(rnorm(100),ncol=5)

X %*% solve(t(X) %*% X) %*% t(X)


# 4
df_sorted <- airquality[order(airquality$Temp), ]
df_sorted



# 5
iran_provinces <- c(
  "Alborz", "Ardabil", "Bushehr", "Chaharmahal and Bakhtiari", 
  "East Azerbaijan", "Esfahan", "Fars", "Gilan", "Golestan", 
  "Hamadan", "Hormozgan", "Ilam", "Kerman", "Kermanshah", 
  "Khuzestan", "Kohgiluyeh and Boyer-Ahmad", "Kurdistan", 
  "Lorestan", "Markazi", "Mazandaran", "North Khorasan", 
  "Qazvin", "Qom", "Razavi Khorasan", "Semnan", 
  "Sistan and Baluchestan", "South Khorasan", "Tehran", 
  "West Azerbaijan", "Yazd", "Zanjan"
)

iran_pop <- c(
  2712400, 1270420, 1163400, 947763, 
  3909652, 5120850, 4851274, 2530696, 1868819, 
  1738234, 1776415, 580158, 3164718, 1952434, 
  4710509, 713052, 1603011, 1760649, 1429475, 
  3283582, 863092, 1273761, 1292283, 6434501, 
  702360, 2775014, 768898, 13267637, 3265219, 
  1138533, 1057461
)

dfIran <- data.frame(iran_provinces,iran_pop )

?Dataframe







