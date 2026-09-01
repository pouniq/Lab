from itertools import combinations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer



# ! wget https://raw.githubusercontent.com/ogulcancicek/An-Introduction-to-Statistical-Learning-Python/refs/heads/main/data/Credit.csv
TARGET_COL = 'Balance'



df = pd.read_csv('credit.csv')
df.head()

df['Region'].unique()
df.info()



X = df.drop(columns = TARGET_COL)
y = df[TARGET_COL]

cat_cols = X.select_dtypes(str).columns
num_cols = X.select_dtypes(np.number).columns


for num_col in num_cols:
    plt.figure(figsize=(10,7))
    plt.title(f'boxplot for {num_col}')
    plt.boxplot(df[num_col])
    plt.show()
    


    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,shuffle=True)    


encoder = OneHotEncoder(drop='first',sparse_output=False, handle_unknown='ignore')

preprocessor = ColumnTransformer(
    [
    ('numerical', 'passthrough', num_cols),
    ('categorical',encoder, cat_cols )
    
    ]
)

X_train_encoded = preprocessor.fit_transform(X_train)
X_test_encoded = preprocessor.transform(X_test)


X_train_const = sm.add_constant(X_train_encoded)
model = sm.OLS(y_train, X_train_const).fit()
print(model)

M_0 = np.mean(X_train_encoded)
p = X_train_encoded.shape[1]


############################################

## 6.1

region_encoded = pd.get_dummies(df['Region'],drop_first=True, prefix='Region').astype(int)
df = pd.concat([df, region_encoded], axis = 1)
df = df.drop(columns = 'Region')

mapping = {'No': 0, 'Yes': 1, 'True': 1, 'False': 0}
df['Own'] = df['Own'].map(mapping)
df['Student'] = df['Student'].map(mapping)
df['Married'] = df['Married'].map(mapping)


X = df.drop(columns = 'Balance')
y = df["Balance"]



def best_subset_model(X,y):
    result = {}

    null_rss = np.sum((y-y.mean())**2)
    result[0] = ([],None, null_rss)


    n,p = X.shape
    predictors = X.columns.tolist()
    for k in range(1,p+1):
        
        best_rss = np.inf
        best_subset = None
        best_model = None
        
        for subset in combinations(predictors,k):
            
            X_const = sm.add_constant(X[list(subset)])
            model = sm.OLS(y, X_const).fit()
            ssr = np.sum(model.resid ** 2)
            
            if ssr < best_rss:
                best_rss = ssr
                best_subset = subset
                best_model = model
        
        result[k] = (best_subset, best_model, best_rss.tolist())
        
    return result
    
    

full_model = sm.OLS(y, X).fit()
full_model.summary()
        
best = best_subset_model(X,y)


for k, (subset,model,ssr) in best.items():
    print(f'k: {k} the subset is {subset} and the ssr is {ssr:.2f}')
         


aic = []
bic = []
r2 = []
for k, (subset, model, ssr) in best.items():
    if model is None:
        continue
    aic_score = model.aic
    bic_score = model.bic
    r2_score = model.rsquared_adj
    aic.append(aic_score)
    bic.append(bic_score)
    r2.append(r2_score)
    print(f'for {k}: aic is {aic}')

plt.bar(range(0,11),aic)
plt.bar(range(0,11),bic)
plt.plot(range(0,11),r2)


# the selection is k = 2
# income and rating

