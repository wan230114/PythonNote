"""
demo07_opencv.py  opencv基础
"""

import numpy as np
import cv2 as cv

# 读取图片并显示
original = cv.imread('../ml_data/forest.jpg')
cv.imshow('Original', original)
# 显示图片某个颜色通道的图像
blue = np.zeros_like(original)
blue[:, :, 0] = original[:, :, 0]  # 0 - 蓝色通道
cv.imshow('Blue', blue)
green = np.zeros_like(original)
green[:, :, 1] = original[:, :, 1]  # 1 - 绿色通道
cv.imshow('Green', green)
red = np.zeros_like(original)
red[:, :, 2] = original[:, :, 2]  # 2 - 红色通道
cv.imshow('Red', red)
# 图像裁剪
h, w = original.shape[:2]
l, t = int(w / 4), int(h / 4)
r, b = int(w * 3 / 4), int(h * 3 / 4)
cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)
#图像缩放 interpolation=线型插值
scaled1 = cv.resize(original, (int(w / 4), int(h / 4)),
    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled1', scaled1)
scaled2 = cv.resize(
    scaled1, None, fx=4, fy=4,
    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled2', scaled2)
cv.waitKey()
# 图像文件保存
cv.imwrite('../ml_data/blue.jpg', blue)
cv.imwrite('../ml_data/green.jpg', green)
cv.imwrite('../ml_data/red.jpg', red)
cv.imwrite('../ml_data/cropped.jpg', cropped)
cv.imwrite('../ml_data/scaled1.jpg', scaled1)
cv.imwrite('../ml_data/scaled2.jpg', scaled2)