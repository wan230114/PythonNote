# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([
        [col_min, 1],
        [col_max, 1]])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    col *= x[0]
    col += x[1]
print(mms_samples)
'''
mms = sp.MinMaxScaler(feature_range=(0, 1))
mms_samples = mms.fit_transform(raw_samples)
'''
mms_samples = sp.MinMaxScaler(
    feature_range=(0, 1)).fit_transform(raw_samples)
print(mms_samples)
