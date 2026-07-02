# K-Means Clustring
# we use IRIS dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


iris = load_iris(as_frame=True)
df = iris.frame


X = df.drop(columns = ['target'])

scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)
x_scaled.mean()
x_scaled.std()

# what is the number cluster we need to have
# elbow method -- help us find the best value
# we need to first find the inertia 
inertias = []
k_range = range(1, 11)
# print(*k_range)

# we will iterate over this k values to find the best number of clusters meaning
# the K value

for k in k_range:
    km = KMeans(n_clusters= k, random_state=42, n_init=10)
    # NOTE: the n_init parameters tell us how many times the process is repeated
    # till we get to the mean of the cluster
    km.fit(x_scaled)
    inertias.append(km.inertia_)
    
# WCSS: within clusters sums of squares
    # the other name for this value is called inertia
    # we trying to see low values (not the lowest value) YES but it is not entirely that 
    # we need to see sharp decrease in our inertia (WCSS) values
    # where we have lots of decrease we can say the k number of cluster is that k
plt.figure(figsize=(10,7))
plt.plot(k_range, inertias, marker = 's')
plt.xlabel('Number of clusters')
plt.ylabel('inertia [WCSS]')
plt.plot()
# elbow is basically a sharp bend, and in this case we can say the k is 2 or 3

k = 3
k_means = KMeans(n_clusters= k , random_state=42, n_init=10)
k_means.fit(x_scaled)

k_means_prediction = k_means.predict(x_scaled)

