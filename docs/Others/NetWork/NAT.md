
# 1. frp

nat的连接方式。访问端无需安装任何软件

## 1.1. 服务端一键配置

```bash
# 1) 下载软件
## 访问： https://github.com/fatedier/frp
## 点击release： https://github.com/fatedier/frp/releases/
## 点击下载对应版本如： https://github.com/fatedier/frp/releases/download/v0.33.0/frp_0.33.0_linux_arm64.tar.gz
wget https://github.com/fatedier/frp/releases/download/v0.29.0/frp_0.29.0_linux_amd64.tar.gz
tar xzvf frp_0.29.0_linux_amd64.tar.gz
cd frp_0.29.0_linux_amd64

# 2) frps.ini配置文件的生成
## 查看服务端的公网IP
IP_pub=`curl ipv4.icanhazip.com 2>/dev/null`
echo "IP_pub=$IP_pub" # 将IP记录下来，便于客户端使用
## 修改为公网IP，可实现无需域名
cat frps_full.ini |sed "s# = frps.com# = $IP_pub#" >frps.ini
## 改一下使用端口，一般而言最好改一下端口，避免与其他网页服务端口如同80和443冲突
sed -i -e 's#vhost_http_port = 80#vhost_http_port = 81#g' -e 's#vhost_https_port = 443#vhost_https_port = 444#g' frps.ini
## 改一下默认密码
sed -i -e 's#token = 12345678#token = user12345678#g' frps.ini

## 3) 后台执行
nohup ./frps -c ./frps.ini &>log &
```

Ps：
- 关于执行。有些操作，如需要指定端口，需要用到root权限
- 关于管理。查看哪些客户端在连接，服务端运行后，可以访问公网IP，如 118.89.194.65:7500 能查看管理面板，管理账户密码都为admin，可在frps.ini自行修改


## 1.2. 客户端一键配置

```bash
# 1) 下载软件
## 访问： https://github.com/fatedier/frp
## 点击release： https://github.com/fatedier/frp/releases/
## 点击下载对应版本如： https://github.com/fatedier/frp/releases/download/v0.33.0/frp_0.33.0_linux_arm64.tar.gz
wget https://github.com/fatedier/frp/releases/download/v0.29.0/frp_0.29.0_linux_amd64.tar.gz
tar xzvf frp_0.29.0_linux_amd64.tar.gz
cd frp_0.29.0_linux_amd64

# 2) frpc.ini配置文件的生成
{
IP_pub=118.89.194.65  # 该行自行修改与服务端对应
HOSTNAME=`hostname`
REMOTE_PORT=6001

echo "[common]
server_addr = $IP_pub
server_port = 7000
token = user12345678

[ssh - $HOSTNAME - $REMOTE_PORT]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = $REMOTE_PORT" >./frpc.ini
}

nohup ./frps -c ./frps.ini &>log &

# 当看到运行日志 Start frps success时
## Enjoy，可以在任意网络环境直接通过ssh方式连接运行了frpc的客户端
ssh user@$IP_pub -p $REMOTE_PORT
```

Ps：
- 多台客户端去连接同一台客户端，配置文件的需要保证让各个客户端的名字和端口不要冲突。


## 1.3. 附，一些成功的配置文件参考
### 1.3.1. 配置文件

#### 1.3.1.1. 服务端，简版conf1
```conf
[common]
# 服务器端端口
bind_port = 7000
# 客户端连接凭证
privilege_token = test12345678
# 最大连接数
max_pool_count = 5
# 客户端映射的端口
vhost_http_port = 80
# 服务器看板的访问端口
dashboard_port = 7500
# 服务器看板账户
dashboard_user = admin
dashboard_pwd = test12345678
```

#### 1.3.1.2. conf2
```conf
[common]
bind_addr = 0.0.0.0
bind_port = 7000
bind_udp_port = 7001

kcp_bind_port = 7000
# proxy_bind_addr = 127.0.0.1

vhost_http_port = 81
vhost_https_port = 444
# vhost_http_timeout = 60

dashboard_addr = 0.0.0.0
dashboard_port = 7500
dashboard_user = admin
dashboard_pwd = admin

# trace, debug, info, warn, error
log_file = ./frps.log
log_level = info
log_max_days = 3

# auth token
token = 12345678

# only allow frpc to bind ports you list, if you set nothing, there won't be any limit
allow_ports = 2000-3000,3001,3003,4000-50000

# pool_count in each proxy will change to max_pool_count if they exceed the maximum value
max_pool_count = 5
# max ports can be used for each client, default value is 0 means no limit
max_ports_per_client = 0

# if subdomain_host is not empty, you can set subdomain when type is http or https in frpc's configure file
# when subdomain is test, the host used by routing is test.frps.com
subdomain_host = 34.90.129.214

# if tcp stream multiplexing is used, default is true
tcp_mux = true
```


