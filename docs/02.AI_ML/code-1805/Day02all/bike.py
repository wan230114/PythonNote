# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
with open('../../data/bike_day.csv', 'r') as f:
    reader = csv.reader(f)
    x, y = [], []
    for row in reader:
        x.append(row[2:13])
        y.append(row[-1])
fn_dy = np.array(x[0])
x = np.array(x[1:], dtype=float)
y = np.array(y[1:], dtype=float)
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
model = se.RandomForestRegressor(
    max_depth=10, n_estimators=1000,
    min_samples_split=2)
model.fit(train_x, train_y)
fi_dy = model.feature_importances_
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
with open('../../data/bike_hour.csv', 'r') as f:
    reader = csv.reader(f)
    x, y = [], []
    for row in reader:
        x.append(row[2:14])
        y.append(row[-1])
fn_hr = np.array(x[0])
x = np.array(x[1:], dtype=float)
y = np.array(y[1:], dtype=float)
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
model = se.RandomForestRegressor(
    max_depth=10, n_estimators=1000,
    min_samples_split=2)
model.fit(train_x, train_y)
fi_hr = model.feature_importances_
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
mp.figure('Bike', facecolor='lightgray')
mp.subplot(211)
mp.title('Day', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_dy.argsort()[::-1]
pos = np.arange(len(sorted_indices))
mp.bar(pos, fi_dy[sorted_indices],
       facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, fn_dy[sorted_indices], rotation=30)
mp.subplot(212)
mp.title('Hour', fontsize=16)
mp.xlabel('Feature', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_hr.argsort()[::-1]
pos = np.arange(len(sorted_indices))
mp.bar(pos, fi_hr[sorted_indices],
       facecolor='lightcoral', edgecolor='indianred')
mp.xticks(pos, fn_hr[sorted_indices], rotation=30)
mp.tight_layout()
mp.show()
