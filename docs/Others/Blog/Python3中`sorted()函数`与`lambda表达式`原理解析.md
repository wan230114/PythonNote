# Python3中`sorted()函数`与`lambda表达式`原理解析

相信很多小伙伴们在一开始学习Python的一些高级用法时遇到过很多困扰。
我准备日常分享一些比较浅显的原理解析帮助大家理解。

博主的原文：
- [lambda表达式](https://wan230114.github.io/PythonNote#00.Python/Chapter06.Function#lambda)
- [sorted()函数](https://wan230114.github.io/PythonNote#00.Python/Chapter06.Function#sorted)

---
@[TOC](目录：)


# 问题描述

很多小伙伴面对这样的排序，很是懵逼：

```python
# 预按照每个字典中键'b'的值进行列表排序
L = [{'a': 1, 'b': 4}, {'a': 1111, 'b': 2}, {'a': 1111, 'b': 3}]
L_sorted = sorted(L, key=lambda d: d['b'], reverse=False)
print(L_sorted)
```
运行结果：
```python
[{'a': 1111, 'b': 2}, {'a': 1111, 'b': 3}, {'a': 1, 'b': 4}]
```

这里面包含了函数高级用法中的sorted和lambda的两个用法

下面，我将逐一解析。

# 原理解析
- `lambda表达式`相当于一个简化的函数
- `sorted(iterable, key=None, reverse=False)`，此处的`key=`需要传递一个函数，相当于将`iterable`中的每一个元素迭代取出，传入`key=`处给定的函数，通过函数处理返回的值组成的新的迭代对象，通过该新对象的排序映射回`iterable`完成排序。

---
示例1：lambda表达式理解：
```python
# 1) 普通函数func_add的定义
def func_add(x, y):
    return x + y
print(func_add(10, 20))  # 30

# 2) 对于函数func_add, 可以使用lambda表达式一行定义
myadd = lambda x, y: x + y
print(myadd(10, 20))  # 30
```

---
示例2: sorted函数理解
```python
# sorted原理解析 —— 自定义函数实现sorted
def my_sorted(iters, key=None, reverse=None):
    if key:
        DICT = dict()
        for it in iters:
            # 用函数处理过后的值做键, 处理相同的键加入列表
            DICT.setdefault(key(it), []).append(it)
        INDEX = list(DICT)  # 获得函数处理过后的值列表
        INDEX.sort(reverse=reverse)  # 排序
        # 按顺序展开
        return [xx for x in INDEX for xx in DICT[x]]
    else:
        INDEX = list(iters)
        INDEX.sort(reversed=reverse)
        return INDEX


names = ['Tom', 'Spike', 'Jerry', 'Tyke']

L = sorted(names, key=len, reverse=True)
print(L)  # 结果 ['Tom', 'Tyke', 'Jerry', 'Spike']

L = my_sorted(names, key=len, reverse=True)
print(L)  # 结果 ['Tom', 'Tyke', 'Jerry', 'Spike']
```


# 附：原文基础知识
## lambda表达式
（原文链接： [lambda表达式](https://wan230114.github.io/PythonNote#00.Python/Chapter06.Function#lambda)）


引入：
- 除了def语句可以创建函数之外，lambda表达式也可以创建函数。

概念：
- lambda表达式（又称匿名函数），用于封装有限的逻辑的函数
- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

语法格式：
- `lambda [变量1，变量2，… ]:表达式`

说明：
- 可以省略变量
- 只能包含一条表达式

---
示例：lambda函数理解
```python
# 1) 普通函数func_add的定义
def func_add(x, y):
    return x + y
print(func_add(10, 20))  # 30

# 2) 对于函数func_add, 可以使用lambda表达式一行定义
myadd = lambda x, y: x + y
print(myadd(10, 20))  # 30

# 3) 语法理解 x 为形参接收值, 后面紧跟表达式返回值
myfunc = lambda x: 123 + x
print(myfunc(100))  # 223

# lambda可以行使正常函数的所有功能
myfunc = lambda: print('hello', end=' ')
print(myfunc())  # hello None

# 求1到10的平方和
fun = lambda x: sum([x * x for x in range(1, x + 1)])
print(fun(10))  # 385
```

##  sorted 函数
（原文链接： [sorted()函数](https://wan230114.github.io/PythonNote#00.Python/Chapter06.Function#sorted)）

- 作用:
  - 将原可迭代对象提供的数据进行排序，生成排序后的列表
- 格式:
  - `sorted(iterable, key=None, reverse=False)`
  - 说明:
    - `iterable` 可迭代对象
    - `key` 函数是用来提供一个排序参考值的函数，这个函数的返回值将作为排序的依据
    - `reverse` 标志用来设置是否降序排序
  - 返回
    - 列表`list`
- 理解：
  - 此处的`key=`需要传递一个函数，相当于将`iterable`中的每一个元素迭代取出，传入`key=`处给定的函数，通过函数处理返回的值组成的新的迭代对象，通过该新对象的排序映射回`iterable`完成排序。


- 与列表中自带方法 `L.sort()` 有什么区别？
  - `sorted(L)`
    - 是Building域名空间的一个系统函数；
    - 是将L作为参数输入，返回新列表，对原列表无影响；
  - `L.sort()`
    - 是list类中的一个方法，只能痛殴；
    - 是将L的内部元素进行直接排列，不返回新对象
  - 示例：
    ```python
    L = [3, 5, 4, 2, 1]
    L2 = sorted(L)
    print("L:", L, "L2:", L2)
    # L: [3, 5, 4, 2, 1] L2: [1, 2, 3, 4, 5]
    a = L.sort()
    print("L:", L, "a:", a)
    # L: [1, 2, 3, 4, 5] a: None
    ```
---
示例1: sorted的简单示例
```python
L = [5, -2, -4, 0, 3, 1]
print(sorted(L))  # 直接按大小排序
# [-4, -2, 0, 1, 3, 5]
print(sorted(L, key=abs))  # 按绝对值排序
# [0, 1, -2, 3, -4, 5]
print(sorted(L, key=abs, reverse=True)  # 按绝对值降序排序
# [5, -4, 3, -2, 1, 0]
```

---
示例2: sorted原理解析 —— 自定义函数实现sorted
```python
# sorted原理解析 —— 自定义函数实现sorted
def my_sorted(iters, key=None, reverse=None):
    if key:
        DICT = dict()
        for it in iters:
            # 用函数处理过后的值做键, 处理相同的键加入列表
            DICT.setdefault(key(it), []).append(it)
        INDEX = list(DICT)  # 获得函数处理过后的值列表
        INDEX.sort(reverse=reverse)  # 排序
        # 按顺序展开
        return [xx for x in INDEX for xx in DICT[x]]
    else:
        INDEX = list(iters)
        INDEX.sort(reversed=reverse)
        return INDEX


names = ['Tom', 'Spike', 'Jerry', 'Tyke']

L = sorted(names, key=len, reverse=True)
print(L)  # 结果 ['Tom', 'Tyke', 'Jerry', 'Spike']

L = my_sorted(names, key=len, reverse=True)
print(L)  # 结果 ['Tom', 'Tyke', 'Jerry', 'Spike']
```

---
高级示例：
- `lambda`与`sorted`高级联用
1. 对列表里的字典排序
```python
L = [{'a': 1, 'b': 4}, {'a': 1111, 'b': 2}, {'a': 1111, 'b': 3}]
L_sorted = sorted(L, key=lambda d: d['b'], reverse=False)
# [{'a': 1111, 'b': 2}, {'a': 1111, 'b': 3}, {'a': 1, 'b': 4}]
```

2. 对字典进行按key排序
```python
d = {'a':25, 'c':27, 'b':20, 'd':22}
L_sorted = sorted(d.items(), key=lambda x:x[0])
print(L_sorted)
# [('a', 25), ('b', 20), ('c', 27), ('d', 22)]
```

3. 对字典进行按values排序

```python
d = {'a':25, 'c':27, 'b':20, 'd':22}
L_sorted = sorted(d.items(), key=lambda x:x[1])
print(L_sorted)
# [('b', 20), ('d', 22), ('a', 25), ('c', 27)]
```

4. 降序排序的另类写法
- 问题一：如何对字母进行数学上写法的降序排序？
  - 利用`ord()`函数转为编码值，再`*-1`
```python
Data = [['y', 2], ['x', 3], ['z', 4], ['a',1]]

# 对每个列表的第一个值进行正常排序
print(sorted(Data, key=lambda x: x[0]))
# [['a', 1], ['x', 3], ['y', 2], ['z', 4]]
# 对每个列表的第一个值进行降序排序
print(sorted(Data, key=lambda x: x[0], reverse=True))
# [['z', 4], ['y', 2], ['x', 3], ['a', 1]]
print(sorted(Data, key=lambda x: ord(x[0])*-1))  # 问题一
# [['z', 4], ['y', 2], ['x', 3], ['a', 1]]

# 对每个列表的第二个值进行正常排序
print(sorted(Data, key=lambda x: x[1]))
# [['a', 1], ['y', 2], ['x', 3], ['z', 4]]
# 对每个列表的第二个值进行降序排序
print(sorted(Data, key=lambda x: x[1], reverse=True))
# [['z', 4], ['x', 3], ['y', 2], ['a', 1]]
print(sorted(Data, key=lambda x: x[1]*-1))
# [['z', 4], ['x', 3], ['y', 2], ['a', 1]]
```

5. 多重排序
- 难点：
  - 如何实现部分列的升序和部分列的降序排序同时存在？
```python
# - 排序规则
#   - 先按照书籍编号降序排序
#   - 再按照书名正序排序
#   - 再按照年份降序排序

# 书籍的编号
number = {
    "Robinson Crusoe": "B",
    "The Old Man and the Sea": "A",
    "The Little Prince": "C",
    "Secret garden": "A",
    "Thorn bird": "A"
}

# 年份，书籍，销售额
data_text = """2017,126,Robinson Crusoe
2017,110,The Old Man and the Sea
2017,152,The Little Prince
2017,98,Secret garden
2017,89,Thorn bird
2018,116,Robinson Crusoe
2018,98,The Old Man and the Sea
2018,176,The Little Prince
2018,79,Secret garden
2018,90,Thorn bird
2019,122,Robinson Crusoe
2019,102,The Old Man and the Sea
2019,187,The Little Prince
2019,102,Secret garden
2019,103,Thorn bird"""

Datas = [x.split(',') for x in data_text.splitlines()]
# 对数据进行排序
result = sorted(Datas, key=lambda x: (ord(number[x[2]])*-1,
                                      x[2], int(x[0])*-1))
# 结果的打印
for x in result:
    print(number[x[2]], *x, sep='\t')
```
运行结果：
```
C       2019    187     The Little Prince
C       2018    176     The Little Prince
C       2017    152     The Little Prince
B       2019    122     Robinson Crusoe
B       2018    116     Robinson Crusoe
B       2017    126     Robinson Crusoe
A       2019    102     Secret garden
A       2018    79      Secret garden
A       2017    98      Secret garden
A       2019    102     The Old Man and the Sea
A       2018    98      The Old Man and the Sea
A       2017    110     The Old Man and the Sea
A       2019    103     Thorn bird
A       2018    90      Thorn bird
A       2017    89      Thorn bird
```

- itemgetter与attrgetter模块的使用
  - 可以简化代码
```python
from operator import itemgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

# 按照索引为2的数据排序
print(sorted(student_tuples, key=itemgetter(2)))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# 多重排序：按照索引为1，再按照2的数据排序
print(sorted(student_tuples, key=itemgetter(1, 2)))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```
```python
from operator import attrgetter

 class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

# 按age排序
print(sorted(student_objects, key=attrgetter('age')))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# 多重排序，先以grade，然后再以age来排序
print(sorted(student_objects, key=attrgetter('grade', 'age')))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

练习:
  - 已知:
    - `names = ['Tom', 'Jerry', 'Spike', 'Tyke']`
  - 排序的依据为原字符串反序的字符串
    - `'moT', 'yrreJ', 'ekipS', 'ekyT'`
  - 结果:
    - `['Spike', 'Tyke', 'Tom', 'Jerry']`

参考：
```python
>>> sorted(['Tom', 'Jerry', 'Spike', 'Tyke'],
           key=lambda x:x[::-1])
['Spike', 'Tyke', 'Tom', 'Jerry']
```
