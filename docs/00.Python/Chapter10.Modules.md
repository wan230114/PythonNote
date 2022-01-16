
# 10. 模块和包

我们为什么需要模块？模块化编程？

> 你在班里叫小明，突然有一天，有个同名的同学也来了你学校，并且同你一个班级，两个人如何从称呼上加以辨别呢？  
> 
> 当同名同学在同一个教室时，需要加一个特殊称谓才能辨别。但若有一天分班了，便可在各自班级直接称呼。
> 
> 模块就相当于这个分班过程！当然，类，函数它们也如此。
> 当程序越来越多时，变量名类似的表达越来越多时，我们就可以使用这个方法，让简易相同的变量名得以反复使用。

---
## 10.1. 基本概念
### 10.1.1. 模块 Module

概念：
- 模块是一个包含有一系列数据，函数，类等组成的程序组  
- 模块是一个文件，模块文件名通常以'.py'结尾  

作用:
- 让一些相关的数据，函数,类等有逻辑的组织在一起，使逻辑结构更加清晰  
- 模块中的变量，函数和类等可提供给其它模块或程序使用

---
### 10.1.2. 包 Package

概念：
- 包是将模块以文件夹的组织形式进行分组管理的方法

作用：
- 将一系列模块进行分类管理，有利于访问命名冲突；  
- 可以在需要时加载一个或部分模块，而不是全部模块（可一定程度上减少加载时间）  

---
特别的：  
包/子包内必须有 `__init__.py` 文件
- 该文件是常规包内必须存在的文件（内容可空）
- 该文件在包加载时被自动调用
- 该文件作用:
  - 编写此包内容，定义默认加载项
  - 在内部填写包的文档字符串

---
包的加载路径（同模块的加载路径搜索）
1. 搜索当前路径
2. 搜索sys.path给定的路径

---
包文件示例:
```python
mypack/
    __init__.py
    menu.py
    games/
        __init__.py
        contra.py
        supermario.py
        tanks.py
    office/
        __init__.py
        excel.py
        word.py
        powerpoint.py
```

从mypack包导入games模块：
- `import mypack.games`
- `from mypack import games`


---
## 10.2. 模块和包的导入

1. 导入语句的实质是在当前环境创建变量来绑定模块/函数/数据。
2. 模块和包的导入语法基本一致，不同的地方在于包的导入必须包内有`__init__.py`文件。
3. `from 包 import *`的语法必须要求`__init__.py`文件中包含`__all__`属性。

---
### 10.2.1. 基本语句

两类基本语句:
```python
import 模块名1 [as 模块新名1], 模块名2[as 模块新名2], ....
from 模块 import ... [as ...]
```

这里的模块泛指“模块”或“包”

#### 10.2.1.1. import 语句

将一个模块整体导入到当前模块中

语法:
```python
# 模块导入
import 模块名1 [as 模块新名1], 模块名2[as 模块新名2], ....
# 包同模块的导入规则相同
import 包名 [as 包别名]
import 包名.模块名 [as 模块新名]
import 包名.子包名.模块名 [as 模块新名]
```

```python
# 模块函数用法:
模块名.函数(参数)

# 属性用法:
模块名.属性名
...
```

示例:
```python
import math  # 导入数学模块
import sys, os  # 导入sys和os模块
import copy as cp
```

#### 10.2.1.2. from import 语句

将某模块的一个或多个属性导入到当前模块的作用域

语法:
```python
from 模块名 import 模块属性名 [as 属性新名1], 模块属性名2 [as 属性新名2]
from 包名 import 模块名 [as 模块新名]
from 包名.子包名 import 模块名 [as 模块新名]
from 包名.子包名.模块名 import 属性名[as 属性新名]
```

特别的，将某模块的所有属性导入到当前的模块，语法为:
```python
from 模块名 import *
from 包名 import *
from 包名.子包名 import *
```

---
示例1:
```python
from math import pi
from math import sin
from math import factorial as fac
```

---
示例2:
```python
from math import *
s = sin(pi/2)
print(factorial(10))
```

---
练习:
1. 输入一个圆的半径，打印出这个圆的面积
2. 输入一个圆的面积，打印出这个圆的半径
(要求用math模块内的函数和变量)

### 10.2.2. 包的导入的一些特殊性质


---
**必要文件及属性：**
1. 每一个包/子包的目录下必须拥有`__init__.py`文件
2. 对于`from 包名 import * `语句的执行，  
   要求包下`__init__.py`中必须指定`__all__ = ['包1', '包2']`  
   否则无法导入模块而报错。

---
**包的导入执行顺序：**
- 当导入主包的子包时：`import 主包.子包`
- 初始化顺序为：  
  `主包.__init__.py`、`主包.子包.__init__.py`

---
**包的相对导入：** 指包内模块的相互导入。

常用于包内部之间的模块导入设计。

语法:
```python
from 相对路径包或模块 import 属性或模块
# 或
from 相对路径包或模块 import *
```

相对路径:
```yml
. 代表当前目录
.. 代表上一级目录
... 代表上二级目录
.... 以此类推
```

注:
- 包的相对导入不能用于import xxx 语句中。
- 相对导入时不能超出包的外部。
- 导入是按照主脚本的当前位置导入所有代码的

示例：
```python
from ..menu import *
from .games import *   # 从当前主包的games模块或包导入所有内容
```

---
### 10.2.3. 模块和包的重新导入

语法：
```python
import mymod
import imp
imp.reload(mymod)  # 在运行时重新加载mymod 模块
```
> *PS：python3中 reload在imp包中； python2中 reload是内置模块；*

---
示例：重新获取模块原本的初始变量
```python
import demo_pacages.demo01_pkg as demo

# 修改属性
print(demo.a)
demo.a = "123"
print(demo.a)

# 直接import是不会直接重新导入的
import demo_pacages.demo01_pkg as demo
print(demo.a)

# 定义重新加载
import imp
imp.reload(demo)
print(demo.a)
```

---
## 10.3. 模块和包的属性

属性简介：
- __doc__属性: 绑定模块文档字符串
  - 模块内第一个没有赋值给任何变量的字符串为文档字符串
