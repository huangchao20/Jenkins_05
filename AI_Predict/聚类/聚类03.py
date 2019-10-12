import time
# import numpy as np
# import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn import metrics
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

centers = [[1, 1], [-1, -1], [1, -1]]
clusters = len(centers)

X, Y = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7, random_state=28)
k_means = KMeans(init='k-means++', n_clusters=clusters, random_state=28)

t0 = time.time()
k_means.fit(X)
km_batch = time.time() - t0
print("K-Means算法模型训练消耗时间:%.4fs" % km_batch)

batch_size = 100
kmb = MiniBatchKMeans(init='k-means++',n_clusters=clusters, batch_size=batch_size, random_state=28)
t0 = time.time()
kmb.fit(X)
kmb_batch = time.time() - t0
print ("Mini Batch K-Means算法模型训练消耗时间:%.4fs" % kmb_batch)

km_y_hat = k_means.labels_
kmb_y_hat = kmb.labels_
print("km_y_hat---------------->>", km_y_hat)
print("kmb_y_hat--------------->>", kmb_y_hat)

k_means_cluster_centers = k_means.cluster_centers_
kmb_cluster_centers = kmb.cluster_centers_
print ("K-Means算法聚类中心点:\ncenter=", k_means_cluster_centers)
print ("Mini Batch K-Means算法聚类中心点:\ncenter=", kmb_cluster_centers)
order = pairwise_distances_argmin(k_means_cluster_centers, kmb_cluster_centers)
print("order:\n", order)



score_funcs = [
    metrics.adjusted_rand_score,
    metrics.v_measure_score,
    metrics.adjusted_mutual_info_score,
    metrics.mutual_info_score,
]

for score_func in score_funcs:
    t0 = time.time()
    km_scores = score_func(Y, km_y_hat)
    print("K-Means算法:%s评估函数计算结果值:%.5f；计算消耗时间:%0.3fs" % (score_func.__name__,km_scores, time.time() - t0))
    
    t0 = time.time()
    kmb_scores = score_func(Y, kmb_y_hat)
    print("Mini Batch K-Means算法:%s评估函数计算结果值:%.5f；计算消耗时间:%0.3fs\n" % (score_func.__name__,kmb_scores, time.time() - t0))