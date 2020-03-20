# 6. 函数FUNCTION
## 6.1.  基本概念
基本认识：
- 函数是可以重复执行的语句块。
- 用于封装语句，调高代码重用性
- 可以重复调用
- 用于定义用户级别的函数

语法：
```python
# 函数定义
def 函数名(形参列表):
	语句块
    return 返回值

# 函数调用
函数名(实参列表)
```

说明：
- 函数的名字就是语句块的名称
- 函数名的命名规则与变量名相同（函数名必须是标识符）
- 函数名是一个变量
- 函数有自己的命名空间，在函数外部不可访问函数内部的变量，在函数内部可以访问外部的变量，要让函数处理外部数据需要用参数给函数传入一些数据。
- 参数列表可以为空
- 语句部分不能为空，如果为空需要用pass填充。
- 函数调用语句是一个表达式，一定会有返回值，能赋值给一个变量。
  - 如果没有return语句，函数执行完毕后返回None对象
  - 如果函数需要返回其它的对象需要用到return语句

## 函数的返回值
- return语句
  - 作用：结束函数的运行，并返回return的结果

<!-- - 定义函数的5种思路方法【？待总结】 -->

- 注意事项：
  1. 函数中默认返回`None对象`，即无`return语句`时也返回一个`None对象`。函数中没有`return语句`相当于末尾加了`return None`
  2. 函数中`return语句`执行后不再返回该函数执行。如递归函数的过程中，return跳转到另一层函数后，将不会返回原函数中继续执行。

---
示例1：return基本用法
```python
def myfunc():
    return 'hello'

a = myfunc()
print(a)  # hello
```


---
示例2：return的默认返回值理解

code1 内置函数print测试，return之深入理解
```python
>>> print(print('hello'))  # 打印什么？
hello
None
```

```python
>>> s = print('hello')  # 会有打印么？
hello
>>> print(s)  # 返回什么？
None
```

code2 自定义函数理解
```python
def myfunc():
    pass

a = myfunc()
print(a)  # 打印什么
```
```
None
```

---
示例3：return使函数结束执行的理解

code1：有return时的函数执行直接跳转不再回来

```python
def myfunc(x):
    if x==0:
        print('到达末端')
    else:
        print('开始执行')
        return myfunc(x-1)
        print('结束执行')

myfunc(3)
```
运行结果：
```
开始执行
开始执行
开始执行
到达末端
```


code2 无return时，执行完的函数将返回原函数继续执行
```python
def myfunc(x):
    if x==0:
        print('到达末端')
    else:
        print('开始执行')
        myfunc(x-1)
        print('结束执行')

myfunc(3)
```
运行结果：
```
开始执行
开始执行
开始执行
到达末端
结束执行
结束执行
结束执行
```

## 函数的参数传递

形参和实参可以理解为调用函数与被调用函数之间的数据传输接口。

实参与形参区别
- 过程：实参传递-->形参接收
- 形参是指调用函数时传递的参数。
- 实参是指被调用函数接收传入的参数。

```python
# 函数定义
def 函数名(形参列表):
	语句块

# 函数调用
函数名(实参列表)
```

### 函数的缺省值理解

#### 缺省值
- 在形参加入初始值，传参时便可省略一部分值。
- 缺省参数规则：
  - 缺省参数可以有零个和多个，甚至全部。
  - 若函数中有缺省参数存在，则必须遵循从右到左依次定义的规则。即缺省参数必须放在参数后面。如`(x, y=0, z=0)`

示例：自己定义的range函数
```python
def myrange(s, end=0, n=1):
    x = s   #代表数开始
    y = end #代表数结束
    if end == 0:
        x = end
        y = s
    L = []
    while x < y:
        L.append(x)
        x += n
    print(L)

myrange(10)
myrange(5, 10)
myrange(5, 10, 2)
myrange(s=5, end=10, n=2)  #报错
```

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 7, 9]
[5, 7, 9]
```


#### 缺省值与函数的创建过程理解
- Python程序自上而下运行，函数的初始化一般只能执行一次。当然也可以使用嵌套函数进行重复定义。
- 若函数创建时，形参定义了初始化值，后续多次的使用中该值是不能再次被重新初始化的。假如是可变对象，将一直持续受到影响。 如下示例：函数在初始化时，形参创建一个可变对象，且重新指定新的对象后仍然回到原对象。

---
题目示例：

经典题目：函数中的形参理解。  

```python
def f(x, L=[123, 1234]):
    L.append(x)
    print(L)

f(2)  # _______
f(3)  # _______
f(3, [3, 2, 1])  # __________
f(4)  # ____________ 此处是精髓
```
答案：
```
[123, 1234, 2]
[123, 1234, 2, 3]
[3, 2, 1, 3]
[123, 1234, 2, 3, 4]
```

code2:
```python
def g():
    def f(x, L=[123, 1234]):
        L.append(x)
        print(L)
    return f

f = g()
f(2)  # _______
f(3)  # _______
f(3, [3, 2, 1])  # __________
f(4)  # ____________ 此处是精髓
f = g()
f(4)  # ____________ 此处是精髓
```
运行结果：
```
[123, 1234, 2]
[123, 1234, 2, 3]
[3, 2, 1, 3]
[123, 1234, 2, 3, 4]
[123, 1234, 4]
```

### 6.2. 函数的参数传递过程理解

```python
# 函数定义
def 函数名(形参列表):
	语句块

