数据分析DAY01


**什么是数据分析？**

数据分析是指用适当的统计分析方法对收集来的大量数据进行分析，提取有用信息和形成结论而对数据加以详细研究和概括总结的过程。

**使用python做数据分析的常用库**
  1. numpy  基础数值算法
  2. scipy  科学计算
  3. matplotlib   数据可视化
  4. pandas       序列高级函数

# 1. numpy概述
1. Numerical Python，数值的Python，补充了Python语言所欠缺的数值计算能力。
2. Numpy是其它数据分析及机器学习库的底层库。
3. Numpy完全标准C语言实现，运行效率充分优化。
4. Numpy开源免费。

## 1.1. numpy历史

1. 1995年，Numeric，Python语言数值计算扩充。
2. 2001年，Scipy->Numarray，多维数组运算。
3. 2005年，Numeric+Numarray->Numpy。
4. 2006年，Numpy脱离Scipy成为独立的项目。

## 1.2. numpy的核心：多维数组

1. 代码简洁：减少Python代码中的循环。
2. 底层实现：厚内核(C)+薄接口(Python)，保证性能。

# 2. numpy基础

## 2.1. ndarray数组

用np.ndarray类的对象表示n维数组

```python
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary))
```

- **内存中的ndarray对象**

    - **元数据（metadata）**
    存储对目标数组的描述信息，如：dim count、dimensions、dtype、data等。
    
    - **实际数据**
        完整的数组数据
        将实际数据与元数据分开存放，一方面提高了内存空间的使用效率，另一方面减少对实际数据的访问频率，提高性能。

- **ndarray数组对象的特点**
    - Numpy数组是同质数组，即所有元素的数据类型必须相同
    - Numpy数组的下标从0开始，最后一个元素的下标为数组长度减1
    
### 2.1.1. ndarray数组对象的创建

np.array(任何可被解释为Numpy数组的逻辑结构)
np.arange(起始值(0),终止值,步长(1))
np.zeros(数组元素个数, dtype='类型')
np.ones(数组元素个数, dtype='类型')

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(type(a))  # <class 'numpy.ndarray'>
a = np.arange(0, 10, 2)
print(a)  # [0 2 4 6 8]
a = np.zeros(10)
print(a)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
a = np.ones(10)
print(a)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

### 2.1.2. ndarray对象属性的基本操作

**数组的维度：** np.ndarray.shape
```python
import numpy as np
ary = np.array([[1,2,3,4], [5,6,7,8]])
print(type(ary), ary.shape)  # <class 'numpy.ndarray'> (2, 4)
```

**元素的类型：** np.ndarray.dtype
```python
import numpy as np
ary = np.array([1, 2, 3, 4])
print(ary, ary.dtype)  # [1 2 3 4] int32
# ary.dtype = 'int64'    error
# print(ary, ary.dtype)
ary = ary.astype('float64') # return new instance
print(ary, ary.dtype)  # [1. 2. 3. 4.] float64
ary = ary.astype('str') # return new instance
print(ary, ary.dtype)  # ['1.0' '2.0' '3.0' '4.0'] <U32
```
**数组元素的个数：** np.ndarray.size
```python
import numpy as np
ary = np.array([[1,2,3,4], [5,6,7,8]])
# 第六章 观察维度，size，len的区别
print(ary.shape, ary.size, len(ary))  # (2, 4) 8 2
```

**数组元素索引(下标)**

数组对象[..., 页号, 行号, 列号]

下标从0开始，到数组len-1结束。

```python
import numpy as np
a = np.array([[[1, 2], [3, 4]],
            [[5, 6], [7, 8]]])
print(a, a.shape)  # [[[1 2] [3 4]]   [[5 6] [7 8]]]  (2, 2, 2)
print(a[0])     # [[1 2] [3 4]]
print(a[0][0])  # [1 2]
print(a[0][0][0])  # 1
print(a[0, 0, 0])  # 1
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i, j, k])  # 1 2 3 4 5 6 7 8
```

### 2.1.3. ndarray对象属性操作详解

**Numpy的内部基本数据类型**

