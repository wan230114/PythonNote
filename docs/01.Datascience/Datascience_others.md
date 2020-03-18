## 投票
统计一维数组中每个元素出现的次数，获取最高的值
```python
from collections import Counter
count = Counter(np.array([0, 0, 1, 2, 2, 2]))
# count: Counter({0: 2, 1: 1, 2: 3})
count.most_common()
# [(2, 3), (0, 2), (1, 1)]
```
应用：该函数可用于后续章节中，自定义KNN算法函数进行投票决策。