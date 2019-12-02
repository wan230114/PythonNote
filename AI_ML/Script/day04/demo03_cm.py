"""
demo03_cm.py  混淆矩阵
"""
import sklearn.naive_bayes as nb
import numpy as np
import matplotlib.pyplot as mp
import sklearn.model_selection as ms
import sklearn.metrics as sm

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

# 输出混淆矩阵
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)

mp.imshow(cm, cmap='gray')
mp.show()