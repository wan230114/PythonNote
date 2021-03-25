# tinc

[使用 Tinc 组建大内网 | 梓喵](https://zimiao.moe/posts/53555/)

[用 tinc 组建局域网其实也简单 | 好运博客](http://www.lucktu.com/archives/763-3.html)

[tinc-1.1pre17在linux下的部署 - 终点站](https://gofinall.com/89.html)



---
## install

- Windows： https://www.tinc-vpn.org/packages/windows/tinc-1.0.35-install.exe
- Windows： https://www.tinc-vpn.org/packages/windows/tinc-1.1pre17-install.exe
- Android： https://tincapp.pacien.org/
- IOS： https://www.tinc-vpn.org/packages/cydia/

- Linux：如下（目前成功测试 CentOS / MacOS ）

```bash
yum -y install gcc readline-devel zlib-devel lzo-devel openssl-devel ncurses-devel
proxychains4 wget https://www.tinc-vpn.org/packages/tinc-1.1pre17.tar.gz
# 安装编译环境
# 解压
tar -xvf tinc-1.1pre17.tar.gz
# 编译安装
cd tinc-1.1pre17
./configure --prefix=/usr   # ./configure
make
make install

# 后续使用路径报错解决
ln -s /var/ /usr/local/
ln -s /usr/local/etc/tinc /etc/
```

其他系统
```bash
# Debian/Ubuntu
apt-get install tinc
# ArchLinux
pacman -S tinc
```

MacOS（暂时未用到，安装频繁出问题）
```bash
# brew install tinc --devel
brew install tinc
brew install tuntap --cask
kextstat |grep -e tun -e tap  # 查看tuntap是否安装成功, 如果失败请看：[使用tinc构建虚拟专网](https://blogs.vicsdf.com/article/4114)
```


---
# server

```bash
# # 创建pid文件生成路径
# mkdir /var/run/
# # 创建配置文件路径
# mkdir /etc/tinc
# 路径报错解决
ln -s /var/ /usr/local/
ln -s /usr/local/etc/tinc /etc/
pkill -9 tincd
# 初始化server，格式: tinc -n 网络名称 init server名
tinc -n hello init server
# 启动tinc
tincd -n hello

IP_LOCAL=10.10.1.1
# 配置tinc的网段
tinc -n hello add subnet $IP_LOCAL
tinc -n hello add address 139.196.159.43

# 配置tinc启动后的网卡
echo 'ifconfig $INTERFACE '$IP_LOCAL' netmask 255.255.255.0'  >/etc/tinc/hello/tinc-up
echo 'ifconfig $INTERFACE down'  >/etc/tinc/hello/tinc-down
chmod a+x /etc/tinc/hello/tinc-*

# 修改配置
{
echo "Name = server
Address=139.196.159.43
Cipher=aes-256-cbc
Digest=sha512
Broadcast = mst
LocalDiscovery = yes
"  >/etc/tinc/hello/tinc.conf
cat /etc/tinc/hello/tinc.conf
}
# 配置说明：
# (1) 配置server的外网ip `curl ipv4.icanhazip.com 2>/dev/null`
# echo 'Address=139.196.159.43' >> /etc/tinc/hello/tinc.conf
# 
# (2) 配置加密方式(可选)
# echo 'Cipher=aes-256-cbc' >> /etc/tinc/hello/tinc.conf
# echo 'Digest=sha512' >> /etc/tinc/hello/tinc.conf\
# 
# (3) 设置广播包发到其他节点的方式(可选)
# 所有节点需要使用相同的方式, 否则可能会产生路由循环
# no 不发送广播包 
# mst 使用 Minimum Spanning Tree, 保证发往每个节点
# direct 只发送给直接访问的节点, 从其他节点接收到的不转发. 如果设置了 IndirectData, 广播包也会发送给有 meta 链接的节点
# 试验阶段
# no | mst | direct
# echo 'Broadcast = mst' >> /etc/tinc/hello/tinc.conf
# 
# (4) 尝试发现本机网络中的节点(可选)
# 允许与本地节点地址建立直接连接
# 目前, 本地发现机制是通过在 UDP 发现阶段发送本地地址的方式
# echo 'LocalDiscovery = yes' >> /etc/tinc/hello/tinc.conf
#

# 重启server
pkill -9 tincd
# # debug方式启动
# tincd -n hello -D -d3
# daemonize方式启动
tincd -n hello

######################################
# 服务端
# 邀请是向现有 VPN 添加新节点的一种简单方法。[Invitations (tinc Manual)](https://www.tinc-vpn.org/documentation-1.1/Invitations.html)
## wan230114.ml/ygpX-CPtlrICcZr8SN0fdDdzLjPRCeOgOSSqCjR2DmO3bgK
# server服务器上生成邀请连接 tinc -n 网络名称 invite 客户端名称
# 要求连接 server的外网ip/随机码
tinc -n hello invite junmac3
tinc -n hello invite vr3
# tinc -n hello invite GE60centos
# 139.196.159.43/LOhaE-f3qmi8DOxjPbn-kW5qYWmqKfwrCQpktljRDS-fyFO6
```



---
# client


## linux / mac

客户端列表：
- 10.10.1.1  vps_sh
- 10.10.1.2  junmac
- 10.10.1.3  GE60centos

```bash
# 0) 规定连入IP及主机名
clientName=junmac3
IP_LOCAL=10.10.1.2

clientName=GE60centos
IP_LOCAL=10.10.1.3

clientName=vr3
IP_LOCAL=10.10.1.4

echo $clientName $IP_LOCAL

# 1) 客户端加入server
tinc join 139.196.159.43:8598/skovW1If8ujtR52qk6IazwE3ggP-iBqAxf7MvUpjqgbTWB9K
# 正确日志：
# Connected to 222.222.222.222 port 655...
# ..................................................................+++ p
# ....................................................+++ q
# Configuration stored in: /etc/tinc/hello
# Invitation successfully accepted.

# 2) 启动tinc
tincd -n hello

# 3) 配置客户端的ip,需要和server的不一样,可以直接加1即可
tinc -n hello add subnet $IP_LOCAL
tinc -n hello add address 139.196.159.43
tinc -n hello add port 8598
cat /etc/tinc/hello/hosts/$clientName

# 4) 配置tinc启动后的网卡,下面的ip需要和上一步一样
# echo 'ip addr add '$IP_LOCAL'/24 dev $INTERFACE
# ip link set $INTERFACE up' >/etc/tinc/hello/tinc-up
echo 'ifconfig $INTERFACE '$IP_LOCAL' 10.10.1.1 up netmask 255.255.255.0'    >/etc/tinc/hello/tinc-up
echo 'ifconfig $INTERFACE '$IP_LOCAL' netmask 255.255.255.0'  >/etc/tinc/hello/tinc-up
echo 'ifconfig $INTERFACE down'  >/etc/tinc/hello/tinc-down
chmod a+x /etc/tinc/hello/tinc-*
cat /etc/tinc/hello/tinc-up
cat /etc/tinc/hello/tinc-down

# 5) 配置文件
{
# echo "Cipher=aes-256-cbc
# Digest=sha512
# LocalDiscovery = yes"  >>/etc/tinc/hello/tinc.conf
# Address=139.196.159.43
echo "Name = $clientName
ConnectTo = server
Address=139.196.159.43
Cipher=aes-256-cbc
Digest=sha512
Broadcast = mst
LocalDiscovery = yes"  >/etc/tinc/hello/tinc.conf
cat /etc/tinc/hello/tinc.conf
}

mkdir -p /usr/local/var/run/

# 重启server
pkill -9 tincd
sudo pkill -9 tincd
# debug方式启动
tincd -n hello -D -d3
sudo tincd -n hello -D -d3
# daemonize方式启动
tincd -n hello
```
