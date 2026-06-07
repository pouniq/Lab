import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    recall_score
)

df = pd.read_csv('diabetes.csv')

df.shape

df['Outcome'].value_counts(normalize=True)

X = df.drop(columns='Outcome')
y = df['Outcome']


# K-fold Setup

kf = KFold(n_splits=5, shuffle=True, random_state=42)

# loop through the fold that we created
    # Understanding Folds
    # we get the fold number

for fold, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
    print(fold)
    print(len(train_idx))
    print(len(test_idx))
    print(train_idx[:5])
    print(test_idx[:5])
    print('----'*50)
    
    
# how enumerate works?
# it gives things index in tupple form.
a = [1,2,3,4]
for i, val in enumerate(a, start=1):
    print(f'index {i} is equal to {val}')
    
    


acc_list = []
precision_list = []
f1_list = []
recall_list = []
roc_auc_list = []


for fold, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
    # we split the data here
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    # scale the data after spliting:
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
   
   
    # train the model:
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)
    
    # getting the prediction:
    y_train_pred = model.predict(X_train)
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test)
    
    # metrics:
    
    acc = accuracy_score(y_test, y_pred)    
    f1 = f1_score(y_test, y_pred)    
    recall = recall_score(y_test, y_pred)    
    roc_auc = roc_auc_score(y_test, y_pred)    
    prec = precision_score(y_test, y_pred)    
    
    # store metrics:
    acc_list.append(acc)
    precision_list.append(prec)
    f1_list.append(f1)
    roc_auc_list.append(roc_auc)
    recall_list.append(recall)
    
    print(f'fold: {fold}')
    print(f'accuracy {acc :.3f}')
    print(f'precision {prec :.3f}')
    print(f'f1 score {f1 :.3f}')
    print(f'roc_auc {roc_auc :.3f}')
    print(f'recall  {recall :.3f}')
    print('----'*50)
      
    
    
    
print(np.mean(acc_list) * 100)
print(np.mean(f1_list)) 
print(np.mean(precision_list)) 
print(np.mean(roc_auc_list)) 
print(np.mean(recall_list)) 
    
    
    