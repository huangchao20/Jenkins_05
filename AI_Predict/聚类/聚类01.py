# import numpy as np
# import sklearn
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

N = 10000
centers = 4
X, Y = make_blobs(n_samples=N, n_features=2, centers=centers, random_state=28)

km = KMeans(n_clusters=centers, init='random', random_state=28)
km.fit(X)

print(Y)

print('---------------------------------------------------------------------------')
y_hat = km.predict(X[:10])
print(y_hat)