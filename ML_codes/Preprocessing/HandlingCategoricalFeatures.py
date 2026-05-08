import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder



train_df = pd.read_csv('train_df_inputed.csv')
test_df = pd.read_csv('test_df_inputed.csv')


X_train = train_df.drop(columns=['Survived'])
y_train = train_df['Survived']




X_test = test_df.drop(columns=['Survived'])
y_test = test_df['Survived']




X_test = X_test.drop(columns=['PassengerId'])
X_train = X_train.drop(columns=['PassengerId'])



num_cols = ['Age', 'SibSp', 'Parch', 'Fare']
cat_cols = ['Pclass', 'Sex' , 'Embarked']



 
 
 
 