# 函数调用
函数名(实参列表)
```

函数传参的方式：

1. 位置传参：
   - 实际传递参数(以下简称"实参")与形式参数(形参)的对应关系按位置来依次对应
   - 实参传递：`func(x1, x2, x3)`
   - 形参接收：`def func(xx1, xx2, xx3):`

2. 序列传参：
   - 序列传参是指在函数调用过程中用"*"将序列拆解后按位置进行传递的传参方式
   - 实参的序列传参使用：
       - 实参传递：`func(*[x1, x2, ...])`，用`*`将序列拆解后按位置一一对应传参；等同于`func(x1, x2, ...)`
       - 形参接收：`def func(xx1, xx2, ...):`简单接收
   - 形参的序列传参使用：
       - 实参传递：`func(x1, x2, ...)`简单传入
       - 形参接收：`def func(*args):`，用`*args`来收集位置传参的时候多余的实参，并组成一个元组`(x1, x2, ...)`由变量`args`绑定。

3. 关键字传参：
    - 关键字传参是指传参时, 按着形参的“名称”给形参赋值
    - 实参和形参按名称进行匹配, 实参和形参通过关键字名称一一对应，定义时参数顺序可以任意。
    - 实参传递：`func(xx1=1, xx2=2, xx3=3)`
    - 形参接收：`def func(xx1, xx2, xx3):`

4. 字典关键字传参:
    - 是指实参为字典,将字典用 "**" 拆解后进行关键传参的传参方式
    - 实参使用：
        - 实参部分：`func(**{'a':1, 'b':2})`，用`**`将字典拆解后按关键字传参
        - 形参部分：`func(a, b)`简单接收
    - 形参使用：
        - 实参部分：`func(a=1, b=2, ...)`简单传入
        - 形参部分：`def func(**kwargs)`，用`**kwargs`来收集关键字传参的时候多余的实参，并组成一个字典`{'a':1, 'b':2, ...}`由变量`kwargs`绑定。


实参的位置规则：
- `位置传参`必须位于最前面；
- `关键字传参`必须位于位置传参之后；
- `序列传参`不可位于`字典关键字传参`之后；
- `字典关键字传参`必须位于最后面，后面可以尾随`关键字传参`。
- 如：
  - 实参传递或形参设置初始值，都必须要定义在无关键字参数之后。或者说关键字传参，要定义在位置形参之后。
  - 错误：`def func(a=1, b, c)`、`func(a=10, 2, 3)`
  - 正确：`def func(b, c, a=1)`、`func(2, 3, a=10)`

```python
def func(b, c, a=1):
    print(a, b, c)

func(2, 3, a=10)  # 10 2 3
```

---

示例：一个实例看懂所有传参方式

```python
def myfun(a, b=0, *args, **kwargs):
    print('a:', a, ' b:', b, ' args:', args, 
          ' kwargs:', kwargs, sep='')

# 位置传参
myfun(1, 2, 3)  # 位置传参
myfun(*(1, 2, 3))  # 序列传参
myfun(*[1, 2, 3])  # 序列传参

# 关键字传参
myfun(d=4, c=3, b=2, a=1)  # 关键字传参
myfun(**{'a': 1, 'b': 2, 'c': 3, 'd':4})  # 字典关键字传参

# 混合传参
myfun(1, 2, *[-1], -2, c=3, *[-3], d=4, **{'e':5})
```

```
a:1 b:2 args:(3,) kwargs:{}
a:1 b:2 args:(3,) kwargs:{}
a:1 b:2 args:(3,) kwargs:{}
a:1 b:2 args:() kwargs:{'d': 4, 'c': 3}
a:1 b:2 args:() kwargs:{'c': 3, 'd': 4}
a:1 b:2 args:(-1, -2, -3, -4, -5) kwargs:{'c': 3, 'd': 4, 'e': 5}
```

### 函数作为实参传递
Python语言相较于其他语言的一个特点：参数还可以传函数

- 一个函数可以作为另一个函数实参传递
- 函数作为另一个函数参数进行传递，从调用函数实参中传入函数名，被调用函数接收。

---
示例： 灵活传max,min,sum函数进形参

```python
def myinput(fn, L):
    return fn(L)  # <<< 注意此处

L = list(range(10))
print(myinput(max, L))  # 9
print(myinput(min, L))  # 0
print(myinput(sum, L))  # 45
```

```python
# 此示例示意get_op这个函数可以返回其它的函数
def get_op():
    s = input("请输入您要做的操作: ")
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = list(range(10))
fx = get_op()
print(fx(L))
```

## 6.4. 函数名的理解
函数名是变量，函数是一个对象，函数对象在创建时该函数被一个变量绑定。

既然函数名是变量，那么函数名同样满足变量的命名规范和特性：
- 只能以字母和下划线开头
- 可以被重新赋值绑定
- 可以被del
- ...


---

示例：交换绑定函数f1和函数f2

code1 嵌套函数的调用
```python
def f1():
    print("f1被调用")

def f2():
    print("f2被调用")

def fx(fn):
    print("fn绑定的是: ", fn)
    fn()   # 调用fn绑定的函数, 此处等同于调用谁呢?

fx(f1)
fx(f2)
```

code2 函数名的交换
```python
def f1():
    print("f1被调用")

def f2():
    print("f2被调用")

f1, f2 = f2, f1
f1()  # 调用f2
f2()  # 调用f1
```

## 6.5. 函数的命名空间（作用域范围）
问题引入：
函数内可使用外部变量，但不可更改变量所绑定的对象。
```python
def func(x):
    print('x:', x, 'y:', y)
    # y += 10  # 报错，域名空间之外变量绑定对象不可变
    print(L)  # [0]
    L[0] += 1
    print(L)  # [1]  # 对象可变
