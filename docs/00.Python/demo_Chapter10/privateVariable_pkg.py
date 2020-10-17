"""
“私有变量”及“__all__列表”说明：
    `from privateVariable_pkg import *` 语句将只能自动导入aaa和bbb
    `__all__` 列表可以不论是否私有，都可自定义指定
"""
print('子模块中：', dir())
aaa = 1
_aaa = 1
__aaa = 1
__aaa__ = 1
bbb = 2
_bbb = 2
__bbb = 2
__bbb__ = 2
print('子模块中：', dir())
__all__ = ['__aaa', '__bbb']  # 手动指定要导入的模块
