#%%
# import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold  # 主要用于K折交叉验证

# 以下是导入iris数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target
print(X.shape, y.shape)

# 定义我们想要搜索的k值（候选集），这里定义8不同的值
ks = [1, 3, 5, 7, 9, 11, 13, 15]

# 进行5折交叉验证，KFo1d返回的是每一折中训练数据和验证数据的index
# 假设数据样本为：[1，3，5，6，11，12，43，12，44，2]，总共10个样本
# 则返回的kf的格式为（前面的是训练数据，后面的是验证集）：
# [0, 1,    3,    5, 6, 7, 8, 9], [2, 4]
# [0, 1, 2,    4,    6, 7, 8, 9], [3, 5]
# [   1, 2, 3, 4, 5, 6, 7, 8   ], [0, 9]
# [0, 1, 2, 3, 4, 5,    7,    9], [6, 8]
# [0,    2, 3, 4, 5, 6,    8, 9], [1, 7]
kf = KFold(n_splits=5, random_state=2001, shuffle=True)
# 保存当前最好的K值和对应的准确率值
best_k = ks[0]
best_score = 0

# 循环每一个K值
for k in ks:
    curr_score = 0
    for train_index, valid_index in kf.split(X):
        # 每一折的训练以及计算准确率
        clf = KNeighborsClassifier(n_neighbors=k)
        clf.fit(X[train_index], y[train_index])
        curr_score = curr_score + clf.score(X[valid_index], y[valid_index])
    # 求一下5折的平均准确率
    avg_score = curr_score/5
    if avg_score > best_score:
        best_k = k
        best_score = avg_score
    print("current best score is: %.2f" % best_score, "best k: %d" % best_k)

print("after cross validation, the final best k is: %d" % best_k)