- __file__属性: 绑定模块对应的文件路径  
	- 对于被导入的模块，文件名为绝对路径格式  
	- 对于直接执行的模块，文件名为相对路径格式  
- __name__属性:
  - 用来记录模块的自身的名字。并在不同使用场景下用于判断是否为主模块  
  - 说明:  
    当此模块作为主模块(主脚本)运行时, __name__绑定'__main__'  
    当此模块不是主模块时，__name__绑定当前使用模块名(文件名去掉.py后缀)  
  - 应用。`if __name__ == '__main__':`语句的一般使用：
    - 当.py文件被直接运行时，`if __name__ == '__main__':`之下的代码块将被运行；
    - 当.py文件以模块形式被导入时，`if __name__ == '__main__':`之下的代码块不被运行。

查看属性方法：
```python
# 主脚本执行
print(__doc__)
print(__file__)
print(__name__)
# 载入模块后：    
import 模块名
print(模块名.__doc__)
print(模块名.__file__)
print(模块名.__name__)
```

查看导入模块的其他属性的方法：
> - help函数： `help(导入的模块)`。包括文档，变量，函数，类，方法等在内的信息。
> - dir 函数：`dir([对象])`。返回绑定的变量的列表，当前对象或作用域内变量名的列表。

---
示例1：

文件
- [demo_pacages/demo01.py](demo_pacages/demo01.py)
- [demo_pacages/demo01_pkg.py](demo_pacages/demo01_pkg.py)

```bash
$ cd demo_pacages/

$ python3 demo01_pkg.py
demo01的__doc__属性： hello, this is help doc for load.
demo01的__file__属性： demo01_pkg.py
demo01的__name__属性： __main__
主脚本将会打印该句话

$ python3 demo01.py
demo01的__doc__属性： hello, this is help doc.
demo01的__file__属性： /Users/chenjun/NoteBook/PythonNote/docs/00.Python/demo_pacages/demo01_pkg.py
demo01的__name__属性： demo01_pkg
若调用该模块将会打印该句话
demo01_pkg.__doc__： hello, this is help doc.
demo01_pkg.__file__： /Users/chenjun/NoteBook/PythonNote/docs/00.Python/demo_pacages/demo01_pkg.py
demo01_pkg.__name__： demo01_pkg
```

---
练习：查看name属性

m1.py
```python
print('m1:', __name__)
```

m2.py
```python
import m1
print('m2:', __name__)
```

m.py
```python
import m2
print('m3:', __name__)
```

执行 `python3 m.py` 将会打印什么？

<details><summary>运行结果：</summary>

```
m1: m1
m2: m2
m: __main__
```

</details>

## 10.4. 模块导入和执行的机制

掌握此原理，可以灵活操作模块载入，并可以解决不同时间、不同版本、重名的模块载入与预期不符的种种问题。

模块被导入和执行的过程:

搜索模块 --> 编译模块 --> 加载执行模块

既：
- 先搜索相关路径找模块(.py文件)
- 判断是否有此模块对应的.py文件，如果.pyc文件比.py文件新，则直接加载.pyc文件
- 否则用模块.py 文件生成 .pyc 并加载执行

---
**搜索模块**

搜索查找<模块.py>的路径顺序
1. 程序所在路径
2. 搜索程序运行时的路径
3. PATHONPATH环境变量，脚本执行前指定的环境变量
4. 搜索标准库目录，搜索内置模块
5. 任何.path文件指定的路径

手动定义模块搜索的两种方法：  
（注意，此方法有风险，请慎用。具体表现为，版本，覆盖顺序等）
- 方法1：

  ```python
  import sys
  print(sys.path)
  # sys.path 记录了Python解释器搜索模块的路径及其搜索顺序
  # 如顺序：python程序所在目录，当前目录，环境变量导入目录，pip的lib安装环境
  # 可灵活加入搜索路径，以此自定义模块搜索，此外，可通过外界export
  sys.path.append('/yourself_path/')
  ```

- 方法2：

  ```bash
  export PYTHONPATH=$PYTHONPATH:/mypath/
  # 此方法实际是在 sys.path的第三位添加
  ```

---
**编译模块**

```yml
pyc模块的编译 compile
              编译             解释执行
    mymod.py -----> mymod.pyc -------> python

过程会判断.py的时间是否比.pyc新
若是：重新编译；若否，跳过编译
```

---
**解释执行**

模块的加载过程:  
- 在模块导入时，模块的所有语句会执行，类似于python3调用该脚本
- 但如果一个模块在前面已经被导入，则再次导入时将不会再次导入执行模块内的语句


## 10.5. 模块的命名空间
### 10.5.1. 模块嵌套

嵌套自动导入

模块作用域嵌套

示例：

m3.py
```python
x = 3
print("m3 x=", x)
```
m4.py
```python
x = 4
import m3
print("m4 x=", x)
print("m4 m3.x=", x)
```
m5.py
```python
x = 5
import m4
print("m5 x=", x)
print("m5 m4.x=", m4.x)
print("m5 m4.m3.x=", m4.m3.x)
```
执行：
```python
>>> import m5
m 3x= 3
m 4x= 4
m4 m3.x= 3
m5 x= 5
m5 m4.x= 4
m5 m4.m3.x = 3
```

### 10.5.2. 定义导入私有数据
from-import导入语句可以管理导入的变量
- 当无__all__列表时，遵循私有变量导入规则
- 当有__all__列表时，则按__all__列表定义的来


#### 10.5.2.1. 私有变量
私有变量不被导入。

示例：

m1.py
```python
aaa = 1
_aaa = 1
__aaa__ = 1

bbb = 2
_bbb = 2
__bbb__ = 2
```

m2.py
```python
import m1
print(dir(m1))  # 导入全部
```

m3.py
```python
from m1 import *
print(dir())  # 只导入 aaa  bbb
```

---
手动定义导入列表

示例：

m1.py
```python
aaa = 1
_aaa = 1
__aaa__ = 1

bbb = 2
_bbb = 2
__bbb__ = 2

__all__ = ['aaa', '__bbb__']
```

m2.py
```python
from m1 import *
print(dir())  # 只导入 aaa  __bbb__
```

#### 10.5.2.2. `__all__`列表

