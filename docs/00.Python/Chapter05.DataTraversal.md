# 5. 数据的遍历访问

- 数据的遍历方法常见的有：
  - for循环遍历（此章不再赘述）
  - 

## 5.2. for循环应用之几大常用推导式

推导式：数据遍历后进行存放列表、字典、集合，或生成生成器的操作

作用：使常用操作语法更为简易

**列表推导式**

- 定义：是由可迭代对象依次生成带有多个元素的列表的表达式

- 语法：  
    ```python
    [表达式 for 变量 in 可迭代对象 [if 真值表达式]]
    ```

- 嵌套语法：（过程与多重for循环一致）
    ```python
    [表达式
        for 变量1 in 可迭代对象1 [if 真值表达式1]
            for 变量2 in 可迭代对象2 [if 真值表达式2]
            …
    ```

- 过程理解:
  1. 先从可迭代对象中取值，用变量绑定取值
  2. 用 if 进行条件判断，如果为真值则添加到列表中
  3. 重复上述操作，直至可迭代对象完全遍历完毕

**字典推导式**

- 定义：字典推导式是用可迭代的对象依次生成字典的表达式

- 语法:
    ```python
    { 键表达式: 值表达式 for 变量 in 可迭代对象 [if 真值表达式]}
    ```
    同样的，推导式内的for子句可以嵌套

**集合推导式**

- 定义：集合推导式是用可迭代对象生成集合的表达式

- 语法：
    ```python
    {表达式 for 变量 in 可迭代对象 [if 真值表达式]}
    ```
    同样的，推导式内的for子句可以嵌套

**生成器表达式**  
  - 生成器表达式与以上语法类似，不同之处在于使用了迭代器，语法使用了元组相同的括号，但却不是生成元组，将放于下一节 [生成器表达式](#jump) 描述

---

示例1：列表推导式的简洁体现
```python
# 三行实现
L = []
for x in range(1, 10):
    L.append(x ** 2)
print(L)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 一行实现：使用列表推导式
L2 = [x ** 2 for x in range(1, 10)]
print(L2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

示例2：列表推导式使用
```python
# 1) 生成1到30内的奇数序列
L3 = [x for x in range(1, 30) if x%2==1]
print(L3)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

# 2) 生成字母与数字混合的序列
L = [x + y for x in 'ABC' for y in '123']
print(L)
# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# 3) 批量转换字符类型，str-->int，转换字符串类型列表为数字类型列表
L = ['100', '200', '300', '400', '500']
L1 = [int(x) for x in L]
print(L)  # [100, 200, 300, 400, 500]
S = '123456789'
L = [int(x) for x in S]
print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4) 批量判断字典的值中是否包含True
D = {1: 0, 2: 0, 3: 1}
print(bool([x for x in D.values() if x]))  # True
```

示例3: 字典和集合的推导式
```python
# 1) 生成一个字典，键为1~4的整数,值为键的平方
print({x: x**2 for x in range(1, 5)})
# {1: 1, 2: 4, 3: 9, 4: 16}

