
# 一些设置要点

## CPU

突破上限设置方法, .vmx手动修改： `numvcpus = "26"`

## 内存

vmem 本地文件的映射要取消掉，因为该文件会完全录入内存，使得内存被一直实际占用这么多。

设置方法, .vmx加入一行： `mainMem.useNamedFile=FALSE`

[VMware虚拟机的vmem是什么文件？vmem文件可以删除吗？ -Win7系统之家](http://www.winwin7.com/JC/7191.html)


