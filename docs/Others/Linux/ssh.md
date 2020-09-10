# 免密登录

将客户端的用户密匙 ~/.ssh/id_rsa.pub 文本内容复制到服务端的 ~/.ssh/authorized_keys

并将服务端 ~/.ssh/authorized_keys 改权限为600

这样从客户端ssh登录到服务端可以免密

```bash
cat ~/.ssh/id_rsa.pub  # 客户端

mkdir ~/.ssh
chmod 700 ~/.ssh
vim ~/.ssh/authorized_keys  # 服务端

chmod 600 ~/.ssh/authorized_keys
```

---
补充：  
```bash
# 客户端生成key
ssh-keygen -t rsa
```
