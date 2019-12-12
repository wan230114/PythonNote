# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
original = cv.imread('../../data/box.png')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)
corners = cv.dilate(corners, None)
mixture = original.copy()
mixture[corners > corners.max() * 0.01] = [0, 0, 255]
cv.imshow('Mixture', mixture)
cv.waitKey()
