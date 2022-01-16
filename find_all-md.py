#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-12-22, 22:26:07
# @ Modified By: Chen Jun
# @ Last Modified: 2021-12-22, 23:11:37
#############################################

# %%

import os
import re

L_res = []
for p, ds, fs in os.walk("."):
    for f in fs:
        if f.endswith(".md"):
            # print(p, ds, f)
            L_res.append(os.path.join(p, f))

L_res.sort()
# %%

# L_gt50 = []
L_gt10 = []
L_lt10 = []
with open("all-md.md", "w") as fo:
    for i, x in enumerate(L_res, start=1):
        with open(x) as fi:
            LEN = len(re.compile("\n").findall(fi.read()))
            # if LEN > 50:
            #     L_gt50.append(x)
            if LEN > 10:
                L_gt10.append(x)
            else:
                L_lt10.append(x)
    # print("\n\n---\n`> 50`:\n\n", file=fo)
    # for i, x in enumerate(L_gt50, start=1):
    #     print(f"- {i}. [`{x}`]({x})", file=fo)
    print("\n\n---\n`> 10`:\n\n", file=fo)
    for i, x in enumerate(L_gt10, start=1):
        print(f"- {i}. [`{x}`]({x})", file=fo)
    print("\n\n---\n`< 10`:\n\n", file=fo)
    for i, x in enumerate(L_lt10, start=1):
        print(f"- {i}. [`{x}`]({x})", file=fo)
