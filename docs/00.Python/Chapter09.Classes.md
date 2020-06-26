# 9.  面向对象
——面向对象编程: Object - Oriented Programing

小结：
> - 研究意义：  
>   打包分类，耦合性低，思维明确；可以少一点全局变量；
> - 研究方法：
>   A.__dict__，dic(A)
> 问题集锦：
> __new__是什么来头？？构造函数？与__init__关系是什么？


## 9.1.  类的简介
### 9.1.1.  基本概念
#### 9.1.1.1.  基本名词解释

- **类(Class)**: 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- **方法**: 类中定义的函数。
- **类变量**: 类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- **数据成员**: 类变量或者实例变量用于处理类及其实例对象的相关的数据。
- **方法重写**: 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- **实例变量**: 定义在方法中的变量，只作用于当前实例的类。
- **继承**: 即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计: 一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- **实例化**: 创建一个类的实例，类的具体对象。
- **对象**: 通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

#### 9.1.1.2. 面向对象简介
- 面向对象简介
  - 什么是对象:  
    对象是指现实中的物体或实体
  - 什么是面向对象:  
    把一切看成对象(实例), 用各种对象之间的关系来描述事务
  - 对象都有什么特征:  
    - 对象有很多属性(名词)
      - 姓名, 性别, 年龄, ...
    - 对象有很多行为(动作，动词)
      - 学习，吃饭，睡觉，工作, ....

示意:
```
  车(类) - -----> > BYD E6(京A.88888)(实例，对象)
        \
         \-----> > BWM X5(京B.66666)(对象)
  狗(类) - -----> > 京巴(户籍号: 000001)
        \
         \-----> > 导盲犬(户籍号: 000002)

  int(类) - -----> > 100  (对象, 实例)
         \
          \-----> > 200 (对象, 实例)
```

#### 9.1.1.3.  类概念探索
- 什么是类？什么是实例？  
  拥有相同属性和行为的对象分为一组，即为一个类  
  类是用来描述对象的工具，用类可以创建此类的对象(实例)  

- 类属性？实例属性？

- 类的本质和实例的本质区别和联系是什么？

### 9.1.2.  类的创建

语法：  
class 语句

```python
class 类名(继承列表):
    ''' 类文档字符串'''
    类变量定义
    实例方法定义
    类方法定义(@classmethod)
    静态方法定义(@staticmethod)
```

作用:
- 创建一个类
- 用于描述对象的行为和属性
- 用于创建此类的一个或多个同类对象(实例)

说明:
- 继承列表可以省略，省略继承列表表示类继承自object
- 类名必须为标识符
- 类名实质上是变量，它绑定一个类

示例见: 【？】  
    class.py

### 9.1.3.  类的基本结构
#### 9.1.3.1.  构造函数

构造函数调用表达式：  
```
类名([创建传参列表])
a = A()
```

作用:  
- 创建这个类的实例对象，并返回此实例对象的引用关系

实例说明:
1. 实例有自己的作用域和名字空间，可以为该实例添加实例变量(也叫属性)
2. 实例可以调用类方法和实例方法
3. 实例可以访问类变量和实例变量

#### 9.1.3.2.  类变量（类属性）

类变量  
- 类变量有一个特点，在类中定义的每一个类不管在任何一个位置（比如某个类函数，某个循环嵌套中），最终都会成为类空间的“全局变量”！实例验证：

实例属性 attribute(也叫实例变量)  
- 每个实例可以用自己的变量，称为实例变量(也叫属性)

使用语法:  
- 实例.属性名

属性的赋值规则:
1. 首次为属性赋值则创建此属性
2. 再次为属性赋值则改变属性的绑定关系

作用:
- 记录每个对象自身的数据

示例见:
atribute.py

---
删除属性方法：
- del 语句

语法:  
- del 对象.属性名

示例:
```python
class Dog:
    pass

dog1 = Dog()
dog1.color = '白色'  # 添加属性
del dog1.color 删除属性
```

del 语句总结:
1) 删除变量 del a
2) 删除列表中的元素 del L[0]
3) 删除字典中的键 del d['name']
4) 删除对象的属性 del dog1.color

#### 9.1.3.3.  实例方法(method):

语法:
```python
class 类名(继承列表):
    def 实例方法(self, 形参1, 形参2, ...):
        '''方法的文档字符串'''
        语句块
```

作用:  
- 用于描述一个对象的行为，让此类型的全部对象都拥有相同的行为