L = [0]
y = 0
func(9)  # 同一命名空间，函数可使用，但不可更改变量和其绑定的对象
```
(若对象是可变的，当然其内部数据也可变)

### 局部变量与全局变量
- 局部变量
  - 定义在函数内部的变量称为局部变量（函数的形参也是局部变量）。
  - 局部变量只能在函数内部使用。
  - 局部变量在函数调用时会创建，被调用后会被销毁
- 全局变量
  - 定义在函数外部,模块内部的变量称为全局变量
  - 所有的函数都可以直接访问"全局"变量,但函数内部不能直接通过赋值语句来改变全局变量

- 局部变量说明：
  1. 在函数内首次对变量赋值是创建局部变量, 再次为变量赋值是修改局部变量的绑定关系
  2. 在函数内部的赋值语句不会对全局变量造成影响
  3. 局部变量只能在其被声明的函数内部访问, 而全局变量可以在整个模块同访问

注意事项1：
- 内部可以访问外部，但外部不可访问内部
  - 函数内部可以访问函数外部的变量,但不能修改函数外部变量的绑定关系
  - 函数外部无法访问函数内部的局部变量

---
示例1:
```python
x = 0
def myadd(a, b):
    c = 1
    x = a + b
    print('内部x:', x)
myadd(100, 200)
print('外部x:', x)  # 0
# print(c)  # NameError: name 'c' is not defined
```

注意事项2：
- 局部变量若有同名全局变量，在使用后将不能再被赋值。
  - 该局部变量可以直接重新赋值，但不会改变影响全局变量空间。
  - 该局部变量，如果先调用后，再重新赋值，则会报错

---
示例：

code1
```python
def f():
    y = 20    # 先改变
    print(y)  # 再使用，正常打印20
y = 10
f()
print(y)  # 正常打印10
```

code2
```python
def f():
    print(y)  # y先使用
    y = 20    # y再改变
    # 报错：UnboundLocalError: local variable 'y' referenced before assignment
y = 10
f()
```

code3
```python
def f():
    c = 20 + y  # y先使用
    y = 20      # y再改变
    # 报错：UnboundLocalError: local variable 'y' referenced before assignment
y = 10
f()
```

注意事项3：
  - 新的作用域命名空间只在函数以及后面类和模块中才会开辟，在if/for/while等语句块中是不会重新开辟局部命名空间（局部变量）。
  - 使用时应注意，局部变量概念只存在于函数（以及后面的类，模块）内部。

如：

```python
data = '123'
if True:
    if True:
        data = 'hello'
print(data)  # 正常输出'hello'
```

```python
data = '123'
def f():
    if True:
        if True:
            data = 'hello'
print(data)  # 依然输出123
```

### 6.5.2.  		Python作用域
作用域也叫命名空间，是访问变量时查找变量名的范围空间。
#### 6.5.2.1.	Python的四个作用域：LEGB

| 作用域              | 英文解释                | 英文简写 |
|------------------|---------------------|------|
| 局部作用域（函数内）       | Local（function）     | L    |
| 外部嵌套函数作用域        | Enclosing function  | E    |
| 函数定义所在模块（文件）的作用域 | Globals（module）     | G    |
| Python内置模块的作用域   | Builtin（python）     | B    |

说明：
```
包含关系：Builtin > Globals > Enclosing > Local
            模块      文件       外部函数   当前函数

变量名的查找规则:
  1. 在访问变量时先查找本地变量, 
     然后是包裹此函数外部的函数内部的变量, 
     之后是全局变量, 
     最后是内置(内建)变量
            L --->  E  ---> G ---> B
  2. 在默认情况下,变量名赋值会创建或者改变本地作用域变量
```

- 一般全局变量为Globals，本地变量为Local。
- Builtin内建作用域变量如max,min,len等是只读的不能改变。
- 变量和del都是在操作Globals作用域，如重新赋值max，优先访问全局的。

- globals和locals函数打印作用域字典
  - globals() 返回当前全局作用域内变量的字典
  - locals()  返回当前局部作用域内的变量的字典

---
示例：
```python
a = 1
b = 2
c = 3

def fx(c, d):
    e = 300
    # 此处有几个局部变量?
    print('locals() 返回', locals())
    # 3个变量：c,d,e
    print("globals() 返回", globals())
    # a,b,c,fx，及其他
    print(c)  # 100
    print(globals()['c'])  # 3

fx(100, 200)
```

```
locals() 返回 {'c': 100, 'd': 200, 'e': 300}
globals() 返回 {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002E8944B1688>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'test.py', '__cached__': None, 
                'a': 1, 'b': 2, 'c': 3, 'fx': <function fx at 0x000002E8960EFEE8>}
100
3
```


---
示例1：重定义max
```python
def max(a, b):
    return min(a, b)
print(max(10, 9))  #9
```

---
示例2：解释LEGB原理
- 由于 Locals 和 Global 优先于 builtin，该命名的优先级就高于 Builtin 了。
- 例如，在 Global下 str定义为123，调用 str时，就会先调用 Global 下的 str（即 123）
```python
print('\nstr:', str)  # <class 'str'>
print(dir())  # [..., '__spec__']

str = 123
print('\nstr:', str)  # 123
print(dir())  # [..., '__spec__', 'str']

del str
print('\nstr:', str)  # <class 'str'>
print(dir())  # [..., '__spec__']
```
运行结果
```

str: <class 'str'>
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
        '__package__', '__spec__']

str: 123
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
        '__package__', '__spec__', 'str']

str: <class 'str'>
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
        '__package__', '__spec__']