# 2) 生成一个集合，1~4的整数
print({x for x in range(1, 5)})
# {1, 2, 3, 4}
```

## 5.3. 可迭代对象的遍历
从内存中取出数据真如我们使用for看起来这么简单吗？让我们来了解一下原理。

- 学习先导：
  - 可迭代对象有三种类型：
    * 可迭代对象`iterable`
    * 迭代器`iterator`
    * 生成器`generator`
  - 可以这样理解三者关系：
    * 可迭代对象`iterable` $>$ 迭代器`iterator` $>$ 生成器`generator`
  - 判断方法：
    - 可以使用`isinstance()`判断一个对象是否是`iterable`/`iterator`/`generator`对象。  
        示例：
        ```python
        from collections import Iterable,Iterator,Generator # 导入对象
        
        def judge(x):
            """判断对象是否是可迭代对象、迭代器对象、生成器对象"""
            print(isinstance(x, Iterable),
                  isinstance(x, Iterator),
                  isinstance(x, Generator))
        
        def myfunc():
            for x in range(5):
                yield  x
        # 1) 判断可迭代对象
        judge([])        # True False False
        # 2) 判断迭代器对象
        judge(iter([]))  # True True False
        # 3) 判断生成器对象
        judge(myfunc())  # True True True
        ```

### 5.3.1. 可迭代对象Iterable
可迭代对象(Iterable)：可以用于for循环的迭代的对象。包括
- 各类数据容器类型（list、tuple、dict、set、str等）
- 迭代器（Iterator）
- 生成器（generator）
- 一些常见函数如`range()`
- ...


### 5.3.2. 迭代器Iterator
#### 5.3.2.1. 基本概念
- 基本概念
  * 迭代器是访问可迭代对象的一种方式。
  * 迭代器是访问可迭代对象的工具(对象)。
- 说明:
  - 迭代器只能向前取值,不能后退
  - 用iter函数可以返回一个可迭代对象的迭代器

- 类别：
  - open(file, 'r')文件对象
  - iter(iterable)函数对象
  - 生成器对象
  - ...

- 迭代器的特征（为什么需要迭代器和生成器？)
  - 惰性计算。调取迭代对象元素前不消耗内存空间，现用现生成。
  - 边调用边删除调用过的对象。迭代器每取出一个元素，迭代器对象将会删除这个元素。

#### 5.3.2.2. 迭代器函数iter()、next()、reversed()
- `iter(iterable)` 从可迭代对象中返回一个迭代器,iterable必须是一个能提供迭代器的可迭代对象
- `next(iterator[, default])` 从迭代器iterator中获取下一条记录。如果无法获取下一条记录，当指定default参数时则返回指定内容，否则触发StopIteration异常。（异常处理可参考后续章节）  
    ```python
    L = [2, 3, 5]
    it = iter(L)  # 让可迭代对象L 提供一个迭代器
    next(it)  # 2
    next(it)  # 3
    next(it)  # 5
    # next(it)  # StopIteration 异常通知
    ```
    注意：next(iterator)，内容必须是迭代器iterator，否则触发TypeError异常。
    ```python
    >>> next([1,2,3])  # 触发异常
    Traceback (most recent call last):
    File "<pyshell#7>", line 1, in <module>
        next([1,2,3])
    TypeError: 'list' object is not an iterator
    >>> next(iter([1,2,3]))  # 正常
        1
    ```
- `reversed()` 反向迭代
  -  `reversed(lst)`一般用于for语句中反向迭代

<span id="jump_for"></span>

- `for语句`的本质：使用迭代器方法取出数据  
    > 解释：  
    > for语句本质上是迭代器的一种封装；  
    > 用iter()函数，while语句、next迭代器方法，try处理迭代结束异常；  
    > 即可遍历列表L中的全部元素。此为for语句本质

---
示例1：for语句的迭代器实现
```python
# 能否不使用for循环，仅用迭代器访问 L 中的数?
# 不使用for循环的迭代：
L = [1, 2, 3, 4]
it = iter(L)
while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        break
print("\nthe end")
# 1 2 3 4 
# the end
```

### 5.3.3. 生成器Generator
- 问题引入：
  - 当出现大数据需要处理时，若将所有数据存储完于内存再运算可能会造成内存溢出，如何解决？
  - 时间 vs 空间
  - 计算机内存有限，生成器函数能用计算的时间换取内存的空间。

- 概念：
  - 生成器是能够动态提供数据的对象

- 特点：
  - 生成器对象也是可迭代对象
  - <font color='red'>生成器是一种特殊的迭代器</font>。
  - 同迭代器一样，数据取出也是一次性的，数据被使用后就被删除

- 成器有两种：
  - 生成器函数
  - 生成器表达式

#### 5.3.3.1. 生成器函数之yield语句

- 定义：  
    - 含有 yield 语句的函数是生成器函数，此函数被调用时将返回一个生成器对象 （ps: yield 翻译为产生或生成）

- 生成器函数说明:
  1. 含有yield的函数返回一个生成器对象，生成器对象是一个可迭代对象
  2. 生成器函数中一般不要使用return，调用 return 也不会有任何返回，并且可能导致生成器提前终止。

- 语法：
    ```python
    def f():
        yield 表达式1
        yield 表达式2
    f()
    ```
    - 说明:
      - yield用于def函数中，目的是将此函数作为生成器函数使用
      - yield用来生成数据，供迭代器 next(it) 函数使用

- 运行机制：
  - 函数中遇到yield语句时，先执行yield之前语句，再送yield之后元素出来参与各类操作，最后执行剩下的语句(与return不同)。

---

示例1：生成器函数
```python
def myyield():
    print("即将生成2")
    yield 2  # 生成2
    print('即将生成3')
    yield 3  # 生成3
    # return 4  #return无任何返回。若存在，后面的语句将不会被执行
    print('即将生成5')
    yield 5
    print("myield函数结束")