说明:  
- 实例方法的实质是函数，是定义在类内的函数
- 实例方法至少有一个形参，第一个形参代表调用这个方法的实例，一般命名为'self'

实例方法的调用语法:  
- 实例.实例方法名(调用传参)
-   或
- 类名.实例方法名(实例, 调用传参)

示例1:  instance_method.py

#### 9.1.3.4.  初始化方法:

作用:
- 对新创建的对象添加属性等初始化操作

语法格式:
```python
class 类名(继承列表):
    def __init__(self[, 形参列表])
        语句块
```
注: [] 里的内容代表可省略
说明:
1. 初始化方法名必须为__init__ 不可改变
2. 初始化方法会在构造函数创建实例后自动调用，且将实例自身通过第一个参数self 传入 __init__ 方法
3. 构造函数的实参将通过 __init__方法的参数列表 传入到 __init__ 方法中
4. 初始化方法内如果需要return 语句返回，则只能返回None
示例见:
init_method.py

#### 9.1.3.5.  析构方法

语法:
```python
class 类名(继承列表):
    def __del__(self):
        语句块
```

作用:
- 通常用来释放此对象占用的资源

说明:
1. 析构方法会在对象被销毁时自动调用
2. python语句建议不要在对象销毁时做任何事情，因为对象销毁的时间难以确定

示例:  del_method.py

示例：  
<不绑定变量也可以实例，只不过语句结束会被销毁>
```python
class Test:
    def prt(self):
        print('start')

    def __del__(self):
        print('over')

Test().prt()  # start  over
```

#### 9.1.3.6.  类方法 @classmethod
问题:
类方法会自动 `a --> a.__class__` 【？】
1. 类方法属于类
2. 实例方法属于该类的实例
3. 请问: 类内能不能有函数, 这个函数不属于类, 也不属于实例

概念：
类方法是描述类的行为的方法, 类方法属于类, 不属于该类创建的实例
说明:
1. 类方法需要用@classmethod装饰器定义
2. 类方法至少有一个形参, 第一个形参用于绑定类, 约定写为'cls'
3. 类实例和对象实例都可以调用类方法
4. 类方法不能访问此类创建的实例的属性(只能访问类变量) 

示例:
- 此示例示意类方法的定义方法和用法
```python
class A:
    v = 0  # <<<---类变量
    def __init__(self):
        self.my_v = 10000

    @classmethod
    def get_v(cls):
        '''此方法为类方法，cls用于绑定调用此方法的类
        此方法用于返回类变量v的值
        '''
        return cls.v
        # return cls.my_v  # 出错

    @classmethod
    def set_v(cls, value):
        cls.v = value

print(A.get_v())  # 0  调用类方法返回值
A.set_v(100)
print(A.get_v())  # 100

a = A()
print(a.get_v())  # 100
a.set_v(200)
print(a.get_v())  # 200
print(A.get_v())  # 200
print(a.my_v)  # 10000
# 无法用类方法访问调用此对象的a的my_v实例变量
print(a.get_v())
```

#### 9.1.3.7.  静态方法@staticmethod
静态方法 @staticmethod
- 静态方法是定义在类内的函数，此函数的作用域是类的内部

静态方法不属于类,也不属于类的实例,它相当于定义在类内普通函数,只是它的作用域属于类

说明:

- 静态方法需要使用staticmethod装饰器定义
- 静态方法与普通函数定义相同，不需要传入self实例参数和cls类参数
- 静态方法只能凭借该类或类的实例调用
- 静态方法不能访问类变量和实例变量(属性)

示例见:
  static_method.py
小结 ：
  实例方法, 类方法, 静态方法, 函数

### 9.1.4.  类的初始化过程
dir(对象)

`['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']`

对象.__dict__
```json
{'__module__': '__main__', 
 '__init__': <function Person.__init__ at 0x00000000025D4840>, 
 '__dict__': <attribute '__dict__' of 'Person' objects>,
 '__weakref__': <attribute '__weakref__' of 'Person' objects>, 
 '__doc__': None}
```

- 实例传参
- 初始化函数__init__
- 生成__dict__
- ...


## 9.2.  继承/派生

继承/派生的概念：
- 继承是从已有的类中派生出新的类，新类具有原类的行为，并能扩展新的行为
- 派生类就是从一个已有的类衍生出新的类，在新的类上可以添加新的属性和行为

作用:
1. 用继承派生机制，可以将一些共有功能加在基类中，实现代码共享.
2. 在不改变超类的代码的基础上改变原有的功能

