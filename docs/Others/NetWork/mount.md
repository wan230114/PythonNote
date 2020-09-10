
## smb

### 服务端

---
#### 服务端安装
```bash
yum install samba samba-client.x86_64 samba-common -y
systemctl start smb
systemctl stop firewalld.service
# samba的基本信息
# 主配置文件： vim /etc/samba/smb.conf      
# 端口：139/tcp 139/udp 445/tcp 445/udp
systemctl restart smb.service

vim /etc/samba/smb.conf
#  89         workgroup = westos     ##工作组的设定
#  90         server string = hello world  ##全局共享信息
#  91         hosts deny = 172.25.8.10     ##用户黑名单
#  92         hosts allow = 172.25.8.11    ##用户白名单
systemctl restart smb.service
# 测试 ：客户端  172.25.8.10  
yum install smaba-client -y
```

---
#### 自定义共享目录:
```bash
########## 服务端 ##########
mkdir /westos
semanage fcontext -a -t samba_share_t '/westos(/.*)?' ##开放当前目录的selinux安全上下文
ls -dZ /westos  # 安全上下文查看 
restorecon -FvvR /westos/
vim /etc/samba/smb.conf  # 见下
# /etc/samba/smb.conf 添加如下：
#[DATA]
#    comment = westos     ##描述
#    path = /westos     ##共享目录
systemctl restart smb
touch /westos/aa
# 设置账户密码：
useradd westos  # 添加系统账户
passwd westos  # 更新系统账户密码 test123456
smbpasswd -a westos  # 为该系统账户单独设置smb密码 test123

########## 客户端 ##########
# 在smb下命令与linux不同，为了方便操作我们通常将其挂载后使用
mkdir mount_22
mount //104.168.172.250/westos ./mount_22 -o username=westos,password=test123
# mount //104.168.172.250/westos /mnt -o username=westos,password=test123
# 客户端永久挂载 
vim /etc/fstab
# //172.25.8.11/westos /mnt cifs defaults,username=westos,password=westos 0 0
```

---
### 客户端


#### 匿名用户登录

```bash
# 服务端
vim /etc/samba/smb.conf
#  124 map to guest = bad user
#  321         [westos]
#  322         comment = westos
#  323         path = /westos
#  324         guest ok = yes                              ###匿名用户可以登陆
systemctl restart smb

# 客户端 
# 测试  IP:172.25.8.250
smbclient -L //104.168.172.250       ##没有密码直接回车 匿名登陆
mount //104.168.172.250/westos  /mnt/ -o username=guest   ##直接回车
df
```


### test

```bash
yum  -y  install  samba-client
smbclient -L //104.168.172.250       ##没有密码直接回车 匿名登陆
mount //104.168.172.250/mount ./mount_22 -o username=chenjun,password=cj123

```

---

### 实战
#### 服务端

**(1) 安装smaba服务**
```bash
yum install samba
# cp /etc/samba/smb.conf /etc/samba/smb.conf--bak
mkdir -p /share
semanage fcontext -a -t samba_share_t '/share(/.*)?' ##开放当前目录的selinux安全上下文
```
**(2) 编辑配置文件**
```bash
vim /etc/samba/smb.conf

```
添加
```
[share]             #文件名[]中的为网络中该目录的名称，path为本地路径
	comment = testuser
	path = /share    #此为你共享的路径
	valid users = testuser
	directory mask = 755
	writable = yes
	browseable = yes
```

**(3) 创建对应的系统账号**
```bash
useradd testuser
passwd testuser  #设置 test123456，任意，不重要
smbpasswd -a testuser  # 设置 test123
```

**(4) 启动smb等服务**
```bash
systemctl restart smb.service 
systemctl restart nmb.service
systemctl start smb.service 
systemctl start nmb.service
systemctl enable smb.service
systemctl enable nmb.service
```

#### 客户端

**(1) 创建挂载目录**
```bash
mkdir -p /mount/share
```

**(2) 挂载A服务器的共享文件到B服务器**
```bash
# yum install cifs-utils
smbclient //104.168.172.250/share  -U 'testuser%test123'
mount -t cifs //104.168.172.250/share /mount/share -o 'username=testuser,password=test123'
mount -t cifs //104.168.172.250/share /mount/share -o 'username=testuser,password=test123,gid=1000,uid=1000'
mount -t cifs //104.168.172.250/share /mount/share -o 'username=testuser,password=test123,gid=1000,uid=1000,dir_mode=0755,file_mode=0755'

umount /mount/share

# 挂载方法
mount -o username=账号,password=密码 //SMB服务器IP/共享目录 /挂载点
# smbclient链接
smbclient //SMB服务器IP/共享目录/ -U 账号%密码
```

**(3)设置开机自动挂载**
```bash
#chmod +X /etc/rc.local
#vi /etc/rc.local
mount -t cifs -o username=root,password='密码' //192.168.1.101/mnt/test/ /home/ceshi
```

备注：
```
//10.148.16.97/logs/    1008G   24G  934G    3% /home/mnt/logs
[root@localhost logs]# umount /home/mnt/logs/
umount: /home/mnt/logs：目标忙。
        (有些情况下通过 lsof(8) 或 fuser(1) 可以
         找到有关使用该设备的进程的有用信息)
退出挂载的目录即可。
```

备注2：
```bash
# 需要先安装
# yum install cifs-utils

# 另外指定smb相同版本，此参数在连接小黑盒时异常有用
mount -t cifs //192.168.3.12/gzsc_project/seqdate /work/download/seqdata_nas -o 'username=chenjun,password=n:L1!O,gid=1009,uid=1009,vers=2.0'
```


### test2

```bash
mount -t cifs //192.168.3.12/share /mount/share -o 'username=testuser,password=test123,gid=1000,uid=1000,dir_mode=0755,file_mode=0755'

```


## sshfs


```bash
sshfs -o nonempty,allow_other,exec   root@xx.xx.xx.xx:/test/zjy/ /test/zjy/
                #    参数                用户@地址:挂载到               挂载到

sshfs test@23.234.225.189:/home/test/share ./mount_22
sshfs -o allow_other,exec test@23.234.225.189:/home/test/share ./mount_22
sshfs -o uid=1000,gid=1000,idmap=file,uidfile=uid_map.txt,gidfile=gid_map.txt,umask=022   test@23.234.225.189:/home/test/share ./mount_22
sshfs -o nonempty,reconnect,allow_other,exec ray@gzscnas:/gzsc_project/seqdate /work/download/seqdata_nas
umount mount_22
```
参数：
- -o：
```
-o allow_other 允许访问其他用户
-o nonempty 允许安装在非空文件/DIR上
-o umask=022 换算成字母是，`----w--w-`，指取消组的写权限、取消其它用户的写权限。
-o umask = M设置文件权限（八进制）
-o uid = N设置文件所有者s
-o gid = N设置文件组
```

```bash
fusermount  -u  /test/zjy/
umount -f /test/zjy/
```