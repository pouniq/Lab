import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# pd.set_option("display:float_format", lambda x : '%.3f' % x)



df = pd.read_csv('diabetes.csv')

X = df.drop(columns='Outcome')
y = df['Outcome']


X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    random_state=43,
                                                    test_size=0.2,
                                                    stratify=y
                                                    )


num_cols = X_train.select_dtypes([np.number]).columns.to_list()
cat_cols = [col for col in X_train.columns if not num_cols]


X_train_srd = X_train.copy()
X_test_srd = X_test.copy()

scaler = StandardScaler()
x_train_scale = scaler.fit(X_train_srd[num_cols])


X_train_srd[num_cols] = x_train_scale.transform(X_train_srd[num_cols])
X_test_srd[num_cols] = x_train_scale.transform(X_test_srd[num_cols])


X_train.describe().T
X_train_srd.describe().T


# -----
MMS = MinMaxScaler()
X_train_mms = MMS.fit(X_train[num_cols])

X_train_m = X_train.copy()
X_test_m = X_test.copy()


X_train_m[num_cols] = X_train_mms.transform(X_train[num_cols])
X_test_m[num_cols] = X_train_mms.transform(X_test[num_cols])




