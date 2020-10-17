"""此文档为__init__的初始化文档，限定__all__"""
print('+' * 20, __name__, '+' * 20)

vars = set(dir())

__all__ = ['m2']  # 定义__all__, 语句from p1 import *才能正常执行

a = 1
_a = 1
__a = 1
