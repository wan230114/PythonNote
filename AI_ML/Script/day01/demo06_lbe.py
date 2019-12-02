"""
demo06_lbe.py  标签编码器
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array(['audi', 'ford', 'audi', 
	'toyota', 'ford', 'bmw', 'toyota', 
	'audi', 'redflag'])
# 获取标签编码器对象
lbe = sp.LabelEncoder()
r_samples = lbe.fit_transform(samples)
print(r_samples)

r_returns = [0, 3, 3, 2, 4, 1]
returns = lbe.inverse_transform(r_returns)
print(returns)

