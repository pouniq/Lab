import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder



train_df = pd.read_csv('train_df_inputed.csv')
test_df = pd.read_csv('test_df_inputed.csv')



target = 'Survived'
X_train = train_df.drop(columns=['Survived'])
y_train = train_df['Survived']


X_test = test_df.drop(columns=['Survived'])
y_test = test_df['Survived']


# X_test = X_test.drop(columns=['PassengerId'])
# X_train = X_train.drop(columns=['PassengerId'])

# the REAL WORK IS BELOW:

num_cols = ['Age', 'SibSp', 'Parch', 'Fare']
cat_cols = ['Pclass', 'Sex' , 'Embarked']

for cat in cat_cols:
    print(f'{cat}, {X_train[cat].unique()} \n ' )
    

binary_or_ordinal_columns = ['Sex', 'Pclass'] # label enc
nominal_columns = ['Embarked'] # hot enc

X_train_enc = X_train.copy()
X_test_enc = X_test.copy()


Label_enc = {}

for col in binary_or_ordinal_columns:
    le = LabelEncoder()
    le.fit(X_train[col])
    Label_enc[col] = le
    # this line code make the labelEncoders separated from each other
    # with this line specific label encoders are placed with specific columns
    
    X_train_enc[col] = le.transform(X_train[col])
    X_test_enc[col] = le.transform(X_test[col])
    
    
X_train_enc



ohe = OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False)
ohe.fit(X_train[nominal_columns])
train_ohe = ohe.transform(X_train[nominal_columns])
test_ohe = ohe.transform(X_test[nominal_columns])

ohe_cols = ohe.get_feature_names_out(nominal_columns)
print('oneHotEncoder columns: ', ohe_cols)


train_ohe_df = pd.DataFrame(train_ohe , columns=ohe_cols, index=X_train.index)
test_ohe_df = pd.DataFrame(test_ohe , columns=ohe_cols, index=X_test.index)


X_train_enc = X_train_enc.drop(columns=['Ticket'])
X_test_enc = X_test_enc.drop(columns=['Ticket', 'Name'])
 

# remove original nominal multi class columns and join the ohe columns

X_train_enc = X_train_enc.drop(columns=nominal_columns)
X_test_enc = X_test_enc.drop(columns=nominal_columns)


X_train_enc = pd.concat([X_train_enc, train_ohe_df], axis=1)
X_test_enc = pd.concat([X_test_enc, test_ohe_df], axis=1)



# Save Encoded df


train_enc_df = X_train_enc.copy()
train_enc_df[target] = y_train.values



test_enc_df = X_test_enc.copy()
test_enc_df[target] = y_test.values


train_enc_df.to_csv('../Preprocessing/train_enc.csv', index=False)
test_enc_df.to_csv('../Preprocessing/test_enc.csv',index=False)