# 此处说明函数返回可迭代对象
it = myyield() # 无任何执行与返回
print(it) # 仅打印迭代对象地址 
# 说明机制：遇到yield语句时，1>执行之前语句，2>送yield元素出来
for x in it:
    print(x)

# 此处说明迭代对象只能使用一次
print('-'*50)
it = myyield()  # it 绑定生成器
print(list(it))  # 可见迭代对象存在
print(list(it))  # 可见迭代对象已删除
```
运行结果：
```
<generator object myyield at 0x00000230A57A05C8>
即将生成2
2
即将生成3
3
即将生成5
5
myield函数结束
--------------------------------------------------
即将生成2
即将生成3
即将生成5
myield函数结束
[2, 3, 5]
[]
```

示例2：使用yield生成偶数序列
```python
def myeven(s, e):
    while s < e:
        if s % 2 == 0:
            yield s
        s += 1

for i in myeven(10, 20):
    print(i, end=' ')
```

运行结果：
```
10 12 14 16 18
```

<span id="jump"></span>

#### 5.3.3.2. 生成器表达式
- 概念：  
    - 生成器表达式是用推导式的形式生成一个新的可被迭代的对象。
    - 它不直接生成对象存储于内存，是在当要被使用时再实时生成。
    - 它更节省内存，理论上可以表示存储无限大数据（因迭代器特性，边使用边从内存中删除）。

- 与列表推导式等相比，生成器表达式的优势:
    - 生成器表达式不存储数据，所有数据都是实时获取的。
    - 不同于另外三个推导式（列表推导式，字典推导式，集合推导式），它们储存数据于实际的内存中生成新对象，而生成器表达式则不。

- 语法:
    ```python
    (表达式 for 变量　in 可迭代对象 [if 真值表达式])
    ```
    说明：if 子句可以省略, for同样可以多重嵌套

---
示例1：next()方法逐个取出数据
```python
it = (x**2 for x in range(1, 4))
print(next(it))  # 1
print(next(it))  # 4
print(next(it))  # 9
# next(it)  # StopIteration
```

### 5.3.4. 原理解读

- 什么是迭代器、生成器？
  - 迭代器Iterator可以看做一个实时生成数据的惰性计算方法。
    - `Iterator`可表示为一个数据流，只能通过`next()`方法不断取出某个数据（for的本质也是封装了next方法），这个数据流可看做一个有序序列，但我们却不能提前知道序列的长度，所以`Iterator`的计算是惰性计算。
    - 由于这个惰性计算特性，可使`Iterator`表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
    - 而生成器是迭代器的一种。
- 迭代器的isinstance判断方法实质是什么？
  - 是判断是否封装`__iter__()`和`__next__()`方法  
  - 如：
    - 可迭代对象：`__iter__()`方法
    - 迭代器：`__iter__()`、`__next__()`方法
    - 生成器：`__iter__()`、`__next__()`等其他方法
  - 但封装了这两种方法的类却不一定具有可迭代对象和迭代器的功能
  - 如果这些方法中用任意代码填充，如`__iter__()`、`__next__()`方法中用`pass`填充。将会使`isinstance()`的判断与真实的迭代器判断具有相同效果。

---

示例1：迭代器对于数据是实时获取的，因而造成取出数据的不同
```python
# 1) 程序1
L = [2, 3, 5, 7]
it = [x for x in L]
L[1] = 30
print(list(it))  # [2, 3, 5, 7]

