## 免密登录

1. 将客户端的用户密匙 ~/.ssh/id_rsa.pub 文本内容复制到服务端的 ~/.ssh/authorized_keys

2. 将服务端 ~/.ssh/authorized_keys 改权限为600

这样从客户端ssh登录到服务端可以免密

```bash
# 实现从客户端连接服务端免密登录：
## 客户端
cat ~/.ssh/id_rsa.pub  # 若没有则执行 `ssh-keygen -t rsa` 生成

## 服务端
# ssh xxx@xxx.xxxx  # 进入服务器
mkdir -p ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
vim ~/.ssh/authorized_keys  # 将客户端的key粘贴进来
```


## 其他
### ssh 高阶用法

```bash
cd ~/.ssh
ssh-keygen -t rsa -C "user@email.com"
```
#### CMD: `ssh-agent`
```bash
# ssh-agent即为ssh代理程序,需要写到.bashrc
ssh-agent $SHELL # pstree
ssh-add /home/.ssh/id_novo
ssh-add /home/.ssh/id_rsa
```
### File: `~/.bashrc`
```bash
ssh-add &>/dev/null || eval `ssh-agent` &>/dev/null # start ssh-agent if not present
[ $? -eq 0 ] && { # ssh-agent has started
ssh-add ~/.ssh/your_private.key1 &>/dev/null # Load key 1
ssh-add ~/.ssh/your_private.key2 &>/dev/null # Load key 2
}
```
#### CMD: `ssh-add`
```bash
# ssh-add命令是把私有密钥添加到ssh-agent的代理中
ssh-agent fish/bash
ssh-add /home/.ssh/id_novo
    -D：删除ssh-agent中的所有密钥.
    -d：从ssh-agent中的删除密钥
    -L：显示ssh-agent中的公钥
    -l：显示ssh-agent中的密钥
    -t life：对加载的密钥设置超时时间,超时ssh-agent将自动卸载密钥
    -X：对ssh-agent进行解锁
    -x：对ssh-agent进行加锁
```
#### File: `~/.ssh/config`
```bash
Host nj
	Hostname 192.168.96.2
	User Test
	PreferredAuthentications publickey
	IdentityFile /home/.ssh/id_novo
```