#%%

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
