# 机器学习DAY06

#### 凝聚层次算法

首先假定每个样本都是一个独立的聚类，如果统计出来的聚类数大于期望的聚类数，则从每个样本出发寻找离自己最近的另一个样本，与之聚集，形成更大的聚类，同时令总聚类数减少，不断重复以上过程，直到统计出来的聚类数达到期望值为止。

凝聚层次算法的特点：

1. 聚类数k必须事先已知。借助某些评估指标，优选最好的聚类数。
2. 没有聚类中心的概念，因此只能在训练集中划分聚类，但不能对训练集以外的未知样本确定其聚类归属。
3. 在确定被凝聚的样本时，除了以距离作为条件以外，还可以根据连续性来确定被聚集的样本。

凝聚层次算法相关API：

```python
# 凝聚层次聚类器
model = sc.AgglomerativeClustering(n_clusters=4)
pred_y = model.fit_predict(x)
```

案例：重新加载multiple3.txt，使用凝聚层次算法进行聚类划分。 

```python
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
x = np.loadtxt('../data/multiple3.txt', delimiter=',')
# 凝聚层次聚类器
model = sc.AgglomerativeClustering(n_clusters=4)
pred_y = model.fit_predict(x)
mp.figure('Agglomerative Cluster', facecolor='lightgray')
mp.title('Agglomerative Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=80)
mp.show()
```

在确定被凝聚的样本时，除了以距离作为条件以外，还可以根据连续性来确定被聚集的样本。

```python
import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as nb
import matplotlib.pyplot as mp
n_samples = 500
x = np.linspace(-1, 1, n_samples)
y = np.sin(x * 2 * np.pi)
n = 0.3 * np.random.rand(n_samples, 2)
x = np.column_stack((x, y)) + n
# 无连续性的凝聚层次聚类器
model_nonc = sc.AgglomerativeClustering( linkage='average', n_clusters=3)
pred_y_nonc = model_nonc.fit_predict(x)
# 近邻筛选器
conn = nb.kneighbors_graph( x, 10, include_self=False)
# 有连续性的凝聚层次聚类器
model_conn = sc.AgglomerativeClustering(
    linkage='average', n_clusters=3, connectivity=conn)
pred_y_conn = model_conn.fit_predict(x)
mp.figure('Nonconnectivity', facecolor='lightgray')
mp.title('Nonconnectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y_nonc, cmap='brg', alpha=0.5, s=30)
mp.figure('Connectivity', facecolor='lightgray')
mp.title('Connectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y_conn, cmap='brg', alpha=0.5, s=30)
mp.show()
```

#### 轮廓系数

好的聚类：内密外疏，同一个聚类内部的样本要足够密集，不同聚类之间样本要足够疏远。

轮廓系数计算规则：针对样本空间中的一个特定样本，计算它与所在聚类其它样本的平均距离a，以及该样本与距离最近的另一个聚类中所有样本的平均距离b，该样本的轮廓系数为(b-a)/max(a, b)，将整个样本空间中所有样本的轮廓系数取算数平均值，作为聚类划分的性能指标s。

轮廓系数的区间为：[-1, 1]。 -1代表分类效果差，1代表分类效果好。0代表聚类重叠，没有很好的划分聚类。

轮廓系数相关API：

```python
import sklearn.metrics as sm
# v：平均轮廓系数
# metric：距离算法：使用欧几里得距离(euclidean)
v = sm.silhouette_score(输入集, 输出集, sample_size=样本数, metric=距离算法)
```

案例：输出KMeans算法聚类划分后的轮廓系数。

```python
# 打印平均轮廓系数
print(sm.silhouette_score( x, pred_y, sample_size=len(x), metric='euclidean'))
```

#### DBSCAN算法

从样本空间中任意选择一个样本，以事先给定的半径做圆，凡被该圆圈中的样本都视为与该样本处于相同的聚类，以这些被圈中的样本为圆心继续做圆，重复以上过程，不断扩大被圈中样本的规模，直到再也没有新的样本加入为止，至此即得到一个聚类。于剩余样本中，重复以上过程，直到耗尽样本空间中的所有样本为止。

DBSCAN算法的特点：

1. 事先给定的半径会影响最后的聚类效果，可以借助轮廓系数选择较优的方案。

2. 根据聚类的形成过程，把样本细分为以下三类：

   外周样本：被其它样本聚集到某个聚类中，但无法再引入新样本的样本。

   孤立样本：聚类中的样本数低于所设定的下限，则不称其为聚类，反之称其为孤立样本。

   核心样本：除了外周样本和孤立样本以外的样本。

DBSCAN聚类算法相关API：

```python
# DBSCAN聚类器
# eps：半径
# min_samples：聚类样本数的下限，若低于该数值，则称为孤立样本
model = sc.DBSCAN(eps=epsilon, min_samples=5)
model.fit(x)
# 获取训练后所有聚类的核心样本的索引数组  
# 可以以此作为掩码，获取所有的核心样本
indices = model.core_sample_indices_
# 每个样本的聚类类别标签  [0,1,2,3,0,1,2,3,0,1,2,3,-1]
labels = model.labels_
# 对于dbscan，会出现-1的情况，label=-1的样本就是孤立样本
```

案例：修改凝聚层次聚类案例，基于DBSCAN聚类算法进行聚类划分，选择最优半径。

