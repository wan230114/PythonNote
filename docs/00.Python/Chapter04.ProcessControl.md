# 4. 流程控制
## 4.1. 逻辑语句
- 学习先导
  - 何为语句与表达式？见第一章[语句和表达式](/00.Python/Chapter01.PythonReview#_1411-语句和表达式)
  - 什么是一个完整的语句/语句块？
  - 本章学习的语句：
    - if-elif-else语句：用于判断语句块的执行与否
    - pass语句
    - 循环控制语句
      - while语句：用于无限循环的逻辑执行
      - for语句：用于<[可迭代对象](/00.Python/Chapter05.DataTraversal#_53-可迭代对象)>的循环（字符串，range()返回对象）
      - break语句：用于终止当前语句块的循环
      - continue语句：用于开始一次当前语句块的新循环
    - 语句嵌套
      - 以上所有语句之间都可以互相层层嵌套，一个语句块中可以包含多个语句块。
      - 一般以缩进关系表示一个语句块


### 4.1.1. if-elif-else语句
- 作用：
  - 选择性执行语句。条件为真，执行if下的语句块，若存在elif则继续判断，当判断至else则执行else下的语句块。
- if-else常规语句
  - 语法：

    ```python
    if 真值表达式:
        语句块1
    else:
        语句块2
    ```
    - 运行机理：本质判断是，`if 布尔值`，实际中运行的是`if bool(obj)`，比如`if 100`为`if bool(100)`  

- if-elif-else多条件判断语句
  - 语法：

    ```python
    if 真值表达式:
        语句1
    elif 真值表达式2:
        语句2
    elif 真值表达式3:
        语句3
    ...
    else:
        语句块4
    ```

- 条件表达式（三元表达式）
  - 作用：同样进行执行控制，但更灵活简洁
  - 语法：

    ```python
    <表达式1> if <真值表达式> else <表达式2>
    ```

  - 返回：若真值表达式为真，则返回表达式1结果，否则返回表达式2结果  
    `<表达式1，为真返回> if <真值表达式> else <表达式2，为假返回>`
    - 注意：
      - `表达式1`和`表达式2`返回的是表达式计算完毕的结果。
        示例：
```python
L = [1, 2, 3]
i = 4
a = L[0] if True else L[i]
```

注意：表达式不是语句，表达式能赋值给变量，语句则不能。此在第一章[语句和表达式](/00.Python/Chapter01.PythonReview#_1411-语句和表达式)已有详细描述。

---
示例1：
```python
a = 25
if 0 <= a < 18:
    print('未成年')
elif a < 30:
    print('年轻人')
else:
    print('不再年轻')
```
运行结果：
```
年轻人
```

示例2：
```python
# 条件表达式
print('a' if True else 'b')
print('a' if False else 'b')

# 使用条件表达式计算绝对值
n = -20
m = n if n > 0 else -n
print(m)
```
运行结果
```
a
b
20
```

### 4.1.2. pass语句
填充语法空白

示例：if语句中的使用
```python
if Ture:
    pass
else:
    print('输入有问题')
```

## 4.2. 循环控制
### 4.2.1. while-else语句
格式：
```python
while <真值表达式1>：
	语句1
else <真值表达式2>：
	语句2
```
运行机制：
> - 第一行while一行中，计算判断<真值表达式1>。  
> - 若为True，则执行完后面语句后又跳回while一行，重新计算判断<真值表达式1>。
> - 若为False，则执行else语句，else语句可以省略。

---

示例：
```python
a = 0
while a < 6:
    print(a, end=' ')
    a += 1
# 0 1 2 3 4 5
```

### 4.2.2. for-else语句
- 作用：循环遍历，返回可迭代“对象”元素
- 格式：

    ```python
    for <变量列表> in <可迭代对象>：
        语句块1
    else:
        语句块2
    ```

    - `<变量列表>`可以直接用多个变量接收，相当于第一章中几种赋值方式中的多重赋值
    - else语句块可以存在，它在循环正常执行结束后将执行。

---

示例：
```python
for a in [(0, '001'), (1, '002'), (2, '003')]:
    print('a:', a)

print('-'*13)
for n, a in [(0, '001'), (1, '002'), (2, '003')]:
    print('n:', n, ', a:', a)

print('-'*13)
for i in range(3, 6):
    print(i, end=' ')
```

运行结果：
```
a: (0, '001')
a: (1, '002')
a: (2, '003')
-------------
n: 0 , a: 001
n: 1 , a: 002
n: 2 , a: 003
-------------
3 4 5
```

#### 4.2.2.1. for常联用的函数——range()
- 格式：
  - `range(s, e, step)`
  - s--开始数值, e--结束数值(不包含), step--步数(可为负数)
  - 规则类似于序列操作中的切片
- 返回：
  - 返回数值序列的“可迭代对象”, 非序列
- 特性：
  - 等差数列。
  - 惰性计算，非一次性将所有数据计算存储于内存中。

---
示例：3个参数的常规使用
```python
it = range(3, 6)
print('it:', it)  # range(3, 6)
for i in range(3, 6):
    print(i, end=' ')
print('\n---------------')
print('3:7:1  ', list(range(3, 8)))      # 3,4,5,6,7
print('3:7:2  ', list(range(3, 8, 2)))   # 3,5,7
print('3:0:1  ', list(range(3, 0)))      # 无
print('3:0:-1 ', list(range(3, 0, -1)))  # 3,2,1
```
运行结果：
```
it: range(3, 6)
3 4 5
---------------
3:7:1   [3, 4, 5, 6, 7]
3:7:2   [3, 5, 7]
3:0:1   []
3:0:-1  [3, 2, 1]
```

示例：range的数据是惰性计算的 —— range的特性测试

```python
from datetime import datetime as dt

t0 = dt.now()
print(range(4*10**7)[-1])
print('耗时：%s秒'%(dt.now() - t0).total_seconds())

t0 = dt.now()
print(list(range(4*10**7))[-1])
print('耗时：%s秒'%(dt.now() - t0).total_seconds())
```

运行结果：
```
39999999
耗时：0.000997秒
39999999
耗时：1.756992秒
```

#### 4.2.2.2. for语句块的机制探索
```python
for <变量列表> in <可迭代对象>：
    语句块1
else:
    语句块2
```

1. `for语句`中的`in`的真正含义：
   - `for ... in ...`语句中的`in`不同于操作运算符`in`；
   - 操作运算符`in`是判断某数据是否存在于某个数据容器或可迭代对象中；
   - 而for语句中的in则是指在当前这个可迭代对象中逐个取值。

2. `for语句`中的可迭代对象变化带来的影响：
   - `for ... in <可迭代对象>`中的`<可迭代对象>`内的数据可以发生改变。
   - 对于序列，长度和内部数据均可以改变，但对于集合，仅能改变内部数据，如果长度发生变化将导致触发异常。
     - 其中，需要注意对于可变序列（列表）的长度变化，若循环中长度一直增加，将有可能造成无限循环。
   - 它们迭代取值是按照`<可迭代对象>`索引来取值的。
     - 下面的示例，对于有序序列（列表）严格按照索引向后取值，但对于集合等无序数据容器则难以找到规律。
   - 因此在实际使用中最好不要在for语句中直接将可迭代对象进行变化，可以尝试浅拷贝或深拷贝后再进行遍历。

3. `for语句`的实现原理：
   - `for语句`的本质：使用迭代器方法取出数据。
   - 使用while、迭代器、next()以及try捕获异常实现，该详细介绍见下一章[迭代器之for语句的本质](/00.Python/Chapter05.DataTraversal#jump_for)

---

##### 4.2.2.2.1. 示例1：探索`for ... in ...`中`in`的含义
code1:
```python
print('for循环探索')
i = 6
for x in range(1, i):
    # for ... in ... 迭代[1,i)
    # 每个循环向后逐个取出元素，赋值给x
    print('x=', x, '  i=', i)
    i -= 1

print('while循环探索')
i = 6
x = 1
while x in range(1, i):
    # ... in ... 判断x是否在[1,i)内
    print('x=', x, '  i=', i)
    x += 1
    i -= 1
```
运行结果：
```
for循环探索
x = 1     i = 6
x = 2     i = 5
x = 3     i = 4
x = 4     i = 3
x = 5     i = 2
while循环探索
x = 1     i = 6
x = 2     i = 5
x = 3     i = 4
```
code2: in的正确使用示例
```python
print('for循环探索')
i = 6
it = range(1, i)
for x in it:
    if x in it:  # in判断操作，判断x是否在[1,i)内
        print('x=', x, '  i=', i)
        i -= 1
        it = range(1, i)
    else:
        break

print('while循环探索')
i = 6
it = range(1, i)
while x in it:  # in判断操作，判断x是否在[1,i)内
    x = next(it)
    print('x=', x, '  i=', i)
    i -= 1
    it = range(1, i)
```
运行结果：
```
for循环探索
x= 1   i= 6
x= 2   i= 5
x= 3   i= 4
while循环探索
x= 1   i= 6
x= 2   i= 5
x= 3   i= 4
```

##### 4.2.2.2.2. 示例2：探索`for语句`中`<可迭代对象>`变化带来的影响

code1: 列表有规律可寻，是按照位置索引向下逐渐取值的
```python
L = [1, 2, 3]
for x in L:
    print(x, L, end=' --> ')
    L.remove(x)  # 此行注释将导致无限循环
    L.append(x+10)
    print(L)
```

```
1 [1, 2, 3] --> [2, 3, 11]
3 [2, 3, 11] --> [2, 11, 13]
13 [2, 11, 13] --> [2, 11, 23]
```

##### 4.2.2.2.3. 示例3：通过for语句机制探索for是否按索引步进取值的

code1: 列表探索

```python
# for语句自动迭代
a = [1, 2, 3, 4, 5, 6]
Index = 0
for item in a:
    print(Index, item, a, end=' --> ')
    a.remove(item)
    print(a)
    Index += 1
print('a最终结果：', a)

# 使用迭代器步进，此为for循环语句的本质
a = [1, 2, 3, 4, 5, 6]
it = iter(a)
Index = 0
while True:
    try:
        item = next(it)
        print(Index, item, a, end=' --> ')
        a.remove(item)
        print(a)
        Index += 1
    except StopIteration:
        break
print('a最终结果：', a)
```
运行结果：
```
0 1 [1, 2, 3, 4, 5, 6] --> [2, 3, 4, 5, 6]
1 3 [2, 3, 4, 5, 6] --> [2, 4, 5, 6]
2 5 [2, 4, 5, 6] --> [2, 4, 6]
a最终结果： [2, 4, 6]
```
（运行结果以上一共重复3次）


code2： 集合探索
```python
# for语句
a = {1, 2, 3, 4, 5, 6}
Index = 0
for item in a:
    print('%3d, %3d'%(Index, item), a, end=' --> ')
    a.remove(item)
    a.add(item+100)
    print(a)
    Index += 1
print('a最终结果：', a)

# 迭代器步进
a = {1, 2, 3, 4, 5, 6}
it = iter(a)
Index = 0
while True:
    try:
        item = next(it)
        print('%3d, %3d'%(Index, item), a, end=' --> ')
        a.remove(item)
        a.add(item+100)
        print(a)
        Index += 1
    except StopIteration:
        break
print('a最终结果：', a)
```

code3: 从集合中取值，无法捕捉索引规律。  
- 可能与存储的数据有关系，不同的值造成取值次数不同
- 集合取值的进一步验证失败，猜想跟哈希计算有关，需要待进一步探索。

```python
def veri(s):
    id_all = {}
    index_all = []
    print('')
    for x in s:
        print('- 原始结果:', s)
        index_all.append(list(s).index(x))
        print(index_all, '第%s次' % len(index_all))
        ids = dict(zip([id(x) for x in s], s))
        id_all.update(ids)
        # print(id_all)
        # print(dict(sorted(id_all.items(), key=lambda x:x[0])))
        print('id列表：', ids)
        # print('id排序：', dict(sorted(ids.items(), key=lambda x:x[0])))
        print(x, s, end=' --> ')
        s.remove(x)
        s.add(x+10)
        # s.update({x+10})
        print(s)

veri({1000, 2000, 3000, 4000})  # 会取出4次
veri({1000, 2000, 3000, 10000})  # 会取出3次
```

### 4.2.3. continue语句 与 break语句
如何在循环中让程序不再向下执行，重新开始一次新的循环？
  - 使用continue语句。

说明：
  - for循环中迭代取下一个元素。

break语句
退出当前语句块

- 注意1：
  - `break`不干扰外层其他语句块  
- 注意2：
  - break作用范围是整个`for-else`、`while-else`语句块。
  - 在`for-else`和`while-else`语句中`break`退出整个语句块。即`for-else`和`while-else`中`else`的语句也被跳过。

---
示例1：内部只能执行1次，外部2次无干扰
```python
for i in range(2):
    print(i)
    for j in ['a', 'b', 'c']:
        print('j:', j)
        if j == 'a':
            break
```
运行结果：
```
0
j: a
1
j: a
```


示例2：break作用范围是整个`for-else`、`while-else`语句块

code1:
```python
for i in [1, 2, 3, 4]:
    if i==2:
        continue  # 见下一节
    print(i)
else:
    print("hello")
```
结果为
```
1
3
4
hello
```

code2:
```python
for i in [1, 2, 3, 4]:
    if i==2:
        break
    print(i)
else:
    print("hello")
```
结果为
```
1
```
## 4.3. 其他语句
#### 4.3.1. 布尔运算
返回：布尔值或对象
运算符：not、and、or
布尔非操作：not x
```python
>>> not True
False
```

布尔与操作：x and y  
机理：从左到右运算，只要有一个不满足就返回x值，否则返回y  
优先返回假值对象。  
先计算x，若x为False，返回x，否则返回y值。  
使用对象表示真假，不同于C/C++的“&”【？】（？？？）。
```python
>>> 0 and 20		#优先返回假值对象
0
>>> 20 and 0
0

>>> 0 and 20		#若x为False，返回x，否则返回y值。
0
>>> 10 and 10
10
>>> 10 and 20
20
>>> 20 and 10
10
```

布尔或操作：x or y
机理：从左到右运算，只要有一个满足就返回x值，否则返回y
优先返回真值对象。
先计算x，若x为True，返回x，否则返回y值。
```python
>>> 0 or 20		#优先返回真值对象
20
>>> 20 or 0
20

>>> 0 or 20		#若x为True，返回x，否则返回y值。
20
>>> 10 or 10
10
>>> 10 or 20
10

>>> 1 or 20
1
>>> 20 or 1
20
# 备注：这个过程完全满足逻辑判断。如
>>> 6>5 and 6>3
True
>>> 6>5 and 7
7
```
#### 4.3.2. 5.1.7.3	正负号运算符
```
+（正号）
-（负号）
一元运算符
语法：+/- 表达式

```