# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import functools


def f1(x):
    return x + 3


def f2(x):
    return x * 6


def f3(x):
    return x - 9


def fc(*fs):
    return functools.reduce(
        lambda fa, fb: lambda x: fa(fb(x)), *fs)

a = 1
b = f3(f2(f1(a)))
print(b)
c = functools.reduce(
    lambda fa, fb: lambda x: fa(fb(x)), [f3, f2, f1])(a)
print(c)
d = fc([f3, f2, f1])(a)
print(d)
