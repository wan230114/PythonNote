# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota', 'ford',
    'bmw', 'toyota', 'ford', 'audi'])
print(raw_samples)
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit(raw_samples).transform(
    raw_samples)
print(lbe_samples)
raw_samples = lbe.inverse_transform(lbe_samples)
print(raw_samples)
