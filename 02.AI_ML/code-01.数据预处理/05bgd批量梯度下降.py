import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

n_epoches = 1000  # 设置最大迭代次数
lrate = 0.01  # 学习率系数，超参数可以反复修改，直到模型达到足够好为止
epoches, losses = [], []  # 每次迭代的：第几次次数，损失值
w0, w1 = [1], [1]  # 设置初始值

for epoch in range(1, n_epoches+1):
    epoches.append(epoch)
    losses.append((
        (train_y - (w0[-1] + w1[-1] * train_x)) ** 2 / 2).sum())
    print('{:4}> w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(
        epoches[-1], w0[-1], w1[-1], losses[-1]))
    d0 = - (train_y - (w0[-1] + w1[-1] * train_x)).sum()
    d1 = - ((train_y - (w0[-1] + w1[-1] * train_x)) * train_x).sum()
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)
w0 = np.array(w0[:-1])  # 去除最后多算的一次
w1 = np.array(w1[:-1])

# 画图
sorted_indices = train_x.argsort()  # 有序索引：[0,1,2,3,4,5]
test_x = train_x[sorted_indices]  # 测试集，按x排序
test_y = train_y[sorted_indices]
pred_test_y = w0[-1] + w1[-1] * test_x  # 预测集

# mp.ion()

# 1) 绘制测试集与预测集的对照曲线
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)  # 标签大小
mp.grid(linestyle=':')  # 网格线
# 绘制训练集的各个点数据
mp.scatter(train_x, train_y, marker='s',
           c='dodgerblue', alpha=0.5, s=80,
           label='Training')
# 绘制测试集的各个点数据
mp.scatter(test_x, test_y, marker='D',
           c='orangered', alpha=0.5, s=60,
           label='Testing')
# 绘制预测集的各个点数据
mp.scatter(test_x, pred_test_y, c='orangered',
           alpha=0.5, s=80, label='Predicted')
# 绘制预测值与测试值之间的连线
for x, y, pred_y in zip(test_x, test_y, pred_test_y):
    mp.plot([x, x], [y, pred_y], c='orangered',
            alpha=0.5, linewidth=1)
# 绘制预测值的预测曲线
mp.plot(test_x, pred_test_y, '--', c='limegreen',
        label='Regression', linewidth=1)
mp.legend()

# 2) 绘制损失w0, w1, loss的变化规律
mp.figure('Training Progress', facecolor='lightgray')
mp.subplot(311)
mp.title('Training Progress', fontsize=20)
mp.ylabel('w0', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w0, c='dodgerblue', label='w0')
mp.legend()

mp.subplot(312)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w1, c='limegreen', label='w1')
mp.legend()

mp.subplot(313)
mp.xlabel('epoch', fontsize=14)
mp.ylabel('loss', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, losses, c='orangered', label='loss')
mp.legend()
mp.tight_layout()

# 3) 绘制损失函数
grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))
flat_w0, flat_w1 = grid_w0.ravel(), grid_w1.ravel()
flat_loss = ((flat_w0 + np.outer(train_x, flat_w1) - train_y.reshape(-1, 1)
              ) ** 2
             ).sum(axis=0) / 2
grid_loss = flat_loss.reshape(grid_w0.shape)

mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=20)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
mp.tick_params(labelsize=10)
ax.plot_surface(grid_w0, grid_w1, grid_loss,
                rstride=10, cstride=10, cmap='jet')
ax.plot(w0, w1, losses, 'o-', c='orangered',
        label='BGD')
mp.legend(loc='lower left')

# 4) 绘制等高线图
mp.figure('Batch Gradient Descent', facecolor='lightgray')
mp.title('Batch Gradient Descent', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(grid_w0, grid_w1, grid_loss, 10, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss, 10,
                  colors='black', linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
          fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered', label='BGD')
mp.legend()

mp.show()
