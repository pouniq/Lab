import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('breast_cancer_dataset.csv')
df.shape

df = df.dropna()
# we have 32 features

df['diagnosis'] = df['diagnosis'].map({'M': 0 , 'B':1})
df['diagnosis'].value_counts(normalize=True)

X = df.drop(columns=['id', 'diagnosis'])
y = df['diagnosis']

df.info()

# NOTE; for doing PCA we need to have numerical features 
# in our case this data is all numerical but when we have 
# other thing:

X = X.select_dtypes(include=[np.number])
X.columns



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    stratify=y,
    random_state=42
)

# NOTE it is important to standardize the features.

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Principal Component Analysis

# fit PCA (to see the most explained Variance)
pca_full = PCA()

X_train_pca_full = pca_full.fit_transform(X_train_scaled)
X_train_pca_full.shape
X_train_scaled.shape

# Explained Variance
exp_var = pca_full.explained_variance_ratio_
cum_exp_var = np.cumsum(exp_var)


# we will find better representation of our data
plt.figure(figsize=(10,7))
plt.plot(np.arange(1, len(cum_exp_var) + 1) ,  cum_exp_var, marker='s')
plt.title('Principal component analysis')
plt.xlabel('PCA')
plt.ylabel('explained Variance')
plt.grid()
plt.show()

# choose the number of components (example: keep 95% explained variance)
n_components_95 = np.argmax(cum_exp_var >= 0.95) + 1 # the first component that would reach 95%

# fit PCA with chosen no. of components
pca = PCA(n_components= n_components_95)
X_train_PCA = pca.fit_transform(X_train_scaled)
X_test_PCA = pca.transform(X_test_scaled)

X_train_PCA.shape
X_train_PCA



# then we can compare our model after and before pca 
# to check whether or not PCA will work or not