| 类型名       | 类型表示符                          |
|--------------|-------------------------------------|
| 布尔型       | bool_                               |
| 有符号整数型 | int8(-128~127)/int16/int32/int64    |
| 无符号整数型 | uint8(0~255)/uint16/uint32/uint64   |
| 浮点型       | float16/float32/float64             |
| 复数型       | complex64/complex128                |
| 字串型       | str_，每个字符用32位Unicode编码表示 |

**自定义复合类型**

```python
"""
demo04_obj.py  自定义复合数据类型
"""
import numpy as np

data = [('zs', [50,51,52], 15),
        ('ls', [83,71,62], 16),
        ('ww', [90,91,92], 17)]

#第一种dtype的设置方式
ary = np.array(data, dtype='U2, 3int32, int32')
print(ary, ary[0][1])
print(ary[0]['f0'])

#第二种dtype的设置方式
ary = np.array(data, 
        dtype=[ ('name', 'str', 2), 
                ('scores', 'int32', 3), 
                ('age', 'int32', 1)])
print('-' * 45)
print(ary, ary.dtype)
print(ary[0]['age']) # 返回zs的年龄
print(ary[2]['scores']) # 返回ww的成绩

# 第三种dtype的设置方式
ary = np.array(data, dtype={
    'names':['name', 'scores', 'age'],
    'formats':['U2', '3int32', 'int32']})
print(ary)
print(ary[0]['age']) # 返回zs的年龄
print(ary[2]['scores']) # 返回ww的成绩


# 第四种dtype的设置方式
d = np.array(data, dtype={'name': ('U3', 0),
                    'scores': ('3int32', 16),
                    'age': ('int32', 28)})
print(d[0]['name'], d[0]['scores'], d.itemsize)

# ndarray数组存放日期数据
dates = ['2011-01-01', '2012-01-01', 
         '2011-02-01', '2012', 
         '2011-01-01 10:10:10']
ary = np.array(dates)
print(ary, ary.dtype)
ary = ary.astype('M8[D]')
print(ary, ary.dtype, ary[1]-ary[0]) 
```

**类型字符码**

| 类型              | 字符码                              |
|-------------------|-------------------------------------|
| np.bool_          | ?                                   |
| np.int8/16/32/64  | i1/i2/i4/i8                         |
| np.uint8/16/32/64 | u1/u2/u4/u8                         |
| np.float/16/32/64 | f2/f4/f8                            |
| np.complex64/128  | c8/c16                              |
| np.str_           | U<字符数>                           |
| np.datetime64     | M8[Y] M8[M] M8[D] M8[h] M8[m] M8[s] |

**字节序前缀，用于多字节整数和字符串：**
`</>/[=]分别表示小端/大端/硬件字节序。`

**类型字符码格式**

<字节序前缀><维度><类型><字节数或字符数>

| 3i4      | 释义                                                                                       |
|----------|--------------------------------------------------------------------------------------------|
| 3i4      | 3个元素的一维数组，每个元素都是整型，每个整型元素占4个字节。                               |
| <(2,3)u8 | 小端字节序，6个元素2行3列的二维数组，每个元素都是无符号整型，每个无符号整型元素占8个字节。 |
| U7       | 包含7个字符的Unicode字符串，每个字符占4个字节，采用默认字节序。                            |

#### 2.1.3.1. ndarray数组对象的维度操作

**视图变维（数据共享）：** reshape() 与 ravel() 

```python
import numpy as np
a = np.arange(1, 9)
print(a)		# [1 2 3 4 5 6 7 8]
b = a.reshape(2, 4)	#视图变维  : 变为2行4列的二维数组
print(b)
c = b.reshape(2, 2, 2) #视图变维    变为2页2行2列的三维数组
print(c)
d = c.ravel()	#视图变维	变为1维数组
print(d)
```

**复制变维（数据独立）：** flatten()

```python
e = c.flatten()
print(e)
a += 10
print(a, e, sep='\n')
```

**就地变维：直接改变原数组对象的维度，不返回新数组**

