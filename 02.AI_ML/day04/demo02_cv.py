"""
demo01_tts.py  训练集测试集划分
"""
import sklearn.naive_bayes as nb
import numpy as np
import matplotlib.pyplot as mp
import sklearn.model_selection as ms

data = np.loadtxt('../ml_data/multiple1.txt', 
	delimiter=',', usecols=(0,1,2), 
	unpack=False)
print(data.shape)
x = data[:, :2]
y = data[:, 2]
# 划分测试集与训练集
train_x, test_x, train_y, test_y = \
	ms.train_test_split(x, y, test_size=0.25, 
	random_state=7)

# 创建并且训练模型
model = nb.GaussianNB()

# 基于新创建的模型进行交叉验证
ac = ms.cross_val_score(model, train_x, train_y,
	cv=5, scoring='accuracy')
print(ac.mean())
pw = ms.cross_val_score(model, train_x, train_y,
	cv=5, scoring='precision_weighted')
print(pw.mean())
rw = ms.cross_val_score(model, train_x, train_y,
	cv=5, scoring='recall_weighted')
print(rw.mean())
f1 = ms.cross_val_score(model, train_x, train_y,
	cv=5, scoring='f1_weighted')
print(f1.mean())





model.fit(train_x, train_y)
# 把训练好的模型应用于测试集，输出准确率
pred_test_y = model.predict(test_x)
print((test_y == pred_test_y).sum() / test_y.size)


# 绘制背景颜色，显示分类边界线
# 把整个空间分为500*500的网格化矩阵
l, r = x[:,0].min()-1, x[:,0].max()+1
b, t = x[:,1].min()-1, x[:,1].max()+1
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, 500),
	np.linspace(b, t, 500))
# 把grid_x与grid_y抻平并在一起成两列，作为测试集x
mesh_x = np.column_stack((grid_x.ravel(), 
	grid_y.ravel()))
mesh_y = model.predict(mesh_x)
grid_z = mesh_y.reshape(grid_x.shape)

#把所有样本点都绘制出来
mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=80)
mp.show()