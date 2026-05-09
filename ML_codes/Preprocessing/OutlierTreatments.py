import pandas as pd
import numpy as np
import seaborn as sns


df_train = pd.read_csv('train_enc.csv')
df_test = pd.read_csv('test_enc.csv')

X_train = df_train.drop(columns='Survived')
y_train = df_train['Survived']


X_test = df_test.drop(columns='Survived')
y_test = df_test['Survived']




sns.boxplot(X_train['Age'])
sns.boxplot(X_train['Fare'])


valid_outlier_cols = ['Age', 'Fare']

def iqr_bounds(series):
    
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    iqr = Q3 - Q1
    lower = iqr - 1.5 * Q1
    upper = iqr + 1.5* Q3
    return lower, upper
    
    

def compute_train_bounds(df, cols):
    bounds = {}
    for col in cols:
        low, high = iqr_bounds(df[col])
        bounds[col] = (low, high)
    return bounds


def cap_outliers_with_bounds(df, bounds):
    df_capped = df.copy()
    for col, (low,high) in bounds.items:
        df_capped[col] = np.where(df_capped[col] < low, low, df_capped[col])
        df_capped[col] = np.where(df_capped[col] > high, high, df_capped[col])
    return df_capped


compute_train_bounds(X_train, valid_outlier_cols)



# App;u

