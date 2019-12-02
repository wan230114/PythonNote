"""
demo06_vc.py   验证曲线
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

def f(s):
	return str(s, encoding='utf-8')

# 读取文件
data = np.loadtxt('../ml_data/car.txt', 
	delimiter=',', dtype='U20', 
	converters={0:f, 1:f, 2:f, 3:f, 4:f, 5:f, 6:f})
# 整理训练集的输入与输出
data = data.T
train_x, train_y = [], []
encoders = []
for col in range(len(data)):
	lbe = sp.LabelEncoder()
	if col < len(data)-1: # 不是最后一列
		train_x.append(lbe.fit_transform(data[col]))
	else:
		train_y = lbe.fit_transform(data[col])
	encoders.append(lbe) #保存每列的标签编码器

train_x = np.array(train_x).T
print(train_x)

# 交叉验证 训练模型
model = se.RandomForestClassifier(max_depth=9, 
	n_estimators=140, random_state=7)
# # 使用validation curve选择最优超参数
# train_scores, test_scores = \
# 	ms.validation_curve(model, train_x, 
# 		train_y, 'max_depth', 
# 		np.arange(5, 15), cv=5)

# # 画图显示超参数取值与模型性能之间的关系
# x = np.arange(5, 15)
# y = test_scores.mean(axis=1)
# mp.figure('max_depth', facecolor='lightgray')
# mp.title('max_depth', fontsize=20)
# mp.xlabel('max_depth', fontsize=14)
# mp.ylabel('F1 Score', fontsize=14)
# mp.tick_params(labelsize=10)
# mp.grid(linestyle=':')
# mp.plot(x, y, 'o-', c='dodgerblue', label='Training')
# mp.xticks(x)
# mp.legend()
# mp.show()


model.fit(train_x, train_y)

# 模型测试
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]
# 在训练时需要把所有的LabelEncoder保存下来，
# 在测试时，对测试数据的每一列使用相同的编码器进行编码，
# 然后进行预测，得出预测结果
data = np.array(data).T
test_x, test_y = [], []
for col in range(len(data)):
	encoder = encoders[col]
	if col<len(data)-1: 
		test_x.append(encoder.transform(data[col]))
	else:
		test_y = encoder.transform(data[col])
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
print(encoders[-1].inverse_transform(pred_test_y))
print(encoders[-1].inverse_transform(test_y))


