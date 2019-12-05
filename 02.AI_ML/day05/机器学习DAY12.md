# 机器学习DAY05

### 支持向量机(SVM)

#### 支持向量机原理

1. **寻求最优分类边界**

   正确：对大部分样本可以正确地划分类别。

   泛化：最大化支持向量间距。

   公平：与支持向量等距。

   简单：线性，直线或平面，分割超平面。

2. **基于核函数的升维变换**

   通过名为核函数的特征变换，增加新的特征，使得低维度空间中的线性不可分问题变为高维度空间中的线性可分问题。 

   **线性核函数**：linear，不通过核函数进行维度提升，仅在原始维度空间中寻求线性分类边界。

   基于线性核函数的SVM分类相关API：

   ```python
   import sklearn.svm as svm
   model = svm.SVC(kernel='linear')
   model.fit(train_x, train_y)
   ```

   案例：对multiple2.txt中的数据进行分类。

   ```python
   import numpy as np
   import sklearn.model_selection as ms
   import sklearn.svm as svm
   import sklearn.metrics as sm
   import matplotlib.pyplot as mp
   x, y = [], []
   data = np.loadtxt('../data/multiple2.txt', delimiter=',', dtype='f8')
   x = data[:, :-1]
   y = data[:, -1]
   train_x, test_x, train_y, test_y = \
       ms.train_test_split(x, y, test_size=0.25, random_state=5)
   # 基于线性核函数的支持向量机分类器
   model = svm.SVC(kernel='linear')
   model.fit(train_x, train_y)
   n = 500
   l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
   b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
   grid_x = np.meshgrid(np.linspace(l, r, n),
                        np.linspace(b, t, n))
   flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))    
   flat_y = model.predict(flat_x)
   grid_y = flat_y.reshape(grid_x[0].shape)
   pred_test_y = model.predict(test_x)
   cr = sm.classification_report(test_y, pred_test_y)
   print(cr)
   mp.figure('SVM Linear Classification', facecolor='lightgray')
   mp.title('SVM Linear Classification', fontsize=20)
   mp.xlabel('x', fontsize=14)
   mp.ylabel('y', fontsize=14)
   mp.tick_params(labelsize=10)
   mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
   mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=80)
   mp.show()
   ```

   **多项式核函数**：poly，通过多项式函数增加原始样本特征的高次方幂
   $$
   y = x_1+x_2 \\
   y = x_1^2 + 2x_1x_2 + x_2^2 \\
   y = x_1^3 + 3x_1^2x_2 + 3x_1x_2^2 + x_2^3
   $$
   案例，基于多项式核函数训练sample2.txt中的样本数据。

   ```python
   # 基于线性核函数的支持向量机分类器
   model = svm.SVC(kernel='poly', degree=3)
   model.fit(train_x, train_y)
   ```

   **径向基核函数**：rbf，通过高斯分布函数增加原始样本特征的分布概率

   案例，基于径向基核函数训练sample2.txt中的样本数据。

   ```python
   # 基于径向基核函数的支持向量机分类器
   # C：正则强度
   # gamma：正态分布曲线的标准差
   model = svm.SVC(kernel='rbf', C=600, gamma=0.01)
   model.fit(train_x, train_y)
   ```

#### 样本类别均衡化

通过类别权重的均衡化，使所占比例较小的样本权重较高，而所占比例较大的样本权重较低，以此平均化不同类别样本对分类模型的贡献，提高模型性能。

样本类别均衡化相关API：

```python
model = svm.SVC(kernel='linear', class_weight='balanced')
model.fit(train_x, train_y)
```

案例：修改线性核函数的支持向量机案例，基于样本类别均衡化读取imbalance.txt训练模型。

```python
... ...
... ...
data = np.loadtxt('../data/imbalance.txt', delimiter=',', dtype='f8')
x = data[:, :-1]
y = data[:, -1]
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=5)
# 基于线性核函数的支持向量机分类器
model = svm.SVC(kernel='linear', class_weight='balanced')
model.fit(train_x, train_y)
... ...
... ...
```

#### 置信概率

根据样本与分类边界的距离远近，对其预测类别的可信程度进行量化，离边界越近的样本，置信概率越低，反之，离边界越远的样本，置信概率高。

获取每个样本的置信概率相关API：

```python
# 在获取模型时，给出超参数probability=True
model = svm.SVC(kernel='rbf', C=600, gamma=0.01, probability=True)
预测结果 = model.predict(输入样本矩阵)
# 调用model.predict_proba(样本矩阵)可以获取每个样本的置信概率矩阵
置信概率矩阵 = model.predict_proba(输入样本矩阵)
```

置信概率矩阵格式如下：

|       | 类别1 | 类别2 |
| ----- | ----- | ----- |
| 样本1 | 0.8   | 0.2   |
| 样本2 | 0.9   | 0.1   |
| 样本3 | 0.5   | 0.5   |

案例：修改基于径向基核函数的SVM案例，新增测试样本，输出每个测试样本的执行概率，并给出标注。

```python
# 整理测试样本
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)
print(probs)

# 绘制每个测试样本，并给出标注
mp.scatter(prob_x[:,0], prob_x[:,1], c=pred_prob_y, cmap='jet_r', s=80, marker='D')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})
```

#### 网格搜索

获取一个最优超参数的方式可以绘制验证曲线，但是验证曲线只能每次获取一个最优超参数。如果多个超参数有很多排列组合的话，就可以使用网格搜索寻求最优超参数组合。

针对超参数组合列表中的每一个超参数组合，实例化给定的模型，做cv次交叉验证，将其中平均f1得分最高的超参数组合作为最佳选择，实例化模型对象。

网格搜索相关API：

```python
import sklearn.model_selection as ms
model = ms.GridSearchCV(模型, 超参数组合列表, cv=折叠数)
model.fit(输入集，输出集)
# 获取网格搜索每个参数组合
model.cv_results_['params']
# 获取网格搜索每个参数组合所对应的平均测试分值
model.cv_results_['mean_test_score']
# 获取最好的参数
model.best_params_   # 最优超参数组合
model.best_score_    # 最优得分
model.best_estimator_  # 最优模型对象
```

案例：修改置信概率案例，基于网格搜索得到最优超参数。

```python
# 基于径向基核函数的支持向量机分类器
params = [{'kernel':['linear'], 'C':[1, 10, 100, 1000]},
    {'kernel':['poly'], 'C':[1], 'degree':[2, 3]}, 
    {'kernel':['rbf'], 'C':[1,10,100,1000], 'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(svm.SVC(probability=True), params, cv=5)
model.fit(train_x, train_y)
for p, s in zip(model.cv_results_['params'],
        model.cv_results_['mean_test_score']):
    print(p, s)
# 获取得分最优的的超参数信息
print(model.best_params_)
# 获取最优得分
print(model.best_score_)
# 获取最优模型的信息
print(model.best_estimator_)
```

### 案例：事件预测

加载event.txt，预测某个时间段是否会出现特殊事件。

案例：

```python
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
```

### 