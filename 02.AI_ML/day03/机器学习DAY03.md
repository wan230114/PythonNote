# 机器学习DAY03

### 集合算法

#### 正向激励

**特征重要性**

作为决策树模型训练过程的副产品，根据每个特征划分子表前后的信息熵减少量就标志了该特征的重要程度，此即为该特征重要性指标。训练得到的模型对象提供了属性：feature_importances_来存储每个特征的重要性。

获取样本矩阵特征重要性属性：

```python
model.fit(train_x, train_y)
fi = model.feature_importances_
```

案例：获取普通决策树与正向激励决策树训练的两个模型的特征重要性值，按照从大到小顺序输出绘图。

```python
import matplotlib.pyplot as mp

model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
# 决策树回归器给出的特征重要性
fi_dt = model.feature_importances_
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
model.fit(train_x, train_y)
# 基于决策树的正向激励回归器给出的特征重要性
fi_ab = model.feature_importances_

mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('Decision Tree', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_dt.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_dt[sorted_indices], facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, feature_names[sorted_indices], rotation=30)
mp.subplot(212)
mp.title('AdaBoost Decision Tree', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_ab.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_ab[sorted_indices], facecolor='lightcoral', edgecolor='indianred')
mp.xticks(pos, feature_names[sorted_indices], rotation=30)
mp.tight_layout()
mp.show()
```

##### 自助聚合

每次从总样本矩阵中以有放回抽样的方式随机抽取部分样本构建决策树，这样形成多棵包含不同训练样本的决策树，以削弱某些强势样本对模型预测结果的影响，提高模型的泛化特性。

##### 随机森林

在自助聚合的基础上，每次构建决策树模型时，不仅随机选择部分样本，而且还随机选择部分特征，这样的集合算法，不仅规避了强势样本对预测结果的影响，而且也削弱了强势特征的影响，使模型的预测能力更加泛化。

随机森林相关API：

```python
import sklearn.ensemble as se
# 随机森林回归模型	（属于集合算法的一种）
# max_depth：决策树最大深度10
# n_estimators：构建1000棵决策树，训练模型
# min_samples_split: 子表中最小样本数 若小于这个数字，则不再继续向下拆分
model = se.RandomForestRegressor(max_depth=10, n_estimators=1000, min_samples_split=2)
```

案例：分析共享单车的需求，从而判断如何进行共享单车的投放。

```python
"""
demo02_rf.py   随机森林回归器
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm

# 读取bike_day.csv数据集
headers = None
data = []
with open('../ml_data/bike_day.csv', 'r') as f:
	for i, line in enumerate(f.readlines()):
		if i==0:
			headers = line.split(',')[2:]
		else:
			data.append(line.split(',')[2:])
headers = np.array(headers)
data = np.array(data, dtype='f8')

# 整理数据集   
x = data[:, 0:11]
y = data[:, -1]
# 拆分测试集与训练集
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]

# 构建随机森林回归器模型  并训练模型
model = se.RandomForestRegressor(max_depth=10, 
	n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
# 针对测试集进行预测  输出评估得分
pred_test_y = model.predict(test_x)
print('r2 for day.csv:', sm.r2_score(test_y, pred_test_y))
# 获取特征重要性
day_fi = model.feature_importances_
day_headers = headers[0:11]
print(day_headers)

# 读取bike_hour.csv数据集
headers = None
data = []
with open('../ml_data/bike_hour.csv', 'r') as f:
	for i, line in enumerate(f.readlines()):
		if i==0:
			headers = line.split(',')[2:]
		else:
			data.append(line.split(',')[2:])
headers = np.array(headers)
data = np.array(data, dtype='f8')

# 整理数据集   
x = data[:, 0:12]
y = data[:, -1]
# 拆分测试集与训练集
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]

# 构建随机森林回归器模型  并训练模型
model = se.RandomForestRegressor(max_depth=10, 
	n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
# 针对测试集进行预测  输出评估得分
pred_test_y = model.predict(test_x)
print('r2 for hour.csv:', sm.r2_score(test_y, pred_test_y))
# 获取特征重要性
hour_fi = model.feature_importances_
hour_headers = headers[0:12]

# 绘制特征重要性柱状图
# 柱状图显示特征重要性
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('Feature Importances', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
x = np.arange(day_fi.size)
sorted_indices = np.argsort(day_fi)[::-1]
mp.bar(x, day_fi[sorted_indices], 0.8, 
	color='dodgerblue', label='day FI')
mp.xticks(x, day_headers[sorted_indices])
mp.legend()

mp.subplot(212)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
x = np.arange(hour_fi.size)
sorted_indices = np.argsort(hour_fi)[::-1]
mp.bar(x, hour_fi[sorted_indices], 0.8, 
	color='orangered', label='hour FI')
mp.xticks(x, hour_headers[sorted_indices])
mp.legend()
mp.show()
```

### 