#2) 程序2
L = [2, 3, 5, 7]
it = (x for x in L)
L[1] = 30
print(list(it))  # [2, 30, 5, 7]
```

示例2：迭代器数据边使用边删除  
code1: ——迭代器数据只能取出一次

```python
a = (x for x in range(5))  # 生成器对象——迭代器中的一种
print(a)  # <generator object <genexpr> at 0x0000000002E58888>
print(list(a))  # [0, 1, 2, 3, 4]
print(list(a))  # []
```

code2: —— 迭代器数据边使用边删除
```python
import copy

L= [1, 2, 3]

print('--------可迭代对象---------')
L0 = L
for x in L0:
    print("x", x, list(copy.deepcopy(L0)))

print('--------迭代器对象---------')
L0 = iter(L)  # 将可迭代对象转换为迭代器对象
for x in L0:
    print("x", x, list(copy.deepcopy(L0)))
```

运行结果：
```
--------可迭代对象---------
x 1 [1, 2, 3]
x 2 [1, 2, 3]
x 3 [1, 2, 3]
--------迭代器对象---------
x 1 [2, 3]
x 2 [3]
x 3 []
```

示例3：使用对象继承新方法，来改变isinstance判断对象属性（了解）
```python
from collections import Iterable, Iterator, Generator

def judge(x):
    print(isinstance(x, Iterable),
          isinstance(x, Iterator),
          isinstance(x, Generator))

class A():
    def __init__(self):
        pass

class B(A):
    def __iter__(self):
        pass

class C(B):
    def __next__(self):
        pass

# 使用列表测试
judge([])       # True False False
judge(iter([])) # True True False

# 使用isinstance()判断对象类型
judge(A())     # False False False
judge(B())     # True False False
judge(C())     # True True False

# 测试对象功能
c = C()
print(next(c)) # 并没有触发异常
```

## 5.4. 迭代器之迭代工具函数zip/enumerate
迭代工具函数的作用是：生成一个个性化的可迭代对象
### 5.4.1. zip函数
- 格式：`zip(iter1 [,iter2, iter3,...])`
- 返回：  
  - 返回一个元组包装的zip对象。此对象用于生成一个个元组，此元组的个数由最小的可迭代对象维度决定。
- 注：
  - 当可迭代对象中的长度不一时，将取长度最小的为基准，其余默认删除

---

示例1：两个列表直接生成字典
```python
# 以下用zip函数生成一个字典
numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
d = dict(zip(names, numbers))
print(d)
# {'中国移动': 10086, '中国电信': 10000, '中国联通': 10010}
```

示例2：多维矩阵行列转置
```python
L = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
L_new = list(zip(*L))
print(L_new)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```
> 备注：`zip(*L)`相当于`zip(L[0], L[1], L[2], ...)`，该知识位于后续函数章节序列位置传参

示例3: 本质探索, zip生成的是一个多维元组组成的迭代器。
```python
from collections import Iterable, Iterator, Generator

def judge(x):
    print(isinstance(x, Iterable),
          isinstance(x, Iterator),
          isinstance(x, Generator))

it = zip(range(3), "ABC", ['A', 'B', 'C'])
judge(it)
for a in it:
    print(a)
```
运行结果
```
True True False
(0, 'A', 'A')
(1, 'B', 'B')
(2, 'C', 'C')
```

### 5.4.2. enumerate函数(枚举函数)
- 作用：
  - 生成一个从指定数（默认为0）开始向后自动生成序号的迭代器
- 格式：
  - `enumerate(iterable[,start=0])`
  - 生成带索引的枚举对象，返回迭代类型为索引-值对(index,value)对, 默认索引从零开始,也可以使用start参数重新指定起始

示例:
```python
names = ['中国移动', '中国电信', '中国联通']
for x in enumerate(names):
    print(x)
for x in enumerate(names, start=100): # 可省略"start="
    print(x)
```
运行结果：
```
(0, '中国移动')
(1, '中国电信')
(2, '中国联通')
(100, '中国移动')
(101, '中国电信')
(102, '中国联通')
```

