import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("breast_cancer_dataset.csv")

df["diagnosis"].value_counts(normalize=True)

# map the values to turn them into numbers
df["diagnosis"] = df["diagnosis"].map({"B": 0, "M": 1})

df.head()
len(df.columns)
# filter method: just removing highly correlated features
df_corr = df.corr()
# plot the heatmap
# imagine if two person are telling you about something important
# but they are talking at the same time, you do not understand anything
# that they are saying. (it happens to the models too), you both are telling
# ONE information - MULTICOLLINEARITY
plt.figure(figsize=(30, 30))
sns.heatmap(df_corr, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5, cbar=True)
# Area and radius are telling us the samething, if one of them
# increases the other one increase too

# NOTE: we have Highly Correlated features
# split into feature and Target
X = df.drop(columns=["diagnosis", "id"])
y = df["diagnosis"]

# Train test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2, stratify=y
)

# Feature Selction Selection


# helper function
def print_metric(name, model, Xtr, Xte, ytr, yte):

    # get predictions
    tr_pred = model.predict(Xtr)
    te_pred = model.predict(Xte)

    # get accuracy score
    tr_acc = accuracy_score(ytr, tr_pred)
    te_acc = accuracy_score(yte, te_pred)

    print(name)
    print(f"train accuracy {tr_acc}")
    print(f"test accuracy {te_acc}")


# beseline model IS when we do not remove any features

baseline_pipe = Pipeline(
    [("scaler", StandardScaler()), ("model", LogisticRegression())]
)

baseline_pipe.fit(X_train, y_train)

print_metric(
    name="baseline model",
    model=baseline_pipe,
    Xtr=X_train,
    ytr=y_train,
    Xte=X_test,
    yte=y_test,
)


# Correlation , the filter method
corr = X_train.corr().abs()  # both Highly & negatively correlated features
sns.heatmap(corr)

to_drop = set()  # we do not want duplicated values and columns to drop (weird)

for i in range(len(corr.columns)):
    for j in range(i):
        # print(X_train.columns[i],X_train.columns[j]) for the comprehension
        if corr.iloc[i, j] > 0.9:  # * 0.9 hell no, it is a high correlation
            to_drop.add(corr.columns[i])
print("columns to drop", to_drop)
selected_filter = [c for c in X_train.columns if c not in to_drop]
print("selected columns", selected_filter)


X_train_f = X_train[selected_filter]
X_test_f = X_test[selected_filter]

filter_pip = Pipeline([("scaler", StandardScaler()), 
                       ("model", LogisticRegression())])

filter_pip.fit(X_train_f,y_train)


print_metric(
    name="model after Feature selection",
    model=filter_pip,
    Xtr=X_train_f,
    ytr=y_train,
    Xte=X_test_f,
    yte=y_test,
)
