# Conda的基本使用

## 配置镜像源
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda
conda config --set show_channel_urls yes
conda config --show
```


```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

```bash
channels:
  - https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/conda
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  - bioconda
  - defaults
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - conda-forge
show_channel_urls: true
```


---
```config
channels:                                                                                                                                                                                                         
  - bioconda
  - conda-forge
  - defaults
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
show_channel_urls: true
```

## 环境配置
```bash
conda info --envs # 查看环境
conda create -n myenv  # 创建一个环境
source activate myenv  # 激活进入 myenv环境
conda deactivate # 退出当前环境
conda env remove --name myenv # 移除环境
```

```bash
# 基于 python3.6 创建一个名为test_py3 的环境
conda create --name test_py3 python=3.6 

# 基于 python2.7 创建一个名为test_py2 的环境
conda create --name test_py2 python=2.7

# 激活 test 环境
activate test_py2  # windows
source activate test_py2 # linux/mac

# 切换到python3
activate test_py3
```

删除环境（不要乱删啊啊啊）

```bash
conda remove -n py36 --all
```

## 安装软件
从conda网页内查找：http://bioconda.github.io/conda-recipe_index.html
- conda search PACKAGENAME：运行命令查找是否存在
- conda 安装R语言以及R包示例

## 示例

### 创建单独环境
```python
conda info --envs # 查看环境
conda create -n R3.6 # 创建名为R3.6的环境
source activate R3.6  
conda list           # 查看当前安装的软件
conda install r-base # 安装R语言
conda install r-stringi # R包 以 r- 开头 
conda deactivate     # 退出当前环境
```

### 安装指定版本
- conda install numpy=1.11：即安装能模糊匹配到numpy版本为1.11
- conda install numpy==1.11：即精确安装numpy为1.11的版本

```bash
conda install R=3.6
```

---

参考
---

- conda 安装R语言及其R包 - 简书  
  https://www.jianshu.com/p/a5e572bc5da5

