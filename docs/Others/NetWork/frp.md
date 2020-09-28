
# 1. frp的基本配置
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
