
#%%

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
