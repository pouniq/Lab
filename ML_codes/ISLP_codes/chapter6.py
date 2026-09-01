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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True,random_state=42)

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
    
    

full_model = sm.OLS(y_train, X_train).fit()
full_model.summary()
        
best = best_subset_model(X_train,y_train)


for k, (subset,model,ssr) in best.items():
    print(f'k: {k} the subset is {subset} and the ssr is {ssr:.2f}')
         


aic = []
bic = []
r2 = []
for k, (subset, model, ssr) in best.items():
    if model is None:
        continue
    
    model = model.predict(y_test, X_test)
    aic_score = model.aic
    bic_score = model.bic
    r2_score = model.rsquared_adj
    aic.append(aic_score)
    bic.append(bic_score)
    r2.append(r2_score)
    print(f'for {k}: aic is {aic}')

plt.plot(range(0,11),aic)
plt.plot(range(0,11),bic)
plt.plot(range(0,11),r2)


# the selection is k = 2
# income and rating


## 6.2



def make_sub_pred(chosen_cols,X,y):
    
    X_const = sm.add_constant(X[chosen_cols])
    model = sm.OLS(y,X_const).fit()
    r2 = model.rsquared
    
    return r2.tolist()

make_sub_pred(['Age','Rating'],X_train,y_train)


best_subset = []
best_model = None
best_r2 = -np.inf

predictors = X_train.columns.tolist()
print(predictors)



used_predictors = []
models = {0:{'subset': [], 'r2':None}}
p = len(predictors)

for k in range(p):
    r2_result = {}
    for col in predictors:
        if col not in used_predictors:
            columns = used_predictors + [col]
            r2 = make_sub_pred(columns,X_train,y_train)
            r2_result[col] = r2
        
    best_set = max(r2_result,  key=r2_result.get)
    best_r2 = r2_result[best_set]
    
    used_predictors = used_predictors + [best_set]
    models[k+1] = {'subset': used_predictors.copy(), 'r2':best_r2 }

for k, det in models.items():
    print(k, det['subset'], det['r2'])
    
    

ks = list(models.keys())
r2s = [models[k]['r2'] for k in ks]

plt.plot(ks, r2s, marker='o')
plt.xlabel('Number of predictors (k)')
plt.ylabel('R²')
plt.title('Forward Stepwise Selection: R² vs. Model Size')
plt.show()
