"""
demo07_LOSS.py  绘制损失函数图像
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
w0, w1 = np.meshgrid(np.linspace(-30, 30, n), 
				   np.linspace(-30, 30, n))
# 基于for循环，遍历5个样本，计算5个样本的总样本误差
loss = 0 
xs = [0.5, 0.6, 0.8, 1.1, 1.4]
ys = [5.0, 5.5, 6.0, 6.8, 7.0]
for x, y in zip(xs, ys):
	loss += (w0+w1*x-y)**2 / 2

# 绘制
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0')
ax3d.set_ylabel('w1')
ax3d.set_zlabel('loss')
ax3d.plot_surface(w0, w1, loss, rstride=30, 
	cstride=30, cmap='jet')
mp.show()
