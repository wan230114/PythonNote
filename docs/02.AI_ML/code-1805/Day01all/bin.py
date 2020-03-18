# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 1.4] = 0
bin_samples[bin_samples > 1.4] = 1
print(bin_samples)
bin = sp.Binarizer(threshold=1.4)
bin_samples = bin.transform(raw_samples)
print(bin_samples)
