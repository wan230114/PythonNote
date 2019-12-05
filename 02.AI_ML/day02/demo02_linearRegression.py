"""
demo02_linearRegression.py 线性回归
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

# 采集数据
x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 训练模型
x = x.reshape(-1, 1) #把x变为 n行1列  
model = lm.LinearRegression()
model.fit(x, y)
# 模型预测  把样本的x传入模型，预测输出
pred_y = model.predict(x)
# 图像绘制
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, 
	s=60, label='Sample')
mp.plot(x, pred_y, c='orangered', 
	label='Regression Line')
mp.legend()
mp.show()
