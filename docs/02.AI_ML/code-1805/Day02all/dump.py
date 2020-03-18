# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pickle
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
x, y = [], []
with open('../../data/single.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))
with open('../../data/linear.pkl', 'wb') as f:
    pickle.dump(model, f)
