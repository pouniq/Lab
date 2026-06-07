library(MASS)
attach(cement)
# first we construct the ANOVA table

fit <- lm.ridge(y ~ x1 + x2 + x3 + x4 , data = cement , lambda = seq(0,1,by=0.01))

plot(fit) 
matplot(as.matrix(fit$coef), type = "l", lty = 1, 
        xlab = "Lambda Index", ylab = "Coefficients", 
        main = "Ridge Trace Plot")

lm.ridge(y ~ x1 + x2 + x3 + x4 , data = cement , validation = cv)

# useful libraries:
# library(ridge)
# library(glmnet)