相关名词:  
- 基类(base class)
- 超类(super class)
- 父类(father class)
- 派生类(derived class)
- 子类

继承说明:
- 任何类都直接可间接的继承自object类
- object类是一切类的超类


### 9.2.1.  单继承
语法:
```python
class 类名(基类名):
    语句块
```

说明:
- 单继承是指派生类由一个基类衍生出来

示例见:
inherit.py

显式，初始化。
```python
def __init__(self, a):
    pass
```

### 9.2.2.  调用父类
#### 9.2.2.1.  通过类对象属性A.__base__

```python
class A:
    pass

class B(A):
    pass

print(B.__base__)  # <class '__main__.A'>
print(B.__base__ is A)  # True
print(A.__base__ is object)  # True
print(object.__base__ is None)  # True
```

- 方法覆盖 override
什么是覆盖
覆盖是指在有继承关系的类中，子类中实现了与基类同名的方法，在子类实例调用该方法时，实际调用的是子类中的覆盖版本的方法的现象叫覆盖

示例见：
```python
class A:
    '''A类'''
    def work(self):
        print("A.work被调用!")

class B(A):
    '''B类'''
    def work(self):
        '''work 方法覆盖了父类的work'''
        print("B.work被调用!")

b = B()
b.work()  # B.work

a = A()
a.work()  # A.work

b.work()  # B.work
b.__class__.__base__.work(b)  # A.work
```

问题:  
【在override.py中 ，b能否调用到父类的work方法?】


#### 9.2.2.2.  super 函数:

- 格式：
```python
super(class, cls)
# 返回绑定超类的实例(要求cls必须为class的实例)
```

类中使用时可以省略参数
- super()
- 返回绑定超类的实例，等同于 super(self.__class__, self), 必须用在方法内调用。如： super().work()等同于super(B, self).work()

作用：
- 返回绑定超类的实例，
- 用超类的实例来调用其父类的覆盖方法

说明：
- 先去找上一层
- super(类，对象)。是按照查找顺序去调用的

示例:  
<此示例示意用super构造函数来间接调用父类的覆盖版本的方法>

```python
class A:
    def work(self):
        print("A.work()")

class B(A):
    def work(self):
        print("B.work()")

    def super_work(self):
        '''此方法先调用一下子类的work,
        再调用一下父类的work'''
        self.work()  # 调用自己的work
        # super(B, self).work()  # 调用父类的work
        super().work()  # 调用父类的work

b = B()
b.work()   # B.work(),
super(B, b).work()   # A.work()
b.super_work()    # B.work()  # A.work()
# super().work()  # 错的!!! super() 不能在方法外使用
```

应用
- 显式调用基类的构造方法
- 当子类中实现了__init__方法，基类的构造方法并不会被调用，此时需要显式调用基类的构造方法

示例见:
super_init.py

```python
class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print("Human.__init__被调用")
    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self, n, a, s):
        super().__init__(n, a)  # 显式调用父类的初始化方法
        self.score = s
        print("Student.__init__被调用")

    def infos(self):
        super().infos()
        print("成绩:", self.score)

# h1 = Human('小张', 18)
# h1.infos()
s1 = Student("魏老师", 35, 60)
s1.infos()
```

### 9.2.3.  类继承判断函数
#### 9.2.3.1.  issubclass()判断实例与对象的继承关系
概念
- 判断一个类的实例是否是另一个类的子类。

语法：
- `issubclass(cls, class_or_tuple)`
- 判断一个类是否继承自其它的类,如果此类cls是class或 tuple中的一个派生子类则返回True,否则返回False

探索实例：
```python
class A:
    pass
class B(A):
    pass
class C(B):
    pass
issubclass(C, (A, B))  # True
issubclass(C, (int, str)) # False
```

探索对象绑定
```python
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?   ', isinstance(a, Dog))
print('a is Cat?   ', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?   ', isinstance(d, Dog))
print('d is Cat?   ', isinstance(d, Cat))
```

run_twice(c)
结果：
```
a is Animal? True
a is Dog?    False
a is Cat?    False
d is Animal? True
d is Dog?    True
d is Cat?    False
Cat is running...
Cat is running...
```

#### 9.2.3.2.  Isinstance()判断对象与对象间继承关系

isinstance(class, class_or_tuple)

返回这个对象class 是否是某个类的对象，或者某些类中的一个类的对象，如果是则返回True, 否则返回False

示例1:

```python
# 例子，如果继承关系是：object -> Animal -> Dog -> Husky
class Animal(object): pass
class Dog(Animal): pass
class Husky(Dog): pass

h = Husky()
# 然后，判断：
print(isinstance(h, Husky))  # True
```

示例2:
```python
isinstance(3.14, float)  # True
isinstance('hello', str)  # True
class Dog:
    pass
dog1=Dog()
isinstance(dog1, Dog)  # True
```

### 9.2.4.  应用

实例：

- 思考下列表代码做什么事儿?
- 继承list类应用其方法

```python
class MyList(list):
    def insert_head(self, n):
        self.insert(0, n)

myl=MyList(range(3, 6))
myl.insert_head(2)
myl.append(6)
print(myl)  # [2, 3, 4, 5, 6]
```


### 9.2.5.  继承和派生研究实例

- 查看内建类的继承
查看python内建类的继承关系的方法:
```python
>>> help(__builtins__)  
>>> __builtins__.__dict__
```
探索：
内建类的继承关系
	object --> int --> bool  
	一切皆对象啊！！！

- 探索继承实质【？可删】


## 9.3.  封装 enclosure

封装 enclosure
- 封装是指隐藏类的实现细节, 让使用者不用关心这些细节
- 封装的目的是让使用者尽可能少的实例变量(属性)进行操作

私有属性:
- "__name"，私有类型，

- python类中, 以双下划线'__'开头, 不以双下划线结尾的标识符为私有成员, 在类的外部无法直接访问
- 单下划线表示，_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
- "_name"，保护类型，protected 类型

示例:
```python
# 此示例示意使用私有属性和私有方法:
class A:
    def __init__(self):
        self.__p1 = 100  #__p1为私有属性,在类的外部不可访问

    def test(self):
        print(self.__p1)  # 可以访问
        self.__m1()  # A类的方法可以调用A类的私有方法

    def __m1(self):
        '''我是私有方法,只有我自己的类中的方法才能调用我哦'''
        print("我是A类的__m1方法!")

a = A()  # 创建对象
# print(a.__p1)  # 在类外看不到__p1属性,访问失败!
a.test()
# a.__m1()  # 出错.无法调用私有方法
```

- 深度探索：  
实例：
```python
#私有变量深度探索：
class Student(object):

    # _xxx 是普通变量, 可直接访问, 人为约定俗成视为私有变量
    # __xxx 是私有变量(private变量), 一般不能直接访问
    # __xxx__ 是特殊变量, 可直接访问, 特殊变量不是private变量。
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 为什么要定义一个方法大费周折？
    # 因为在方法中，可以对参数做检查，避免传入无效的参数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


print('（一）实例化')
bart = Student('Bart Simpson', 59)

print('（二）访问私有变量')
# （1）正常访问
print(bart.get_name())  # 'Bart Simpson'
# （2）错误访问
try:
    print(bart.__name)  # 访问报错
except AttributeError as e:
    print('不能直接访问__name, 报错！！错误是：', e)
    # 私有变量机制：因为Python解释器对外把__name变量改成了_Student__name。
    # 所以还可以通过漏洞访问。强烈建议不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

print('（三）验证私有变量机制')
print(bart._Student__name)  # 'Bart Simpson'
print(bart.get_name())  # 'Bart Simpson'

print('（四）修改内部私有变量')
# （1）正常修改
bart.set_score(89)
print(bart.get_score())  # 'Bart Simpson'
# （2）非正常修改（利用机制）
bart._Student__name = 'New Name'
print(bart.get_name())  # 'New Name'
# （3）错误修改
bart.__name = 'hello'
print(bart.__name)  # 'New Name'
print(bart.get_name())  # 'Bart Simpson'
# 设置__name变量！
# 实质是外部代码给bart新增了一个__name变量，并没有改变私有变量
# 内部的__name变量已经被Python解释器自动改成了_Student__name
```

## 9.4.  多态

静态与动态
- 动态语言：可以在运行的过程中，修改代码
- 静态语言：编译时已经确定好代码，运行过程中不能修改

多态 polymorphic
- 字面意思: "多种状态"
- 多态是指在继承 / 派生关系的类中, 调用基类对象的方法, 实际能调用子类的覆盖版本方法的现象叫多态

说明:
- 多态调用的方法与对象相关, 不与类型相关
- Python的全部对象都只有"运行时状态(动态)", 没有"C++/Java"里的"编译时状态(静态)"

面向对象的编程语言的特征:
- 继承
- 封装
- 多态
- 如: C + + / Java / Python / Swift / C


