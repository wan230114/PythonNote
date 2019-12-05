"""
demo01_scale.py  均值移除
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([[17, 100, 4000], 
					[20, 80, 5000], 
					[23, 60, 5500]])

r_samples = sp.scale(samples)
print(r_samples)
print(r_samples.mean(axis=0))
print(r_samples.std(axis=0))