模块中的`__all__`列表是一个用来存放可导出属性的字符串列表。  
注意：`__all__`列表 只对 `from import *` 语句起作用

模块的隐藏属性（模块中以'_'开头的属性）
- 在from xxx import *导入时将不被导入,通常称这些属性为隐藏属性
- 限定当用from xxx import *语句导入时，只导入`__all__`列表内的属性


- 在包里面__init__.py内的 `__all__` 列表
作用:
用来记录此包中有哪些包或模块需要在from import *语句导入时被导入

## 10.6. 模块的分类:
1. 内置模块(builtins) 在解析器的内部可以直接使用
2. 标准库模块,安装python时已安装具可直接使用
3. 第三方模块（通常为开源), 需要自己安装
4. 用户自己编定的模块(可以作为其它人的第三方模块)

### 10.6.1. 内建模块
什么是内建模块？
builtins是内建模块
Python启动时相当于执行`from builtins in *`，识别max，len，等

### 10.6.2. 自定义模块
#### 10.6.2.1. 模块中载入的变量作用范围

载入模块并不是将模块的内容直接替换到主模块，

global的全局变量作用域是在文件（模块）范围

示例：

pkg_var.py
```python
var = 100

def print_var():
    global var
    print('载入模块var:', var)

def set_var(n):
    global var

var = n
```

pkg_var_load.py
```python
from pkg_var import var

var = 200  # 赋值只能改变本模块内的全局变量
from mymod6 import print_var
print_var()  # 100
from mymod6 import set_var
set_var(300)
print_var()  # 300

print('主模块var:', var)  # 200
```

主模块运行结果
```
载入模块var: 100
载入模块var: 300
主模块var: 200
```

### 10.6.3. 一个示例搞定所有包导入知识点

---
示例：一个实例搞懂“`__init__`”、“`__all__`”、相对导入“`.`”

文件内容：


`demo_pkg/m5.py`：
```python
from .mm import main as mm_main
print('this is m4')
mm_main()	
demo_pkg/pdemo_pkg/__init__.py
print(__file__)	demo_pkg/pdemo_pkg/aa.py
print('this is aa')
```

`demo_pkg/pdemo_pkg/a1.py`：
```python
from ..pp1 import aa
# 相对导入上一级的目录下的pp1的aa
print('this is a1')	demo_pkg/pdemo_pkg/a2.py
from .. import mm
# 相对导入上一级包下的mm
print('this is a2')
```

`demo_pkg/pdemo_pkg/a3.py`
```python
from ...p1 import mm
# 测试导入主包边界之外的包，报错
print('this is a2')	
```

执行：
```python
# 1、在p1目录同级目录下（即p1外部），运行脚本或进入命令行窗口
>>> from p1 import *    # 使用__all__定义需要导入的模块
C:\Users\11701\Desktop\Pakage\p1\__init__.py
this is mm
this is m2
this is m3

>>> import p1.m1    # 包内不能直接导入
ModuleNotFoundError: No module named 'mm'

>>> import p1.m2
C:\Users\11701\Desktop\Pakage\p1\__init__.py
this is mm
this is m2

>>> import p1.m3
C:\Users\11701\Desktop\Pakage\p1\__init__.py
this is mm
this is m3

>>> import p1.m4
C:\Users\11701\Desktop\Pakage\p1\__init__.py
this is mm
this is m4

>>> import p1.m5
C:\Users\11701\Desktop\Pakage\p1\__init__.py
this is mm
this is m4
running p1.mm.main()

>>> p1.m4.mm_main()
running p1.mm.main()

>>> import p1.pp1.a1
C:\Users\11701\Desktop\Pakage\p1\__init__.py
C:\Users\11701\Desktop\Pakage\p1\pp1\__init__.py
this is aa
this is a1

>>> import p1.pp1.a2
C:\Users\11701\Desktop\Pakage\p1\__init__.py
C:\Users\11701\Desktop\Pakage\p1\pp1\__init__.py
this is aa
this is a2

>>> import p1.pp1.a3  # 超出主包外部，导入报错
ValueError: attempted relative import beyond top-level package
# 2.进入目录p1之后，运行命令行或脚本
>>> import m1  # 正常

>>> import 其他  # 报错

```


文件导入MD代码
```bash
find demo_Chapter10/demo.py demo_Chapter10/demo_pkg -type f|sort|grep -v pyc|while read x; do echo -e "\n\n---\n$x\n"'```python\n'"`cat $x`"'\n```'; done >>Chapter10.Modules.md
```

文件示例：



---
demo_Chapter10/demo.py
```python
print("
-----
包导入示例：")
print('+' * 20, __name__, '+' * 20)


print(":::", __name__, ": 1) demo_pkg 包整体导入")
S = set(dir()) | {"S"}
import demo_pkg.m1
print("demo_pkg 新增环境：", sorted(set(dir(demo_pkg)) - demo_pkg.vars))
print(":::", __name__, ": 1) 新增环境：", set(dir()) - S, '
')


print(":::", __name__, ": 2) demo_pkg 包通过 from * 导入")
S = set(dir()) | {"S"}
from demo_pkg import *
print(":::", __name__, ": 2) 新增环境：", set(dir()) - S, '
')


print(":::", __name__, ": 3) demo_pkg 包通过 from 导入 mm")
S = set(dir()) | {"S"}
from demo_pkg import mm
print(":::", __name__, ": 3) 新增环境：", set(dir()) - S, '
')
```


---
demo_Chapter10/demo_pkg/__init__.py
```python
"""此文档为__init__的初始化文档，限定__all__"""
print('+' * 20, __name__, '+' * 20)

vars = set(dir())

__all__ = ['m2']  # 定义__all__, 语句from p1 import *才能正常执行

a = 1
_a = 1
__a = 1
```


---
demo_Chapter10/demo_pkg/chl.py
```python
print('chl被导入')
```


---
demo_Chapter10/demo_pkg/m1.py
```python
"""Model m1."""
print('+' * 20, __name__, '+' * 20)


def main():
    print('[running] m1的main函数')
```


---
demo_Chapter10/demo_pkg/m2.py
```python
"""Model m2."""
print('+' * 20, __name__, '+' * 20)


def main():
    print('[running] m2的main函数')
```


