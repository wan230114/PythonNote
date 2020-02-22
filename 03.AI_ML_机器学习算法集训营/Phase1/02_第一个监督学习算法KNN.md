# 2. 第一个监督学习算法KNN（K近邻算法）

最容易理解的算法：理解核心不超过5分钟  
最容易突现的算法：从零突现不超过5行代码  

## 算法思想

选择一个预测目标，计算“预测目标”和“所有样本”之间的距离或者相似度，然后选择距离最近的前K个样本，然后通过这些样本的分类来投票决策。 

![](img/2020-01-12-23-10-25.png)

## 2.1. 代码实例

<font face="仿宋">

**1) 导入模块**  
第一个import是用来导入一个样本数据。sklearn库本身已经提供了不少可以用来测试模型的样本数据，所以通过这个模块的导入就可以直接使用这些数据了。  
第二个import是用来做数据集的分割，把数据分成训练集和测试集，这样做的目的是为了评估模型。  
第三个是导入了KNN的模块，是sklearn提供的现成的算法。  
  
**2) 导入数据集**  
这几行代码是用来导入数据集的。在这里我们导入的数据集叫做iris数据集，也是开源数据中最为重要的数据集之一。  
这个数据包含了3个类别，所以适合的问题是分类问题。另外，具体数据集的描述可以参考：https://archive.ics.uci.edu/ml/datasets/Iris/  
从print(x,y)结果可以看到X拥有四个特征，并且标签y拥有0，1，2三种不同的值。  
  
**3) 数据集分割**  
在这里X存储的是数据的特征，y存储的每一个样本的标签或者分类。我们使用 train_test_split来把数据分成了训练集和测试集。主要的目的是为了在训练过程中也可以验证模型的效果。如果没有办法验证，则无法知道模型训练的好坏。   
这里的random_state就像随机生成器中的seed。通过不同的值采样的训练数据和测试数据是不一样的。设定一个固定的random_state有助于诊断程序本身，因为每次所期待的结果都会一样。  
  
**4) 使用KNN算法**  
这部分是KNN算法的主要模块。首先在这里我们定义了一个KNN object，它带有一个参数叫做n_neighbors=3， 意思就是说我们选择的K值是3.   
  
**5) 模型评估**  
这部分的代码主要用来做预测以及计算准确率。计算准确率的逻辑也很简单，就是判断预测和实际值有多少是相等的。如果相等则算预测正确，否则预测失败。  

</font>

```python
# 1) 导入模块
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 2) 导入数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 3) 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2003)

# 4) 使用KNN算法
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# 5) 模型评估
correct = np.count_nonzero((predictions == y_test) == True)
print("Accuracy is: %.3f" % (correct/len(X_test)))
```


## 2.2. KNN算法的具体实现细节
### 2.2.1. 自定义代码实现
改进版：（使用类定义实现同sklearn一样的调用方法）
```python
# 1) 导入模块
from sklearn import datasets
from collections import Counter  # 为了做投票
from sklearn.model_selection import train_test_split
import numpy as np


class KNN_model(object):
    def __init__(self, n_neighbors):
        self.n_neighbors = n_neighbors

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        return np.array([self.__knn_classify__(self.X, self.y, xx_test)
                         for xx_test in X_test])

    def __euc_dis__(self, instance1, instance2):
        """
        计算两个样本instance1和instance2之间的欧式距离
        instance1: 第一个样本， array型
        instance2: 第二个样本， array型
        """
        # TODO
        dist = np.sqrt(sum((instance1 - instance2)**2))
        return dist

    def __knn_classify__(self, X, y, testInstance):
        """
        给定一个测试数据testInstance, 通过KNN算法来预测它的标签。
        X: 训练数据的特征
        y: 训练数据的标签
        testInstance: 测试数据，这里假定一个测试数据 array型
        """
        # TODO  返回testInstance的预测标签 = {0,1,2}
        # 计算每个测试数据到每个点的距离
        distances = [self.__euc_dis__(x, testInstance) for x in X]
        # 取出排名前n个的元素索引, n_neighbors 选择多少个neighbors?
        kneighbors = np.argsort(distances)[:self.n_neighbors]
        # 取出这些元素组成新序列，进行统计每个元素次数
        count = Counter(y[kneighbors])
        # 列出最常见的元素，取第一个数。作为分类的y值输出
        return count.most_common()[0][0]


# 2) 导入iris数据
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 3) 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2003)

# 4) 预测结果。
clf = KNN_model(n_neighbors=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# 5) 模型评估
correct = np.count_nonzero((predictions == y_test) == True)
print("Accuracy is: %.3f" % (correct/len(X_test)))
```

### 2.2.2. 基本的4个信息
为了实现一个KNN算法，我们需要具备四个方面的信息：`向量化-->标注-->距离计算-->k的选择`

1. 把一个物体表示成向量
2. 标记好每个物体的标签（i.e.，offer / no offer）
3. 计算两个物体之间的距离/相似度
4. 选择合适的k

第一、任何的算法的输入一定是数量化的信息，我们把它叫做特征，需要把现实生活中的物体通过数字化的特征来进行描述。

![](img/2019-11-21-12-08-02.png)

