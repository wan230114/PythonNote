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


# 手动安装

```bash
unzip proxychains-ng.zip
./configure --prefix=$PWD/install
make
make install
mkdir install/clean_bin/
sed -i "s#^socks4#\#socks4#" ./src/proxychains.conf
echo -e "socks5 \t127.0.0.1 2049" >>./src/proxychains.conf
# echo -e "socks5 \t127.0.0.1 1080" >>./src/proxychains.conf
echo $PWD/install/bin/proxychains4 -f $PWD/src/proxychains.conf '$@' >>install/clean_bin/proxychains4
chmod a+x install/clean_bin/proxychains4
echo 'export PATH='$PWD/install/clean_bin/':$PATH' >>~/.bashrc
```