---
demo_Chapter10/demo_pkg/mm.py
```python
"""Model mm. 此示例演示包的相对导入，演示`.`及`..`的作用"""
print('+' * 20, __name__, '+' * 20)


### 1) import写法，注意前面跟了包名
print('import demo_pkg.m1')
S = set(dir()) | {"S"}
import demo_pkg.m1
print("::: %s 新增环境：" % __name__, set(dir()) - S)
demo_pkg.m1.main()


### 2) from 包 import 模块 写法
S = set(dir()) | {"S"}
from demo_pkg import m1
print("::: %s 新增环境：" % __name__, set(dir()) - S)

S = set(dir()) | {"S"}
from . import m1
print("::: %s 新增环境：" % __name__, set(dir()) - S)

S = set(dir()) | {"S"}
from . import *
print("::: %s 新增环境：" % __name__, set(dir()) - S)


## 3) from 包 import 子包 写法
S = set(dir()) | {"S"}
from demo_pkg import pkg_children
print("::: %s 新增环境：" % __name__, set(dir()) - S)


def main():
    print('[mm:]', __doc__, __file__, __name__)


if __name__ == "__main__":
    print('mm当前为主模块')
else:
    print('mm当前为子模块')
```


---
demo_Chapter10/demo_pkg/pkg_children/__init__.py
```python
print('+' * 20, __name__, '+' * 20)

__all__ = ['aa']

from . import aa
```


---
demo_Chapter10/demo_pkg/pkg_children/aa.py
```python
print('+' * 20, __name__, '+' * 20)
print('___________________ [ demo_pkg.pkg_children ] ___________________')

print("1) 相对导入上一级包下的chl")
from .. import mm
import demo_pkg.chl

print("2) 相对导入上一级的目录下的mm模块的main函数")
from ..m2 import main
main()

print('___________________ [ demo_pkg.pkg_children ] ___________________')

# 相对路径注意事项
### 不可用于import语句，否则触发 SyntaxError: invalid syntax
# import .mm
# import ..mm
### 不可导入包之外，否则触发 ValueError: attempted relative import beyond top-level package
# from ..demo01 import *
```



<!-- [./Chapter10.Modules2.md](./Chapter10.Modules2.md ':include:') -->

## 10.7. 常用模块
### 10.7.1. sys模块
——系统模块
此模块都是运行时系统的信息，与系统相关的信息
#### 10.7.1.1. sys模块的方法

| 变量                     | 返回   | 描述                                                                               |
|--------------------------|--------|------------------------------------------------------------------------------------|
| sys.path                 | 列表   | 返回路径的列表，模块搜索路径 path[0] 是当前脚本程序的路径名，否则为 ''             |
| sys.modules              | 字典   | 已加载模块的字典                                                                   |
| sys.version              | 字符串 | 版本信息字符串                                                                     |
| sys.version_info         | 元组   | 版本信息的命名元组                                                                 |
| sys.platform             | 字符串 | 操作系统平台名称信息                                                               |
| sys.argv                 | 列表   | 返回关于当前路径的列表。命令行参数 argv[0] 代表当前脚本程序路径名:[路径,数值,数值] |
| sys.copyright            | 字符串 | 获得Python版权相关的信息                                                           |
| sys.builtin_module_names | 元组   | 获得Python内建模块的名称（字符串元组）                                             |
| 标准输入输出时会用到     |        |                                                                                    |
| sys.stdin                | 【？】 | 标准输入文件对象，多用于input()                                                    |
| sys.stdout               |        | 标准输出文件对象,多用于print()                                                     |
| sys.stderr               |        | 标准错误输出文件对象, 用于输出错误信息                                             |


sys模块的方法

| 函数名                   | 返回   | 描述                                                                      |
|--------------------------|--------|---------------------------------------------------------------------------|
| sys.exit([arg])          |        | 退出程序，正常退出时sys.exit(0)，args可以是任意字符串(返回1)或0-127的整数 |
| sys.getrecursionlimit()  | 整型数 | 得到递归嵌套层次限制（栈的深度）                                          |
| sys.setrecursionlimit(n) | None   | 得到和修改递归嵌套层次限制（栈的深度）                                    |


#### 10.7.1.2. 应用

---
sys.version检测程序是否是在python3环境下运行：
```python
import sys
print("i'm in python%s" % sys.version[0])
print("当前程序正运行在:", sys.platform, '上')
if sys.version_info[0] < 3:
    print("can not run in python2")
    sys.exit(0)  # exit programe
    print("-------------------")

print("programe running normally")
"""
i'm in python3
当前程序正运行在: win32 上
programe running normally
"""
```

---
sys.argv从Linux命令窗口传入参数
文件：test.py
```python
import sys
print(sys.argv)
```
命令行输入运行：
```bash
$ python3 get_sys.py 1 2 3
['get_sys.py', '1', '2', '3']
$ python3 get_sys.py
['get_sys.py']
```

---
捕获标准输入函数的末尾换行符
输出函数
等价情况：

```python
print('hello')
sys.stdout.write('hello' + '\n')
```

输入函数
sys.stdin.readline( )会将标准输入全部获取，包括末尾的'\n'，不同于input自动去掉末尾'\n'
等价情况：
```python
input( )
sys.stdin.readline( )[:-1]
sys.stdin.readline( ).strip('\n')
```

---
解决python2里面的编码问题
```python
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 8: ordinal not in range(128)
if sys.version[0] == '2':
    import sys
    reload(sys)
sys.setdefaultencoding('gb18030')
```
```python
导入其他路径下的模块：
sys.path.append('/xxx/tools')
import xxxxx
```

### 10.7.2. os模块
——系统模块
import os

#### 10.7.2.1. 常用属性

```python
os.sep	   # 返回当前使用系统的分隔符 (windows '\';linux '/')
os.linesep # 返回当前使用系统的换行符 (windows '\r\n';linux '\n')
os.path    # 返回模块搜索的路径
os.pardir  # 返回当前目录的父目录代表字符串('..')
os.curdir  # 返回当前目录代表的字符串(为'.') 
```

