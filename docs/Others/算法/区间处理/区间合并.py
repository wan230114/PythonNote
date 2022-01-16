#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-05-07, 23:47:56
# @ Modified By: Chen Jun
# @ Last Modified: 2021-09-01, 12:13:56
#############################################

# 合并区间，并告知合并使用的Index有哪些

def merge_intervals(intervals):
    result = {}
    Index = list(intervals.keys())
    (start_candidate, stop_candidate) = intervals[Index[0]]
    L_tmp_Index = [Index[0]]
    for k in Index[1:]:
        start, stop = intervals[k]
        if start <= stop_candidate:
            stop_candidate = max(stop, stop_candidate)
            L_tmp_Index.append(k)
        else:
            result[(start_candidate, stop_candidate)] = L_tmp_Index
            (start_candidate, stop_candidate) = (start, stop)
            L_tmp_Index = [k]
    result[(start_candidate, stop_candidate)] = L_tmp_Index
    return result


intervals = [
    (5, 10), (8, 12), (11, 14), (13, 20),
    (22, 25), (24, 30),
    (33, 37), (36, 40),
]
intervals = dict(enumerate(intervals, start=0))
print(merge_intervals(intervals))
