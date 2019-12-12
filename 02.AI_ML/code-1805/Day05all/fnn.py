# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as mp
import matplotlib.patches as mc
train_x = np.array([
    [6, 7],
    [4.7, 8.5],
    [3.4, 8.5],
    [2, 7],
    [2, 5],
    [3.4, 3],
    [6, 2],
    [8.6, 3],
    [10, 5],
    [10, 7],
    [8.6, 8.5],
    [7.3, 8.5]])
model = sn.NearestNeighbors(n_neighbors=3,
                            algorithm='ball_tree')
model.fit(train_x)
test_x = np.array([
    [4.7, 8],
    [4, 6.5],
    [4, 6],
    [4.7, 5],
    [5.7, 4.6],
    [6.3, 4.6],
    [7.3, 5],
    [8, 6],
    [8, 6.5],
    [7.3, 8]])
nn_distances, nn_indices = model.kneighbors(test_x)
print(nn_indices)
print(nn_distances)
mp.figure('Find Nearest Neighbors',
          facecolor='lightgray')
mp.title('Find Nearest Neighbors', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.axis('equal')
mp.scatter(train_x[:, 0], train_x[:, 1], c='k',	zorder=2)
cs = mp.get_cmap('gist_rainbow', len(nn_indices))(
    range(len(nn_indices)))
for i, (x, nn_index) in enumerate(
        zip(test_x, nn_indices)):
    mp.gca().add_patch(mc.Polygon(
        train_x[nn_index], ec='none', fc=cs[i],
        alpha=0.25, zorder=0))
    mp.scatter(x[0], x[1], c=cs[i], s=80, zorder=1)
mp.show()
