import numpy as np
import pandas as pd
from scipy.stats import loguniform
from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


df = pd.read_csv('diabetes.csv')
df

# check missing values
df.isnull().sum()


# making X, y:
X = df.drop(columns='Outcome')
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# creating a Pipeline
# (scaler + model)

pipeline = Pipeline(
    [
        ('scaler', StandardScaler()),
        ('model', SVC())
    ]
)

# GridSearchCV
# it will tries all parameters

param_grid = [
    {
        # when you have different things on your pipeline
        # you need to specify what parameter you are targeting
        # with PARAMETERNAME__  (DOUBEL UNDERSCORE)
        'model__kernel': ['linear'],
        'model__C': [0.1,1,10,100]
    },
    {
        'model__kernel': ['rbf'],
        'model__C': [0.1,1,10,100],
        'model__gamma': ['scale','auto',0.01,0.1,1]
    },
    {
        'model__kernel': ['poly'],
        'model__C': [0.1,1,10],
        'model__gamma': ['scale', 'auto', 0.01,0.1],
        'model__degree': [2, 3, 4]
    } ]


grid = GridSearchCV(
    estimator= pipeline,
    param_grid= param_grid,
    cv = 5,
    scoring= 'accuracy',
    return_train_score= True,
    n_jobs= -1 # running in parallel, GPU run doing tasks in parallel 
)

grid.fit(X_train, y_train)

print('gridSearchCV results:')
print('Best Params', grid.best_params_)
print('Best Cross validation Score  (average)', grid.best_score_)


test_acc = grid.score(X_test, y_test)
print('test Accuracy', test_acc)

# analysing Results:
grid_result_cv_df = pd.DataFrame(grid.cv_results_)
# select only useful columns

grid_result_cv_df = grid_result_cv_df[['params', 'mean_train_score','mean_test_score','rank_test_score']].sort_values('rank_test_score')
grid_result_cv_df 
len(grid_result_cv_df)




param_dist = [
    {
        # when you have different things on your pipeline
        # you need to specify what parameter you are targeting
        # with PARAMETERNAME__  (DOUBEL UNDERSCORE)
        'model__kernel': ['linear'],
        'model__C': loguniform(0.01, 100)
    },
    {
        'model__kernel': ['rbf'],
        'model__C': loguniform(0.01, 100),
        'model__gamma': loguniform(0.0001, 100)
    },
    {
        'model__kernel': ['poly'],
        'model__C': loguniform(0.01, 100),
        'model__gamma':loguniform(0.0001, 100)
    } ]


random_e = RandomizedSearchCV(
    estimator= pipeline,
    param_distributions=param_dist,
    n_iter=20,
    cv = 5,
    scoring= 'accuracy',
    return_train_score= True,
    n_jobs= -1 
)

random_e.fit(X_train, y_train)


print('RadomSearch CV results:')
print('Best Params', random_e.best_params_)
print('Best Cross validation Score  (average)', random_e.best_score_)


test_acc_r = grid.score(X_test, y_test)
print('test Accuracy', test_acc_r)


ran_result_cv_df = pd.DataFrame(random_e.cv_results_)
# select only useful columns

ran_result_cv_df = ran_result_cv_df[['params', 'mean_train_score','mean_test_score','rank_test_score']].sort_values('rank_test_score')
ran_result_cv_df 
len(grid_result_cv_df)

