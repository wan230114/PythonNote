"""
demo04_dump.py  保存模型
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
model = lm.LinearRegression()
model.fit(x, y)

# 保存
with open('../ml_data/lm.pkl', 'wb') as f:
	pickle.dump(model, f)

print('dump success!')