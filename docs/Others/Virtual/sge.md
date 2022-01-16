# 1. 使用

使用教程： （已部署好，可直接使用）

```bash
docker run --name centos7_sge --hostname control  --privileged=true  --cap-add SYS_ADMIN -it centos7_sge bash
docker run --name centos7_sge --hostname control  --privileged=true  --cap-add SYS_ADMIN -v $PWD:/sge_share -it centos7_sge bash



/opt/sysoft/sge/default/common/sgemaster    # 控制节点启动
/opt/sysoft/sge/default/common/sgeexecd     # 计算节点启动

source /opt/sysoft/sge/default/common/settings.sh  # 可加入bashrc
qhost

su sgeadmin
cd ~
echo "echo start. && sleep 20 && echo end." >run.sh
qsub -V -cwd -o stdout.txt -e stderr.txt run.sh
qsub -cwd run.sh
ls
```


---
# 2. 部署过程

docker

```bash
# 部署准备：
docker run --name centos7_sge --hostname control  --privileged=true  --cap-add SYS_ADMIN -it centos7_base bash
# docker commit -a "chenjun"  -m  "centos7_base" centos7_base centos7_base
# docker commit -a "chenjun"  -m  "centos7_sge2" centos7_sge centos7_sge2
# docker run --name centos7_sge --hostname control  --privileged=true  --cap-add SYS_ADMIN -it centos7_sge2 bash

# 部署过程：
# ... 

# 部署完成后：
docker commit -a "chenjun"  -m  "centos7_sge" centos7_sge centos7_sge
```



## 2.1. Start

在CentOS7部署SGE
发表于2019 年 4 月 17 日
CentOS7的第三方源EPEL不再提供SGE（Son of Grid Engine）软件了，需要自己手动安装SGE。

### 2.1.1. 设置防火墙，开放SGE所需要的端口

```bash
firewall-cmd --add-port=992/udp --permanent
firewall-cmd --add-port=6444/tcp --permanent
firewall-cmd --add-port=6445/tcp --permanent
systemctl restart firewalld.service
```

### 2.1.2. 从SGE官网下载最新版本的SGE源码包并进行编译和安装

安装依赖的系统软件

```bash
# 安装epel源
yum -y install epel-release
# 安装gcc
yum -y install gcc automake autoconf libtool make
yum -y install csh java-1.8.0-openjdk java-1.8.0-openjdk-devel gcc ant automake hwloc-devel openssl-devel libdb-devel pam-devel libXt-devel motif-devel ncurses-libs ncurses-devel
yum -y install ant-junit junit javacc
```

下载SGE软件并进行编译

```bash
wget https://arc.liv.ac.uk/downloads/SGE/releases/8.1.9/sge-8.1.9.tar.gz -P ~/software/
tar zxf ~/software/sge-8.1.9.tar.gz
cd sge-8.1.9/source
./scripts/bootstrap.sh
./aimk -no-herd -no-java
./aimk -no-herd       # 进行图形化安装，不太推荐。我尝试使用该方式编译，导致后续没能部署成功
```

将编译好的SGE安装到指定的文件夹（需要使用root用户执行）

```bash
mkdir -p /opt/sysoft/sge
export SGE_ROOT=/opt/sysoft/sge
./scripts/distinst -local -allall -noexit # 虽然普通用户在目标文件夹有写权限，但是程序要对一些文件进行权限修改，使用root用户不会报错。
cd ../../ && rm sge-8.1.9/ -rf
echo 'export SGE_ROOT=/opt/sysoft/sge' >> ~/.bashrc
echo 'PATH=$PATH:/opt/sysoft/sge/bin/:/opt/sysoft/sge/bin/lx-amd64/' >> ~/.bashrc
source ~/.bashrc    #普通用户也需要进行变量设置
```

### 2.1.3. 部署SGE前设置主机名
部署SGE前，需要设置好各个节点的主机名，需要修改3个文件。修改配置文件 /etc/sysconfig/network 内容：

