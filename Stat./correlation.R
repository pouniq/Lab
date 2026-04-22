#----
# correlations
library(ggplot2)
data('iris')
head(iris)
plot(iris$Sepal.Length , iris$Sepal.Width)

ggplot(iris , aes(Sepal.Length , Sepal.Width ,color=Species)) + 
  geom_point() + theme_bw()

pnorm(2.72)
