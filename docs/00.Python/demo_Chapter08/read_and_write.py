#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-01-06, 21:14:22
# @ Modified By: Chen Jun
# @ Last Modified: 2021-01-19, 23:28:36
#############################################

# %%

with open("a.txt", "w") as fo:
    fo.write("aaa")

print("---")
with open("a.txt", "r+") as fi:
    print(fi.read())
    fi.write("bbb")

print("---")
with open("a.txt", "r+") as fi:
    fi.write("ccc")

print("---")
with open("a.txt", "r+") as fi:
    print(fi.read())