vim /etc/sysconfig/network

```bash
NETWORKING=yes
HOSTNAME=control 
```

修改配置文件 /proc/sys/kernel/hostname 内容：

vim /proc/sys/kernel/hostname
```bash
control
```

修改配置文件 /etc/hosts 内容（注意删除掉127.0.0.1和localhost的行）：

vim /etc/hosts

```bash
192.168.30.1 control
192.168.30.2 node2
192.168.30.3 node3
192.168.30.4 node4 
```


### 2.1.4. 在所有节点上部署SGE

补充：提前准备工作
添加sgeadmin用户组，及sgeadmin用户

```bash
groupadd -g 490 sgeadmin
useradd -u 495 -g 490 -m -d /home/sgeadmin -s /bin/bash -c "SGE Admin" sgeadmin
```

在管理节点上部署SGE：

```bash
cd $SGE_ROOT
./install_qmaster
```


运行部署命令后，会进入交互式界面。基本上全部都按Enter键使用默认设置即可。需要注意的事项是：

1. 有一步骤是启动Grid Engine qmasster服务，可能会启动不了导致失败。原因是多次运行该命令进行部署，第一次会成功运行qmaster daemon，以后重新运行该程序进行部署则会失败。需要删除相应的sge_qmaster进程再进行部署。 
2. 启动Grid Engine qmasster服务，要提供部署SGE的节点主机名信息，按y和Enter键使用一个文件来提供主机信息，输入文件路径/etc/hosts提供主机信息。
只有先进行一个控制节点部署后，才能对各个计算节点进行部署。计算节点的部署比较简单，交互过程全部按Enter即可。

```bash
./install_execd
```


### 2.1.5. 启动SGE软件

部署完毕后，若需要使用SGE软件，则执行如下命令载入SGE的环境变量信息：

```bash
source /opt/sysoft/sge/default/common/settings.sh
```

或将该信息添加到~/.bashrc从而永久生效：

```bash
echo 'source /opt/sysoft/sge/default/common/settings.sh' >> ~/.bashrc
source ~/.bashrc
```

启动SGE软件方法：

```bash
/opt/sysoft/sge/default/common/sgemaster    # 控制节点启动
/opt/sysoft/sge/default/common/sgeexecd     # 计算节点启动
```

查看SGE软件运行日志文件：

Qmaster:      /opt/sysoft/sge/default/spool/qmaster/messages
Exec daemon:  /opt/sysoft/sge/default/spool/<hostname>/messages


### 2.1.6. 使用SGE软件

部署完毕SGE后，会生成一个默认主机用户组@allhosts，它包含所有的执行节点；生成一个默认的all.q队列名，它包含所有节点所有计算资源。默认的队列包含的计算资源是最大的。 通过使用命令qconf -mq queuename来对队列进行配置。修改hostlist来配置该队列可以使用执行主机；修改slots来配置各台执行主机可使用的线程数。从而对队列的计算资源进行设置。

```bash
qconf -as control
qconf -ss
```

#### 2.1.6.1. 使用qconf命令对SGE进行配置：

```bash
qconf -ae hostname
    # 添加执行主机
qconf -de hostname
    # 删除执行主机
qconf -sel
    # 显示执行主机列表

qconf -ah hostname
    # 添加管理主机
qconf -dh hostname
    # 删除管理主机
qconf -sh
    # 显示管理主机列表

qconf -as hostname
    # 添加提交主机
qconf -ds hostname
    # 删除提交主机
qconf -ss
    # 显示提交主机列表

qconf -ahgrp groupname
    # 添加主机用户组
qconf -mhgrp groupname
    # 修改主机用户组
qconf -shgrp groupname
    # 显示主机用户组成员
qconf -shgrpl
    # 显示主机用户组列表

qconf -aq queuename
    # 添加集群队列
qconf -dq queuename
    # 删除集群队列
qconf -mq queuename
    # 修改集群队列配置
qconf -sq queuename
    # 显示集群队列配置
qconf -sql
    # 显示集群队列列表

qconf -ap PE_name
    # 添加并行化环境
qconf -mp PE_name
    # 修改并行化环境
qconf -dp PE_name
    # 删除并行化环境
qconf -sp PE_name
    # 显示并行化环境
qconf -spl
    # 显示并行化环境名称列表

qstat -f
    # 显示执行主机状态
qstat -u user
    # 查看用户的作业
qhost
    # 显示执行主机资源信息
```

