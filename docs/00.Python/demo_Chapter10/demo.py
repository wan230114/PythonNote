print("\n-----\n包导入示例：")
print('+' * 20, __name__, '+' * 20)


print(":::", __name__, ": 1) demo_pkg 包整体导入")
S = set(dir()) | {"S"}
import demo_pkg.m1
print("demo_pkg 新增环境：", sorted(set(dir(demo_pkg)) - demo_pkg.vars))
print(":::", __name__, ": 1) 新增环境：", set(dir()) - S, '\n')


print(":::", __name__, ": 2) demo_pkg 包通过 from * 导入")
S = set(dir()) | {"S"}
from demo_pkg import *
print(":::", __name__, ": 2) 新增环境：", set(dir()) - S, '\n')


print(":::", __name__, ": 3) demo_pkg 包通过 from 导入 mm")
S = set(dir()) | {"S"}
from demo_pkg import mm
print(":::", __name__, ": 3) 新增环境：", set(dir()) - S, '\n')
