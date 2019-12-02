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








