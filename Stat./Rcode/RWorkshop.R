sum = 0
for (i in 1:100){
  if (i%%2 == 0 ){
    sum = sum + i
  }
}


hi <- function(a,b) a+b
hi(2,3)


##### اگر اندازه بردار ها برابر نباشه ####
# قانون بازیافت
x <- c(3,2,4,45,5)
y <- c(3,2,4,45,5,6,7)
x+y

#### Data Structures #####
x[1:3]

seq(1, 100 , 0.2)


#### Example_2 #####
m <- sample(1:100 , 10)
 
m[m%%2==0]

#### List #####
# you can change the name of each elements in list
# meaning like this

l <- list('hello' , FALSE , c(1,2,4,553,2,14) , 19)
 
names(l) <- c('greeting' , 'Logical' , 'vector' , 'nineteen')
l$vector

#### Matrix #####
# یک نکته ای که هست آر ، سطری پر میکنه اعداد رو 
k <- matrix(1:30 , nrow = 5)
kk <- matrix(1:30 , nrow = 5 , byrow = TRUE)

#### DataFrame #####
df <- as.data.frame(kk)

#### Example_3 #####

df[is.na(df)]
df['V1']
 

#### Visualization #####
# GGPlOT2
# Grammer of Graphics

library(ggplot2)

ggplot(mpg) + geom_point(aes(trans , hwy))


# Diomends
View(diamonds)

ggplot(data = diamonds) + geom_bar(aes(cut))
  