```


示例3：外部嵌套函数Enclosing function调用
由于LEGB的原则，print_y中的y调用的是print_y所在空间
```python
def print_y1():  # 属于外部嵌套函数Enclosing function
    print('\nprint_y1:', y)     # 10
    print('locals:', locals())
    print('globals:', globals())


def f():
    y = 20
    print_y1()  # 10

    def print_y2():
        print('locals:', locals())
        print('\nprint_y2:', y)  # 20
        print('locals:', locals())
        print('globals:', globals())
    print_y2()  # 20


def main():
    y = 100  # main的作用域内，对其他函数无影响
    f()


y = 10
main()
```
运行结果：
```

print_y1: 10
locals: {}
globals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000024F9AE61648>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'test.py', '__cached__': None, 'print_y1': <function print_y1 at 0x0000024F9AF0A0D8>, 'f': <function f at 0x0000024F9AF0E558>, 'main': <function main at 0x0000024F9AF0E798>, 'y': 10}
locals: {'y': 20}

print_y2: 20
locals: {'y': 20}
globals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000024F9AE61648>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'test.py', '__cached__': None, 'print_y1': <function print_y1 at 0x0000024F9AF0A0D8>, 'f': <function f at 0x0000024F9AF0E558>, 'main': <function main at 0x0000024F9AF0E798>, 'y': 10}
```
原理解释：

![](img/c5_namespace.png)

#### 利用可变对象“穿透”作用域限制
- 前面我们提到，当局部作用域的变量名和外部同名时，如果没有直接引用，直接创建新对象进行重新赋值绑定后，会在当前局部作用域创建一个同名局部变量，并且与外部互相不干扰。
- <font color="red">但当外界的这个变量绑定的是一个可变对象，并且我们不创建新对象进行重新绑定，直接对这个可变对象操作改动会发生什么？</font>
- 对这个可变对象内部进行数据修改，将能实现内部影响外界空间，内部数据可以同外界共通，实现“穿透”作用域限制。

示例：
```python
v=[100]
def f():
    v.append(200)
    v.extend([300])
    v[0] = 200
    # v+=[400]  # 报错，猜测虽然+=不更改原对象，但+=的操作中v被重新赋值
f()
print(v)  # [200, 200, 300]
```

注意：这个特性很可能带来未预料到的问题发生，比如只是想传递一个数据进入函数做某些操作计算，结果对外层的数据对象也发生了修改。

```python
L=[100]
def f(v):
    v.append(200)
    v.extend([300])
    v[0] = 200
    v+=[400]
f(L)
print(L)  # [200, 200, 300, 400]
```


## 6.6. 高级函数
### 6.6.1. lambda表达式（lambda匿名函数）
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
示例：
```python
def func_add(x, y):
    return x + y
print(func_add(10, 20))  # 30

# 对于函数func_add, 可以使用lambda表达式一行定义
myadd = lambda x,y: x + y
print(myadd(10, 20))  # 30

myadd = lambda: print('hello', end=' ')
print(myadd())  # hello None

