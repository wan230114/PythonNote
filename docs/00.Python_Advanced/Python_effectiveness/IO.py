# %%

import os
from datetime import datetime as dt


def print_runtime(func):
    def do(*args, **kwargs):
        t0 = dt.now()
        print("Running function:", func.__name__)
        # print('[开始运行]%s' % t0)
        result = func(*args, **kwargs)
        t1 = dt.now()
        # print('[运行结束]%s' % t1)
        print('used time: %s \n' % (t1-t0))
        return result
    return do


@print_runtime
def touch_file_w():
    with open("test.txt", "w") as fo:
        for i in range(int(5000 * 1024**2 / 100)):
            fo.write("1"*99+"\n")


@print_runtime
def touch_file_wb():
    with open("test.txt", "wb") as fo:
        for i in range(int(5000 * 1024**2 / 100)):
            fo.write(b"1"*99+b"\n")


@print_runtime
def read_r():
    with open("test.txt", "r", encoding="utf8") as fo:
        for line in fo:
            line


@print_runtime
def read_rb():
    with open("test.txt", "rb") as fo:
        for line in fo:
            line


@print_runtime
def read_rb_decode():
    with open("test.txt", "rb") as fo:
        for line in fo:
            line.decode("utf8")


touch_file_w()
touch_file_wb()
read_r()
read_rb()
read_rb_decode()
os.remove("test.txt")
