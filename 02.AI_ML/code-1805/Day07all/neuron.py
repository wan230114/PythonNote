# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import neurolab as nl
import matplotlib.pyplot as mp
x = np.array([
    [0.3, 0.2],
    [0.7, 0.4],
    [0.4, 0.6],
    [0.9, 0.5]])
y = np.array([
    [0],
    [0],
    [0],
    [1]])
model = nl.net.newp([[0, 1], [0, 1]], 1)
error = model.train(x, y, epochs=50, show=1, lr=0.01)
mp.figure('Training Progress', facecolor='lightgray')
mp.title('Training Progress', fontsize=20)
mp.xlabel('Epoch', fontsize=14)
mp.ylabel('Error', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(error, 'o-', c='orangered', label='Error')
mp.legend()
mp.show()
