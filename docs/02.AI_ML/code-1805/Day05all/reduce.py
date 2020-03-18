# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import functools


def f1(x, y):
    return x + y


A = [2, 3, 4]
print(functools.reduce(f1, A))
print(functools.reduce(lambda x, y: x * y, A))
