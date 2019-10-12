import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.cluster import MiniBatchKMeans, KMeans
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

print("K_Means算法模型训练消耗时间：%.4fs" % km_batch)

batch_size = 100000
mbk = MiniBatchKMeans(init='k-means++', n_clusters=clusters, batch_size=batch_size, random_state=28)
t0 = time.time()
mbk.fit(X)
mbk_batch = time.time() - t0

print("Mini Batch K-Means算法模型训练消耗时间:%.4fs" % mbk_batch)

km_y_hat = k_means.predict(X)
mbk_y_hat = mbk.predict(X)

print(km_y_hat[:10])
print(mbk_y_hat[:10])
print(k_means.cluster_centers_)
print(mbk.cluster_centers_)

k_means_cluster_centers = k_means.cluster_centers_
mbk_cluster_centers = mbk.cluster_centers_

print("K-Means算法聚类中心点:\ncemter=", k_means_cluster_centers)
print("MiniBatch K-Means算法聚类中心点:\ncenter=", mbk_cluster_centers)

order = pairwise_distances_argmin(k_means_cluster_centers, mbk_cluster_centers)



plt.figure(figsize=(12, 6), facecolor='w')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)
cm = mpl.colors.ListedColormap(['#FFC2CC', '#C2FFCC', '#CCC2FF'])
cm2 = mpl.colors.ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c=Y, s=6, cmap=cm, edgecolors='none')
plt.title(u'原始数据分布图')
plt.xticks(())
plt.xticks(())
plt.grid(True)

plt.subplot(222)
plt.scatter(X[:, 0], X[:, 1], c=km_y_hat, s=6, cmap=cm, edgecolors='none')
plt.scatter(k_means_cluster_centers[:, 0], k_means_cluster_centers[:, 1], c=range(clusters), s=60, cmap=cm2, edgecolors='none')
plt.title(u'K-Means算法聚类结果图')
plt.xticks(())
plt.yticks(())
plt.text(-3.8, 3, 'train time: %.2fms' % (km_batch*100000))
plt.grid(True)

plt.subplot(223)
plt.scatter(X[:, 0], X[:, 1], c=mbk_y_hat, s=6, cmap=cm, edgecolors='none')
plt.scatter(mbk_cluster_centers[:, 0], mbk_cluster_centers[:, 1], c=range(clusters), s=60, edgecolors='none')
plt.xticks(())
plt.yticks(())
plt.text(-3.8, 3, 'train time: %.2fms' % (mbk_batch*100000))
plt.grid(True)

different = list(map(lambda x: (x!=0) & (x!=1) & (x!=2), mbk_y_hat))
for k in range(clusters):
    different += ((km_y_hat == k)!= (mbk_y_hat == order[k]))

identic = np.logical_not(different)
different_nodes = len(list(filter(lambda x:x, different)))
plt.subplot(224)
plt.plot(X[identic, 0], X[identic, 1], 'w', markerfacecolor= '#bbbbbb', marker='.')
plt.plot(X[identic, 0], X[identic, 1], 'w', markerfacecolor='m', marker='.')
plt.title(u'Mini Batch K-Means和K-Means算法预测结果不同的点')
plt.xticks(())
plt.yticks(())
plt.text(-3.8, 2, 'different nodes :%d' % different_nodes)

plt.show()

