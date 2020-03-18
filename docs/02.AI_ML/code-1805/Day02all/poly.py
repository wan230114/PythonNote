# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
train_x, train_y = [], []
with open('../../data/single.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        train_x.append(data[:-1])
        train_y.append(data[-1])
train_x = np.array(train_x)
train_y = np.array(train_y)
model = pl.make_pipeline(sp.PolynomialFeatures(10),
                         lm.LinearRegression())
model.fit(train_x, train_y)
pred_train_y = model.predict(train_x)
print(sm.r2_score(train_y, pred_train_y))
test_x = np.linspace(
    train_x.min(), train_x.max(), 1000).reshape(-1, 1)
pred_test_y = model.predict(test_x)
mp.figure('Polynomial Regression', facecolor='lightgray')
mp.title('Polynomial Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, c='dodgerblue', alpha=0.75,
           s=60, label='Sample')
mp.plot(test_x, pred_test_y, c='orangered',
        label='Regression')
mp.legend()
mp.show()