```python
a.shape = (2, 4)
print(a)
a.resize(2, 2, 2)
print(a)
```

#### 2.1.3.2. ndarray数组切片操作

```python
#数组对象切片的参数设置与列表切面参数类似
#  步长+：默认切从首到尾
#  步长-：默认切从尾到首
数组对象[起始位置:终止位置:步长]
#默认位置步长：1
```

```python
import numpy as np
a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])  # 1 2 3
print(a[3:6])   # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[...])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9
```

**多维数组的切片操作**

```python
# 多维数组切片
import numpy as np
print('-' * 45)
a = np.arange(1, 10)
a = a.reshape(3, 3)
print(a)
print(a[:2, :])  # 切出前两行数据
print(a[:2, :2])  # 切出前两行两列数据
print(a[::2, :])  # 
print(a[..., :1])  # 切出每一行第一列数据
```

#### 2.1.3.3. ndarray数组的掩码操作

```python
"""
demo07_mask.py  掩码操作
"""
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a + 10)
print(a * 2.5)
print(a + a)

# 输出100以内3的倍数
a = np.arange(1, 10)
mask = a % 3 == 0
print(mask)
print(a[mask])

mask = [2, 2, 3, 3, 6, 6, 4, 4]
print(a)
print(a[mask])
```

#### 2.1.3.4. 多维数组的组合与拆分

长度相等数组组合：
1. 垂直方向操作
2. 水平方向操作
3. 深度方向操作（3维）

```python
import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 垂直方向完成组合操作，生成新数组
c1 = np.vstack((a, b))
# 垂直方向完成拆分操作，生成两个数组
d1, e1 = np.vsplit(c, 2)

# 水平方向完成组合操作，生成新数组
c2 = np.hstack((a, b))
# 水平方向完成拆分操作，生成两个数组
d2, e2 = np.hsplit(c, 2)

# 深度方向（3维）完成组合操作，生成新数组
c3 = np.dstack((a, b))
# 深度方向（3维）完成拆分操作，生成两个数组
d3, e3 = np.dsplit(i, 2)
```

长度不等的数组组合：

```python
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4])
# 填充b数组使其长度与a相同
# pad_width=(a, b)：在数组首部补a个元素，尾部补b个元素
b = np.pad(b, pad_width=(0, 1), mode='constant', constant_values=-1)
print(b)
# 垂直方向完成组合操作，生成新数组
c = np.vstack((a, b))
print(c)
```

多维数组组合与拆分的相关函数：

```python
# 通过axis作为关键字参数指定组合的方向，取值如下：
# 若待组合的数组都是二维数组：
#	0: 垂直方向组合
#	1: 水平方向组合
# 若待组合的数组都是三维数组：
#	0: 垂直方向组合
#	1: 水平方向组合
#	2: 深度方向组合
np.concatenate((a, b), axis=0)
# 通过给出的数组与要拆分的份数，按照某个方向进行拆分，axis的取值同上
np.split(c, 2, axis=0)
```

简单的一维数组组合方案

```python
a = np.arange(1,9)		#[1, 2, 3, 4, 5, 6, 7, 8]
b = np.arange(9,17)		#[9,10,11,12,13,14,15,16]
#把两个数组摞在一起成两行
c = np.row_stack((a, b))
print(c)
#把两个数组组合在一起成两列
d = np.column_stack((a, b))
print(d)
```

### 2.1.4. ndarray类的其他属性

- shape - 维度
- dtype - 元素类型
- size - 元素数量
- ndim - 维数，len(shape)
- itemsize - 元素字节数
- nbytes - 总字节数 = size x itemsize
- real - 复数数组的实部数组
- imag - 复数数组的虚部数组
- T - 数组对象的转置视图
- flat - 扁平迭代器

```python
import numpy as np
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.real, a.imag, sep='\n')
print(a.T)
print([elem for elem in a.flat])
b = a.tolist()
print(b)
```

# 3. numpy快速生成数组
```python
# 从-π到π区间拆10个点
import numpy as np
x = np.linspace(-np.pi, np.pi, 10)
print(x)
```