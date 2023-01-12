#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2022-11-05, 11:12:10
# @ Modified By: Chen Jun
# @ Last Modified: 2022-11-05, 11:55:20
#############################################

# %%
import numpy as np
from sklearn.cluster import KMeans

# %%
################################
########## 1) 基本使用 ##########
################################

# 1. 先用5个点，5个聚类，训练重心
X = np.array([0, 1/3, 1/2, 2/3, 1]).reshape(-1, 1)
km = KMeans(n_clusters=5, random_state=0).fit(X)
print("查看重心:", list(km.cluster_centers_.reshape(-1)))
# 2. 获得分类与lable的映射关系
cluster = dict(zip(km.labels_.reshape(-1), X.reshape(-1)))
cluster

# %%
# 3. 输入inDatas，准备使用KMeans分类
inDatas = [0, 0.1, 0.01,
           1/3, 1/3+0.01, 1/3-0.01,
           1/2, 1/2+0.01, 1/2-0.01,
           2/3, 2/3+0.01, 2/3-0.01,
           1, 1+0.01, 1-0.01,
           ]
y = km.predict(np.array(inDatas).reshape(-1, 1))  # 会得出每个sample属于哪一类
# 4. 输出result, 归类后的结果
result = list(map(lambda x: cluster[x], y))
result

# %%
##############################
########## 2) 封装  ##########
##############################


class useKMeans(object):
    """docstring for useKMeans."""

    def __init__(self):
        # 先用5个点，5个聚类，定义重心
        X = np.array([0, 1/3, 1/2, 2/3, 1]).reshape(-1, 1)
        self.km = KMeans(n_clusters=5, random_state=0).fit(X)
        # print("查看重心:", list(self.km.cluster_centers_.reshape(-1)))
        # 获得分类与lable的映射关系
        self.cluster = dict(zip(self.km.labels_.reshape(-1), X.reshape(-1)))

    def predict(self, inDatas):
        # 会得出每个sample属于哪一类
        y = self.km.predict(np.array(inDatas).reshape(-1, 1))
        # 输出result, 归类后的结果
        return list(map(lambda x: self.cluster[x], y))


# 输入inDatas，准备使用KMeans分类
inDatas = [0, 0.1, 0.01,
           1/3, 1/3+0.01, 1/3-0.01,
           1/2, 1/2+0.01, 1/2-0.01,
           2/3, 2/3+0.01, 2/3-0.01,
           1, 1+0.01, 1-0.01,
           ]
kms = useKMeans()
result = kms.predict(inDatas)
result
