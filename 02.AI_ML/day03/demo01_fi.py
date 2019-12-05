"""
demo01_fi.py   特征重要性
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import numpy as np
import sklearn.ensemble as se

# 加载数据集
boston = sd.load_boston()
print(boston.data.shape) # 输入集
print(boston.target.shape)  # 输出集 
fnames = boston.feature_names
print(fnames)

# 打乱数据集
x, y = su.shuffle(boston.data, boston.target, 
	random_state=7)
# 划分训练集与测试集
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]

# 构建决策树模型， 训练模型
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
# 预测
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
# 输出单棵决策树的特征重要性
dt_fi = model.feature_importances_


# 正向激励决策树的特征重要性
# 构建正向激励决策树模型
model = se.AdaBoostRegressor(model, 
	n_estimators=400, random_state=7)
model.fit(train_x, train_y)
ad_fi = model.feature_importances_


# 柱状图显示特征重要性
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('Decision Tree', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
x = np.arange(13)
sorted_indices = np.argsort(dt_fi)[::-1]
mp.bar(x, dt_fi[sorted_indices], 0.8, 
	color='dodgerblue', label='DT FI')
mp.xticks(x, fnames[sorted_indices])
mp.legend()

mp.subplot(212)
mp.title('AdaBoostRegressor', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = np.argsort(ad_fi)[::-1]
mp.bar(x, ad_fi[sorted_indices], 0.8, 
	color='orangered', label='AdaBoost FI')
mp.xticks(x, fnames[sorted_indices])
mp.legend()


mp.show()

