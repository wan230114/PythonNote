"""
demo05_car.py
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

# 读取文件
data = np.loadtxt('../ml_data/car.txt', 
	delimiter=',', dtype='U20')
# 整理训练集的输入与输出
data = data.T
train_x, train_y = [], []
for col in range(len(data)):
	if col < len(data)-1: # 不是最后一列
		lbe = sp.LabelEncoder()
		train_x.append(lbe.fit_transform(data[col]))
	else:
		train_y = lbe.fit_transform(data[col])
train_x = np.array(train_x).T
print(train_x.shape)


# 交叉验证 训练模型

# 模型测试
