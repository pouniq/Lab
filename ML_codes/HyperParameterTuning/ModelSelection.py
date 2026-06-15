import numpy as np
import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score,
    GridSearchCV
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv('diabetes.csv')
df

X = df.drop(columns='Outcome')
y = df['Outcome']


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    stratify=y,
    test_size=0.2,
    random_state=42
)

# stratified K-fold
k = 5
cv = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)

# Model Selection 

models = {
    'LogisticRegression':  LogisticRegression(),
    'SVC': SVC(),
    'RandomForestClassifier': RandomForestClassifier()
}

cv_scores = {}
for name, model in models.items():
    # pipeline: Scaler + model
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])
    # Cross validation scores
    scores = cross_val_score(
        
        estimator= pipeline,
        X = X_train,
        y = y_train,
        cv = cv,
        scoring= 'accuracy'
    )
    print(f'{name} - cross val scores: {scores}')
    cv_scores[name] = scores.mean()
    
    # mean_cross_val_scores
        
    print(cv_scores)
    print(name)
    print(f'Mean CV accuracy {scores.mean():.3f}')
    print('-'*50)
    # Logistic Regression have the best CV accuracy
   
best_model = max(cv_scores, key=cv_scores.get)
print(f'best selected model is {best_model}') 

# Hyper Parameter Tuning 
# GridSearchCV
# we used the best model from the previous section

param_grid = {
    'LogisticRegression': {
        'model__C': [0.01,0.1,1,10] # we specifiy to the model parameter to not confused them in StandardScaler
        
    },
    'SVC' : {
        'model__C': [0.1,1,10],
        'model__kernel': ['linear', 'rbf']
    },
    'RandomForestClassifier': {
        'model__n_estimator': [100,300,500],
        'model__max_depth': [None, 5, 10],
        'model__min_samples_split': [2,5,10]
    }
}





# Create Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', models[best_model])
])


grid_search = GridSearchCV(
    estimator= pipeline,
    param_grid= param_grid[best_model],
    cv = cv,
    scoring= 'accuracy',
    n_jobs= -1
)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print('best CV Accuracy score', grid_search.best_score_)


# final evaluation on unseen data
y_pred = best_model.predict(X_test)
y_test

print('final best test score' , accuracy_score(y_test, y_pred))

# great trick
print(classification_report(y_test, y_pred))







