#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun  
# @ Author Email: 1170101471@qq.com  
# @ Created Date: 2021-07-30, 18:10:00  
# @ Modified By: Chen Jun  
# @ Last Modified: 2021-07-30, 18:10:06  
#############################################
# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'


import numpy as np
import pandas as pd

INDEX1 = [["MSI", "MSI", "MSI", "TMB", "TMB", "TMB"], [
    "Coding Region Size in Megabases",
    "Number of Passing Eligible Variants",
    "Percent Unstable MSI Sites",
    "Total TMB Sites Unstable",
    "Total TMB",
    "Usable MSI Sites",
]]
INDEX2 = [["TMB", "TMB", "TMB", "MSI", "MSI", "MSI"], [
    "Total TMB",
    "Coding Region Size in Megabases",
    "Number of Passing Eligible Variants",
    "Usable MSI Sites",
    "Total TMB Sites Unstable",
    "Percent Unstable MSI Sites",
]]



ff = pd.DataFrame(np.arange(6).reshape(6, 1), index=INDEX1)
ff.loc["MSI"].loc["Coding Region Size in Megabases"] = 1
ff



df1 = pd.DataFrame(np.arange(6).reshape(6, 1), index=INDEX2)
df1.loc["TMB"].loc["Total TMB"] = 1
df1



df1 = pd.DataFrame(np.arange(6).reshape(6, 1), index=INDEX2)
df1.loc[("TMB","Total TMB")] = 1
df1



df1 = pd.DataFrame(np.arange(6).reshape(6, 1), index=INDEX2)
df1.index


