# Outliers are extreme values that would clutter ou
# machine learning models and make it more difficult


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('train.csv')

num_cols = ['Age' , 'SibSp' , 'Fare' , 'Parch']
cat_cols = ['Sex' , 'Embarked' , 'Survived', 'Cabin', 'Pclass']

df_num = df[num_cols]

# using boxplot to select outlier
# we are taking the IQR and we will see if there is outliers our not.

for col in num_cols:
    plt.figure(figsize=(10,7))
    sns.boxplot(x = df[col])
    plt.title(f'boxplot of {col}')
    plt.show()

df['Age'].quantile(0.25)
# IQR method:
# when we multiple + and - 1.5 of IQR we get the whiskers of boxplot
def iqr_bounds(series, factor=1.5):
        q1 = series.quantile(0.25)
        q2 = series.quantile(0.75)
        iqr = q2 - q1
        lower_bound = q1 - factor * iqr
        upper_bound = q2 + factor * iqr

        return lower_bound, upper_bound, iqr

iqr_bounds(df['Age'])


for col in num_cols:
    col_clean = df_num[col].dropna()
    lower, upper , iqr = iqr_bounds(col_clean)
    outlier_mask = (col_clean > upper) | (col_clean < lower)
    num_outlier = outlier_mask.sum()
    total = col_clean.shape[0]
    
    print(f'IQR analysis for {col}')
    print(f'lower bound {lower:.2f}')
    print(f'Upper bound {upper:.2f}')
    print(f'IQR: {iqr}')
    print(f'we have {num_outlier} outliers out of {total}')
    print('-'*50)


# Z-score method of outlier detection.
# |Z| = (x - mean(x)) / std(x)
# if the distribution is normal then if each vale is larger than 3 or 
# -3 then we have outlier.

z_threshold = 3.0
for col in num_cols:
    col_clean = df_num[col].dropna()
    mean = col_clean.mean()
    std = col_clean.std()
    z_score = (col_clean - mean) / std
    outlier_mask = np.abs(z_score) > z_threshold
    num_outlier = outlier_mask.sum()
    total = col_clean.shape[0] 

    print(f'IQR analysis for {col}')
    print(f'mean: {mean} , std: {std}')
    print(f'threshold: {z_threshold}')
    print(f'outlier {num_outlier} in {total}')
    print('-'*50)
    
# in Z-score method the assumpation that our data is normally distributed
# could not be broken.

# Statistics measures with or without outliers

fare_clean = df['Fare'].dropna()
lower_fare , upper_fare , Iqr_fare = iqr_bounds(fare_clean)
fare_inliners = fare_clean[(fare_clean >= lower_fare ) & (fare_clean <= upper_fare)]

print(f'Max {fare_clean.max()}, min: {fare_clean.min()}')
print(f'Mean {fare_clean.mean()}, Median: {fare_clean.median()}')
print("After deleting Outliers from our Fare column")
print(f'Max {fare_inliners.max()}, min: {fare_inliners.min()}')
print(f'Max {fare_inliners.mean()}, min: {fare_inliners.median()}')







