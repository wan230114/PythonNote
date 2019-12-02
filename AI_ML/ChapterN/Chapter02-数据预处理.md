# 1. 数据预处理

数据预处理的过程： 输入数据 -> 模型 -> 输出数据

数据样本矩阵

| 年龄 | 学历 | 经验 | 性别 | 月薪  |
| ---- | ---- | ---- | ---- | ----- |
| 25   | 硕士 | 2    | 女   | 10000 |
| 20   | 本科 | 3    | 男   | 8000  |
| ...  | ...  | ...  | ...  | ...   |

一行一样本，一列一特征。

**数据预处理相关库**

```python
# 解决机器学习问题的科学计算工具包
import sklearn.preprocessing as sp
```

## 1.1. 均值移除(标准化)

由于一个样本的不同特征值差异较大，不利于使用现有机器学习算法进行样本处理。**均值移除**可以让样本矩阵中的每一列的平均值为0，标准差为1。

如何使样本矩阵中的每一列的平均值为0呢？

```
例如有一列特征值表示年龄： 17, 20, 23
mean = (17 + 20 + 23)/3 = 20
a' = -3
b' =  0
c' =  3
完成！
```

如何使样本矩阵中的每一列的标准差为1呢？

```
a' = -3
b' =  0
c' =  3
s' = std(a', b', c') 
[a'/s',  b'/s',  c'/s']
```

均值移除API：

```python
import sklearn.preprocessing as sp
# scale函数用于对函数进行预处理，实现均值移除。
# array为原数组，返回A为均值移除后的结果。
A = sp.scale(array)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
```

## 1.2. 范围缩放

将样本矩阵中的每一列的最小值和最大值设定为相同的区间，统一各列特征值的范围。一般情况下会把特征值缩放至[0, 1]区间。

如何使一组特征值的最小值为0呢？

```python
例如有一列特征值表示年龄： [17, 20, 23]
每个元素减去特征值数组所有元素的最小值即可：[0, 3, 6]
```

如何使一组特征值的最大值为1呢？

```python
[0, 3, 6]
把特征值数组的每个元素除以最大值即可：[0, 1/2, 1]
```

范围缩放API：

```python
# 创建MinMax缩放器
mms = sp.MinMaxScaler(feature_range=(0, 1))
# 调用mms对象的方法执行缩放操作, 返回缩放过后的结果
result = mms.fit_transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
print(raw_samples)
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([
        [col_min, 1],
        [col_max, 1]])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    col *= x[0]
    col += x[1]
print(mms_samples)
# 根据给定范围创建一个范围缩放器
mms = sp.MinMaxScaler(feature_range=(0, 1))
# 用范围缩放器实现特征值的范围缩放
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)
```

## 1.3. 归一化

有些情况每个样本的每个特征值具体的值并不重要，但是每个样本特征值的占比更加重要。

|      | Python | Java | PHP |
| ---- | ------ | ---- | --- |
| 2017 | 10     | 20   | 5   |
| 2018 | 8      | 5    | 0   |

所以归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和。变换后的样本矩阵，每个样本的特征值绝对值之和为1。

归一化相关API：

```python
# array 原始样本矩阵
# norm  范数
#    l1 - l1范数，向量中个元素绝对值之和
#    l2 - l2范数，向量中个元素平方之和
# 返回归一化预处理后的样本矩阵
sp.normalize(array, norm='l1')
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
print(raw_samples)
nor_samples = raw_samples.copy()
for row in nor_samples:
    row /= abs(row).sum()
print(nor_samples)
print(abs(nor_samples).sum(axis=1))
# 归一化预处理
nor_samples = sp.normalize(raw_samples, norm='l1')
print(nor_samples)
print(abs(nor_samples).sum(axis=1))
```

## 1.4. 二值化

有些业务并不需要分析矩阵的详细完整数据（比如图像边缘识别只需要分析出图像边缘即可），可以根据一个事先给定的阈值，用0和1表示特征值不高于或高于阈值。二值化后的数组中每个元素非0即1，达到简化数学模型的目的。

二值化相关API：

```python
# 给出阈值, 获取二值化器
bin = sp.Binarizer(threshold=阈值)
# 调用transform方法对原始样本矩阵进行二值化预处理操作
result = bin.transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
print(raw_samples)
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 80] = 0
bin_samples[bin_samples > 80] = 1
print(bin_samples)
# 根据给定的阈值创建一个二值化器
bin = sp.Binarizer(threshold=80)
# 通过二值化器进行二值化预处理
bin_samples = bin.transform(raw_samples)
print(bin_samples)
```

## 1.5. 独热编码

为样本特征的每个值建立一个由一个1和若干个0组成的序列，用该序列对所有的特征值进行编码。

（个人理解：取出每一列(样本特征)数值进行去重排序，然后按照位置进行编码，如下，看每一竖行）
```
两个数   三个数	四个数
1		3		2
7		5		4
1		8		6  
7		3		9
为每一个数字进行独热编码：
1-10    3-100	2-1000
7-01    5-010   4-0100
        8-001   6-0010
                9-0001
编码完毕后得到最终经过独热编码后的样本矩阵：
101001000
010100100
100010010
011000001
```

独热编码相关API：

```python
# 创建一个独热编码器
# sparse： 是否使用紧缩格式（稀疏矩阵）
# dtyle：  数据类型
ohe = sp.OneHotEncoder(sparse=是否采用紧缩格式, dtype=数据类型)
# 对原始样本矩阵进行处理，返回独热编码后的样本矩阵。
result = ohe.fit_transform(原始样本矩阵)
```

```python
ohe = sp.OneHotEncoder(sparse=是否采用紧缩格式, dtype=数据类型)
# 对原始样本矩阵进行训练，得到编码字典
encode_dict = ohe.fit(原始样本矩阵)
# 调用encode_dict字典的transform方法 对数据样本矩阵进行独热编码
result = encode_dict.transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
# 创建独热编码器
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
# 用独特编码器对原始样本矩阵做独热编码
ohe_dict = ohe.fit(raw_samples)
ohe_samples = ohe_dict.transform(raw_samples)

ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)
```


## 1.6. 标签编码

根据字符串形式的特征值在特征序列中的位置，为其指定一个数字标签，用于提供给基于数值算法的学习模型。

标签编码相关API：

```python
# 获取标签编码器
lbe = sp.LabelEncoder()
# 调用标签编码器的fit_transform方法训练并且为原始样本矩阵进行标签编码
result = lbe.fit_transform(原始样本矩阵)
# 根据标签编码的结果矩阵反查字典 得到原始数据矩阵
samples = lbe.inverse_transform(result)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'ford',
    'audi'])
print(raw_samples)
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)
inv_samples = lbe.inverse_transform(lbe_samples)
print(inv_samples)
```
