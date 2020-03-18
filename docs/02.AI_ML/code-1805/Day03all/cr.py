# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import mpl_toolkits.axes_grid1 as mg
x, y = [], []
with open('../../data/multiple1.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)
train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y, test_size=0.25, random_state=7)
model = nb.GaussianNB()
print(ms.cross_val_score(
    model, x, y, cv=10,
    scoring='precision_weighted').mean())
print(ms.cross_val_score(
    model, x, y, cv=10,
    scoring='recall_weighted').mean())
print(ms.cross_val_score(
    model, x, y, cv=10,
    scoring='f1_weighted').mean())
print(ms.cross_val_score(
    model, x, y, cv=10,
    scoring='accuracy').mean())
model.fit(train_x, train_y)
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h),
                     np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / pred_test_y.size)
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)
cr = sm.classification_report(test_y, pred_test_y)
print(cr)
mp.figure('Naive Bayes Classification',
          facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y,
           cmap='brg', s=60)
mp.figure('Confusion Matrix', facecolor='lightgray')
mp.title('Confusion Matrix', fontsize=20)
mp.xlabel('Predicted Class', fontsize=14)
mp.ylabel('True Class', fontsize=14)
mp.xticks(np.unique(pred_test_y))
mp.yticks(np.unique(test_y))
mp.tick_params(labelsize=10)
im = mp.imshow(cm, interpolation='nearest', cmap='jet')
for row in range(cm.shape[0]):
    for col in range(cm.shape[1]):
        mp.text(col, row, str(cm[row, col]),
                color='white', fontsize=14,
                fontstyle='italic', ha='center',
                va='center')
dv = mg.make_axes_locatable(mp.gca())
ca = dv.append_axes('right', '6%', pad='3%')
cb = mp.colorbar(im, cax=ca)
mp.show()
