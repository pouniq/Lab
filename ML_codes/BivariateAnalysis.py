# In the analysis of data and knowing about the dataset
# one the ways to deeper our understanding about our data
# is to do bivariate analysis meaning finding out about the relationships
# they have with each other, we can catogrize them into 3 groups.
# numerical by numerical , numerical by categorical, categorical by categorical.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr # correlation coeficients

df = pd.read_csv('train.csv')


num_cols = ['Age' , 'SibSp' , 'Fare' , 'Parch']
cat_cols = ['Sex' , 'Embarked' , 'Survived', 'Cabin', 'Pclass']

df_num = df[num_cols].dropna()
df_num.head()
df['Survived_label'] = df['Survived'].map({0:"No" , 1:'Yes'})


# numerical Vs numerical features.
# scatter plot.
# create the numerical pairs.

num_pairs = [
    ('Age', 'Fare'),
    ('Age', 'Parch'),
    ('Age' , 'SibSp'),
    ('SibSp' , 'Fare'),
    ('SibSp' , 'Parch'),
    ('Fare' , 'Parch')
]

for x,y in num_pairs:
   plt.figure(figsize=(5,3)) 
   sns.scatterplot(x = df[x] , y=df[y])
   plt.title(f'{x} vs. {y}')
   plt.xlabel(x)
   plt.ylabel(y)
   plt.show()

# in this dataset we do not have a very strong relation between our
# numerical values we need to find out about correlations too.

# Correlation Matrix.
# as we all know, the correlation range from -1 to +1 
# if one unit increases other unit decreases by the factor of the correlation

cor = df[num_cols].corr()
sns.heatmap(cor)
   
# there is one concept called ??multicolinarity??, it is where the correlation 
# is close to +1 (positive correlation).

# Pearson Correlation coeficient
# the r is the correlation coeficient and the p is the pValue.
# if the p is less than 0.05 then we have a strong confidence
# and if the pValue is higher than 0.05 then we it is a random coincidence

for col in num_cols:
    if col != 'Fare':
        r, p = pearsonr(df_num[col] , df_num['Fare'])
        print(f'for {col} vs Fare the r is {r:.3f} and p is {p:.3f}')

    
# Numerical vs Categorical

plt.figure(figsize=(5,3))
sns.boxplot(x = df['Survived_label'] , y= df['Age'])
plt.title('survived vs age boxplot')


num_for_box = ['Age' , 'Fare']
cat_for_box = ['Survived_label' , 'Sex' , 'Pclass']


for num in num_for_box:
    for cat in cat_for_box:
        plt.figure(figsize=(7,5))
        sns.boxplot(x = df[cat], y = df[num])

# Grouped statistics
df_num.groupby(df['Survived_label']).mean()


# A more detailed Group statistics

for cat in ['Survived_label' , 'Sex' , 'Pclass']:
    print(f'Group statistics by fare and {cat}')
    print(df.groupby(cat)['Fare'].mean())
    print('-'*50)


# Categorical vs Categorical Features

# crosstabs examples
# that is intersting data that we got from the data:
print(pd.crosstab(df['Sex'] , df['Survived_label']))
print(pd.crosstab(df['Pclass'] , df['Survived_label']))
# we will uderstand why that model behaved like that, it is not black box NO MORE
# with more understanding and information we have better understanding about the pattern
# in our data

# countplot:
plt.figure(figsize=(10,7))
sns.countplot(x = df['Sex'] , hue= df['Survived_label'])
plt.title('Survived vs Sex')
plt.show()



plt.figure(figsize=(10,7))
sns.countplot(x = df['Pclass'] , hue= df['Survived_label'])
plt.title('Survived vs Sex')
plt.show()












