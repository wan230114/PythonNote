# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as mp
train_x = 10 * np.random.rand(100, 1) - 5
train_y = np.sinc(train_x).ravel()
train_y += 0.2 * (0.5 - np.random.rand(train_y.size))
model = sn.KNeighborsRegressor(
    n_neighbors=10, weights='distance')
model.fit(train_x, train_y)
test_x = np.linspace(-5, 5, 10000).reshape(-1, 1)
test_y = np.sinc(test_x)
pred_test_y = model.predict(test_x)
mp.figure('KNN Regression', facecolor='lightgray')
mp.title('KNN Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, c='dodgerblue',
           s=60, label='Training')
mp.plot(test_x, test_y, '--', c='limegreen',
        linewidth=1, label='Testing')
mp.plot(test_x, pred_test_y, c='orangered',
        label='Predicted Testing')
mp.legend()
mp.show()
