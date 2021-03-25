# CentOS

```bash
yum -y install git gcc automake autoconf libtool make
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure
make && make install
cp ./src/proxychains.conf /etc/proxychains.conf
# vim /etc/proxychains.conf
sed -i "s#^socks4#\#socks4#" /etc/proxychains.conf
echo -e "socks5 \t127.0.0.1 1080" >>/etc/proxychains.conf
cd .. && rm -rf proxychains-ng
```

# Ubuntu

```bash
apt install proxychains4  # 18.04+
apt install proxychains  # 16.04

vim /etc/proxychains.conf
```