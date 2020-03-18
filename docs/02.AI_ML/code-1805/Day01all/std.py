# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)
print(raw_samples.mean(axis=0))
print(raw_samples.std(axis=0))
std_samples = raw_samples.copy()
for col in std_samples.T:
    col_mean = col.mean()
    col_std = col.std()
    col -= col_mean
    col /= col_std
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
