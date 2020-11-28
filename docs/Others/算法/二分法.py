#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2020-11-04, 10:46:18
# @ Modified By: Chen Jun
# @ Last Modified: 2020-11-07, 18:02:04
#############################################

"""
二分法示例
"""


def do(START, INDATA):
    LEN_INDATA = len(INDATA) - 1
    s, e = 0, LEN_INDATA  # 定义位置坐标
    while True:
        # 1) 二分
        n = int((e - s)/2)
        n = 1 if not n else n  # 处理最后一次整形为零无法归位问题
        # 2) 判断并重新分配坐标
        if START < INDATA[s+n]:
            e = e - n
        else:
            s = s + n
        # 3）判断退出条件
        if s == e or INDATA[s] == START or INDATA[e] == START:
            break
    return INDATA[s]


if __name__ == "__main__":
    print(do(START=5, INDATA=[10, 20, 30, 40, 50]))
    print(do(START=20, INDATA=[10, 20, 30, 40, 50]))
    print(do(START=29, INDATA=[10, 20, 30, 40, 50]))
    print(do(START=100, INDATA=[10, 20, 30, 40, 50]))
