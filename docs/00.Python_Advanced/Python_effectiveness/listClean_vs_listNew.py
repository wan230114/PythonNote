# %%

from effectivenessTookIT.print_runtime import print_runtime

Time = 4*10**6  # 定义重复测试次数


@print_runtime
def listClean():
    L = []
    for i in range(Time):
        for x in range(10):
            L.append(x)
        L.clear()


@print_runtime
def listNew():
    L = []
    for i in range(Time):
        for x in range(10):
            L.append(x)
        L = []


listClean()
listNew()

# 执行结果:
# 3.9.7 (default, Sep 16 2021, 13:09:58) 
# [GCC 7.5.0]
# used time: 0:00:04.065442, function: listClean
# used time: 0:00:04.187883, function: listNew

# 3.11.0 | packaged by conda-forge | (main, Oct 25 2022, 06:24:40) [GCC 10.4.0]
# used time: 0:00:02.104051, function: listClean
# used time: 0:00:02.099097, function: listNew
