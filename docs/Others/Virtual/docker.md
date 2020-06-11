虚拟化技术之docker


# linux准备

yum换源：  
[ref](https://blog.csdn.net/sinat_33384251/article/details/91404617)

```bash
# 1,备份一下原本的yum源：
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
# 2,下载阿里云的yum源【我下的是CentOS7的，如果需要其他版本，那么只需要将下面的7改成5或6即可】【这一步需要能联网】：
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
# 3,之后运行给install生成缓存
yum clean all
yum makecache
yum -y install git screen
```


# docker的安装

```bash
yum install -y yum-utils device-mapper-persistent-data lvm2 bind-utils
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo 
yum install docker-ce
# 开机自启
sudo systemctl enable docker 
# 启动docker服务  
sudo systemctl start docker
# 
```

CentOS Docker 安装 | 菜鸟教程
https://www.runoob.com/docker/centos-docker-install.html

linux安装docker - 简书  
https://www.jianshu.com/p/2dae7b13ce2f

# docker进程管理

```bash
docker ps  # 查看进程
docker ps -a  # 查看所有进程，包括曾运行现已退出的进程
docker image rm <IMAGE_ID>  # 镜像删除
```

# 镜像操作

## 基本: 拉取、查看、启动、进入
```bash
# 拉取centos7镜像
docker pull centos:7
# 查看当前主机存在的所有镜像
docker images
# 启动镜像centos7，如果不指定 /bin/bash，容器运行后会自动停止
docker run -d -i -t <IMAGE_ID> /bin/bash
# 进入容器，使用exec或attach
# docker ps|head -2|sed 1d|awk '{print $1}'|xargs -i echo docker exec -it {} bash
docker exec -it <CONTAINER_ID> bash
docker attach <CONTAINER_ID>
```

运行命令说明：这样就能启动一个一直停留在后台运行的Centos了。如果少了/bin/bash的话，Docker会生成一个Container但是马上就停止了，不会一致运行即使有了-d参数。


### 高级启动方式

加入-v参数，代表将本地目录~/share_docker挂载为容器的/share_dir，不存在时则自动创建
```bash
# 使容器启动sshd服务并一直运行
docker run -dit 5746fb19a6cb /usr/sbin/sshd -D

# 共享端口 外部8080 --> 内部8080
docker run  -p 8080:8080 -dit 5746fb19a6cb /usr/sbin/sshd -D

# 配置共享文件夹
docker run -dit -v ~/share_docker:/share_dir centos_conda /bin/bash
docker run -dit -v /root/docker/data:/root/workdir/ centos_conda /usr/sbin/sshd -D
```

参考：详解Docker挂载本地目录及实现文件共享_mager的专栏-CSDN博客_docker共享目录  
https://blog.csdn.net/magerguo/article/details/72514813/


## 镜像内自定义操作

安装ssh

目的：通过ssh方式简易登录运行。（docker运行后，同一个镜像每次运行的ID不同，进入docker内部略显麻烦。）

```bash
# 安装ifconfig，搜索真实名字：yum search ifconfig
yum install -y net-tools.x86_64 openssh-server 
# 启动ssh服务
cd ~ && nohup /usr/sbin/sshd -D &>sshd.log &
```

查看ip，设置sshd连接登录。

## 镜像打包

### **step1: 镜像准备**

先清理缓存等文件，使得打包体积更小
```bash
yum clean all
conda clean -a
```

### **step2: 打包到镜像**

方法一：
```bash
docker commit -a "chenjun"  -m "bwa/bowtie2/hisat2" 966527ad7f5b centos_conda
```

方法二：

文件夹准备
```
mkdir demo && cd demo
vim Dockerfile
```
Dockerfile内容示例：
```bash
FROM centos:7.2.1511
WORKDIR /root/
EXPOSE 22
```

```
docker build -t centos_conda ./
```

### **step3: 镜像打包到本地文件**
```bash
docker save -o centos_conda.tar centos_conda:latest
```
把打包的centos_conda镜像存储为本地目录中 centos_conda.tar 文件，发布到网上供客户安装使用

加载docker镜像文件的方法
```bash
docker load -i  centos_conda.tar
docker load -i  nginx.tar
```

## 普通用户执行docker

```bash
# 添加 docker 用户组
groupadd docker
# 把需要执行的 docker 用户添加进该组，这里是 test
gpasswd -a test docker
# 重启 docker
systemctl restart docker
su -l test
# 运行...
# 运行成功
docker ps -a 
```

新开用户加入docker组，并没有获得系统级权限，只是能运行docker。

不过使用docer run -v 挂载共享文件夹运行后，docker内创建的文件用户与组会在外部系统显示相同，如果是root下创建，那么就是root权限，这一点需要注意一下。

## 可能有用的教程：
---
- 网络配置出错
  - 进入后的网络控制，发现没有ifconfig，直接yum安装  
  - 无法ping外网，查找资料重建docker0网络解决，资料地址

```bash
[root@8f10fbd6bd5a /]# yum install -y net-tools
[root@localhost ~]# pkill docker
[root@localhost ~]# iptables -t nat -F
[root@localhost ~]# ifconfig docker0 down
[root@localhost ~]# brctl delbr docker0
[root@localhost ~]# systemctl restart docker
[root@localhost ~]# docker start <CONTAINER ID>
```

---
端口映射：

```
接下来只要启动就可以了
/usr/sbin/sshd -D

接下来就是常用的命令了，将端口映射到宿主机，我这里就是VM分配的linux系统。
#退出，但不停止容器
Ctrl+P+Q
#回到Docker下面，停止容器
docker stop <容器ID>
#提交当前容器到镜像
docker commit <容器ID> <NAME/VERSION>
#启动新容器，并且进行端口映射
docker run -itd -p 50001:22 <刚才提交的镜像ID>  /bin/bash
```
好了，这样我们在windows下利用ssh工具访问宿主机的IP端口就可以访问到容器了
我这里就是192.168.99.100:50001