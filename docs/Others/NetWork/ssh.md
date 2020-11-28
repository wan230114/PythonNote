ssh 高阶用法

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