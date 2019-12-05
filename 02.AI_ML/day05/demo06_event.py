"""
demo06_event.py 事件预测
1. 读文件，整理二维数组: data   shape:(5040, 5)
2. 解析data，数据预处理后整理输入集与输出集 
   x:(5040,4)   y:(5040,)
   数据预处理时：非数字字符串的特征需要做标签编码，
   数字字符串的特征需要做转换编码
3. 拆分测试集与训练集 
4. 构建svm模型并训练模型，使用测试集进行测试
5. 模型评估
6. 业务应用
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm


class DigitEncoder():
	# 模拟LabelEncoder编写的数字编码器

	def fit_transform(self, y):
		return y.astype('i4')
		
	def transform(self, y):
		return y.astype('i4')

	def inverse_transform(self, y):
		return y.astype('str')

data = []
with open('../ml_data/event.txt', 'r') as f:
	for line in f.readlines():
		data.append(line.split(','))
data = np.array(data)
data = np.delete(data, 1, axis=1)
cols = data.shape[1]  #获取一共有多少列
x, y = [], []
encoders = []
for i in range(cols):
	col = data[:, i]
	# 判断当前列是否是数字字符串
	if col[0].isdigit():
		encoder = DigitEncoder()
	else:
		encoder = sp.LabelEncoder()
	# 使用编码器对数据进行编码
	if i < cols-1:
		x.append(encoder.fit_transform(col))
	else:
		y = encoder.fit_transform(col)
	encoders.append(encoder)


x = np.array(x).T
y = np.array(y)

# 拆分测试集与训练集
train_x, test_x, train_y, test_y = \
	ms.train_test_split(x, y, test_size=0.25, 
		random_state=7)

# 构建模型
model=svm.SVC(kernel='rbf', class_weight='balanced')
model.fit(train_x, train_y)
# 测试
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y,pred_test_y))


# 业务应用
data = [['Tuesday', '13:30:00', '21', '23']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x) 
print(encoders[-1].inverse_transform(pred_y))

