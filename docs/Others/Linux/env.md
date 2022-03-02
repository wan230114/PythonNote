
```bash
a=123

echo 'echo a:$a' >a.sh
echo 'echo do ok.' >do.sh
chmod a+x do.sh

export PATH=$PWD/:$PATH

do.sh

# 1. 直接运行命令
echo a:$a
# a:123

# 2. `. shell.script`相当于将脚本内容加载到当前环境运行
. a.sh 
# a:123

# 3. `sh shell.script`创建新的子环境
sh a.sh 
# a:

```