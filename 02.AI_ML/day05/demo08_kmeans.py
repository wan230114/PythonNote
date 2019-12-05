"""
demo08_kmeans.py  kmeans聚类
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')
# 构建聚类模型
model = sc.KMeans(n_clusters=4)
model.fit(x)
# 返回每个样本的聚类的类别标签: 0/1/2/3
pred_y = model.labels_
# 返回所有的聚类中心样本
centers = model.cluster_centers_
print(centers)
# 绘制分类边界线
n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x = np.meshgrid(np.linspace(l, r, n),
                     np.linspace(b, t, n))
flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))    
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

mp.figure('K-Means Cluster', facecolor='lightgray')
mp.title('K-Means Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, 
	cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=pred_y, 
	cmap='brg', s=80)
mp.scatter(centers[:, 0], centers[:,1],
	c='red', marker='+', s=500)

mp.show()