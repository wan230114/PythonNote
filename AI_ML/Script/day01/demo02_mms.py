"""
demo02_mms.py  范围缩放
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([[17., 100., 4000.], 
					[20., 80., 5000.], 
					[23., 60., 5500.]])

mms = sp.MinMaxScaler(feature_range=(0, 1))
r_samples = mms.fit_transform(samples)
print(r_samples)

# 手动实现范围缩放
for col in samples.T:
	col_min = col.min()
	col_max = col.max()
	A = np.array([[col_min, 1], [col_max, 1]])
	B = np.array([0, 1])
	X = np.linalg.lstsq(A, B)[0]
	col *= X[0]
	col += X[1]
print(samples)