#### 2.1.6.2. 使用qsub提交作业

qsub简单示例：
```bash
source /opt/sysoft/sge/default/common/settings.sh
qhost

su sgeadmin
cd ~
echo "echo start. && sleep 20 && echo end." >run.sh
qsub -V -cwd -o stdout.txt -e stderr.txt run.sh
qsub -cwd run.sh
ls
```

其中run.sh中包含需要运行的程序，其内容示例为如下三行：

```shell
qsub的常用参数：
-V
    将当前shell中的环境变量输出到本次提交的任务中。
-cwd
    在当前工作目录下运行程序。默认设置下，程序的运行目录是当前用户在其计算节点的家目录。
-o
    将标准输出添加到指定文件尾部。默认输出文件名是$job_name.o$job_id。
-e
    将标准错误输出添加到指定文件尾部。默认输出文件名是$job_name.e$job_id。
-q
    指定投递的队列，若不指定，则会尝试寻找最小负荷且有权限的队列开始任务。
-S
    指定运行run.sh中命令行的软件，默认是tcsh。推荐使用bash，设置该参数的值为 /bin/bash 即可，或者在run.sh文件首部添加一行#$ -S /bin/bash。若不设置为bash，则会在标准输出中给出警告信息：Warning: no access to tty (Bad file descriptor)。
-hold_jid
    后接多个使用逗号分隔的job_id，表示只有在这些job运行完毕后，才开始运行此任务。
-N
    设置任务名称。默认的job name为qsub的输入文件名。
-p
    设置任务优先级。其参数值范围为 -1023 ~ 1024 ，该值越高，越优先运行。但是该参数设置为正数需要较高的权限，系统普通用户不能设置为正数。
-j y|n
    设置是否将标准输出和标准错误输出流合并到 -o 参数结果中。
-pe
    设置并行化环境。
```

#### 2.1.6.3. 任务提交后的管理：

```bash
qstat -f
    # 查看当前用户在当前节点提交的所有任务，任务的状态有4中情况：qw，等待状态，刚提交任务的时候是该状态，一旦有计算资源了会马上运行；hqw，该任务依赖于其它正在运行的job，待前面的job执行完毕后再开始运行，qsub提交任务的时候使用-hold_jid参数则会是该状态；Eqw，投递任务出错；r，任务正在运行；s，被暂时挂起，往往是由于优先级更高的任务抢占了资源；dr，节点挂掉后，删除任务就会出现这个状态，只有节点重启后，任务才会消失。

qstat -j jobID
    # 按照任务id查看

qstat -u user
    # 按照用户查看

qdel -j jobID
    # 删除任务
```

---

参考：
---

[在CentOS7部署SGE | 陈连福的生信博客](http://www.chenlianfu.com/?p=2858)

[Installation of SGE on CentOS 7](http://www.softpanorama.org/HPC/Grid_engine/Installation/installation_of_sge_centos7.shtml#n20181108X_sge_installation_on_centos_7)

[wangkaisine/SGE-On-CentOS: Intro how to install and use SGE(Sun Grid Engine) on ConteOS 7](https://github.com/wangkaisine/SGE-On-CentOS)

[用vmhgfs-fuse .host:/ /mnt/hgfs挂载后需要超级用户才能ls hgfs-CSDN论坛](https://bbs.csdn.net/topics/392053153)