应用：  
实例1：动态的指令输入函数执行

```python
class Point:
    def draw(self):
        print('正在画一个点')

class Circle:
    def draw(self):
        print("正在画一个圆")

def my_draw(s):
    s.draw()  # 此处显示出多态中的动态

L = [Circle(), Point(), Point(), Circle()]
for s in L:
    my_draw(s)
```

### 9.4.1.  多继承
多继承 multiple inheritance

概念
- 多继承是指一个子类继承自两个或两个以上的基类

语法:
```python
class 类名(基类名1, 基类名2, ....):
    语句块
```
说明:
1. 一个子类同时继承自多个父类, 父类中的方法可以同时被继承下来
2. 如果两个父类中有同名的方法, 而在子类中又没有覆盖此方法时, 调用结果难以确定

多继承的问题(缺陷)  
- 标识符(名字空间冲突的问题), 要谨慎使用多继承
- 话外：为了解决多继承的命名冲突，C++不支持多继承，引入了虚函数等概念，Java则…

命名冲突时执行的先后顺序：
实例1：命名冲突，优先执行__mro__列表中排更前面的语句
```python
class A:
    def work(self):
        print("A.work被调用!")

class B:
    def work(self):
        print("B.work被调用!")

class AB(A, B):
    pass

a = A()
b = B()
ab = AB()
a.work()  # A.work
b.work()  # B.work
print(AB.__mro__)  # (<class ... <class 'object'>)
ab.work()  # A.work，默认谁在前调用谁
```

```
A.work被调用!
B.work被调用!
(<class '__main__.AB'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
A.work被调用!
```

- __mro__的查找规则
使用C3算法
语法：
类名.__mro__		 返回查找对象排列的元组
作用：
类内的__mro__属性用来记录继承方法的查找顺序


实例探索：
	对于如下继承关系，如何查找？
```
          obj
     __  __|__ __
   /   |       |   \
  /    |       |    \
  A1   A2      A3   A4
   \   |       |   /  |
    \  |       |  /   |
      B1        B2    B3
     / |        | \   |
   /   |        |   \ |
 C1   C2        C3   C4
  \   |          |    /
   \__|____ ____|__/
            |
            S
```

```python
class A1: pass
class A2: pass
class A3: pass
class A4: pass
class B1(A1, A2): pass
class B2(A3, A4): pass
class B3(A4): pass
class C1(B1): pass
class C2(B1): pass
class C3(B2): pass
class C4(B2, B3): pass
class S(C1,C2,C3,C4): pass
print(S.__mro__)

'''
(<class '__main__.S'>, 
    <class '__main__.C1'>, <class '__main__.C2'>, 
        <class '__main__.B1'>, 
            <class '__main__.A1'>, 
            <class '__main__.A2'>, 
    <class '__main__.C3'>, <class '__main__.C4'>, 
        <class '__main__.B2'>, 
    <class '__main__.A3'>, 
        <class '__main__.B3'>, 
    <class '__main__.A4'>, 
                <class 'object'>)
'''
```

### 9.4.2.  函数重写

函数重写 override
- 重写是在自定义的类内添加相应的方法,让自定义的类生成的对象(实例)像内建对象一样进行内建的函数操作

对象转字符串函数重写
- repr(obj)  返回一个能代表此对象的表达式字符串, 通常:
  - eval(repr(obj)) == obj   (通常用于计算机通信)
- str(obj)   通过给定的对象返回一个字符串(这个字符串通常是给人看的)

repr()和str()区别

探索实例

```python
a = str(1+2)
b = repr(1+2)
print(a == b, a, b)
```

---
对象转字符串函数重写方法

```python
repr() 函数的重写方法:
    def __repr__(self):
        return 能够表达self内容的字符串

str() 函数的重写方法:
    def __str__(self):
        return 人能看懂的字符串
```

说明:
1. str(obj) 函数优先调用obj.__str__()方法返回字符串
2. 如果obj没有__str__()方法, 则调用obj.__repr__()方法返回的字符串
3. 如果obj没有__repr__()方法, 则调用object类的 __repr__() 实例方法显示 < xxxx > 格式的字答鼓足

示例：
```python
class MyNumber:
    pass
    # def __len__(self):
    #     return 100

n1 = MyNumber()

x = len(n1)  # 重写了__len__方法才可以使用，否则报错
print('x =', x)
```

