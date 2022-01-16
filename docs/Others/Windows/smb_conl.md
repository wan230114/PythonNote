
搜索关键词： [smb win 其他端口](https://cn.bing.com/search?q=smb+win+%E5%85%B6%E4%BB%96%E7%AB%AF%E5%8F%A3)

参考教程 ： [Win10突破公网限制，实现通过非标端口访问公网Samba服务 - 无限时光 - 既见君子,云胡不喜,浅喜如苍狗,深爱似长风](https://blog.netimed.cn/archives/Linux/20191217/182.html)


---
## 1. 开启转发服务

启动 windows 的 ip helper 服务

这个 ip helper 服务，就是用来搞端口转发的，没有了它就没法转发了。

用管理员身份打开cmd，运行以下命令：

```cmd
sc config LanmanServer start= disabled
net stop LanmanServer
sc config iphlpsvc start= auto
```


---
## 2. 设置端口转发
```powershell
# 设置转发
netsh interface portproxy add v4tov4 listenport=445 listenaddress=127.0.0.1 connectport=4450 connectaddress=gzsc.myqnapcloud.cn

# 查看转发
netsh interface portproxy show all
# 侦听 ipv4:                 连接到 ipv4:
# 地址            端口        地址            端口
# --------------- ----------  --------------- ----------
# 127.0.0.1       445         gzsc.myqnapcloud.cn 4450

# 查看445端口, 此处可能失败，见下一步
netstat -ano|findstr 445
#   TCP    127.0.0.1:9993         127.0.0.1:50445        TIME_WAIT       0
```

---
## 3. 安装 smb1.0

打开后检测 smb 1.0 是否已经开启，如果未开启需要安装。具体方法为：打开控制面板，然后点击程序，找到打开或关闭Windows功能，找到smb 1.0相关勾选，全选，全部安装。

对于 Windows 8、Windows 10 和 Windows Server 2012命令如下：

```powershell
Get-SmbServerConfiguration | Select EnableSMB1Protocol
# 正常开启的显示内容
# EnableSMB1Protocol
# ------------------
#               True
# 查看445端口
netstat -ano|findstr 445
#   TCP    127.0.0.1:9993         127.0.0.1:50445        TIME_WAIT       0
```

---
## 4. 访问及映射

在 文件资源管理器（我的电脑） 中添加网络位置，或直接进行磁盘映射：

```shell
//127.0.0.1/gzsc_project
```

