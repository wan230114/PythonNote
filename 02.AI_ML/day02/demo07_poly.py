"""
demo07_poly.py 多项式回归模型
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import sklearn.preprocessing as sp
import sklearn.pipeline as pl
import sklearn.metrics as sm

# 采集数据
x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 训练模型
x = x.reshape(-1, 1) #把x变为 n行1列  

# 训练多项式回归模型
model = pl.make_pipeline(
	sp.PolynomialFeatures(10), 
	lm.LinearRegression())
model.fit(x, y)
# 模型预测  把样本的x传入模型，预测输出
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))

# 绘图所需参数
px = np.linspace(x.min(), x.max(), 1000)
px = px.reshape(-1, 1)
py = model.predict(px)

# 多项式回归模型不能做超出x范围的预测业务
cx = np.array([[-8], [-9], [-10], [-20]])
cy = model.predict(cx)
print(cx)
print(cy)

# 图像绘制
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, 
	s=60, label='Sample')
mp.plot(px, py, c='orangered', 
	label='Regression Line')
mp.legend()
mp.show()