内建函数的重写
```python
# 此示例示意一个自定义的数字类型重写 repr和 str的方法
#重写前：
class Mytest:

    def __init__(self, value):
        self.data = value

n1 = Mytest(100)

print('问题1:')
print(str(n1))  # 调用 n1.__str__(self)
print(n1)  # 等同于print(str(n1))，与上句执行结果一致

print('问题2:')
print(repr(n1))

print('问题3:')
n = int(n1)  # 普通的int方法无法做事情
print(type(n1))
print(type(n))
print(n)
```

```
问题1:
<__main__.Mytest object at 0x0000000001DEE160>
<__main__.Mytest object at 0x0000000001DEE160>
问题2:
<__main__.Mytest object at 0x0000000001DEE160>
问题3:
Traceback (most recent call last):
  File "07_str_repr.py", line 34, in <module>
    n = int(n1)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'Mytest'
```

```python
#重写后：
class Mytest:

    def __init__(self, value):
        self.data = value

    def __str__(self):
        print("__str__被调用")
        return "数字: %d" % self.data

    def __repr__(self):
        print("__repr__被调用")
        return 'Mytest(%d)' % self.data

    def __int__(self):
        print("__int__被调用")
        return int(self.data)

n1 = Mytest(100)

print('问题1:')
print(str(n1))  # 调用 n1.__str__(self)
print(n1)  # 等同于print(str(n1))，与上句执行结果一致

print('问题2:')
print(repr(n1))

print('问题3:')
n = int(n1)
print(type(n1))
print(type(n))
print(n)
```

```
问题1:
__str__被调用
数字: 100
__str__被调用
数字: 100
问题2:
__repr__被调用
Mytest(100)
问题3:
__int__被调用
<class '__main__.Mytest'>
<class 'int'>
100
```

其他问题深究
```python
>>> i = -100
>>> abs(i)
100
>>> i.__abs__()
100
>>> help(int)

 ...
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 ...
```

## 9.5.  对象的属性管理函数
详见文档

对象属性管理函数:  
详见: python_base_docs_html/内建函数(builtins).html

`getattr(obj, name[, default]`
- 从一个对象得到对象的属性；getattr(x, 'y') 等同于x.y; 当属性不存在时,如果给出default参数,则返回default,如果没有给出default 则产生一个AttributeError错误

`hasattr(obj, name)`
- 用给定的name返回对象obj是否有此属性,此种做法可以避免在getattr(obj, name)时引发错误

`setattr(obj, name, value)`
- 给对象obj的名为name的属性设置相应的值value, set(x, 'y', v) 等同于 x.y = v

`delattr(obj, name)`
- 删除对象obj中的name属性, delattr(x, 'y') 等同于 del x.y


### 9.5.1.  获取对象信息

```python
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self, xx):
        print(xx)
        return self.x * self.x

obj = MyObject()

## 有属性'x'吗？
print(hasattr(obj, 'x'))  # True

## 获取属性'x', getattr 和 直接调用
print(getattr(obj, 'x'), obj.x)  # 9 9
# print(getattr(obj, 'y') # 触发异常AttributeError
print(getattr(obj, 'y', 404)) # 获取属性'z'，如果不存在，返回默认值404

## 设置一个属性'y'
print(setattr(obj, 'y', 19))

## 获取方法
print(hasattr(obj, 'power'))  # True
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# 调用fn()与调用obj.power()是一样的
print(fn(3))  # 3 81
```


## 9.6.  类的属性查看方法
### 9.6.1.  类对象属性

```python
#-*-coding:UTF-8-*-
class A:
    __slots__ = ['a','b']
    pass

# 类属性
print(A.__base__)  # 返回元组，包含其所有父类继承对象（按照多继承查找规则__mro__）
print(A.__dict__)  # 返回字典，查看类中实例变量
print(A.__mro__)   # 返回元组，查看多继承查找顺序

# 实例属性
a = A()
print(a.__class__) # 返回实例对象绑定的类对象
print(A)
print(A.__class__) # 返回实例对象绑定的类对象
print(type(A))

print(A.__slots__) # 返回被限制的类属性的列表，必须提前定义
print(a.__slots__) # 返回被限制的类属性的列表，必须提前定义
```

### 9.6.2.  预置的实例属性

类在实例化时，会自动生成一个字典，存储实例变量

#### 9.6.2.1.  类的__dict__属性

作用：
- __dict__属性绑定一个存储此实例自身变量的字典

示例:
```python
class Dog:
    pass

dog1=Dog()
print(dog1.__dict__)  # {}
dog1.color="白色"
print(dog1.__dict__)  # {'color': '白色'}
```

	应用：
	示例1：字典对象传参妙用
	# 传入字典参数，减少代码
	# 原代码：
