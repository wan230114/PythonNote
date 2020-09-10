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
