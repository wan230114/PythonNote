"""
demo05_load.py  加载模型对象
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import pickle 
# 采集数据
x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 训练模型
x = x.reshape(-1, 1) #把x变为 n行1列  

# 加载模型
with open('../ml_data/lm.pkl', 'rb') as f:
	model = pickle.load(f)

# 模型预测  把样本的x传入模型，预测输出
pred_y = model.predict(x)

# ----------------------------------
# 模型评估
# ----------------------------------
m1 = sm.mean_absolute_error(y, pred_y)
m2 = sm.mean_squared_error(y, pred_y)
m3 = sm.median_absolute_error(y, pred_y)
r2 = sm.r2_score(y, pred_y)
print('mean_absolute_error:', m1)
print('mean_squared_error:', m2)
print('median_absolute_error:', m3)
print('r2:', r2)


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
