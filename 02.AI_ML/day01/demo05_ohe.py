"""
demo05_ohe.py  独热编码
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([[1, 3, 2], 
					[7, 5, 4], 
					[1, 8, 6], 
					[7, 3, 9]])
# 构建独热编码器对象
ohe = sp.OneHotEncoder(sparse=True, dtype='i4')
r_samples = ohe.fit_transform(samples)
print(r_samples, type(r_samples))

encoder_dict = ohe.fit(samples)
r_samples = encoder_dict.transform(samples)
print(r_samples, type(r_samples))

