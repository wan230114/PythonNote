# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import matplotlib.pyplot as mp
boston = sd.load_boston()
feature_names = boston.feature_names
x, y = su.shuffle(boston.data, boston.target,
                  random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
fi_dt = model.feature_importances_
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4),
    n_estimators=400, random_state=7)
model.fit(train_x, train_y)
fi_ab = model.feature_importances_
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('Decision Tree', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_dt.argsort()[::-1]
pos = np.arange(len(sorted_indices))
mp.bar(pos, fi_dt[sorted_indices],
       facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, feature_names[sorted_indices],
          rotation=30)
mp.subplot(212)
mp.title('AdaBoost Decision Tree', fontsize=16)
mp.xlabel('Feature', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_ab.argsort()[::-1]
pos = np.arange(len(sorted_indices))
mp.bar(pos, fi_ab[sorted_indices],
       facecolor='lightcoral', edgecolor='indianred')
mp.xticks(pos, feature_names[sorted_indices],
          rotation=30)
mp.tight_layout()
mp.show()
