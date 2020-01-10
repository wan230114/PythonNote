# Python3中multiprocessing的Process创建子进程在Windows和Linux下的区别
## 结论：
尽量在Linux中使用多进程，Linux中更遵循程序设计之初的规范。

>比如实例1中，Windows是全代码重头运行，无法共享父进程全局变量，全局变量会重新建立，Linux则是按照规矩仅从函数段运行。
>比如实例2-2中，Windows下使用多进程，将全局变量作为参数传递，可以解决由于代码执行控制造成的子进程和父进程是无法共享一个对象的问题。

## 实例1：
```python
# -*- coding: utf-8 -*-
import multiprocessing as mp
from time import sleep
import os

a = 1
print("[父/子] PID", os.getpid(), a, "===================")


def fun(xx):  # 进程事件
    sleep(1)
    global a
    print("[子]", "-----------------", a)
    print("[子]", "子进程事件")
    print("[子]", "传入内容：", xx)
    print("[子]", 'PID', os.getpid())
    a = 10000
    print("[子]", "-----------------", a)


# windows下运行需要此句判断，否则报错，Linux下无需
if __name__ == "__main__":
    print("[父]", 'PPID', os.getpid())
    p = mp.Process(target=fun, args=('test',))  # 创建进程对象

    p.start()  # 启动进程
    print("[父]", "这是父进程")
    p.join()  # 回收进程

    print("[父]", "===================", a)
```

windows运行结果：
```
[父/子] PID 9272 1 ===================
[父] PPID 9272
[父] 这是父进程
[父/子] PID 22788 1 ===================
[子] ----------------- 1
[子] 子进程事件
[子] 传入内容： test
[子] PID 22788
[子] ----------------- 10000
[父] =================== 1
```
Linux运行结果：
```
[父/子] PID 36 1 ===================
[父] PPID 36
[父] 这是父进程
[子] ----------------- 1
[子] 子进程事件
[子] 传入内容： test
[子] PID 37
[子] ----------------- 10000
[父] =================== 1
```
结果中，Windows下运行`[父/子] PID 22788 1 ===================`多打印了。
由此可见，Windows是全代码重头运行，无法共享父进程全局变量，全局变量会重新建立，Linux则是按照规矩仅从函数段运行。

## 实例2-1：
```python
from multiprocessing import Process, Array
import time

# 创建共享内存，存入列表　
shm = Array('i', [1,2,3,4,5])
# shm = Array('i', range(5))
# shm = Array('i', 5)  # 表示开辟５个空间


def fun():
    # shm 是可迭代对象
    for i in shm:
        print(i)
    # 修改共享内存
    print(list(shm))
    shm[3] = 1000


if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    p.join()

    print("=================")
    for i in shm:
        print(i)
```
Windows下运行结果：
```
1
2
3
4
5
[1, 2, 3, 4, 5]
=================
1
2
3
4
5
```
Linux下运行结果：
```
1
2
3
4
5
[1, 2, 3, 4, 5]
=================
1
2
3
1000
5
```
由此实例可见，<font color="red"><b>Windows下程序并未报错，且未达到我们运行的效果</b></font>——修改共享内存中的第4位数为1000。
## 实例2-2：
```python
from multiprocessing import Process, Array
import time

# 创建共享内存，存入列表　
shm = Array('i', [1,2,3,4,5])
# shm = Array('i', range(5))
# shm = Array('i', 5)  # 表示开辟５个空间


def fun(shm):
    # shm 是可迭代对象
    for i in shm:
        print(i)
    # 修改共享内存
    print(list(shm))
    shm[3] = 1000


if __name__ == '__main__':
    p = Process(target=fun, args=(shm,))
    p.start()
    p.join()

    print("=================")
    for i in shm:
        print(i)
```
由此可见，如果要在Windows下使用多进程，最好将全局变量作为参数传递，子进程和父进程是无法共享一个对象的。
## 实例2-3：
```python
from multiprocessing import Process, Array
import time


def fun(shm):
    # shm 是可迭代对象
    for i in shm:
        print(i)
    # 修改共享内存
    print(list(shm))
    shm[3] = 1000


if __name__ == '__main__':
    # 创建共享内存，存入列表　
    # shm = Array('i', [1,2,3,4,5])
    shm = Array('i', range(5))
    # shm = Array('i', 5)  # 表示开辟５个空间
    p = Process(target=fun, args=(shm,))
    p.start()
    p.join()

    print("=================")
    for i in shm:
        print(i)
```

Windows下和Linux下运行结果皆为：
```
0
1
2
3
4
[0, 1, 2, 3, 4]
=================
0
1
2
1000
4
```
当然，该写法和上一个实例一样的效果。都是将全局变量作为参数传递给需要多进程的函数了

# 附

subprocess模块

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

见

——廖雪峰笔记 \> Python3 \> 进程和多线程 \> 多进程
