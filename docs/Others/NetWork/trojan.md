
# 1. Trojan

## 1.1. 服务端配置

```bash
# yum -y install docker
# systemctl start docker
# docker run  -d -it --privileged --name centos7-trojan -p 80:80 -p 443:443 centos:centos7 bash
# docker exec -it centos7-trojan bash
mkdir -p /Public/nettools  &&  cd /Public/nettools
wget --no-check-certificate https://raw.githubusercontent.com/tcp-nanqinlang/general/master/General/CentOS/bash/tcp_nanqinlang-1.3.2.sh && chmod a+x tcp_nanqinlang-1.3.2.sh
./tcp_nanqinlang-1.3.2.sh
# # 单网卡
# wget https://github.com/tcp-nanqinlang/lkl-rinetd/releases/download/1.1.0-nocheckvirt/tcp_nanqinlang-rinetd-centos-nocheckvirt.sh
# bash tcp_nanqinlang-rinetd-centos-nocheckvirt.sh

wget --no-check-certificate -O tcp.sh https://github.com/cx9208/Linux-NetSpeed/raw/master/tcp.sh && chmod +x tcp.sh
./tcp.sh

wget https://github.com/V2RaySSR/Trojan/raw/master/Trojan.sh
chmod a+x Trojan.sh
sed -i 's#~/.acme.sh/acme.sh#~/.acme.sh/acme.sh --register-account -m 1170101471@qq.com #g' Trojan.sh
./Trojan.sh
# 打开证书授权网站注册邮箱。[证书 - ZeroSSL](https://app.zerossl.com/certificates)
# 修改两行：
# git clone https://github.com/acmesh-official/acme.sh.git
# cd .acme.sh
# ./acme.sh --install -m 1170101471@qq.com
# ~/.acme.sh/acme.sh --register-account -m 1170101471@qq.com
# [Tue Oct 12 22:33:04 CST 2021] ACCOUNT_THUMBPRINT='YFQJJx7tZt91whTCI-xiSxSPoUcJPEJ1eNDpblNKn9U'
```

```bash
# 证书升级
~/.acme.sh/acme.sh --update-account
# 5.后期维护命令
acme.sh --list  # 列出所有证书
# acme.sh --renew -d soulchild.site -d *.soulchild.site --force  # 手动强制更新证书
# acme.sh --renew-all  # 手动更新所有证书
# acme.sh --revoke  # 撤销证书
# acme.sh --remove -d soulchild.site  # 删除证书
# acme.sh --cron  # 通过cronjob更新所有证书。
# acme.sh --upgrade  # 升级acme.sh
# acme.sh --uninstall  # 卸载acme.sh
```

```bash
systemctl restart nginx.service
# 申请https证书
mkdir /usr/src/trojan-cert
curl https://get.acme.sh | sh

your_domain=gzscbio.ga
~/.acme.sh/acme.sh --register-account -m 1170101471@qq.com   --issue  -d $your_domain  --webroot /usr/share/nginx/html/
~/.acme.sh/acme.sh --register-account -m 1170101471@qq.com   --installcert  -d  $your_domain   \
    --key-file   /usr/src/trojan-cert/private.key \
    --fullchain-file /usr/src/trojan-cert/fullchain.cer \
    --reloadcmd  "systemctl force-reload  nginx.service"

# if test -s /usr/src/trojan-cert/fullchain.cer; then
# cd /usr/src
# wget https://github.com/trojan-gfw/trojan/releases/download/v1.13.0/trojan-1.13.0-linux-amd64.tar.xz
# wget https://github.com/trojan-gfw/trojan/releases/download/v1.14.0/trojan-1.14.0-linux-amd64.tar.xz
# tar xf trojan-1.*
# 下载trojan客户端
# wget https://github.com/atrandys/trojan/raw/master/trojan-cli.zip
# unzip trojan-cli.zip
\cp /usr/src/trojan-cert/fullchain.cer /usr/src/trojan-cli/fullchain.cer
systemctl force-reload trojan
```

```bash
your_domain=gzscbio.ga
~/.acme.sh/acme.sh --renew -d $your_domain
~/.acme.sh/acme.sh --renew -d $your_domain  --force

# crontab -e
# "/root/.acme.sh"/acme.sh --cron --home "/root/.acme.sh"
```


---
### 1.1.1. 手动配置

```bash
yum -y install epel-release
# 运行yum makecache生成缓存
yum makecache
# 然后更新
yum update
yum -y install gcc automake autoconf libtool make

# 查看防火墙状态
firewall-cmd --state
# 停止firewall
systemctl stop firewalld.service
# 禁止firewall开机启动
systemctl disable firewalld.service 
```

```bash
git clone https://github.com/trojan-gfw/trojan.git
cd trojan/
mkdir build
cd build/
cmake ..
make
ctest
sudo make install
```

### Acme 脚本申请证书

```bash
# yum update -y          #CentOS 命令
yum install -y curl    #CentOS 命令
yum install -y socat    #CentOS 命令

curl https://get.acme.sh | sh

# 2021 年 6 月 17 日更新：
# 从 acme.sh v 3.0.0 开始，acme.sh 使用 Zerossl 作为默认 ca，您必须先注册帐户（一次），然后才能颁发新证书。
# 具体操作步骤如下：
# 1、安装 Acme 脚本之后，请先执行下面的命令（下面的邮箱为你的邮箱）
~/.acme.sh/acme.sh --register-account -m xxxx@xxxx.com
# 2、其他的命令暂时没有变动

```
### Acme 脚本删除证书

```bash

```


修复方法记录：
```bash
# "/root/.acme.sh"/acme.sh --cron --home "/root/.acme.sh" --force
"/root/.acme.sh"/acme.sh --revoke 
```

### 更改端口

修改 /usr/local/etc/trojan/config.json 配置文件里面的443来改trojan端口



## 1.2. 客户端配置

```bash
export PATH=/usr/src/trojan/:$PATH

# 改完执行 ，然后用域名+新端口进去就行了
trojan restart
systemctl restart trojan-web

trojan updateWeb
trojan update
```



# 2. 其他

```bash
wget -P /root -N --no-check-certificate "https://raw.githubusercontent.com/mack-a/v2ray-agent/master/install.sh" && chmod 700 /root/install.sh && /root/install.sh
```

## docker 

```bash
sudo mkdir /etc/trojan
cd /etc/trojan
# 将下载的包中的配置文件和cer证书放在该目录
ls
# config.json  CONTRIBUTORS.md  examples  fullchain.cer  LICENSE  README.md
# 编辑config.json，将local_addr改为0.0.0.0
docker pull trojangfw/trojan
# 启动
docker run -dt --name trojan -v /etc/trojan/:/config -p 11080:1080 trojangfw/trojan
# 通过SwitchyOmega使用0.0.0.0 11080，查看状态
# 可以查看日志
docker logs -f trojan
mkdir /etc/trojan

```


```bash
SSPASSWORD=asdofqjsnfoqwgrjqwdjgfp
docker run -d --name container1 -p 9001:9001 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 9001 -k $SSPASSWORD -m aes-256-cfb


```