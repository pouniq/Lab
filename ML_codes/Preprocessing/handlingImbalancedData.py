import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE



df = pd.read_csv('diabetes.csv')

X = df.drop(columns='Outcome')
y = df['Outcome']


X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    random_state=43,
                                                    test_size=0.2,
                                                    stratify=y
                                                    )


y_train.value_counts()


rus = RandomUnderSampler(random_state=42)
X_train_rus, y_train_rus = rus.fit_resample(X_train, y_train)

y_train_rus.value_counts()




ros = RandomOverSampler(random_state=42)
X_train_ros , y_train_ros = ros.fit_resample(X_train, y_train)
y_train_ros.value_counts()





smote = SMOTE()
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)


