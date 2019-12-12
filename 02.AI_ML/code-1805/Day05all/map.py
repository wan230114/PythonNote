# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def f1(x):
    return x + 3


a = 1
b = f1(a)
print(b)
A = [1, 2, 3]
'''
B = []
for x in A:
    B.append(f1(x))
'''
B = list(map(f1, A))
print(B)
C = list(map(lambda x: x + 3, A))
print(C)
