"""
demo03_normalization.py  归一化（正则化）
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([[17., 100., 4000.], 
					[20., 80., 5000.], 
					[23., 60., 5500.]])

r_samples = sp.normalize(samples, norm='l1')
print(r_samples)