# 求1到10的平方和
fun = lambda x: sum([x * x for x in range(1, x + 1)])
print(fun(10))  # 385
```

### 6.6.2. eval函数 和 exec函数
- eval函数
  - 作用:
    - 把一个字符串当成一个表达式来执行,返回表达式执行后的结果
  - 格式:
    - `eval(source [, globals=None[, locals=None]])`
  - 运行机制：
    - 先将参数1字符串表达式格式化预执行，再用参数2赋值，再用参数3赋值
  - 示例1：
    ```python
    a = eval('1')  # 创建数值1对象
    b = eval('[]')  # 创建列表空对象
    c = eval('a + 10')  # 计算 a + 10
    print(a, b, c)  # 1 [] 11
    ```
  - 示例2：
    ```python
    x = 10
    y = 20
    print(eval('x + y'))  # 30
    # 自定义global环境变量，local环境变量
    print(eval('x + y', {'x':1, 'y':2}))  # 3
    print(eval('x + y', {'x':1, 'y':2}, {'x':100}))  # 102
    # print(eval('x + y', {'x':1}))  # 无y报错
    ```

- exec函数:
  - 作用:
    - 把一个字符串当成'程序'（语句）来执行
  - 格式:
    - `exec(source, globals=None, locals=None)`
  - 示例1:
    ```python
    x = 100
    y = 200
    s = '''z = x+y
    print('z =', z)
    print("hello world!")
    '''
    exec(s)  # 执行 s这个字符串  # z= 300  # hello world!
    ```
  - 示例2: 执行过后的变量也会更新到给定环境中
    ```python
    x = 100
    y = 200
    dict_local = {'x': 1}
    exec(s, None, dict_local)  # z= 201   # hello world!
    print(dict_local)  # {'x': 1, 'z': 201}
    ```
  - 注：
    - 当字符串过长时，可以使用隐式换行：`\`或`('' '' '')`。详细描述见第三章 [长字符串的换行](00.Python/Chapter03.DataContainers.md#huanhang)。

6.7  	函数式编程
- 函数式编程
概念：是指用一系列函数解决问题
  函数是一等公民(Guido)
  1. 函数本身可以赋值给变量,赋值后变量绑定函数
  2. 允许将函数本身作为参数传入另一个函数
  3. 允许函数返回一个函数
好处:
  用每一个函数完成细小的功能,一系列函数在任意组合可以完成大问题
函数的可重入性:
当一个函数在运行时不读取和改变除局部作用域以外的变量时,此函数为可重入函数
可重入函数在每次调用时,如果参数一定,则结果必然一定
示例:
  可重入函数:
def add1(x, y):
	return x + y
    
  不可重入函数示例:
y = 200
def add2(x):
    return x + y
print(add2(10))  # 210
y = 300
print(add2(10))  # 310


6.7.1  	高阶函数
概念：什么是高阶函数(high order function)？
    满足下列条件中一个的函数即为高阶函数
      1. 函数接收一个或多个函数作为参数传入
      2. 函数返回一个函数
- python中内建的高阶函数:
  map, filter, sorted
map是用函数取迭代对象的值
filter是用函数判断筛选对象的值
sorted是用函数排序对象的值
6.7.1.1	map 函数
格式：
	map(func, *iterables)
	func是<可传参函数>，*iterables是<可迭代对象>
用函数和对可迭代对象中的每一个元素作为参数返回新的可迭代对象;当最短的一个可迭代对象不再提供数据时迭代结束
返回：
可迭代对象
要求: 
func函数接收的参数个数必须与可迭代对象的个数相同【？我不认同】
示例:
>>> def square(x) :            # 计算平方数
        return x ** 2
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]

# 字符拼接
>>> list = ['abc','def','xyz']
>>> map(lambda x: 'str_'+x, list);
['str_abc', 'str_def', 'str_xyz']

for x in map(lambda x: x**2 , range(1, 5)):
    print(x, end=' ')  # 1 4 9 16
for x in map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7, 8, 9, 10]):
    print(x, end=' ')  # 6 8 10 12

练习 :
  1. 求 1**2 + 2**2 + 3**2 + ...+ 9**2的和
     (用函数式和高阶函数map实现)
s=0
for x in map(lambda x:x**2,range(1,10)):
    s+=x
print(s)
  2. 求: 1**9 + 2**8 + 3**7 + .... + 9**1的和
s = 0
for x in map(lambda x, y: x ** y,
             range(1, 10),
             reversed(range(1, 10))):
    s += x
print(s)


6.7.1.2	filter 函数:
格式:
filter(function, iterable)
作用:
筛选可迭代对象iterable中的数据,返回一个可迭代对象,此可迭代对象将对iterable提供的数据进行筛选
说明:
函数function 将对iteralbe中的每个元素进行求布尔值,返回True则保留,返回False则丢弃
示例见:
print('test1:')
for x in filter(lambda x: x % 2 == 1, range(41, 53)):
    print(x, end=' ')    # 41 43 45 47 49 51

print('\ntest2:')
def func1(x):
    if x % 2 == 1:
        return x
for x in filter(func1, range(41, 53)):
    print(x, end=' ')    # 41 43 45 47 49 51

练习:
  1. 把之前写的is_prime(x)判断x是否为素数的函数复制过来
     1) 用filter函数把100到200的全部素数求出来,放入列表L中
     2) 求300 ~ 400之间全部素数的和


    
6.7.1.3	sorted 函数
作用:
将原可迭代对象提供的数据进行排序，生成排序后的列表
格式:
sorted(iterable, key=None, reverse=False)
说明:
iterable 可迭代对象
key 函数是用来提供一个排序参考值的函数，这个函数的返回值将作为排序的依据
key的值有：
reverse 标志用来设置是否降序排序
- 简单示例:
L = [5, -2, -4, 0, 3, 1]
L2 = sorted(L)  # [-4, -2, 0, 1, 3, 5]
# 要得到这样的结果该怎么办？
L3 = sorted(L, key=abs)  # [0, 1, -2, 3, -4, 5]

names = ['Tom', 'Jerry', 'Spike', 'Tyke']
L = sorted(names, key=len)
# 结果 ['Tom', 'Tyke', 'Jerry', 'Spike']
- 示例：与lambda高级联用
1、lambda与sorted联用对列表里的字典排序
>>> L = [{'a': 1, 'b': 4}, {'a': 1111, 'b': 2}, {'a': 1111, 'b': 3}]
>>> sorted(L, key=lambda d: d['b'], reverse=False)
[{'a': 1111, 'b': 2}, {'a': 1111, 'b': 3}, {'a': 1, 'b': 4}]
2、对字典进行按key排序
>>> d={'a':25,'c':27,'b':20,'d':22}
>>> sorted(d.keys())
['a', 'b', 'c', 'd']
3、对字典进行按values排序
>>> d={'a':25,'c':27,'b':20,'d':22}
>>> sorted(d.items(),key=lambda item:item[1])
[('b', 20), ('d', 22), ('a', 25), ('c', 27)] 
>>> sorted(d.items(),key=lambda item:item[1],reverse=True)
[('c', 27), ('a', 25), ('d', 22), ('b', 20)]
4、对列表多重排序
>>> sorted([2,3,4,1],key=lambda x: x)
[1, 2, 3, 4]
>>> sorted([2,3,4,1],key=lambda x: x*-1)
[4, 3, 2, 1]
>>> sorted([['a',2], ['b',3], ['c',4], ['d',1]],key=lambda x: x[1]*-1)
[['c', 4], ['b', 3], ['a', 2], ['d', 1]]
对sorted的key=function中lambda的理解：
>>> sorted([['a',2, 1], ['b',3,1],['bb',4,1], ['c',4,2], ['d',1,2]],key=lambda x: (x[2], x[1]*-1))
[['bb', 4, 1], ['b', 3, 1], ['a', 2, 1], ['c', 4, 2], ['d', 1, 2]]

>>> def fn(x):
...     return (x[2], x[1]*-1)
...
>>> sorted([['a',2, 1], ['b',3,1],['bb',4,1], ['c',4,2], ['d',1,2]],key=fn)
[['bb', 4, 1], ['b', 3, 1], ['a', 2, 1], ['c', 4, 2], ['d', 1, 2]]



利用模块，编程排序（不如lambda灵活，特别是目前未找到多重排序如何实现一正排序同时一负排序）
Operator 模块函数（python 列表排序方法sort、sorted技巧篇 - whaben - 博客园）

上面的key参数的使用非常广泛，因此python提供了一些方便的函数来使得访问方法更加容易和快速。operator模块有itemgetter，attrgetter，从2.6开始还增加了methodcaller方法。使用这些方法，上面的操作将变得更加简洁和快速：

>>> from operator import itemgetter, attrgetter
>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

operator模块还允许多级的排序，例如，先以grade，然后再以age来排序：
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]


练习:
  已知:
    names = ['Tom', 'Jerry', 'Spike', 'Tyke']
  排序的依据为原字符串反序的字符串
             'moT', 'yrreJ', 'ekipS', 'ekyT'
  结果:
    ['Spike', 'Tyke', 'Tom', 'Jerry']
参考：
>>> sorted(['Tom', 'Jerry', 'Spike', 'Tyke'],key=lambda x:x[::-1])
['Spike', 'Tyke', 'Tom', 'Jerry']

#### 排序操作
- sorted函数
```python
sorted(iterable[, reverse=False])
  对任意可迭代元素排序，返回生成一个排序后的列表
