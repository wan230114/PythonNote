# Numpy中一些没用的技巧

## 行列转置

```python
import numpy as np
a = np.array([1, 2, 3, 4])
print(a.T.reshape(1,-1))
if 1:
    print("a is :")
    print(a)
```

## 一切皆为维度，没有水平垂直的说法

```python
import numpy as np
a = np.arange(0,20).reshape(2,2,5)
a
np.split(a, indices_or_sections=(3,), axis=2)

# 0是1维，有2个大元素，最外层
# 1是2维，有2个大元素，第二层
# 2是3维，有5个数值元素，最内层
# split翻译就是在第3维去将数据分成两份，分割的位置是第3维的第3个位置
# 水平垂直说法不利于维度理解
```

