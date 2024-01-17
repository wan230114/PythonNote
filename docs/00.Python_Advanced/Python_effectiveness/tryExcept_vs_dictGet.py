# %%

from effectivenessTookIT.print_runtime import print_runtime

Time = 5*10**7  # 定义重复测试次数
D = {"a": 1}


@print_runtime
def try_except1():
    for i in range(Time):
        try:
            a = D["a"]
        except:
            a = ""


@print_runtime
def try_except2():
    for i in range(Time):
        try:
            a = D["aa"]
        except:
            a = ""


@print_runtime
def dict_get1():
    for i in range(Time):
        D.get("a", "")


@print_runtime
def dict_get2():
    for i in range(Time):
        D.get("aa", "")


try_except1()
try_except2()
dict_get1()
dict_get2()


# 执行结果:
# 3.9.7 (default, Sep 16 2021, 13:09:58)
# [GCC 7.5.0]
# used time: 0:00:03.336183, function: try_except1
# used time: 0:00:14.347548, function: try_except2
# used time: 0:00:05.118862, function: dict_get1
# used time: 0:00:05.144695, function: dict_get2

# 执行结果:
# 3.11.0 | packaged by conda-forge | (main, Oct 25 2022, 06:24:40) [GCC 10.4.0]
# used time: 0:00:02.250443, function: try_except1
# used time: 0:00:14.398226, function: try_except2
# used time: 0:00:03.808639, function: dict_get1
# used time: 0:00:03.303311, function: dict_get2