### 1.3.2. frpc

```bash
[common]
server_addr = 34.90.129.214
server_port = 7000
token = test12345678

[ssh_6002]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6002
```


# zerotier

实现内网穿透，p2p的连接方式。访问端必须安装需要通信的软件。

```bash
# 安装
curl -s https://install.zerotier.com | bash

# 启动
zerotier-one -d

# 获取地址和服务状态
zerotier-cli status

# 加入、离开、列出网络
zerotier-cli join b6079f73c63927ea  # Network ID
zerotier-cli leave b6079f73c63927ea  # Network ID
zerotier-cli listnetworks
```


# tailscale

万能安装：
```bash
# docker
# https://hub.docker.com/r/tailscale/tailscale
# docker run -d --name=tailscaled -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --privileged tailscale/tailscale tailscaled
# docker run -d --name=tailscaled -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --privileged tailscale/tailscale tailscaled
# 启动
docker run -d --name=tailscaled -v /dev/net/tun:/dev/net/tun --network=host --privileged tailscale/tailscale tailscaled
# 登录
docker exec tailscaled tailscale up
# 查看状态
docker exec tailscaled tailscale status
```

nas中安装
```bash
# ps: nas 中使用， 安装 Container Station 应用，随后 docker 打开 centos7， 设置网络模式为Host， 打开shell进行常规安装：
# !!!!  注意： /dev/net/tun 必须是套接字文件，如果系统中不存在，需要手动安装 参考mkinfo命令 或者从一台centos打包/dev/net/tun过来。
#
docker stop centos7_nat
docker rm centos7_nat
#
docker run --name centos7_nat -v /dev/net/:/dev/net/ --network=host --privileged=true -dit centos:centos7 /usr/sbin/init
docker exec -it centos7_nat bash
# rm /dev/net/tun
```

Linux 常规安装
```bash
# 安装
curl -fsSL https://tailscale.com/install.sh | sh
# 登录
tailscale up

systemctl enable --now tailscaled
systemctl start tailscaled

# 装好后启动：
docker start centos7_nat  # 容器启动
docker exec centos7_nat tailscale up  # 登录
docker exec centos7_nat tailscale status  # 查看内网设备

# 登录管理账户, 关系秘钥自动90天失效
```


```bash
# https://github.com/tailscale/tailscale-synology

cd
# qnaq
# 去官网下载 https://github.com/ivokub/tailscale-qpkg.git
# 手动安装 如： Tailscale_v1.20.4_x86.qpkg
# 然后
cd `getcfg SHARE_DEF defVolMP -f /etc/config/def_share.info`/.qpkg/Tailscale
./Tailscale.sh start  # 通过逐步运行命令找到报错 /dev/net/tun 不是套接字文件
./tailscale up
./tailscale -socket var/run/tailscale/tailscaled.sock up

# 群辉
wget https://github.com/tailscale/tailscale-synology/archive/refs/tags/v1.20.1.zip
unzip v1.20.1.zip
cd tailscale-synology-1.20.1/
make
```

## 局域网组网及连接目的主机方法

tailscale 软件进行局域网组网， smb协议直连目的主机。

1. 安装软件 tailscale
    - 官网地址：https://tailscale.com/download
    - 左击屏幕左下角开始菜单，在其中找到程序tailscale启动，一般在右下角程序栏中会出现图标，如果找不到可点击箭头符号查看折叠隐藏程序。
2. 登录账户
    - 右击tailscale软件, 选择 `Log in...`, 在弹出的网页界面选择 `Sign in with Microsoft` 进行登录 , 登录以下账号即可。
    - 账户： `xxx@outlook.com`
    - 密码： `xxxx`
3. 找到目的主机的名字及IP待用。 方法1: 
    - 当前目的主机名为 `xxx-qnap` , IP为 `100.144.21.70` , （*PS:* 目的主机默认开启445端口的smb协议访问）。
4. Windows 访问及映射
    - 在 文件资源管理器（我的电脑） 中直接进行磁盘映射(推荐), 或添加网络位置：
    - 格式为：`\\IP\访问目录` ， 如 `\\100.144.21.70\xxx_xxx`


> ***PS：***  
> 当新增设备时，需手动管理设备，在末尾点击三个点选择`Enable key expiry`以防止登录失效。 管理网址为: https://login.tailscale.com/admin/machines , 登录账户同上。



---
# 一些待测试博客

- [ ] [[高级项目] 树莓派内网穿透方法大全 - 知乎](https://zhuanlan.zhihu.com/p/108624497)
