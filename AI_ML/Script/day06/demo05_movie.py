"""
demo05_movie.py  电影推荐
"""
import json
import numpy as np

with open('../ml_data/ratings.json', 'r') as f:
    ratings = json.loads(f.read())
# 获取所有用户列表
users = list(ratings.keys())
# 存储用户与用户之间相似度信息的矩阵
scmat = []
for user1 in users:
	scrow = []   # 存储user1对所有用户的相似度得分
	for user2 in users:
		movies = set() # 存储两个人都看过的电影
		for movie in ratings[user1]:
			if movie in ratings[user2]:
				movies.add(movie)
		# 通过movies列表 计算两人的相似度得分
		if len(movies) == 0:
			score = 0
		else:  
		    # a:存储user1的电影评分  b:存储user2的电影评分
		    a, b = [], []
		    for movie in movies:
		    	a.append(ratings[user1][movie])
		    	b.append(ratings[user2][movie])
		    # 通过欧式距离得分算法计算相似度
		    a = np.array(a)
		    b = np.array(b)
		    score = np.corrcoef(a,b)[0,1]
			# score = 1 / (1+np.sqrt(((a-b)**2).sum()))
		scrow.append(score)
	scmat.append(scrow)

print(np.round(scmat, 2))

