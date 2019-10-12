import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
import sklearn.datasets as ds
import warnings

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
warnings.filterwarnings(action='ignore', category=UserWarning)

np.random.seed(0)
n_clusters = 4
centers = ((-1, 1), (1, 1), (1, -1), (-1, -1))
N = 1000
data1, y1 = ds.make_blobs(n_samples=N, n_features=2, centers=centers, random_state=0)

n_noise = int(0.1 * N)
r = np.random.rand(n_noise, 2)

min1, min2 = np.min(data1, axis=0)
max1, max2 = np.min(data1, axis=0)
r[:, 0] = r[:, 0] * (max1 - min1) + min1
r[:, 1] = r[:, 1] * (max2 - min2) + min2
data1_noise = np.concatenate((data1, r), axis=0)
y1_noise= np.concatenate((y1, [4] * n_noise))

data2, y2 = ds.make_moons(n_samples=N, noise=.05)
data2 = np.array(data2)
n_noise = int(0.1 * N)
r = np.random.rand(n_noise, 2)
min1, min2 = np.min(data2, axis=0)
max1, max2 = np.max(data2, axis=0)
r[:, 0] = r[:, 0] * (max1 - min1) + min1
r[:, 1] = r[:, 1] * (max2 - min2) + min2
data2_noise = np.concatenate((data2, r), axis=0)
y2_noise = np.concatenate((y2, [3] * n_noise))

def expandBorder(a, b):
    d = (b - a) * 0.1
    return a -d, b + d
    
cm = mpl.colors.ListedColormap(['#FF0000', '#00FF00',  '#0000FF', '#d8e507', '#F0F0F0'])
plt.figure(figsize=(14, 12), facecolor='w')
linkages = ("ward", "complete", "average")

for index, (n_clusters, data, y) in enumerate(((4, data1, y1), (4, data1_noise, y1_noise), (2, data2, y2), (2, data2_noise, y2_noise))):
    plt.subplot(4, 4, 4 * index + 1)
    plt.scatter(data[:, 0], data[:, 1], c=y, cmap=cm, facecolor='none')
    plt.title(u'原始数据', fontsize=17)
    plt.grid(b=True, ls=':')
    min1, min2 = np.min(data, axis=0)
    max1, max2 = np.max(data, axis=0)
    plt.xlim(expandBorder(min1, max1))
    plt.ylim(expandBorder(min2, max2))
    connectivity = kneighbors_graph(data, n_neighbors=7, mode='distance', metric='minkowski', p=2, include_self=True)
    connectivity = (connectivity + connectivity.T)
    for i, linkage in enumerate(linkages):
        print(n_clusters)
        ac = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', connectivity=connectivity, linkage=linkage)
        ac.fit(data)
        y = ac.labels_
        
        plt.subplot(4, 4, i + 2 + 4 * index)
        plt.scatter(data[:, 0], data[:, 1], c=y, cmap=cm)
        plt.title(linkage, fontsize=17)
        plt.grid(b=True, ls=':')
        plt.xlim(expandBorder(min1, max1))
        plt.ylim(expandBorder(min2, max2))
plt.suptitle(u'AGNES层次聚类的不同合并策略', fontsize=30)
plt.tight_layout(0.5, rect=(0, 0, 1, 0.95))
plt.show()
    




