import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

x, y = [], []  # 输入和输出
with open('../ml_data/multiple1.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)
train_x, test_x, train_y, test_y = ms.train_test_split(
     x, y, test_size=0.25, random_state=7)

# 训练分类器，朴素贝叶斯分类器
model = nb.GaussianNB(solver='liblinear', C=1000)
