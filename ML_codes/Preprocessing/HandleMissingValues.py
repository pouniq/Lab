import pandas as pd
import numpy as np


df_train = pd.read_csv('train_df.csv')
df_test = pd.read_csv('test_df.csv')


target = "Survived"
X_train = df_train.drop(columns = [target])
y_train = df_train[target]


X_test = df_test.drop(columns = [target])
y_test = df_test[target]



X_train.isna().sum()
y_train.isna().sum()

X_test.isna().sum()
y_test.isna().sum()




X_train.isna().mean() * 100
y_train.isna().mean() * 100

X_test.isna().mean() * 100
y_test.isna().mean() * 100







missing_threshold = 40
missing_percentage = X_train.isna().mean() * 100
missing_values = missing_percentage[missing_percentage > missing_threshold ].index.to_list()


X_train = X_train.drop(columns=missing_values)
y_train = y_train.drop(columns=missing_values)


cols_list = X_train.columns.to_list()
num_cols = ['Age', 'SibSp', 'Fare', 'Parch']
cat_cols = ['Sex', 'Ticket', 'Embarked']


X_train_inputed = X_train.copy(deep=True)
X_test_inputed = X_test.copy()

X_train_inputed.drop(columns=['PassengerId' , 'Name'], inplace = True)


# numeric cols inputation


numeric_medians = {}
numeric_mean = {}

for col in num_cols:
    
    mean = X_train_inputed[col].mean() 
    median = X_train_inputed[col].median()
    
    print(f'Median for {col} is {median}')
    print(f'mean for {col} is {mean}')
    
    numeric_medians[col] = median
    
    print(f'filling the {col} NA with {median}') 
    X_train_inputed[col] = X_train_inputed[col].fillna(median)
    
    X_test_inputed[col] = X_test_inputed[col].fillna(median)

    print('-'*50)
    
    


for col in num_cols:
    if X_train_inputed[col].isnull().sum() == 0:
        continue

    median = X_train_inputed[col].median()
    numeric_medians[col] = median

    X_train_inputed[col] = X_train_inputed[col].fillna(median)
    X_test_inputed[col] = X_test_inputed[col].fillna(median)



#


cat_mode = {}
for col in cat_cols:
    mode_val = X_train[col].mode()[0]
    cat_mode[col] = mode_val
    
    print(f'for {col} the mode is {mode_val} \n')
    X_train_inputed[col] = X_train_inputed[col].fillna(mode_val)
    X_test_inputed[col] = X_test_inputed[col].fillna(mode_val)
    print(f'filled the {col} with the {mode_val}')
    print('-' * 50)
    
    

X_train_inputed.isnull().sum()

X_test_inputed[X_train_inputed.isnull()]['Embarked']




train_df = X_train_inputed
train_df['Survived'] = y_train.values


test_df = X_test_inputed
test_df['Survived'] = y_test.values


train_df.to_csv('train_df_inputed.csv', index= False)
test_df.to_csv('test_df_inputed.csv', index= False)