选项:
  iterable    可以是序列
  reverse     默认缺省参数reverse=True，代表正序，False代表逆序
```
- 列表中自带方法
```python
L.sort()
```
列表中的方法L.sort()与函数方法L.sorted()有什么区别？
示例：
L2 = sorted(L)


6.7.2  	递归函数 recursion
- 递归函数
直接或间接的调用自身的函数
特征：
递归一定要控制递归的层数，当符合一定条件时要终止递归调用 
几乎所有的递归都能用while循环来代替
- 优点:
递归可以把问题简单化，让思路更为清晰,代码更简洁
- 缺点:
递归因系统环境影响大，当递归深度太大时，可能会得到不可预知的结果
示例:
def f():
  f()  # 直接调用自己，进入递归
f()
# 函数间接调用自身
def fa():
  fb()
def fb():
  fa()
fa()
print("递归完成")

- 注意事项：
递归要防止栈溢出，有调用层数限制。
当递归层数过多会出现报错，应使用循环替代
示例：
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

f(998)  # 正常运行
# f(999)  # 报错，RecursionError

def f(n):
    r = 1
    i = 1
    while i <= n:
        r *= i
        i += 1
    return r

f(998) # 正常运行
f(999) # 正常运行


- 递归的两个阶段：
递推阶段:  从原问题出发，按递归公式递推从未知到已知，最终达到递归的终止条件
回归阶段: 按递归终止条件求出结果，逆向逐步代入递归公式，回归到问题求解

示例见:
def fn(n):
    print("递归进入第", n, '层')
    # 当递归进入第三层时，将不再向下走，开始回归
    if n == 3:
        return
    fn(n + 1)
    print('递归退出第', n, '层')

fn(1)
print("程序结束")

'''
递归进入第 1 层
递归进入第 2 层
递归进入第 3 层
递归退出第 2 层
递归退出第 1 层
程序结束
'''


示例:
写一个函数求n的阶乘（递归实现）
  见:
def myfac(n):
    if n == 1:
        return 1
    return n * myfac(n-1)

print('5的阶乘是:', myfac(5))

- 递归的实现方法
先假设函数已经实现

练习:
  写一个函数mysum(n), 用递归方法求
    1 + 2 + 3 + 4 + .... + n的和
  def mysum(n):
      ....
  print(mysum(100))  # 5050
def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n-1)

print(mysum(4))

练习:
  1. 已知:
      第五个人比第四个人大2岁
      第四个人比第三个人大2岁
      第三个人比第二个人大2岁
      第二个人比第一个人大2岁
      第一个人说他10岁
    编写程序算出第5个人几岁?
      (思考是否可以使用递归和循环两种方式来做)
# 循环实现
x=1
age=10
while x<5:
    age=age+2
    x+=1
print(age)

# 递归实现
def f(n):
    if n==1:
        return 10
    return 2+f(n-1)
print(f(5))
  2. 已知有列表:
     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
     1) 写一个函数print_list(lst)打印出列表内的所有元素
        print_list(L)  # 3 5 8 10 13 14...
     2) 写一个函数sum_list(lst): 返回这个列表中所有元素的和
       print(sum_list(L))  # 86
    注:
      type(x) 可以返回一个变量的类型
      如:
        >>> type(20) is int  # True
        >>> type([3, 5, 8]) is list  # True
def func(x):
    if type(x) == typeL:
        for xx in x:
            if type(xx) == typeL:
                # 使用return跳转后将不会回到原函数
                # return func(xx)
                func(xx)
            else:
                print(xx)
                newL.append(xx)
    else:
        print(x)
        newL.append(x)
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
typeL = type(L)  # type([3, 5, 8]) is list  # True
newL = []
func(L)
print('\nnewL:\n', newL)



6.7.3  	闭包 closure 闭包函数
概念：
闭包是指引用了此函数外部嵌套函数作用域变量的函数
语法：
闭包必须满足三个条件:
  1. 必须有内嵌函数（def一行）
  2. 内嵌函数必须引用外部函数中的变量（y）
  3. 外部函数返回值必须是内嵌函数.（fn）
应用：
定义一次以后可以减少传参数量
- 实例：
示例1:
def make_power(y):
    def fn(x):
        return x ** y
    return fn

pow2 = make_power(2)
print('5的平方是:', pow2(5))

print('5的平方是:', make_power(2)(5))  # 还可以一句话直接生成

pow3 = make_power(3)
print("6的立方是", pow3(6))

# 计算
# 1** 2 + 2**2 + 3**2 + ..... + 9 ** 2
print(sum(map(lambda x: x**2, range(1, 9))))
print(sum(map(make_power(2), range(1, 9))))

示例2：
def get_fx(a, b, c):
    def fx(x):
        return a*x**2 + b*x**1 + c
    return fx

# 创建函数 f(x) = 1*x**2 + 2*x**1 + 3
f123 = get_fx(1, 2, 3)
print(f123(20))
print(f123(50))

f654 = get_fx(6,5,4)
print(f654(20))
print(f654(50))
我的理解：
def f(info):
    def fn(x):
        print('hello1')
        print(info)
        print(x)
    return fn

do = f('hello2')
do('hello3')
- 应用：减少print(file=fo)的写法次数
import time


def f(foname):
    def g(*args):
        print(*args, file=fo)
    fo = open(foname, 'w', buffering=1)
    return g


def main():
    myprint = f('my.log')
    # print([1, 2], {4: 4}, 1, 2)
    myprint([1, 2], {4: 4}, 1, 2)
    # fo.write(str([1, 2]) + str({4: 4}))
    time.sleep(20)
    # print([1, 2], {4: 4}, 1, 2)
    myprint([1, 2], {4: 4}, 1, 2)


if __name__ == '__main__':
    main()


  3. 改写之前的学生信息管理程序
     要求添加四个功能:
        | 5)  按学生成绩高-低显示学生信息 |
        | 6)  按学生成绩低-高显示学生信息 |
        | 7)  按学生年龄高-低显示学生信息 |
        | 8)  按学生年龄低-高显示学生信息 |



模块也是对象

6.7.4  	装饰器 decorators(专业提高往篇)
问题:
函数名 /  函数名()  区别
函数名是变量，它绑定一个函数
什么是装饰器？
概念： 
装饰器是一个函数，主要作用是用来包装另一个函数或类(后面会讲)
作用：
是在不改变原函数名(或类名)的情况下改变被包装对象的行为
函数装饰器:
函数装饰器是指装饰器是一个函数，传入的是一个函数，返回的也是一个函数
语法:
def 装饰器函数名(参数):
    语句块
    return 函数对象
@装饰器函数名<换行>
def 函数名(形参列表):
    语句块
函数名()
优秀参考文档：
这是我见过最全面的Python装饰器详解！没有学不会这种说法！ - Python程序员的博客 - CSDN博客
https://blog.csdn.net/qq_42156420/article/details/81169554

6.7.4.1	运行机制：
- 原理描述：
1. 调用顺序，遵循入栈出栈思想
2. 装饰器实际上是一个闭包函数
@mydeco
def myfunc()....
 	等同于
myfunc = mydeco(myfunc)
- 运行过程
1.	将函数名myfun(x)作为一个对象传入装饰器函数形参fn，即fn=myfun(x)
2.	装饰器函数中，return返回其内部定义的子函数fx，并使用参数x
3.	子函数内部可以直接return返回fn(n)

示例见:
import time


def mydeco(fn):
    def fx(x, y=0):
        t0 = time.time()
        print('start', x, y)
        fn(x)  # 若此处调用myfunc()会导致无穷循环
        print('运行', time.time() - t0, '秒')
    return fx


@mydeco
def myfunc(x):
    time.sleep(1)
    print('被装饰函数', x)

L = [0]
myfunc(5)  # 相当于 f = mydeco(myfunc); f(5)
	运行结果：
start 5 0
被装饰函数 5
运行 1.0078682899475098 秒
探索：
def mydeco1(function):
    print('阶段一：程序读取mydeco1（1）')

    def func(x, y=10):
        print('--> 开始mydeco1(myfunc(5))')
        function(x)
        print('mydeco1，over, x=%d,y=%d' % (x, y))
    print('阶段一：程序读取mydeco1（2）')
    return func


def mydeco2(function):
    print('阶段一：程序读取mydeco2（1）')

    def func(x):
        print('--> 开始mydeco2(myfunc(5))')
        function(x)
        print('mydeco2，over, x=%d' % (x,))
    print('阶段一：程序读取mydeco2（2）')
    return func

print('--------------------------')
@mydeco2  # 3,mydeco1( mydeco2( myfunc(5) )
@mydeco1  # 2,         mydeco2( myfunc(5) ) )
def myfunc(x):  # 1,            myfunc(5)
    print('----> 运行myfunc(5), x=%d' % x)

print('-------------\n开始执行myfunc(5)')
myfunc(5)

6.7.4.2	应用实例：
# 此示例示意再加一个装饰器用来添加余额变动提醒功能


def send_message(fn):
    # 小姜写了一个装饰器函数用来发送短信  # send_message(fn=privillage_check(savemoney("小张", 200)))
    def fy(name, x):
        mod = fn(name, x)  # 先办业务
        if mod == "无权限":
            print("%s无权限操作" % name)
        elif mod:
            print('发短信给%s存了%s元, 剩余%s元' % (name, x, L[0]))
        else:
            print('发短信给%s取了%s元, 剩余%s元' % (name, x, L[0]))
    return fy


def privillage_check(fn):
    # 小赵写了一个装饰器函数:  privillage_check(fn=savemoney("小张", 200))
    def fx(name, x):
        print("\n正在检查权限.....")
        if name in {"小张", "小赵"}:
            mod = fn(name, x)  # 权限通过可以调用相应函数
            return mod
        else:
            return "无权限"
    return fx


@send_message  # send_message(privillage_check(savemoney("小张", 200)))
@privillage_check  # privillage_check(savemoney("小张", 200))
# 写一个操作数据的函数(此函数用来示意存钱操作)
def savemoney(name, x):     # 魏老师写的函数,用于存钱
    print(name, '存钱', x, '元')
    L[0] += x
    return 1


@send_message
@privillage_check
def withdraw(name, x):      # 冯老师写的函数，用于取钱
    print(name, '取钱', x, '元')
    L[0] -= x
    return 0

L = [0]
# ---- 以下是调用者小闵写的程序 -------
savemoney("小张", 2000)
withdraw("小张", 1000)
withdraw('小赵', 100)
savemoney('小赵', 400)
withdraw('小李', 500)
withdraw('小杜', 500)

# 运行结果
'''
正在检查权限.....
小张 存钱 2000 元
发短信给小张存了2000元, 剩余2000元

正在检查权限.....
小张 取钱 1000 元
发短信给小张取了1000元, 剩余1000元

正在检查权限.....
小赵 取钱 100 元
发短信给小赵取了100元, 剩余900元

正在检查权限.....
小赵 存钱 400 元
发短信给小赵存了400元, 剩余1300元

正在检查权限.....
小李无权限操作

正在检查权限.....
小杜无权限操作
'''
6.7.4.3	示例：给运行函数前后加上运行的时间
import time


def print_runtime(func):
    def do(*args, **kwargs):
        gettime = lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('[开始运行]%s' % gettime())
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time() - t0
        print('[运行结束]%s' % gettime())
        print('[运行了%.3f秒]\n' % t1)
    return do


@print_runtime
def do(x, y, *args, **kwargs):
    time.sleep(2)
    print(x, y, args, kwargs)


if __name__ == '__main__':
    do(1, 2)
    do(1, 2, 3, 4, n=5, nn=6)
运行结果：
[开始运行]2019-09-11 15:28:21
1 2 () {}
[运行结束]2019-09-11 15:28:23
[运行了2.008秒]

[开始运行]2019-09-11 15:28:23
1 2 (3, 4) {'n': 5, 'nn': 6}
[运行结束]2019-09-11 15:28:25
[运行了2.006秒]

6.7.4.4	示例：给运行函数前后加上运行的时间（格式化）
import time


def getformattime(n):
    s = '%.3fs' % (n % 60)
    for x in [(n / 60 % 60, 'm'),
              (n / 60**2 % 24, 'h'),
              (n / 60**2 / 24, 'd')]:
        if x[0] < 1:
            break
        s = '%d%s_' % x + s
    return s


def print_runtime(func):
    def do(*args, **kwargs):
        gettime = lambda: time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())
        print('[开始运行]%s' % gettime())
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time() - t0
        print('[运行结束]%s' % gettime())
        print('[运行了%.3f秒] %s\n' % (t1, getformattime(t1)))
    return do


@print_runtime
def f(a=1):
    time.sleep(1.4)
    print(a)


print(getformattime(3600 * 25 + 3700))
f('ceshi')
运行结果：
1d_2h_1m_40.000s
[开始运行]2019-10-09 23:45:06
ceshi
[运行结束]2019-10-09 23:45:08
[运行了1.406秒] 1.406s
6.8  	函数的文档字符串
定义：
函数内第一次未赋值给任何变量的字符串是此函数的文档字符串
说明:
1. 文档字符串通常用来说明本函数的功能和使用方法
2. 在交互模式下，输入:help(函数名) 可以查看函数的文档字符串
- 语法:
def 函数名(形参列表):
    '''函数的文档字符串'''
    函数语句块
- 查看方法：
help(函数名) 用于查看函数的帮助信息

函数的 __doc__ 属性
__doc__ 属性用于记录文档字符串。用来绑定函数的文档字符串

函数的 __name__ 属性
__name__ 用于记录函数的名称。用来绑定函数名(字符串)
示例:
def hello():
    '''此函数用来打招呼...
    这是函数的文档字符串
    '''
    pass
>>> help(hello)

函数的定义语法:
@装饰器1
@装饰器2
...
def 函数名(位置形参, *元组形参(或*), 命名关键字形参, **字典形参):
  '''文档字符串'''
  语句块

6.9  	机制研究
函数绑定
6.9.1  	可变对象思考（函数中的）
- 现象
面试题,思考？
L = [1, 2, 3]
def f(n=0, lst=[]):
 lst.append(n)
 print(lst)

f(4, L)  # 打印结果是什么？·[1, 2, 3, 4]
f(5, L)  # 打印结果是什么？ [1, 2, 3, 4, 5]
f(100)  [100]
f(200)  # 打印结果是什么？为什么？  [100, 200]

如下代码的打印结果是什么？
L = [1, 2, 3]


def f(n=0, lst=None):
    if lst is None:
        lst = []
    lst.append(n)
    print(lst)

f(4, L)  # 打印结果是什么？·[1, 2, 3, 4]
f(5, L)  # 打印结果是什么？ [1, 2, 3, 4, 5]
f(100)  # [100]
f(200)  # 打印结果是什么？为什么？  [200]
- 本质理解
函数在一开始初始化时，初始形参的变量即被创建和绑定一个对象。
若调用函数不再改变，绑定的对象将在之后的调用处理中也一直是该对象。

用列表进行函数传参ID是否变化？
L是独立的空间，函数内可以直接更改L，内外都相同
示例：
>>> def f(x,L):
...     print("ID",id(L))
...     L+=[1]
...     L.append(x)
...
>>> L
[1, 2, 3]
>>> f(9,L)
ID 21181864
>>> L
[1, 2, 3, 1, 9]
>>> id(L)
21181864

