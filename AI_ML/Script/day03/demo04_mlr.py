"""
demo04_mlr.py  多元逻辑分类
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

x = np.array([
    [4, 7],
    [3.5, 8],
    [3.1, 6.2],
    [0.5, 1],
    [1, 2],
    [1.2, 1.9],
    [6, 2],
    [5.7, 1.5],
    [5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

# 把整个空间分为500*500的网格化矩阵
l, r = x[:,0].min()-1, x[:,0].max()+1
b, t = x[:,1].min()-1, x[:,1].max()+1
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, 500),
	np.linspace(b, t, 500))
# 把grid_x与grid_y抻平并在一起成两列，作为测试集x
mesh_x = np.column_stack((grid_x.ravel(), 
	grid_y.ravel()))
# 创建模型，针对test_x预测相应输出
model = lm.LogisticRegression(
	solver='liblinear', C=200)
model.fit(x, y)
mesh_y = model.predict(mesh_x)
# 把预测结果变维：500*500，用于绘制分类边界线
grid_z = mesh_y.reshape(grid_x.shape)

# 绘制散点图
mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 为网格化矩阵中的每个元素填充背景颜色
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()