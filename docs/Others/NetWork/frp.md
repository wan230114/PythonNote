## 下载软件

```bash
# 访问： https://github.com/fatedier/frp
# 点击release： https://github.com/fatedier/frp/releases/
# 点击下载对应版本如： https://github.com/fatedier/frp/releases/download/v0.33.0/frp_0.33.0_linux_arm64.tar.gz

wget https://github.com/fatedier/frp/releases/download/v0.33.0/frp_0.33.0_linux_arm64.tar.gz

tar xzvf frp*.tar.gz
cd frp*
```

# frps
## 配置文件

### conf1
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

### conf2
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


# frpc

```bash
[common]
server_addr = 34.90.129.214
server_port = 7000

[ssh_6002]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6002
```
