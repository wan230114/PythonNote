# 免密登录

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
vim ~/.ssh/authorized_keys  # 将客户端的key粘贴进来
chmod 600 ~/.ssh/authorized_keys
```

