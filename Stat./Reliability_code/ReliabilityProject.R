##### Description.
# In This code I want to implement what I had learned in
# Reliability Course in University, with main focus of 
# Reliability Data Analytics.
install.packages(c("knitr", "dplyr", "survival", "ggplot2", "here", "tibble"))
library(knitr)
library(dplyr)
library(survival)
library(ggplot2)
library(tibble)

lung[,c('time','status','age','sex')]
# time: survival time in days
# the 1 means censored data and 2 means dead (failure)
# 1 mean male , 2 mean female

# to make this easier for myself I turned censored data to 0 and failure to 1
# and made male to 0 and female to 1
lung <-
  lung |> 
  mutate(
    status = recode(status, `1` = 0, `2` = 1),
    sex = recode(sex, `1` = 0, `2` = 1)
  )

head(lung[,c('time','status','age','sex')])


date_ex <- 
  tibble(
    sx_date = c("2007-06-22", "2004-02-13", "2010-10-27"), 
    last_fup_date = c("2017-04-15", "2018-07-04", "2016-10-31")
  )

date_ex

