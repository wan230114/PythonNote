# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pickle
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open('../../data/single.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)
with open('../../data/linear.pkl', 'rb') as f:
    model = pickle.load(f)
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75,
           s=60, label='Sample')
sorted_indices = x.T[0].argsort()
mp.plot(x[sorted_indices], pred_y[sorted_indices],
        'o-', c='orangered', label='Regression')
mp.legend()
mp.show()
