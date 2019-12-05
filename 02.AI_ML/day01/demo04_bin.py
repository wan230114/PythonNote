"""
demo04_bin.py  二值化
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([[17., 100., 4000.], 
					[20., 80., 5000.], 
					[23., 60., 5500.]])

bin = sp.Binarizer(threshold=80)
r_samples = bin.transform(samples)
print(r_samples)

samples[samples<=80] = 0
samples[samples>80] = 1
print(samples)







