# %%

from effectivenessTookIT.print_runtime import print_runtime

Time = 5*10**7  # 定义重复测试次数


a1 = "123\t456\t789\t0"
a2 = b"123\t456\t789\t0"
split_a1 = "\t"
split_a2 = b"\t"


@print_runtime
def strSplit():
    L = []
    for i in range(Time):
        a1.split(split_a1)


@print_runtime
def unicodeSplit():
    L = []
    for i in range(Time):
        a2.split(split_a2)


strSplit()
unicodeSplit()

# 执行结果:
# 3.9.7 (default, Sep 16 2021, 13:09:58) 
# [GCC 7.5.0]
# used time: 0:00:12.076150, function: strSplit
# used time: 0:00:10.831690, function: unicodeSplit

# 3.11.0 | packaged by conda-forge | (main, Oct 25 2022, 06:24:40) [GCC 10.4.0]
# used time: 0:00:09.189947, function: strSplit
# used time: 0:00:09.155327, function: unicodeSplit

# 3.11.0 | packaged by conda-forge | (main, Oct 25 2022, 06:24:40) [GCC 10.4.0]
# used time: 0:00:09.273300, function: strSplit
# used time: 0:00:09.353146, function: unicodeSplit
