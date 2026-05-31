# https://www.youtube.com/watch?v=Bubo_7R7h0Q&t=1164s
# kaplan-meier analysis (Non-parametric)
# Life Table
# cox proportional Hazards model (SemiParametric)
# statistical assumptions:
  # 
# Censoring: Right Censoring
library(asaur)

# یک دیتای که راجب بازگشتن به مصرف سیگار است بعد از مدتی دوری از آن
df <- pharmacoSmoking
head(df)

#  متغیری است که نشان دهنده سنسور سمت راست داده های ماستrelapse  
# if the value is 0 the data is censored,  and if the value is 1 the relapse happened 
# to them.


# checking the distribution
hist(df$ttr) 
hist(subset(df$ttr, df$relapse == 1))
hist(subset(df$ttr, df$relapse == 0 ) , xlim = c(0,200) ) 

head(df[,c('ttr','relapse')])
 


Surv2(df$ttr, df$relapse)





# Kaplan-Meier Analysis
library(survival)
km_1 <- survfit(Surv(ttr, relapse) ~ 1 ,
                data = df,
                type = 'kaplan-meier')
print(km_1)

# how many subjects we have in our dataset? (125)
# the events in the km_1 output is saying that how many
# people actually experienced the event (relapsed) before
# the end of the experiment. (89)
# the lower & upper bound for our confidence interval. (between 25 to 75)
 


# when we put ~ 1 in there we are saying that return a null model
# a model without a covariance

summary(km_1)

# summarize KM results. (by time intervals) (create a life table)
# seasonal pattern
summary(km_1, times= c(0,12, 24, 36, 48, 60))

# plot cumulative survival rates
plot(km_1)


# install something visually better plot
# install.packages('survminer')
library(survminer)
ggsurvplot(km_1,
           data=df,
           risk.table = TRUE,
           conf.int = TRUE,
           ggtheme = theme_bw())


# plot with categorical covariate.


km_2 <- survfit(Surv(ttr, relapse) ~ levelSmoking ,
                data = df,
                type = 'kaplan-meier',
                )

ggsurvplot(km_2,
           data=df,
           risk.table = TRUE,
           conf.int = TRUE,
           ggtheme = theme_bw(),
           pval = T,
           pval.method = T)



km_3 <- survfit(Surv(ttr, relapse) ~ ageGroup2 ,
                data = df,
                type = 'kaplan-meier',
)

ggsurvplot(km_3,
           data=df,
           risk.table = TRUE,
           conf.int = TRUE,
           ggtheme = theme_bw(),
           pval = T,
           pval.method = T)




km_4 <- survfit(Surv(ttr, relapse) ~ ageGroup4 ,
                data = df,
                type = 'kaplan-meier',
)

ggsurvplot(km_4,
           data=df,
           risk.table = TRUE,
           conf.int = TRUE,
           ggtheme = theme_bw(),
           pval = T,
           pval.method = T)



# Cox regression model (PH), proportional hazards
cox_reg0 <- coxph(Surv(ttr, relapse) ~ 1,
                  data = df)
summary(cox_reg0)

####


cox_reg1 <- coxph(Surv(ttr, relapse) ~ ageGroup4,
                  data = df)
summary(cox_reg1)

# the concordance and usually the logrank test show us that
# when we provide the categorical data is it significently 
# different than the null model when we set ~1 ?
# it will compare it to the first one.
 

cox_reg2 <- coxph(Surv(ttr, relapse) ~ ageGroup4 + yearsSmoking + grp,
                  data = df)
summary(cox_reg2)

head(df)



cox_reg3 <- coxph(Surv(ttr, relapse) ~ age + grp ,
                  data = df)
summary(cox_reg3)


# to do our prediction we need to grand mean center our values
# to make them useful.

# logOverAllRisk = -0.03529 * age + ... 


# nested comparison
# we do ANOVA to compare these models
library(tidyr)


cox_reg2 <- coxph(Surv(ttr, relapse) ~ ageGroup4 + yearsSmoking + grp,
                  data = df)

cox_reg3 <- coxph(Surv(ttr, relapse) ~ age + grp ,
                  data = df)

 

anova(cox_reg2, cox_reg3)




