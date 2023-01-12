# 汇总

```bash

{
docker run --rm --name samba-server -it -d -p 139:139 -p 445:445 \
    -v /mfs1/tmpworkdir/:/shareDir\
    dperson/samba \
    -p -u "test;test123456" \
    -s "shareDir;/shareDir;yes;yes;no;test"
}

```
# 磁盘挂载管理命令


```bash
# 1) lsblk ： 查看设备的挂载情况
lsblk
lsblk -f
# NAME            FSTYPE      LABEL           UUID                                   MOUNTPOINT
# sda                                                                                
# ├─sda1          xfs                         19c5a942-927a-402f-9a34-d7a186a5c435   /boot
# └─sda2          LVM2_member                 ITA43h-NWmF-5VQZ-JTqm-e9V8-3v1d-sjHz2I 
#   ├─centos-root xfs                         8edce1d9-c0c2-417d-b7b2-a231cfcc7c02   /
#   └─centos-swap swap                        e003d1d2-d199-4b3d-bad4-c79ab3c2967c   [SWAP]
# sdb                                                                                
# sr0             iso9660     CentOS 7 x86_64 2018-11-25-23-54-16-00

# sdb为待处理磁盘
# NAME所示磁盘都默认存放于/dev内。


# 2) fdisk ：分区操作
fdisk /dev/sdb  # 对sdb分区操作
# m     # 看菜单命令
# n     # 添加新分区
# p     # 选择分区类型
# 1     # enter默认
# ...   # 可一直enter默认
# w     # 保存分区退出
lsblk


# 3) mkfs ：格式化
mkfs -t ext4 /dev/sdb1

# 4) 挂载
mkdir /work
mount /dev/sdb1 /work

# 5) 设置自动挂载（永久挂载，当你重启Linux之后，仍然可以挂载）
# 永久挂载：通过修改 /etc/fstab 实现挂载
# vim /etc/fstab
# 添加：（挂载点，挂载路径，磁盘类型，...）
# /dev/sdb1 /work                                 ext4    defaults        0 0

# 执行如下命令生效：
mount -a
```


---
fdisk命令菜单解释：

|命令|英文解释|中文解释|
|---|----------------------------------------|----------------------------|
| a | toggle a bootable flag                 | 切换可启动标志             |
| b | edit bsd disklabel                     |                            |
| c | toggle the dos compatibility flag      | 切换dos兼容性标志          |
| d | delete a partition                     | 删除一个分区               |
| g | create a new empty GPT partition table | 创建个新的空GPT分区表      |
| G | create an IRIX (SGI) partition table   | 创建个IRIX (SGI) 分区表    |
| l | list known partition types             | 列出已知的分区类型         |
| m | print this menu                        | 打印这个菜单               |
| n | add a new partition                    | 添加新分区                 |
| o | create a new empty DOS partition table | 创建一个新的空DOS分区表    |
| p | print the partition table              | 打印分区表                 |
| q | quit without saving changes            | 不保存更改就退出           |
| s | create a new empty Sun disklabel       | 创建一个新的空太阳磁盘标签 |
| t | change a partition's system id         | 更改分区的系统id           |
| u | change display/entry units             | 改变显示/输入单元          |
| v | verify the partition table             | 验证分区表                 |
| w | write table to disk and exit           | 将表写入磁盘并退出         |
| x | extra functionality (experts only)     | 额外功能(仅限专家使用)     |




# 分区容量拓展

## 简单的方法

参考：[扩展数据盘的分区和文件系统（Linux）_云硬盘 EVS_用户指南_扩容云硬盘_扩展磁盘分区和文件系统（Linux）_华为云](https://support.huaweicloud.com/usermanual-evs/evs_01_0109.html)

```bash
# （可选）执行以下命令，安装growpart扩容工具。
yum install cloud-utils-growpart
# （可选）执行以下命令，安装gdisk软件包。
yum install gdisk

# 查看磁盘的分区信息。
fdisk -l
df -TH
# 卸载磁盘
umount /work/

# 执行以下命令，指定数据盘待扩容的分区，通过growpart进行扩容。
# growpart 数据盘 分区编号
growpart /dev/sdb 1
resize2fs  /dev/sdb1
df -TH
```

扩容前后对比：
```shell
$ lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb               8:16   0  1.6T  0 disk
└─sdb1            8:17   0  200G  0 part /work

$ lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb               8:16   0  1.6T  0 disk
└─sdb1            8:17   0  1.6T  0 part /work
```


## 麻烦的方法

```bash
# 卸载分区
# 1、停掉该分区的业务的读写
# 2、shell> umount /data
umount /work
# 3、如果提示busy,使用fuser找出kill掉进程
fuser -m -v /work
fuser -m -v -i -k /work
# 看看情况
lsblk
fdisk -l
fdisk /dev/sdb  # 对sda1进行重新分区
# fdisk /dev/sdb
# p #查看磁柱号 ，记住，后面要用到
# d #删除之前的分区
# n #建立新分区
# p #主分区
# 1 #第一个主分区

# 调整分区
e2fsck -f /dev/sdb1 #检查分区信息
resize2fs /dev/sdb1 #调整分区大小
mount -a
df -h
lvm
# ...
```


```bash
分区： 
fdisk /dev/sdb
# p　　　　　　  #查看已分区数量（我看到有两个 /dev/sda1 /dev/sda2） 
# n　　　　　　　#新增加一个分区
# p　　　　　　　#分区类型我们选择为主分区 
# 　　　　　　   #分区号输入3（因为1,2已经用过了,sda1是分区1,sda2是分区2,sda3分区3） 
# 回车　　　　　  #默认（起始扇区）
# 回车　　　　　  #默认（结束扇区）
# t　　　　　　　 #修改分区类型 
# 　　　　　　   #选分区3
# 8e　　　　　 　#修改为LVM（8e就是LVM）
# w　　　　　  　#写分区表
# q　　　　　  　#完成，退出fdisk命令
mkfs.xfs /dev/sdb2 -f

```

```bash
lvm
# 这是初始化刚才的分区3
pvcreate /dev/sdb2
# 将初始化过的分区加入到虚拟卷组centos (卷和卷组的命令可以通过 vgdisplay查看)
vgextend centos /dev/sdb2
# vgdisplay查看free PE /Site
vgdisplay
vgdisplay -v
# 扩展已有卷的容量（6143 是通过 vgdisplay 查看free PE /Site的大小）
# lvm> lvextend -l+6143 /dev/mapper/centos-root　　
lvextend -l+358399 /dev/sdb1
pvdisplay
```