class Person:
    def __init__(self, _obj):
        self.name = _obj['name']
        self.age = _obj['age']
        self.energy = _obj['energy']
        self.gender = _obj['gender']
        self.email = _obj['email']

	#修改代码：
class Person:
    def __init__(self, _obj):
        self.__dict__.update(_obj)

d = {'name': 1, 'age': 2, 'energy': 3, 'gender': 4, 'email': 5}
s1 = Person(d)
print(s1.__dict__)  # 实例对象的字典
print('s1.name', s1.name)
print('------------------------------')
print(Person.__dict__)  # 类对象的字典

{'name': 1, 'age': 2, 'energy': 3, 'gender': 4, 'email': 5}
s1.name 1
------------------------------
{'__module__': '__main__', '__init__': <function Person.__init__ at 0x0000000001DD4840>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


#### 9.6.2.2.  类的__class__属性
__class__属性绑定创建此实例(类实例)的类
	作用:
可以借助于此属性来访问创建此实例的类

	示例:
class Dog:
    pass

dog1 = Dog()
dog2 = dog1.__class__()

print(Dog)  # 类对象Dog，结果<class '__main__.Dog'>
print(dog1.__class__)  # 类对象Dog，结果<class '__main__.Dog'>
print(dog2.__class__)  # 类对象Dog，结果<class '__main__.Dog'>

print(dog1)  # 命名为dog1的实例对象，结果<__main__.Dog object at 0x02FD5F10>
print(dog1)  # 命名为dog1的实例对象，结果<__main__.Dog object at 0x02FF0590>
print(Dog())  # 未绑定变量的实例对象，结果<__main__.Dog object at 0x02FF0650>
print(Dog)   # 类对象，结果<class '__main__.Dog'>

#### 9.6.2.3.  类的__base__属性
  __base__属性用来记录此类的基类

	示例:
  class Human:
      pass
  class Student(Human):
      pass
  class Teacher(Human):
      pass
  Student.__base__ is Human  # True

内建类的继承关系见:
  >>> help(__builtins__)

注意，返回的是其所有继承对象的元组
class ParentClass1: 
    pass

class ParentClass2: 
    pass

class SubClass1(ParentClass1):
    pass

class SubClass2(ParentClass1,ParentClass2): 
    pass

print(type(SubClass1.__bases__))
print(SubClass1.__bases__)
print(SubClass2.__mro__)

### 9.6.3.  类的__slots__属性
	问题描述：
在创建类实例对象时，一般会初始化生成字典，记录类属性。
所有类属性都是用字典记录的，通过 实例名.__dict__ 可查看访问。
	__slots__作用:
限定一个类创建的实例只能有固定的属性(实例变量)，不允许对象添加列表以外的属性
访止用户因错写属性的名称而发生程序错误
说明:
含有__slots__属性的类所创建的实例没有__dict__属性,即此实例不用字典来存储对象的属性
__slots__列表作用：
1.	定义一个特殊的__slots__变量，来限制该class实例能添加的属性
2.	阻止实例化类时为实例分配字典dict。
3.	减少内存
	网络原话：
在python新式类中，可以定义一个变量__slots__，它的作用是阻止在实例化类时为实例分配字典dict
使用slots可以让内存使用减少3.5倍！！# 通过 (200 - 4) / ((60 - 4) * 1.0) 计算得来【来源：
https://www.jb51.net/article/118024.htm
】

说明:
含有__slots__列表的类创建的实例对象没有__dict__属性, 即此实例不用字典来保存对象的属性(实例变量)
	示例:
示例1：限制添加实例属性
class Person(object):
    __slots__ = ("name", "age")	 # 即便是[]，也不能再添加属性


P = Person()
P.name = "老王"
P.age = 20
# P.score = 100  # 此句报错
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
# AttributeError: Person instance has no attribute 'score'
	注意：可以正常添加类属性，__slots__只是限制添加实例属性
...
P.__class__.score = 100
print(Person.score)
Person.score=10
print(Person.score)
	注意：添加的类属性，名字不能与实例属性相同，否则会发生冲突

示例2：此示例示意 类的变量 __slots__列表的作用
class Student:
    __slots__ = ['name', 'score']
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student('小张', 58)
print(s1.score)
# s1.socre = 100  # 此处错写了属性名,但在运行时不会报错!
# print(s1.__dict__)  # 报错
s1.score = 100
print(s1.score)  # 请问打印的值是多少?

### 9.6.4.  self代表类的实例，而非类
self代表类的实例，而非类本身
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
	self不是python关键字，若将self替换为其他单词一样正常运行。
实例：
class A:
     def prt1(self):
         print(self)
     def prt2(self):
         print(self.__class__)


a = A()
# 调用实例对象: <__main__.Test object at 0x7feddc55e2b0>
print(a)    # 类外调用实例对象
A().prt1()  # 类中调用实例对象

# 调用类对象: <class '__main__.Test'>
print(a.__class__)    # 类外通过实例去调用类对象
print(A().__class__)  # 类外通过实例去调用类对象
print(A)    # 类外调用类对象
A().prt2()  # 类中调用类对象

print(a.__class__ is A)  # True


### 9.6.5.  类变量（类属性）
类变量class variable(也叫类属性)
#### 9.6.5.1.  问题引入：
	全局的变量有哪些？
>>> class Human:
		def __init__(self,n):
 			self.name = n
>>> h1 = Human('小张')
>>> h2 = Human('小李')
>>> dir()	#可以看到有3个变量，h1,h2,Human，分别绑定实例1，实例2，类对象
结论：dir()查看有3个变量，类名变量绑定类
实例变量 不同于 类变量
问题:
1. 对象内可以有:
   实例变量
   实例方法
2. 类内可以有:
   类变量
   类方法  # 这个可以有
#### 9.6.5.2.  基本概念
类变量：
类变量是的类的属性，此属性属于类，不属于类的实例
作用：
通常用来存储该类对象共有的数据
说明：
类变量可以通过类直接访问
类变量可以通过类的实例直接访问
类变量可以通过此类的实例的__class__属性间接访问
语法：
class 类名(继承列表):
    类变量名 = 表达式
    ...

#### 9.6.5.3.  应用
# <类的实例对象> 不同于 <类的对象> ，但前者可以访问和修改后者变量
# 类变量的定义和使用
class Human:
count = 0  # 创建类变量

print("Human的类变量count=", Human.count)  # 0
Human.count = 100
print(Human.count)  # 100

# Human类的实例可以访问和修改count类变量
class Human:
count = 0  # 创建类变量

h1 = Human()
print("用h1对象访问Human的count变量", h1.count)  # 0
h1.count = 100  # 此做法是为实例添加一个变量，并不是修改类变量
print(h1.count)  # 100
print(Human.count) # 0
h1.__class__.count = 200  # 此做法修改类变量
print("h1.count=", h1.count)  # 100
print('Human.count=', Human.count)  # 200

# 此示例示意用类变量来记录对象的个数
class Car:
    count = 0  # 创建类变量, 用来记录汽车对象的总数
    def __init__(self, info):
        print(info, "被创建")
        self.data = info  # 记录传入数据
        self.__class__.count += 1  # 让车的总数加1

    def __del__(self):
        print(self.data, '被销毁')
        # 当车被销毁时总数自动减1
        self.__class__.count -= 1  

print('当前汽车总数是:', Car.count)
b1 = Car("BYD 京A.88888")
print(Car.count)
b2 = Car('TESLA 京B.00000')
b3 = Car('Audi, 京C.66666')
print('当前汽车总数是:', Car.count)
del b1
del b2
print("当前汽车数是:", Car.count)

### 9.6.6.  类的文档字符串:
类内第一个没有赋值给任何变量的字符串是类的文档字符串
类的文档字符串由类的__doc__属性绑定

说明:
类的文档字符串用类的__doc__属性可以访问
类的文档字符串可以用help()函数查看
  示例:
    class Dog:
        '''这是类的文档字符串'''
        pass
    >>> help(Dog)
    >>> dog1 = Dog()
    >>> help(dog1)

## 9.7.  研究实例
### 9.7.1.  实例属性和类属性区别
class Student(object):
    name = 'Student'


s = Student()  # 创建实例s
print('s.name:', s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
print('Student.name:', Student.name)  # 打印类的name属性
# Student
s.name = 'Michael'  # 给实例绑定name属性
print(" --> 修改s.name = 'Michael'" )
print("s.name:", s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
print('Student.name:', Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
# Student
del s.name  # 如果删除实例的name属性
print(' --> 删除del s.name ')
print('s.name:', s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student

s.name: Student
Student.name: Student
 --> 修改s.name = 'Michael'
s.name: Michael
Student.name: Student
 --> 删除del s.name 
s.name: Student
