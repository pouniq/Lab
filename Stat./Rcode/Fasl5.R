# X1, X2, ..., Xn (متغیرهای تصادفی)
# x1,x2, ..., xn (مشاهدات)

# MLE ----
## اول از همه ما تابع درستنمایی را می نویسیم بعد از آن تحت پارامترهای آن 
## آن را ماکزیمم می کنیم
obs <- c(82, 87, 88, 85, 91,87, 88, 72, 91, 92, 95, 
         86, 82, 84, 91, 94, 86, 97, 86, 83, 82, 83, 71, 79, 83 )
?fitdistr
# یک متغیره هست
library(MASS)
mu.hat <- mean(obs)
v.hat <- sd(obs)

v.xbar <- v.hat^2 / length(obs)


# خروجی هایی که به ما میده توی پرانتز انحراف معیار توزیع مجانبی از میانگین و واریانس هست
# توزیع هایی که توی آر شناخته شده هستند قابل استفاده می باشند
fbs.fit1 <- fitdistr(obs , 'normal')
fbs.fit2 <- fitdistr(obs , 'cauchy')

?fitdistr


## توزیع گامبل ----
dgumble <- function(x, mu, sigma){
  exp(-(x-mu)/ sigma - exp(-(x-mu)/sigma))/sigma
}


## برآورد گشتاوری ----
# در اینجا برآورد گشتاوری رو دادیم به عنوان اعداد اولیه و شروع

sigma0 <- sqrt(6) / pi * sd(obs)
mu0 <- mean(obs) - 0.57 * sigma0


fit.dist.g <- fitdistr(obs, dgumble, start = list(mu = mu0, sigma = sigma0))
# we need initial values when optimizing custom functions)

logLik(fit.dist.g)


# AIC & BIC
# AIC: -2logl(\hat{\theta}) + 2 * k
# BIC: -2logl(\hat{\theta}) + k * logn
# اون مدلی که کمتره، مدلی بهتری است

AIC(fit.dist.g)
AIC(fbs.fit2)



# نرمال بودن توزیع جامعه ----

## شاپیرو ویلک --- صرفا برای نرمال بودن --- متداول ترین برای توزیع نرمال----
# H0: نرمال بودن
# H1: نرمال نبودن

shapiro.test(obs)
# فرض صفر رد نشد
# یعنی نرمال هست

## ازمون کلموگروف - اسمیرنوف ----
# برای هر توزیعی به علاوه نرمال استفاده میشود

ks.test(obs, 'pnorm')
# H0: نرمال بودن
# H1: نرمال نبودن --- میتونیم بزرگ یا کوچکی را خودمون تعیین کنیم
# اینجا گفته که مشاهدات ما توزیع نرمال نیستند

ks.test(obs, 'pnorm', mean= mean(obs), sd= sd(obs))
# ولی برای این میانگین و واریانس ها نرمال بودن قبول می شود
# warning: به دلیل اینکه داده های تکراری داریم 



# F(t) < F(t_0)
ks.test(obs, 'pnorm', mean= mean(obs), sd= sd(obs), alternative= 'less')


# F(t) > F(t_0)
ks.test(obs, 'pnorm', mean= mean(obs), sd= sd(obs), alternative= 'greater')


# exponential 
# H0 is rejected
ks.test(obs, 'pexp', rate= 1/mean(obs))


# آزمون فرض برای میانگین و واریانس ----
# H0 : \mu = 90
# H1: \mu != 90\
# آزمون تی زمانی استفاده می شود که نرمال بودن تایید شود
t.test(obs, mu = 90)
# H0 is rejected then \mu is not equal to 90
# we can change the confidence level
t.test(obs, mu = 90, conf.level = 0.9)



# به جای میانگین از میانه استفاده می کنیم 
# آزمون های ویلکاکسون  
# میانگین مرکزی : میانه است 
# برای آزمون کردن میانه داده ها از آزمون ویلکاکسون استفاده می کنیم
# تصحیح پیوستگی
# H0 : \mu = 90
# H1: \mu != 90
# ناپارامتری دکتر بهبودیان

wilcox.test(obs, mu=90)

wilcox.test(obs, mu=90, alternative = 'greater')


# correct = F : میگه که از تصحیح پیوستگی استفاده نکن
wilcox.test(obs, mu=90, alternative = 'greater', correct = F)



# Example
# بررسی واریانس های دو نمونه
x1 <- c(12,13,32,23,33,37,25,16,19,20,25)
x2 <- c(43,54,38,55,58,45,44,57,56,48,50)
t.test(x1,x2)
# H0 is rejected & we accept H1.
t.test(x1,x2, mu=90)
t.test(x1,x2, mu=90, alternative = 'less')
t.test(x1,x2, var.equal = T)





