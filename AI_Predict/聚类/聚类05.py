from itertools import cycle
from time import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import Birch
from sklearn.datasets.samples_generator import make_blobs

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

xx = np.linspace(-22, 22, 10)
yy = np.linspace(-22, 22, 10)
xx, yy = np.meshgrid(xx, yy)

n_centers = np.hstack((np.ravel(xx)[:, np.newaxis], np.ravel(yy)[:, np.newaxis]))
X, y = make_blobs(n_samples= 1000, n_features=2, centers=n_centers, random_state=28)
birch_models = [Birch(threshold=1.7, n_clusters=None), Birch(threshold=0.5, n_clusters=None), Birch(threshold=1.7, n_clusters=100)]

final_step = [u'直径=1.7;n_lusters=None',u'直径=0.5;n_clusters=None',u'直径=1.7;n_lusters=100']

plt.figure(figsize=(12, 8), facecolor='w')
plt.subplots_adjust(left=0.02, right=0.98, bottom=0.1, top=0.9)
colors_ = cycle(colors.cnames.keys())
cm = mpl.colors.ListedColormap(colors.cnames.keys())

for ind, (birch_model, info) in enumerate(zip(birch_models, final_step)):
    t = time()
    birch_model.fit(X)
    time_ = time() - t
    
    labels = birch_model.labels_
    centroids = birch_model.subcluster_centers_
    n_clusters = len(np.unique(centroids))
    print ("Birch算法，参数信息为：%s；模型构建消耗时间为:%.3f秒；聚类中心数目:%d" % (info, time_, len(np.unique(labels))))
    
    subinx = 221 + ind
    plt.subplot(subinx)
    
    for this_centroid, k, col, in zip(centroids, range(n_clusters), colors_):
        mask = labels == k
        plt.plot(X[mask, 0], X[mask, 1], 'w', markerfacecolor=col, marker='.')
        #plt.plot(X[mask, 0], X[mask, 1], 'w', markerfacecolor=col, marker='.')
        if birch_model.n_clusters is None:
            #plt.plot(this_centroid[0], this_centroid[1], '*', markerfacecolor=col, markeredgecolor='k', markersize=2)
            plt.plot(this_centroid[0], this_centroid[1], '*', markerfacecolor=col, markeredgecolor='k', markersize=2)
        plt.xlim([-25, 25])
        plt.ylim([-25, 25])
        plt.title(u'Birch算法%s，耗时%.3fs' % (info, time_))
        plt.grid(False)
    
    plt.subplot(224)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=1, cmap=cm, edgecolors='none')
    plt.ylim([-25, 25])
    plt.xlim([-25, 25])
    plt.title(u'原始数据')
    plt.grid(False)
    
    plt.show()