第二、由于KNN是监督学习算法，所以需要提前标注好的样本。
![](img/2019-11-21-14-33-25.png)

第三、我们需要想办法来计算两个样本之间的距离或者相似度，之后才能选出最相近的样本。

![](img/2019-11-21-14-31-51.png)

第四、需要知道如何选择最合适的K值，那为了理解这一点首先要理解K对模型本身的影响。这部分在第二节里会做重点解释。

![](img/2019-11-21-15-05-39.png)


## 2.3. 如何选择最合适的K值？
### 2.3.1. 决策边界

图示：

![](img/2019-11-21-15-13-12.png)

### 2.3.2. 决策边界的种类
决策边界分成两大类，分别是`线性决策边界`和`非线性决策边界`。拥有线性决策边界的模型我们称为线性模型，反之非线性模型。

图示：

![](img/2019-11-21-15-20-34.png)

引出新问题，`泛化`和`过拟合`问题？

在上述决策边界里，后两个是非线性的决策边界。而且如视频里所说的一样，最后一个决策边界在数据上的表现是最好的。

但这不代表未来数据上，也就是测试数据上表现最好。这里涉及到了一个很重要的概念，叫做模型的泛化能力，可以简单理解成“它在新的环境中的适应能力”，当然这个环境需要跟已有的环境类似才行。

### 2.3.3. 决策边界的确认方法


图示：**（通过KNN算法确认区域内每个像素点所属绿色还是红色）**

![](img/2019-11-21-15-52-06.png)

代码示例：不同k，对边界的影响
```python
import matplotlib.pyplot as plt    
import numpy as np    
from itertools import product    
from sklearn.neighbors import KNeighborsClassifier    
    
# 生成一些随机样本    
n_points = 100    
X1 = np.random.multivariate_normal([1,50], [[1,0],[0,10]], n_points)    
X2 = np.random.multivariate_normal([2,50], [[1,0],[0,10]], n_points)    
X = np.concatenate([X1,X2])    
y = np.array([0]*n_points + [1]*n_points)    
print (X.shape, y.shape)    
    
    
# KNN模型的训练过程    
clfs = []    
neighbors = [1,3,5,9,11,13,15,17,19]    
for i in range(len(neighbors)):    
    clfs.append(KNeighborsClassifier(n_neighbors=neighbors[i]).fit(X,y))     
       
    
# 可视化结果    
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1    
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1    
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),    
                     np.arange(y_min, y_max, 0.1))    
    
f, axarr = plt.subplots(3,3, sharex='col', sharey='row', figsize=(15, 12))    
for idx, clf, tt in zip(product([0, 1, 2], [0, 1, 2]),    
                        clfs,    
                        ['KNN (k=%d)'%k for k in neighbors]):    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])    
    Z = Z.reshape(xx.shape)    
        
    axarr[idx[0], idx[1]].contourf(xx, yy, Z, alpha=0.4)    
    axarr[idx[0], idx[1]].scatter(X[:, 0], X[:, 1], c=y,    
                                  s=20, edgecolor='k')    
    axarr[idx[0], idx[1]].set_title(tt)    
        
plt.show()
```
### 2.3.4. 交叉验证

交叉验证是机器学习建模中非常非常重要的一步，也是大多数人所说的“调参”的过程。

在KNN里，通过交叉验证，我们即可以得出最合适的K值。它的核心思想无非就是把一些可能的K逐个去尝试一遍，然后选出效果最好的K值。

#### 2.3.4.1. K折交叉验证(K-fold Cross Validation)
—— 常用的交叉验证技术

**思想总结**：
> 逐次取每一组超参数，对一个完整数据集，按不同部分部位依次取出数据集做测试集，验证模型，计算该部位的准确率，随后取不同部位准确率的平均值，比较不同超参数下的平均准确率孰高孰低，取准确率更高的对应超参数。

K通常选取5、10、20  

![](img/2019-12-11-19-19-17.png)

![](img/2019-12-11-19-00-41.png)

最极端的情况下，我们可以采用leave_one_out交叉验证，也就是每次只把一个样本当做验证数据，剩下的其他数据都当做是训练样本。
- 留一法leave_one_out



## 2.4. 特征缩放
- 线性归一化（Min-max Normalization）
- 标准差归一化（Z-score Normalization）

## 2.5. 图像识别项目
- 图片原始特征
  - 转换为像素值

- 常用的图片特征【rotation-invariant，旋转不变特征？】
  - 颜色特征（Color Histogram）
  - SIFT（Scale-invariant feature transform）
  - HOG（Histogram of Oriented Grandient）

## 2.6. KNN进阶
### 2.6.1. 缺失值的处理
- 删除属性：相应的属性全部删掉，即整列。
- 删除记录：删除相应的记录，即整行。
- 填补法：均值、中位数的填补法

### 2.6.2. 特征编码技术

数据的一些类别(categorical)特征。可以通过以下方式编码：
- 标签编码
- 独热编码

一般如何处理数值型变量呢？ 这个答案我相信很多人都知道，其实就是直接去使用，不做任何的编码。那是不是数值类型的变量真的就没必要做一些编码操作呢？ 其实不一定的。有一种技术叫做`变量的离散化操作`。

