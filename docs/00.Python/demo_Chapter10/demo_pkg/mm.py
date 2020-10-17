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
