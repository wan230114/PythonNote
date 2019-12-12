# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
data = []
with open('../../data/car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
model = se.RandomForestClassifier(
    max_depth=8, random_state=7)
n_estimators = np.arange(50, 550, 50)
train_scores1, test_scores1 = ms.validation_curve(
    model, x, y, 'n_estimators', n_estimators, cv=5)
test_mean1 = test_scores1.mean(axis=1)
model = se.RandomForestClassifier(
    n_estimators=150, random_state=7)
max_depth = np.arange(1, 11)
train_scores2, test_scores2 = ms.validation_curve(
    model, x, y, 'max_depth', max_depth, cv=5)
test_mean2 = test_scores2.mean(axis=1)
mp.figure('n_estimators', facecolor='lightgray')
mp.title('n_estimators', fontsize=20)
mp.xlabel('n_estimators', fontsize=14)
mp.ylabel('Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(n_estimators, test_mean1, 'o-',
        color='dodgerblue')
mp.figure('max_depth', facecolor='lightgray')
mp.title('max_depth', fontsize=20)
mp.xlabel('max_depth', fontsize=14)
mp.ylabel('Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(max_depth, test_mean2, 'o-',
        color='orangered')
mp.show()
