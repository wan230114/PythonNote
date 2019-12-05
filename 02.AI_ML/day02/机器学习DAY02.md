# 机器学习DAY02

### 线性回归

绘制随着每次梯度下降，w<sub>0</sub>，w<sub>1</sub>，loss的变化曲线。

```python
# 绘制随着每次梯度下降，w0，w1，loss的变化曲线。
w0 = w0[:-1]
w1 = w1[:-1]

mp.figure('Training Progress', facecolor='lightgray')
mp.subplot(311)
mp.title('Training Progress', fontsize=16)
mp.ylabel('w0', fontsize=13)
mp.grid(linestyle=':')
mp.plot(epoches, w0, color='dodgerblue',
	label='w0')
mp.legend()
mp.subplot(312)
mp.ylabel('w1', fontsize=13)
mp.grid(linestyle=':')
mp.plot(epoches, w1, color='orangered',
	label='w1')
mp.legend()
mp.subplot(313)
mp.title('Training Progress', fontsize=16)
mp.ylabel('loss', fontsize=13)
mp.grid(linestyle=':')
mp.plot(epoches, losses, color='red',
	label='loss')
mp.legend()

mp.tight_layout()
mp.show()
```

基于三维曲面绘制梯度下降过程中的每一个点。

```python
# 基于三维曲面绘制梯度下降过程中的每一个点
import mpl_toolkits.mplot3d as axes3d

grid_w0, grid_w1 = np.meshgrid(
	np.linspace(0, 9, 500), 
	np.linspace(0, 3.5, 500))
grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
	grid_loss += (grid_w0+grid_w1*x - y)**2 / 2
# 绘图
mp.figure('Loss Function')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0', fontsize=14)
ax3d.set_ylabel('w1', fontsize=14)
ax3d.set_zlabel('loss', fontsize=14)
ax3d.plot_surface(grid_w0, grid_w1, grid_loss,
	rstride=30, cstride=30, cmap='jet')
ax3d.plot(w0, w1, losses, 'o-', 
	color='orangered', label='BGD')

```

以等高线的方式绘制梯度下降的过程。

```python
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

```

### 线性回归

线性回归相关API：

```python
import sklearn.linear_model as lm
# 创建模型
model = lm.LinearRegression()
# 训练模型
# 输入为一个二维数组表示的样本矩阵
# 输出为每个样本最终的结果
model.fit(输入, 输出) # 通过梯度下降法计算模型参数
# 预测输出  
# 输入array是一个二维数组，每一行是一个样本，每一列是一个特征。
result = model.predict(array)
```

案例：基于线性回归训练single.txt中的训练样本，使用模型预测测试样本。

```python
"""
demo02_linearRegression.py 线性回归
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

# 采集数据
x, y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 训练模型
x = x.reshape(-1, 1) #把x变为 n行1列  
model = lm.LinearRegression()
model.fit(x, y)
# 模型预测  把样本的x传入模型，预测输出
pred_y = model.predict(x)
# 图像绘制
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, 
	s=60, label='Sample')
mp.plot(x, pred_y, c='orangered', 
	label='Regression Line')
mp.legend()
mp.show()
```

#### 评估训练结果误差（metrics）

线性回归模型训练完毕后，可以利用测试集评估训练结果误差。sklearn.metrics提供了计算模型误差的几个常用算法：

```python
import sklearn.metrics as sm

# 平均绝对值误差：mean(∑|实际输出-预测输出|)
sm.mean_absolute_error(y, pred_y)
# 平均平方误差：SQRT(1/mΣ(实际输出-预测输出)^2)
sm.mean_squared_error(y, pred_y)
# 中位绝对值误差：MEDIAN(|实际输出-预测输出|)
sm.median_absolute_error(y, pred_y)
# R2得分，(0,1]区间的分值。分数越高，误差越小。
sm.r2_score(y, pred_y)
```

案例：在上一个案例中使用sm评估模型误差。

```python
# 平均绝对值误差：1/m∑|实际输出-预测输出|
print(sm.mean_absolute_error(y, pred_y))
# 平均平方误差：SQRT(1/mΣ(实际输出-预测输 出)^2)
print(sm.mean_squared_error(y, pred_y))
# 中位绝对值误差：MEDIAN(|实际输出-预测输出|)
print(sm.median_absolute_error(y, pred_y))
# R2得分，(0,1]区间的分值。分数越高，误差越小。
print(sm.r2_score(y, pred_y))
```

#### 模型的保存和加载

模型训练是一个耗时的过程，一个优秀的机器学习模型是非常宝贵的。可以模型保存到磁盘中，也可以在需要使用的时候从磁盘中重新加载模型即可。不需要重新训练。

模型保存和加载相关API：

```python
import pickle
pickle.dump(内存对象, 磁盘文件) # 保存模型
model = pickle.load(磁盘文件)  # 加载模型
```

案例：把训练好的模型保存到磁盘中。

```python
# 将训练好的模型对象保存到磁盘文件中
with open('../../data/linear.pkl', 'wb') as f:
    pickle.dump(model, f)
    
# 从磁盘文件中加载模型对象
with open('../../data/linear.pkl', 'rb') as f:
    model = pickle.load(f)
# 根据输入预测输出
pred_y = model.predict(x)
```

#### 







