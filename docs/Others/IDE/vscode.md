
## windows10 排错指南

windows10下Bad owner or permissions on .ssh/config的解决办法

2020-06-12阅读 4.7K0

方法很简单，亲测有效。

1. 进入如下路径C:\Users\用户名\.ssh，你会看到有config这个文件
2. 右击config,属性→安全→高级→禁止继承→删除所有继承(忘了全称了，大概这个意思)→确定

如果系统是英文：

Properties -> Security -> Advanced -> Disable Inheritance -> Remove all inherited permissions from this object

参考Bad owner or permissions on C:\Users\USER/.ssh/config

