# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import scipy.misc as sm
import sklearn.cluster as sc
import matplotlib.pyplot as mp
image = sm.imread(
    '../../data/lily.jpg', True).astype(np.uint8)
x = image.reshape(-1, 1)
model = sc.KMeans(n_clusters=2)
model.fit(x)
y = model.labels_
centers = model.cluster_centers_.squeeze()
quanted = centers[y].reshape(image.shape)
mp.figure('Image', facecolor='lightgray')
mp.title('Image', fontsize=20)
mp.axis('off')
mp.imshow(image, cmap='gray')
mp.figure('Quanted', facecolor='lightgray')
mp.title('Quanted', fontsize=20)
mp.axis('off')
mp.imshow(quanted, cmap='gray')
mp.show()
