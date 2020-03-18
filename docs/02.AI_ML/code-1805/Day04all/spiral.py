# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as nb
import matplotlib.pyplot as mp
n_samples = 500
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_samples, 1))
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_samples, 2)
x = np.hstack((x, y)) + n
model_nonc = sc.AgglomerativeClustering(
    n_clusters=3, linkage='average')
pred_y_nonc = model_nonc.fit_predict(x)
conn = nb.kneighbors_graph(x, 10, include_self=False)
model_conn = sc.AgglomerativeClustering(
    n_clusters=3, linkage='average',
    connectivity=conn)
pred_y_conn = model_conn.fit_predict(x)
mp.figure('Nonconnectivity', facecolor='lightgray')
mp.title('Nonconnectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.axis('equal')
mp.scatter(x[:, 0], x[:, 1], c=pred_y_nonc,
           cmap='brg', s=60)
mp.figure('Connectivity', facecolor='lightgray')
mp.title('Connectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.axis('equal')
mp.scatter(x[:, 0], x[:, 1], c=pred_y_conn,
           cmap='brg', s=60)
mp.show()
