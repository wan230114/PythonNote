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
