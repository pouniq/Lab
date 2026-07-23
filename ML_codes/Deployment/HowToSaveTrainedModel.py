# models are trained once and used multiple times
# save the trained model as local file
# - joblib
# - pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

CSV_PATH = 'diabetes.csv'
TARGET_COL = 'Outcome'

df = pd.read_csv(CSV_PATH)
df[TARGET_COL].value_counts()

df.isnull().sum()

# all the missing values have been encoded with 0

X = df.drop(columns = ['Outcome'])
y = df[TARGET_COL]


X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model_pip = Pipeline(
    [
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(class_weight='balanced'))
    ]
)

model_pip.fit(X_train, y_train)

X_train_pred = model_pip.predict(X_train)
y_pred = model_pip.predict(X_test)
accuracy_score(y_pred , y_test)


## how to save the model ? ##
from joblib import dump

# path where model's file need to be saved
# we give the absolute path
# we need to create .joblib at the end too
joblib_path = "/Users/pouniq/Lab/ML_codes/Deployment/model_dir/diabetes_logistic.joblib"
 

# provide name for the model

# save the pipeline
dump(model_pip, joblib_path)
print(f"Saved with Joblib -> {joblib_path}")

