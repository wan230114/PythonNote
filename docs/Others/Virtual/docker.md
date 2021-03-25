<h1> 虚拟化技术之docker </h1>

docker基本概念简介：
- images：基础镜像
- container：以基础镜像为模板进行运行的实例，该实例经修改可以再导出到基础镜像。

# 1. docker的安装


## 1.1. Centos下docker的安装

---
yum换源（该步骤根据需求可直接跳过）[—— ref](https://blog.csdn.net/sinat_33384251/article/details/91404617)

```bash
# 1,备份一下原本的yum源：
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
# 2,下载阿里云的yum源【我下的是CentOS7的，如果需要其他版本，那么只需要将下面的7改成5或6即可】【这一步需要能联网】：
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
# 并替换部分字段（非阿里云机器需要做）
# sed -i -e '/mirrors.cloud.aliyuncs.com/d' -e '/mirrors.aliyuncs.com/d' /etc/yum.repos.d/CentOS-Base.repo
# 3,之后运行给install生成缓存
yum clean all
yum makecache
# yum -y install git screen
```


```bash
yum install -y yum-utils device-mapper-persistent-data lvm2 bind-utils
# yum-config-manager --add-repo  https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo 
## 报错时使用，安装最新版containerd.io。 Error:Problem: package docker-ce-3:19.03.8-3.el7.x86_64 requires containerd.io >= 1.2.2-3
# dnf install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
yum -y install docker-ce
## 开机自启
sudo systemctl enable docker 
## 启动docker服务  
sudo systemctl start docker
```

参考：
- [CentOS Docker 安装 | 菜鸟教程](https://www.runoob.com/docker/centos-docker-install.html)
- [linux安装docker - 简书](https://www.jianshu.com/p/2dae7b13ce2f)

## 1.2. Ubuntu下docker的安装

略

## 1.3. Mac下docker的安装

```bash
brew cask install docker
```

## 1.4. 执行环境

普通用户执行docker

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



---
# 2. 镜像操作

## 2.1. 拉取及基本启动

1. 基本操作命令: 拉取、查看、启动、进入

```bash
# 1. 拉取centos7镜像
docker pull centos:7
# 2. 查看当前主机存在的所有镜像
docker images

# 3. 运行基础镜像的实例。
## 启动镜像centos7，如果不指定 /bin/bash，容器运行后会自动停止
docker run -dit <IMAGE_ID/Name> bash

# 4. 进入容器实例，使用exec或attach
docker exec -it <CONTAINER_ID/Name> bash
docker attach <CONTAINER_ID/Name>
```

2. 高级启动方式

```bash
# 使容器启动sshd服务并一直运行：/usr/sbin/sshd -D
docker run  -dit <IMAGE_ID/Name> /usr/sbin/sshd -D
# 指定容器名字：--name CONTAINER_test （后续可不再输入复杂ID，而输入此名）
docker run  --name CONTAINER_test -dit <IMAGE_ID/Name> bash
# 端口映射外部8080 --> 内部80：-p 8080:80
docker run  -p 8080:80 -dit <IMAGE_ID/Name> bash
# 配置共享文件夹：-v /local_path/:/docker_path/ (路径不存在时自动创建)
docker run  -v /local_path/:/docker_path/ -dit <IMAGE_ID/Name> bash
# 执行完毕自动删除镜像实例
docker run  --rm -dit <IMAGE_ID/Name> ls /

# 一些实例：
## 使用docker内部程序完成计算，并路径映射，外部输入到输出外部
docker run --rm --user `id -u`:`id -g`   -v $PWD/input:/input:ro  -v $PWD/output:/output   bioliquidator/bamliquidator   /input/04032013_D1L57ACXX_4.TTAGGC.hg18.bwt.sorted.bam -o /output
```

参考：[详解Docker挂载本地目录及实现文件共享_mager的专栏-CSDN博客_docker共享目录](https://blog.csdn.net/magerguo/article/details/72514813/)


---
## 2.2. 镜像的管理和删除

```bash
# 查看当前运行中的镜像实例
docker ps
# 查看所有的镜像实例，包括曾运行现已退出的进程
docker ps -a
# 对停止状态的镜像实例开始运行
docker start <CONTAINER_ID/Name>
# 对运行状态的镜像实例停止运行
docker stop <CONTAINER_ID/Name>
# 镜像实例删除
docker rm <CONTAINER_ID/Name>
# 镜像删除：docker rmi <IMAGE_ID/Name>/<IMAGE_NAME>
docker rmi <IMAGE_ID/Name>
```

参考：[Docker中如何删除image（镜像）_dabenxiong的专栏-CSDN博客](https://blog.csdn.net/flydreamzhll/article/details/80900509)


## 2.3. 镜像内的一些常用环境更改

安装ssh
1. 通过ssh方式简易登录运行，可以共享登录。
2. docker运行后，同一个镜像每次运行的ID不同，进入docker内部略显麻烦，当然可以指定镜像及其实例名字。

```bash
# 登录镜像后
# 安装ifconfig，搜索真实名字：yum search ifconfig
yum install -y net-tools.x86_64 openssh-server 
# 启动ssh服务
cd ~ && nohup /usr/sbin/sshd -D &>sshd.log &
# 查看ip，设置sshd连接登录。
# yum install -y net-tools  # 无ifconfig问题解决
```

---
# 4. 镜像打包


## 4.1. **step1: 镜像准备**

先清理缓存等文件，使得打包体积更小
```bash
# 容器实例内
yum clean all
conda clean -a
```


## 4.2. **step2: 打包到镜像**

方法一：
```bash
docker commit -a "chenjun"  -m "bwa/bowtie2/hisat2" 966527ad7f5b centos_test
```

方法二：

文件夹准备
```bash
mkdir demo && cd demo
vim Dockerfile
docker build -t centos_test ./
```
Dockerfile内容示例：
```yml
FROM centos:7
WORKDIR /root/
EXPOSE 22
```


## 4.3. **step3: 镜像打包到本地文件**

```bash
docker save -o centos_test.tar centos_test:latest
```
把打包的centos_test镜像存储为本地目录中 `centos_test.tar` 文件，发布到网上供客户安装使用

加载docker镜像文件的方法
```bash
docker load -i  centos_test.tar
docker load -i  nginx.tar
```

# 一些实战操作

## centos建立常用基础运行包，并打包镜像

### 2.1.1. 容器 —— 基础运行环境的制作

---
#### 2.1.1.1. 容器制作
```bash
cd $workdir
# 拉取镜像
docker pull ubuntu:16.04
# 进入容器
docker run --name ubuntu_base -dit ubuntu:16.04  /bin/bash
docker ps
docker exec -it ubuntu_base bash # 登录
```

---
#### 2.1.1.2. 换源
```bash
cp /etc/apt/sources.list /etc/apt/sources.list--bak
# cp /etc/apt/sources.list--bak /etc/apt/sources.list
{
echo "# deb cdrom:[Ubuntu 16.04 LTS _Xenial Xerus_ - Release amd64 (20160420.1)]/ xenial main restricted
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse #Added by software-properties
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse
" >/etc/apt/sources.list
apt-get update
apt-get upgrade
}

apt-get install -y vim less curl wget git
# proxychains4
apt-get install -y proxychains

# vim /etc/proxychains.conf
```

#### 2.1.1.3. 基础镜像打包
```bash
# 安装完 proxychains4 ， conda
# 打包为基础镜像
docker commit -a "last"  -m "ubuntu_base" ubuntu_base ubuntu_base
# docker commit -a "bq"  -m "ubuntu_base" ubuntu_base ubuntu_base
```

---
### 2.1.2. 配置容器并进入容器

```bash
cd $workdir
# 进入容器
docker run \
    --name ubuntu_CRC \
    -v $PWD/share:/share \
    -dit ubuntu_base  /bin/bash
docker ps
docker exec -it ubuntu_CRC bash # 登录
```

## 镜像移植
```bash
# 机器1：
# 保存镜像：
docker save -o centos7_base.tar centos7_base:latest

# 机器2：
# 导入镜像：
docker load -i  centos7_base.tar 

# 运行：
docker run \
    --name centos7_test \
    -p 8080:80 \
    -v $PWD/share_dir:/share_dir \
    -dit centos7_base  /bin/bash

# docker stop centos7_test
# docker start centos7_test

# 登录
docker exec -it centos7_test bash
```
