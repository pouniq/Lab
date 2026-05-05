rm(list=ls())
# setwd('Documents/term6/Regression2') you can set the 
# directory that you want to work on here, to get rid of
# the hassle of going through files and other things.
df <- read.table('p060.txt', header=TRUE)
attach(df)

model <- lm(Y~.,data = df)
summary(model)


# ANOVA table

AnovaModel <- as.matrix(df[2:7])
anova(lm(Y ~ AnovaModel , df))


# What i've learned from this code:
# when you put dot (.) it means get all the columns
# in the dataset to be our independent variables.
#
# header = TRUE:
# when header is TRUE then we have our dataset with the corresponding
# column names.
# 
# Attach:
# 

