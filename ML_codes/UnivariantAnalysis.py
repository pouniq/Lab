# analysis of a One column to find out about their distributions,...
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

df.columns

# identifying and separating the numerical and categorical columns
num_cols = ['Age' , 'SibSp' , 'Fare' , 'Parch']
cat_cols = ['Sex' , 'Embarked' , 'Survived', 'Cabin', 'Pclass']

# numerical feature analysis.
# when you are training models you need to know that the range of the 
# features are not a issue, so you need to take care of that first.
df[num_cols].head()

# summary statistics
df[num_cols].describe()

# mean, median, mode.
df[num_cols].mean()
df[num_cols].median()
df[num_cols].mode() # most repeated value is not so much useful
# in the world of numerical values, we can use them in categorical 
# data though and it is absolutly fascinating and we can use that for 
# inputations too.


# Variance and standard devation
# how much it is different from the average value
# the advantage of using std is that the result that 
# we get is in the range of our features.

df[num_cols].var()
df[num_cols].std()


# skewness and kurtosis
# how deviated is the feature from the Normal distribution is.
df[num_cols].skew()
df[num_cols].kurtosis()

# histograms

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.hist(df['Age'])

plt.figure(figsize=(10,6))
plt.subplot(2,2,2)
plt.hist(df['Fare'])


plt.figure(figsize=(10,6))
plt.subplot(2,2,3)
plt.hist(df['SibSp'])


plt.figure(figsize=(10,6))
plt.subplot(2,2,4)
plt.hist(df['Parch'])

plt.show()

# -------------------THE IMPORTANCE OF HISTOGRAMS---------------------
# 1)
# why we do this is VERY important, because linear models, 
# like Simple Regression , Logistic Regression work on 
# base and understanding that the data that we provide 
# to the model is Normally distributed and if that assumption
# is not True then we have to do some Transformation to make 
# the data normally Distributed
# 2)
# one of the ways that we can do outlier detection is by
# histograms. we can do that in Box plots too.
# --------------------------------------------------------------------
for col in num_cols:
    plt.figure(figsize=(5,3))
    sns.histplot(df[col] , kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('frequency')
    plt.show()
    

# Boxplots

for col in num_cols:
    plt.figure(figsize=(10,7))
    sns.boxplot(df[col])
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('frequency')
    plt.show()
    
# in regarding that we should or should not drop the outlier is 
# one question that you can ask 'is the value of outliers LOGICAL?'
# because if it is model would struggle to work on real worl scenarios.

# -------------------------------------------------------------------- 
# categorical Feature Analysis.
# Frequency Table
    # with normalize = TRUE we get percentages.
    # binary classification, the data distribution of each class
    # should be equal, we should have equal number of samples for
    # each class, specially the target value.
df['Pclass'].value_counts(normalize=True)

df['Pclass'].value_counts()

for cat in cat_cols:
    print(f'frequency table for {cat}')
    print(df[cat].value_counts())
    print(f'proportion table for {cat}')
    print(df[cat].value_counts(normalize=True))
    print('-'*50)


# countplot
df['Sex']=df['Sex'].replace({'male': 0 , 'female':1})
df['Embarked'].nunique()
df['Embarked']=df['Embarked'].replace({'S': 0 , 'C':1 , 'Q':2})

df['Cabin'].nunique()
# for col in cat_cols:
#     plt.figure(figsize=(10,7))
#     sns.countplot(df[col])
#     plt.title(f'countplot of {col}')
#     plt.xlabel(col)
#     plt.ylabel('count')
#     plt.show()
    
# when we have inbalanced number of rows for a feature then one thing
# that we can do is to join the group similar to each other to have a
# more balanced groups.

# key findings
# capture the finding that you have find in the short summary at
# the bottom of the analysis to remind yourself of what needs to be
# done, to do not forgot about important things that you have found.