#### 10.7.2.2. 路径操作
```python
# 目录创建
os.mkdir('./cache')  # 当文件夹存在时抛出异常退出
os.makedirs('./test/cache', exist_ok=True)  # 可创建多层递归目录，当文件夹存在时自动跳过创建不报错

# 目录及文件删除
os.remove("./test.txt")  # 删除文件test.txt
os.removedirs("./a/b/c") # 递归向上一级删除空目录，如c为空则删除c，再判断b,a
os.rmdir(path)  # path是文件夹路径，注意文件夹需要时空的才能被删除

# 目录切换
os.chdir('/home/test')   #切换当前工作路径(切换到'/home/test'路径下)


# 目录文件列表获取
os.listdir('./')  #列表形式列出指定目录下的所有文件和文件夹的名称
os.walk('./')     #列表形式列出指定目录下的所有目录以及其子文件夹文件

# 文件(夹)重命名
os.rename("oldname","new")  # 重命名文件/目录

# 返回文件或目录的相关路径
os.getcwd()  #返回当前工作目录绝对路径
os.path.abspath('./test.txt') # 返回给定路径绝对路径：'/home/test/test.file'
os.path.basename('./asdf/asdf/test.txt')  # 返回文件文件名：'test.txt' 
os.path.dirname('./a/b/test.txt') # 返回文件父文件夹路径：'./a/b'

# 返回文件路径前缀和后缀组成的二元元组
os.path.splitext('01.tonglu.py')        # ('01.tonglu', '.py')
os.path.splitext('./a/b/01.tonglu.py')  # ('./a/b/01.tonglu', '.py')

# 路径判断
os.path.isdir('/home/test')  #判断路径是否为文件夹，返回布尔值
os.path.isfile('/home/test')  #判断路径是否为文件，返回布尔值
os.path.exists('/home/test.txt') #判断路径或文件是否存在，返回布尔值

# 路径拼接
os.path.join('a','aa','aaa')   #得到'a/aa/aaa'
```

示例：
```python
# 检测输出文件夹是否存在，若不存在则创建文件夹
def mkdir(dirpath):
    isExists = os.path.exists(dirpath)
    if not isExists:
        os.makedirs(dirpath)
mkpath = "WGCNA_Module_Gene_ID--goseq"  # 输出文件夹
mkdir(dirpath)

# 以上内容可用另一个函数代替：os.makedirs
os.makedirs(dirpath, exist_ok=True)
```

生成当前文件夹所有文件的总列表
```python
['%s/%s'%(a,file) for a,b,c in os.walk("Report") for file in c]
```

#### 10.7.2.3. 执行shell命令
```python
os.system()   #执行Linux语句，返回执行执行脚本的最后一句执行状态，成功返回0
os.popen().read()  #执行Linux语句，返回语句的标准输出结果
```

其他方法：subprocess模块
```python
import subprocess
p = subprocess.Popen(
        "ls / test_zxcv.txt",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
output, err = p.communicate()
p_status = p.wait()
print(output, err, p_status, sep='\n')
```

示例：
摘自： bin/encode_lib_common.py （encode-chip-seq-pipeline）

```python
import os
import subprocess
import logging as log

def run_shell_cmd(cmd):
    p = subprocess.Popen(
        ['/bin/bash', '-o', 'pipefail'],  # to catch error in pipe
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        preexec_fn=os.setsid)  # to make a new process with a new PGID
    pid = p.pid
    pgid = os.getpgid(pid)
    log.info('run_shell_cmd: PID={}, PGID={}, CMD={}'.format(pid, pgid, cmd))
    stdout, stderr = p.communicate(cmd)
    rc = p.returncode
    err_str = 'PID={}, PGID={}, RC={}\nSTDERR={}\nSTDOUT={}'.format(
        pid, pgid, rc, stderr.strip(), stdout.strip())
    if rc:
        # kill all child processes
        try:
            os.killpg(pgid, signal.SIGKILL)
        except:
            pass
        finally:
            raise Exception(err_str)
    else:
        log.info(err_str)
    return stdout.strip('\n')

run_shell_cmd('ls')
```

#### 10.7.2.4. 进程操作

```python
os.getpid()  # 获取当前进程PID
os._exit([status]) #
```

- 退出程序中os._exit()和sys.exit()的区别？
  1. os._exit()直接退出
  2. sys.exit()是触发系统异常，可以被捕获

示例：
脚本

```python
import os,sys 
# os._exit(1)
try:
    sys.exit("进程退出")
except SystemExit as e:
    print(e)

print("Process exit")
```
运行结果：
```
进程退出
Process exit
```

### 10.7.3. random随机模块
- 说明：
random模块是用于模拟或生成随机输出的模块.

import random as R

