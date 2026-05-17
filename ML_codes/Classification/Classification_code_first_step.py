import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    roc_auc_score
    
)


df = pd.read_csv('../Preprocessing/diabetes.csv')
df

# we are gonna do some Logistic regression analysis

df.isnull().sum()

# we have imbalanced data
df['Outcome'].value_counts()

X = df.drop(columns=['Outcome'])
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    random_state=42,
                                                    test_size=0.2, 
                                                    stratify=y)



Scaler = StandardScaler()
X_train_scaled = Scaler.fit_transform(X_train)
X_test_scaled = Scaler.transform(X_test)


model = LogisticRegression()
lr = model.fit(X_train_scaled, y_train)

y_test_pred = lr.predict(X_test_scaled)
y_train_pred = lr.predict(X_train_scaled)

# this is were we see the probabilities of each class prediction
y_test_prob = model.predict_proba(X_test_scaled)
y_test_prob = model.predict_proba(X_test_scaled)[:,1]

y_test[:3]
y_test_pred[:3]
y_test_prob[:3]


# Evalution Metrics
def print_metrics(title, y_true, y_pred):
    # accuracy Score
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    print(title)
    print(f'accuracy: {acc:.2f}% \n precision: {prec:.2f}% \n recall: {rec:.2f}% \n f1_score: {f1:.2f}%')
    
print_metrics('Test metrics', y_test, y_test_pred)
print_metrics('Train Metrics', y_train, y_train_pred)



cm = confusion_matrix(y_test,y_test_pred)

plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=['Predicted 0' , 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.title('Confustion Matrix')
plt.show()




# ROC and AUC curve
fpr, tpr, thresholds = roc_curve(y_test, y_test_prob)
auc_score = roc_auc_score(y_test, y_test_prob)

plt.figure(figsize=(10,7))
plt.plot(fpr, tpr, label = f'AUC: {auc_score :.2%}')
plt.plot([0,1], [0,1], linestyle = '--')
plt.legend()
plt.show()


# plt.scatter([0,1],[0,1])




 