import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 50)

titanic_dataset = pd.read_csv('train.csv')


titanic_dataset['id'] = np.arange(1, len(titanic_dataset)+1)
# when we have id column we would drop it becuase it do not 
# make any effect
# this is where i put some columns that are not good quality

titanic_dataset['Constant'] = 1

titanic_dataset['Embarked'].unique()
titanic_dataset['Embarked_Town'] = titanic_dataset['Embarked'].replace(
    {'S': 'Southampton',
    'C': 'Cherbourg',
    'Q': 'Queenstown'}
) 



sample_index = titanic_dataset.dropna().sample(6, random_state = 42).index

df = titanic_dataset

df['EmbarkTownDirty']=df['Embarked'].copy()

df.loc[sample_index[0:2], 'EmbarkTownDirty'] = df.loc[sample_index[0:2], 'EmbarkTownDirty'].str.upper()
df.loc[sample_index[2:4], 'EmbarkTownDirty'] = df.loc[sample_index[2:4], 'EmbarkTownDirty'].str().strip().apply(lambda x :f' {x} ')   
df.loc[sample_index[4:6], 'EmbarkTownDirty'] = df.loc[sample_index[4:6], 'EmbarkTownDirty'] = 'Unkown'


# the data quality checks are performed here.

# 1.Basic Dataset overview
df.shape
df.dtypes
df.info()
df.columns
print(df.nunique) # that was a cool trick
df.describe()

# 2. missing values
missing_count = df.isna().sum().sort_values(ascending = False)
missing_percent = (df.isna().mean() * 100 ).sort_values(ascending = False)
print('Missing values Summary')
missing_summary = pd.DataFrame(
    {
        'missing_count':missing_count,
        'missing_percent': missing_percent
        })
missing_summary

# if for example a column like Age have lot of outliers 
# we use the Median of the column and replace it with the median,
# but if we have little bit of outlier then we can use the mean.
# this process is called inputation.


# 3. Duplicates
duplicates_ms = df.duplicated()
numberOfDuplicates = print('the number of duplicated rows:' , duplicates_ms.sum())
# then if we have duplicated rows then we run this code below:
# df_no_duplicates = df.drop_duplicates()

# 4. data type validation
expected_dtypes = {
    'Survived': 'int64',
    "Pclass": 'int64'
}
for col, expected in expected_dtypes.items():
    if col in df.columns:
        actual = df[col].dtype 
        print(f'the column of {col}, the expected data type is {expected} \n  and the actual data type is {actual}')
        print('-'*50)
        
# example fo changing a data type.
# df['Pclass'] = df['Pclass'].astype('int64')



# 5. Constant and quasi-constant columsn
n_rows = len(df)
nunique = df.nunique()

constant_cols = nunique[nunique == 1].index.to_list()
print('Constant columns', constant_cols)

# quasi-constants: mean the columns that are almost constant, like 80%
# we are talking about percentages

quasi_constant_cols = []
percent_of_constant = 0.95
for col in df.columns:
    top_frequency = df[col].value_counts(normalize=True, dropna=False).values[0]
    if top_frequency > percent_of_constant and col not in constant_cols:
        quasi_constant_cols.append(col)  
        
print(f'quasi-constant columns we have {percent_of_constant}% constant rows on', quasi_constant_cols)        


# 6. ID like columns
n_rows = len(df)
id_like_cols = []

for col in df.columns:
    if df[col].nunique(dropna=False) == n_rows:
        id_like_cols.append(col)
        
print('id like columns' , id_like_cols)


# 7. String inconsistencies
object_cols = df.select_dtypes(include=['object']).columns.to_list()

print('String, Object and category datatypes', object_cols)

# simple clean: strip spaces and convert to lower case
# it is useful in the world of NLP because making it lower case is better.
df['embark_town_clean'] = (
    df['EmbarkTownDirty'].astype('str').str.strip().str.lower().replace('unkown' , np.nan)
)


#8. high null columns
high_null_threshold = 0.4 # 40 percent or more values are missing in the values
high_null_cols = missing_summary[missing_summary['missing_percent'] >= high_null_threshold * 100]
print('columns with high missing percentage',high_null_cols)

#9. high zero columns (numeric)
numeric_cols = df.select_dtypes([np.number]).columns.to_list()
zero_share = {}

for col in numeric_cols:
    zero_share[col] = (df[col] == 0).mean()

zero_share_series = pd.Series(zero_share).sort_values(ascending=False)
high_zero_threshold = 0.8
high_zero_cols = zero_share_series[zero_share_series >= high_zero_threshold] 
print('columns with high zero percentage',high_zero_cols)