| 函数名                             | 返回         | 描述                                                                |
|------------------------------------|--------------|---------------------------------------------------------------------|
| R.random()                         | 浮点数       | 返回一个[0, 1) 之间的随机实数                                       |
| R.uniform(a,b)                     | 浮点数       | 返回[a,b) 区间内的随机实数                                          |
| R.randrange([start,] stop[, step]) | 整型数       | 返回range(start,stop,step)中的随机数                                |
| R.randint(a,b)                     | 整型数       | 返回[a,b]范围内的随机数                                             |
| R.choice(seq)                      | 原始元素对象 | 从序列中返回随意元素                                                |
| R.shuffle(seq[, random])           | None         | 随机指定序列(主要用于列表)的顺序(乱序序列）。一般讲原始有序列表打乱 |
| R.sample(seq,n)                    | 列表         | 从序列中选择n个随机且不重复的元素                                   |
| R.getrandbits(nbit)                |              | 以长整型的形式返回用nbit位来表示的随机数                            |
| R.seed(a=None)                     |              | 用给定的数a设置随机种子,不给参数a则用当前时间设置随机种子           |


示例：
```python
import random as R
R.random()      #浮点数，返回一个[0, 1) 之间的随机实数
R.uniform(0,1)  #浮点数，返回[a,b) 区间内的随机实数

R.randrange(0, 10, 1)  #整型数，返回range(start,stop,step)中的随机数
R.randint(0, 1)  #整型数，返回[a,b]范围内的随机数，此处随机生成0或1

R.choice('abcde')  #原始元素对象，从序列中返回随意元素

a = list('abcde')
R.shuffle(a)  #None，随机指定序列(主要用于列表)的顺序(乱序序列）。一般讲原始有序列表打乱
a

R.sample('abcde', 3)  # 列表，从序列中选择n个随机且不重复的元素
R.getrandbits(8)   #，以长整型的形式返回用nbit位来表示的随机数

for i in range(5): # 测试5次设置相同随机种子后的随机数结果
    R.seed(a=1)  #，用给定的数a设置随机种子,不给参数a则用当前时间设置随机种子
    print([R.randint(0,100) for x in range(10)])
```

练习:
```
  猜数字游戏:
    随机生成一个0~100的整数,用变量x绑定
    让用户输入一个数y,输出猜数字的结果.
       1) 如果y等于x,则提示"恭喜您猜对了!", 退出程序
       2) 如果y大于x,同提示"您猜大了"
       3) 如果y小于x,同提示"您猜小了"
      让用户循环输入，直到猜对为止，同时显示用户猜数字的次数后退出程序
```


### 10.7.4. math数学模块
文档参见:
python_base_docs_html/数学模块math.html
- 数学模块 math  
模块名: math

- 注：  
linux下为内建模块  
Mac OS下为标准库模块

- 数学模块用法：  
import math  
或  
from math import *

常用属性

| 属性    | 描述          |
|---------|---------------|
| math.e  | 自然对数的底e |
| math.pi | 圆周率pi      |


常用函数

| 函数名              | 描述                                                    |
|---------------------|---------------------------------------------------------|
| math.ceil(x)        | 对x向上取整，比如x=1.2，返回2                           |
| math.floor(x)       | 对x向下取整，比如x=1.2，返回1                           |
| math.sqrt(x)        | 返回x的平方根                                           |
| math.factorial(x)   | 求x的阶乘                                               |
| math.log(x[, base]) | 返回以base为底x的对数, 如果不给出base,则以自然对数e为底 |
| math.log10(x)       | 求以10为底x的对数                                       |
| math.pow(x, y)      | 返回 x**y (x的y次方)                                    |
| math.fabs(x)        | 返回浮点数x的绝对值                                     |


角度和弧度degrees互换

| 函数名          | 描述              |
|-----------------|-------------------|
| math.degree(x)  | 将弧度x转换为角度 |
| math.radians(x) | 将角度x转换为弧度 |


三角函数	

| 函数名       | 描述                          |
|--------------|-------------------------------|
| math.sin(x)  | 返回x的正弦(x为弧度)          |
| math.cos(x)  | 返回x的余弦(x为弧度)          |
| math.tan(x)  | 返回x的正切(x为弧度)          |
| math.asin(x) | 返回x的反正弦(返回值为为弧度) |
| math.acos(x) | 返回x的反余弦(返回值为为弧度) |
| math.atan(x) | 返回x的反正切(返回值为为弧度) |


### 10.7.5. time时间模块

PC时间简介：
- 公元纪年是从公元 0000年1月1日0时开始的
- 计算机元年是从1970年1月1日0时开始的,此时时间为0,之后每过一秒时间+1
  - UTC 时间 (Coordinated Universal Time) 是从Greenwich时间开始计算的.
  - UTC 时间不会因时区问题而产生错误
  - DST 阳光节约时间(Daylight Saving Time)，又称夏令时, 是一个经过日照时间修正后的时间

模块时间时间元组：
- 时间元组是一个9个整型元素组成的，这九个元素自前至后依次为:
  - 四位的年(如: 1993)
  - 月 (1-12)
  - 日 (1-31)
  - 时 (0-23)
  - 分 (0-59)
  - 秒 (0-59)
  - 星期几 (0-6, 周一是 0)
  - 元旦开始日 (1-366)
  - 夏令时修正时间 (-1, 0 or 1).
注：如果年份值小于100,则会自动转换为加上1900后的值


#### 10.7.5.1. 模块内容
模块名: time
此模块提供了时间相关的函数，且一直可用
- 时间模块导入：
```python
import time   # 或
from time import xxx   # 或
from time import *
```

##### 10.7.5.1.1. 变量

| 变量          | 描述                                                 |
|---------------|------------------------------------------------------|
| time.altzone  | 夏令时时间与UTC时间差(秒为单位)                      |
| time.daylight | 夏令时校正时间                                       |
| time.timezone | 本地区时间与UTC时间差(秒为单位)                      |
| time.tzname   | 时区名字的元组， 第一个名字为未经夏令时修正的时区名, 第一个名字为经夏令时修正后的时区名

注：CST为中国标准时间(China Standard Time UTC+8:00)



#### 10.7.5.2. 应用
实例1：
格式化输出日期
```python
import time

T1 = time.localtime()  # time.struct_time(...)
# 格式化输出字符串，及从字符串格式化读入
Ts = time.strftime("%Y-%m-%d %H:%M:%S", T1)  # '2018-9-23 18:45:23'
T2 = time.strptime(Ts, "%Y-%m-%d %H:%M:%S")
print(T1 == T1, Ts)
```


#### 10.7.5.3. 实例练习

- 写一个程序，输入您的出生日期
  1. 算出你已经出生多少天?
  2. 算出你出生的那天是星期几

- 写一个程序，以电子时间格式显示时间: HH:MM:SS (要求：不停显示当前时间即可)

- 编写一个闹钟程序，启动时设置定时时间，到时间后打印"时间到" 然后退出

- 编写函数fun,其功能是求下列多项式的和:  
    Sn = 1 + 1/1! + 1/2! + 1/3! + 1/4! +...+ 1/n!  
    建议用数学模块中的math.factorial来求  
    当n为50时，Sn的值  


#### 10.7.5.4. 扩展：使用datetime模块格式化间隔时间

```python
import datetime
import time

time_start = datetime.datetime.now()
time.sleep(1)
time_spend = datetime.datetime.now() - time_start
print('耗时:', time_spend)  # 耗时: 0:00:01.003083
```


### 10.7.6. string字符串模块
python string模块

```python
>>> import string

>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase  小写字母
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase  大写字母
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits  数字
'0123456789'
>>> set(string.digits) 集合
{'0', '7', '3', '9', '2', '1', '8', '4', '6', '5'}
>>> string.hexdigits  16进制
'0123456789abcdefABCDEF'
>>> string.octdigits  8进制
'01234567'
>>> string.punctuation 符号
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.printable 
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
>>> string.whitespace 空白符
' \t\n\r\x0b\x0c'
```

- 应用： 生成正则字符串

```python
>>> string.digits
'0123456789'
>>> type(string.digits)
<class 'str'>

# 特殊联用：
>>> t = "1231asdfa123123"
>>> t.lstrip(string.digits)   #去除字符串数字开头的数字
'asdfa123123'
>>> t.lstrip("0123456789")
'asdfa123123'
```

---

- str.split()默认参数小知识

括号中的默认分隔符：
string.whitespace
既：空格，换行符，回车符，垂直制表符，换页符。
并且多个连续的whitespace视为单个分隔符。
```python
>>> help(str.split) # 查看帮助文档, 注意关键词whitespace
>>> import string
>>> string.whitespace
' \t\n\r\x0b\x0c'

>>> 'a\t\t   \tb\n\n c'.split()
['a', 'b', 'c']
>>> 'a\t\t   \tb\n\n c'.split("\t")
['a', '', '   ', 'b\n\n c']
```


六个“空字符”：

| ASCII码 | 字符表示 | 显示 | 描述 |
| - |-|-|-|
| 9 | `\t` | 无 | HT，horizontal tab，水平制表符 |
| 10 | `\n` | 空一行 | LF，line feed，换行 |
| 11 | `\x0b`（十六进制） | □ | VT， |vertical tab，垂直制表符
| 12 | `\x0c`（十六进制） | ￪ | FF，form feed，换 |页
| 13 | `\r` | 无 | CR，carriage return，回车 |
| 32 | `\x20`（十六进制） | 无 | space，空格 |


### 10.7.7. shutil文件操作

Python中复制文件：

```python
import shutil
shutil.copyfile(fileold, filenew)
```

### 10.7.8. pprint规则打印结构数据
自动将无序结构排序，并结构化打印。
示例：
```python
import pprint

D = {
    'a': {'aa': 1, 'bb': 2},
    'a1': {'aa': 1, 'bb': 2, 'c': 3},
    'a2': {'aa': 1, 'bb': 2},
    'a3': {'aa': 1, 'bb': 2, 'c': 3,
           'd': {'bb': 2, 'bbb': {'bb': 2, 'bbb': {'bb': 2, 'bbb': 3}}}},
    'b': {'bb': 2, 'bbb': 3}
}
pprint.pprint(D)
```

结果
```
{'a': {'aa': 1, 'bb': 2},
 'a1': {'aa': 1, 'bb': 2, 'c': 3},
 'a2': {'aa': 1, 'bb': 2},
 'a3': {'aa': 1,
        'bb': 2,
        'c': 3,
        'd': {'bb': 2, 'bbb': {'bb': 2, 'bbb': {'bb': 2, 'bbb': 3}}}},
 'b': {'bb': 2, 'bbb': 3}}
```

### 10.7.9. argparse解析参数

#### 10.7.9.1. 常规用法

**创建对象** `parser = argparse.ArgumentParser()`
```python
import argparse
parser = argparse.ArgumentParser(
            description='Process some integers.')
```

**添加参数** `parser.add_argument()`  

可用选项, `add_argument()`常用的参数：

```python
default     Value：设置参数的默认值
type        str: 'int'/'str'/...，把从命令行输入的结果转成设置的类型
nargs       int/'?'/'*'/'+'：定义数量, ?代表0-n个参数，当为0从default取值
dest        var：设置变量，提供例如dest="a"，那么可以通过args.a访问该参
required    bool：如 required=True 表示强制该参数必须提供。
metavar     str：定义帮助文档显示的输入类型
help        str：自定义帮助文档的字符串

action      action = 'action'：参数触发的动作，6种动作：
    'store'    保存参数，默认
    'store_ture'/'store_false'：保存相应的布尔值，
            如'store_true'：当该参数存在时为Ture，默认为False
            如'store_false'：当该参数存在时为False，默认为True
    'store_const'：保存一个被定义为参数规格一部分的值（常量），而不是一个来自参数解析而来的值。
    'append'：将值保存在一个列表中。
    'append_const'：将一个定义在参数规格中的值（常量）保存在一个列表中。

count       参数出现的次数

choices      list：限定允许输入的参数值，如[0,1,2,3]

version     打印程序版本信息
```

参考：[(转) argparse — 解析命令参数和选项 - liujiacai - 博客园](https://www.cnblogs.com/liujiacai/p/9890495.html)

**获取参数值**
```python
args = parser.parse_args()  # 获取所有
argv = vars(parser.parse_args())
Largs = [args.file_sh, args.line, args.thread]  # 手动获取部分
```

#### 10.7.9.2. 互斥参数（互斥选项）

（来源：百度keyword: `argparse 互斥`）

定义互斥的选项是选项分组特性的一个特例，使用add_mutually_exclusive_group()而不是add_argument_group()。

argparse会为你强制执行互斥性，因此一次使用仅能给出该群组的选项中的一个。

```python
import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action="store_true")

print(parser.parse_args())
```


#### 子程序

```python
import argparse

subparsers = parser.add_subparsers(title='subcommands',
                                    description='valid subcommands',
                                    help='additional help'
                                    )

view = subparsers.add_parser('view', help='用于打印所有的 job name')
view.add_argument('fipath', type=str,
                    help=('输入需要操作的sjm语法文件'))
view.add_argument('-k', '--keyword', type=str, default=False,
                    help=('输入想要提取的关键词，如：... '))

split = subparsers.add_parser('split', help='用于打印所有的 job name')
split.add_argument('fipath', type=str,
                    help=('输入需要操作的sjm语法文件'))
split.add_argument('-k', '--keyword', type=str, default=False,
                    help=('输入想要提取的关键词，如：... '))
```


#### 10.7.9.3. 框架1：万能

```python
import sys
import argparse


def fargv():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('用自定义的替换列表, '
                     '替换原文件中某一列的旧名字为新名字（并输出未替换成功的行信息）'),
        epilog=('注意事项：\n'
                '    None\n'
                '当前版本：\n'
                '  v1.6 修复xxx的问题\n'
                '历史版本：\n'
                '  v1.0 初始版本，实现提取功能，添加为-k参数\n'
                ))
    parser.add_argument('-i', '--inputfile', type=str, required=True,
                        help=('输入文件'))
    parser.add_argument('-o', '--outfile', type=str, required=True, default=False,
                        help=('输出文件'))
    parser.add_argument('--keep', action='store_true',
                        help='是否怎样怎样')
    # 参数组，只能选择其中一个
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m1', help=('模式1'))
    group.add_argument('-m2', help=('模式2'))
    group.add_argument('-m3', help=('模式3'))
    args = parser.parse_args()
    return args.__dict__

def fmain(**args):
    pass


def main():
    # sys.argv = '1 -l listfile -i file -n 1,2'.split()
    sys.argv = ['', '-h']
    args = fargv()
    print(*list(args.keys()), sep=", ")
    print(*list(args.values()), sep=", ")
    # fmain(**args)


if __name__ == '__main__':
    main()
```

#### 10.7.9.4. 框架2：简易
```python
import sys
import argparse


def fargv():
    parser = argparse.ArgumentParser(description='Process introduction.')
    parser.add_argument('prjlist', type=str,
                        help='输入需要运行的prjlist')
    parser.add_argument('dnums', type=str, 
                        help='输入需要运行的dnums，如0216,1908,1919,1920')
    parser.add_argument('-w', '--win', type=int,
                        help='-w/-win的使用帮助')
    parser.add_argument('-t', '--thread', type=int,
                        help='-t/--thread的帮助')
    parser.add_argument('-k', '--iskeep', action='store_true', 
                        default=False,
                        help='是否怎样怎样')
    args = parser.parse_args()
    return args.__dict__


def fmain(kwargs):
    pass


def main():
    sys.argv = ['', 'file', 'file2']
    kwargs = fargv()
    # print(kwargs)
    # print(*list(kwargs.keys()),sep=", ")
    fmain(**kwargs)

if __name__ == '__main__':
    main()
```


#### 10.7.9.6. 框架3：加入子程序控制
```python
import sys
import argparse


def fargv():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('本程序用于处理sjm语法文件'
                     '版本简介：\n'
                     '    v1.0 初始版本'),
        epilog=('注意事项：\n'
                '    None'
                ))

    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='additional help'
                                       )

    view = subparsers.add_parser('view', help='用于打印所有的 job name')
    view.add_argument('fipath', type=str,
                      help=('输入需要操作的sjm语法文件'))
    view.add_argument('-k', '--keyword', type=str, default=False,
                       help=('输入想要提取的关键词，如：... '))

    split = subparsers.add_parser('split', help='用于打印所有的 job name')
    split.add_argument('fipath', type=str,
                       help=('输入需要操作的sjm语法文件'))
    split.add_argument('-k', '--keyword', type=str, default=False,
                       help=('输入想要提取的关键词，如：... '))
    # parser.add_argument('-pp', '--prjpath', type=str, default=False,
    #                     help=('输入手动定义指定文件夹路径的所属项目的文件'))
    # parser.add_argument('-d', '--dirnums', type=str, default="1,2,3,4,5",
    #                     help='输入想统计的几级目录，如：3,4,5,6')
    # parser.add_argument('-k', '--iskeep', action='store_true',
    #                     default=False,
    #                     help='是否怎样怎样')
    args = parser.parse_args()
    # print(args.__dict__)
    return args.__dict__


def fmain(fipath, keyword):
    print(fipath, keyword)


def main():
    sys.argv = ['', '-h']    # print(fargv())
    sys.argv = ['', 'view', '-h']
    sys.argv = ['', 'split', '-h']
    # sys.argv = ['', 'view', './s2-2.job']
    # print(fargv())

    args = fargv()
    # print(*list(args.keys()),sep=", ")
    fmain(**args)


if __name__ == '__main__':
    main()
```

#### 10.7.9.7. 示例：接受多个参数

```python
import argparse

def fargv():
    parser = argparse.ArgumentParser(description='merge.')
    parser.add_argument('-i', '--input', type=str, nargs='*',
                        help='输出文件名字')
    parser.add_argument('-o', '--out', type=str,
                        help='输出文件名字')
    args = parser.parse_args()
    return args.input, args.out


def fmain(finames, foname):
    print(finames, foname)
    # Lopen = [gzip.open(x) for x in finames]


def main():
    sys.argv = ['', '-i', 'a', 'b', 'c', '-o', 'a']
    fi, fo = fargv()
    fmain(fi, fo)


if __name__ == '__main__':
    main()
```

### 10.7.10. logging日志调试模块

logging 打印输出

```python
import logging
log_format='%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
```
输出
2019-11-07 09:26:04,438 - DEBUG: debug
2019-11-07 09:26:04,438 - INFO: info
2019-11-07 09:26:04,438 - WARNING: warning
2019-11-07 09:26:04,438 - ERROR: error

### pickle环境保存

```python
import pickle
a, b = 1, 3
pickle.dump((a, b), open("test.pydb", "wb"))
aa, bb = pickle.load(open("test.pydb", "rb"))
print(a, b, aa, bb)
```

## 10.8. 第三方包

### 10.8.1. 安装及管理

安装
```python
pip3 install -i  https://pypi.tuna.tsinghua.edu.cn/simple/ django
```

查看Python已经安装包名称已经版本号的两个命令：

```bash
pip list
pip freeze
# 或
python -m pip list
python -m pip freeze
```

python环境的迁移
```bash
pip freeze >requirements.txt
pip install -r requirements.txt
```


### 10.8.2. 进度条打印功能增强模块

- 显示进度条模块
tqdm是python中很常用的模块，它的作用就是在终端上出现一个进度条，使得代码进度可视化。

```python
# 1.使用tpdm显示进度条
from tqdm import tqdm,trange
for i in tqdm(range(10000)):
    sleep(0.01)
for i in trange(100):
    sleep(0.1)
```

### 10.8.3. 存储变量的模块
- 提升读取速度的模块
pickle 将python数据类型存储为二进制文件，【二进制读取速度是文本方式的几十倍？】



