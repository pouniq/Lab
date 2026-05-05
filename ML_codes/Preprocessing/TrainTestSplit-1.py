# prevent from data leakage
# the model already knows about the test data.

import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv('../train.csv')
pd.set_option('display.max_columns', None)

# Sometimes you need to drop columns before train_test_split
# df = df.drop(columns = ['Alive'])

# dropping rows with missing values in the target.
df.isnull().sum()
# we don't have any missing values in the 'Survived' column.


target = 'Survived'
missing_target_values = df[target].isnull().sum()
print(f'Rows with missing values on the target values are {missing_target_values}')
df = df.dropna(subset= [target]) # drop the rows that are missing in the target.
print(f'shape after removing missing values {df.shape}')



# separate X and y :

X = df.drop(columns= [target])
y = df[target]


print(f'the distribution of Target values: \n {y.value_counts()} \n')
print('-'*50)
print(f'the distribution of Target values in percentage: \n {y.value_counts(normalize=True).round(3)}')

# here if we had Imbalaced dataset, we should make sure to handle that too.

# check if the dist. is Uniform
# train -> ML model training
# tets -> ML model evaluation 

# X -> X_train , X_test
# y -> y_train , y_test
 
 
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y,
    test_size=0.2,
    random_state=42,
    stratify=y # this stratify parameter is gonna help us to have the same dist. as the original dataset
)

print(f'Shapes:')
print(f'X_train:{X_train.shape}')
print(f'y_train:{y_train.shape}')
print(f'X_test:{X_test.shape}')
print(f'y_test:{y_test.shape}')


# the overall cycle and usecases.
# X_train, y_train -> model
# X_test -> go through the above model and we get y_pred
# compare y_pred with y_test



 
print(f'the distribution of Target values: \n {y.value_counts()} \n')
print('-'*50)
print(f'the distribution of Target values in percentage: \n {y.value_counts(normalize=True).round(3)}')


print(f'the distribution of Target values: \n {y_train} \n')
print('-'*50)
print(f'the distribution of Target values in percentage: \n {y_train.value_counts(normalize=True).round(3)}')


print(f'the distribution of Target values: \n {y_test.value_counts()} \n')
print('-'*50)
print(f'the distribution of Target values in percentage: \n {y_test.value_counts(normalize=True).round(3)}')

# here we can see that `stratify` would work really well on our dataset

 # do your preprocessing AFTER train_test_split
 
    