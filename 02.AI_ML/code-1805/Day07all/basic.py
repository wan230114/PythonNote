# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import cv2 as cv
original = cv.imread('../../data/forest.jpg')
print(original.shape, original.dtype)
cv.imshow('Original', original)
blue = np.zeros_like(original)
blue[..., 0] = original[..., 0]
cv.imshow('Blue', blue)
green = np.zeros_like(original)
green[..., 1] = original[..., 1]
cv.imshow('Green', green)
red = np.zeros_like(original)
red[..., 2] = original[..., 2]
cv.imshow('Red', red)
h, w = original.shape[:2]
l, t = int(w / 4), int(h / 4)
r, b = int(w * 3 / 4), int(h * 3 / 4)
cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)
scaled1 = cv.resize(original, (int(w / 2), int(h / 2)))
cv.imshow('Scaled1', scaled1)
scaled2 = cv.resize(scaled1, None, fx=2, fy=2,
                    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled2', scaled2)
cv.waitKey()
cv.imwrite('../../data/blue.jpg', blue)
cv.imwrite('../../data/green.jpg', green)
cv.imwrite('../../data/red.jpg', red)
cv.imwrite('../../data/cropped.jpg', cropped)
cv.imwrite('../../data/scaled1.jpg', scaled1)
cv.imwrite('../../data/scaled2.jpg', scaled2)