```python
import numpy as np
import sklearn.cluster as sc
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x = np.loadtxt('../data/perf.txt', delimiter=',')
epsilons, scores, models = np.linspace(0.3, 1.2, 10), [], []
for epsilon in epsilons:
    # DBSCAN聚类器
    model = sc.DBSCAN(eps=epsilon, min_samples=5)
    model.fit(x)
    score = sm.silhouette_score(
        x, model.labels_, sample_size=len(x), metric='euclidean')
    scores.append(score)
    models.append(model)
scores = np.array(scores)
best_index = scores.argmax()
best_epsilon = epsilons[best_index]
print(best_epsilon)
best_score = scores[best_index]
print(best_score)
best_model = models[best_index]
```

案例：获取核心样本、外周样本、孤立样本。并且使用不同的点型绘图。

```python
best_model = models[best_index]
pred_y = best_model.fit_predict(x)
core_mask = np.zeros(len(x), dtype=bool)
core_mask[best_model.core_sample_indices_] = True
offset_mask = best_model.labels_ == -1
periphery_mask = ~(core_mask | offset_mask)
mp.figure('DBSCAN Cluster', facecolor='lightgray')
mp.title('DBSCAN Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
labels = best_model.labels_
mp.scatter(x[core_mask][:, 0], x[core_mask][:, 1], c=labels[core_mask], 
           cmap='brg', s=80, label='Core')
mp.scatter(x[periphery_mask][:, 0], x[periphery_mask][:, 1], alpha=0.5,
           c=labels[periphery_mask], cmap='brg', marker='s', s=80, label='Periphery')
mp.scatter(x[offset_mask][:, 0], x[offset_mask][:, 1],
           c=labels[offset_mask], cmap='brg', marker='x', s=80, label='Offset')
mp.legend()
mp.show()
```

**聚类模型**

KMeans、MeanShift（均值漂移），凝聚层次、DBSCAN



### 推荐引擎

推荐引擎意在把最需要的推荐给用户。

在不同的机器学习场景中通常需要分析相似样本。而统计相似样本的方式可以基于欧氏距离分数，也可基于皮氏距离分数。

**欧氏距离分数**
$$
欧氏距离分数 = \frac{1}{1+欧氏距离}
$$
计算所得欧氏距离分数区间处于：(0, 1]，越趋于0样本间的欧氏距离越远，样本越不相似；越趋于1，样本间的欧氏距离越近，越相似。

构建样本之间的欧氏距离得分矩阵：
$$
\left[
 \begin{array}{c}
  	  & a & b & c & d & .. \\
  	a & 1 & 0.2 & 0.3 & 0.4 & .. \\
  	b & 0.2 & 1 & x & x & .. \\
  	c & 0.3 & x & 1 & x & .. \\
  	d & 0.4 & x & x & 1 & .. \\
  	.. & .. & .. & .. & .. & .. \\

  \end{array}
  \right]
$$
案例：解析ratings.json，根据每个用户对已观看电影的打分计算样本间的欧氏距离，输出欧氏距离得分矩阵。

```python
import json
import numpy as np

with open('../data/ratings.json', 'r') as f:
    ratings = json.loads(f.read())
users, scmat = list(ratings.keys()), []
for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()
        for movie in ratings[user1]:
            if movie in ratings[user2]:
                movies.add(movie)
        if len(movies) == 0:
            score = 0
        else:
            x, y = [], []
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
            score = 1 / (1 + np.sqrt(((x - y) ** 2).sum()))
        scrow.append(score)
    scmat.append(scrow)
users = np.array(users)
scmat = np.array(scmat)
for scrow in scmat:
    print('  '.join('{:.2f}'.format(score) for score in scrow)) 
```

**皮尔逊相关系数**

```
A = [1,2,3,1,2] 
B = [3,4,5,3,4] 
m = np.corrcoef(A, B)
```

皮尔逊相关系数 = 协方差 / 标准差之积

相关系数处于[-1, 1]区间。越靠近-1代表两组样本反相关，越靠近1代表两组样本正相关。

案例：使用皮尔逊相关系数计算两用户对一组电影评分的相关性。

```python
score = np.corrcoef(x, y)[0, 1]
```

**按照相似度从高到低排列每个用户的相似用户**

```python
# scmat矩阵中每一行为 每一个用户对所有用户的皮尔逊相关系数
for i, user in enumerate(users):
    # 拿到所有相似用户与相似用户所对应的皮尔逊相关系数
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[sorted_indices != i]
    similar_users = users[sorted_indices]
    similar_scores = scmat[i, sorted_indices]
    print(user, similar_users, similar_scores, sep='\n')
```

**生成推荐清单**

1. 找到所有皮尔逊系数正相关的用户
2. 遍历当前用户的每个相似用户，拿到相似用户看过但是当前用户没有看过的电影作为推荐电影
3. 多个相似用户有可能推荐同一部电影，则取每个相似用户对该电影的评分得均值作为推荐度。
4. 可以把相似用户的皮尔逊系数作为权重，皮尔逊系数越大，推荐度越高。

```python
    # 找到所有皮尔逊系数正相关的用户
    positive_mask = similar_scores > 0
    similar_users = similar_users[positive_mask]
    # 相似用户对应的皮尔逊相关系数
    similar_scores = similar_scores[positive_mask]
    #存储对于当前用户所推荐的电影以及电影的推荐度(推荐电影的平均分)
    recomm_movies = {}
    #遍历当前用户的每个相似用户
    for i, similar_user in enumerate(similar_users):
        #拿到相似用户看过但是当前用户没有看过的电影
        for movie, score in ratings[similar_user].items():
            if (movie not in ratings[user].keys()):
                if movie not in recomm_movies:
                    recomm_movies[movie] = []
                else:
                    recomm_movies[movie].append(score)
                    
    print(user)
    movie_list = sorted(recomm_movies.items(), key=lambda x:np.average(x[1]), reverse=True)
    print(movie_list)
```















