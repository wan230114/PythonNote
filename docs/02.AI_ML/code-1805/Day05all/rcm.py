# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import numpy as np
with open('../../data/ratings.json', 'r') as f:
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
            score = np.corrcoef(x, y)[0, 1]
        scrow.append(score)
    scmat.append(scrow)
users = np.array(users)
scmat = np.array(scmat)
for i, user in enumerate(users):
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[
        sorted_indices != i]
    similar_users = users[sorted_indices]
    similar_scores = scmat[i, sorted_indices]
    positive_mask = similar_scores > 0
    similar_users = similar_users[positive_mask]
    similar_scores = similar_scores[positive_mask]
    score_sums, weight_sums = {}, {}
    for similar_user, similar_score in zip(
            similar_users, similar_scores):
        for movie, score in ratings[
                similar_user].items():
            if movie not in ratings[user].keys():
                if movie not in score_sums.keys():
                    score_sums[movie] = 0
                score_sums[movie] += score * similar_score
                if movie not in weight_sums.keys():
                    weight_sums[movie] = 0
                weight_sums[movie] += similar_score
    movie_ranks = {}
    for movie, score_sum in score_sums.items():
        movie_ranks[movie] = score_sum / weight_sums[movie]
    sorted_indices = np.array(list(
        movie_ranks.values())).argsort()[::-1]
    recomms = np.array(list(
        movie_ranks.keys()))[sorted_indices]
    print(user, '->', recomms)
