#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-07-15, 11:23:44
# @ Modified By: Chen Jun  
# @ Last Modified: 2021-07-30, 16:33:53  
#############################################

# %%
import numpy as np
import pandas as pd


def compress(df, names):
    L = []
    for k, x in df.groupby(names):
        L.append([x[xx].drop_duplicates().to_list()
                  for xx in x.columns])
    df = pd.DataFrame(L, columns=df.columns)
    for name in names:
        df[name] = df[name].map(lambda x: x[0])
    return df


df = pd.DataFrame(
    [["a1", "A", 1],
        ["a2", "B1", 1],
        ["a2", "B2", 2],
        ["a3", "C1", 1],
        ["a3", "C2", 2],
        ["a3", "C2", 3],
     ], columns=["name", "type", "value"]
)

names = ["name"]

df2 = compress(df, names)
print(df2)

print(df.explode(names[0]))

# %%


def decompression(df, names):
    df = df.copy()
    df[names] = df[names].applymap(lambda x: x.split(","))
    for name in names:
        df = df.explode(name)
    return df


df3 = decompression(df2, ["type", "value"])

print(df, end="\n\n")
print(df2, end="\n\n")
print(df3, end="\n\n")
