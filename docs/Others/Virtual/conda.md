# 1. Conda的基本使用

## 1.1. 配置镜像源
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

```cfg
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - defaults
show_channel_urls: true
```

- 取出`待查找类D`：将`当前查找类D`放入到`查找列表__mro__`
- 判断1：`待查找类D`的所有`父类`及`父类的父类`是否还未遍历完毕？
  - 否，则取出object，放入到`查找列表__mro__`，【查找结束】
  - 是，准备从`当前查找类`继续向上查找剩余的父类，进行判断2。
    - 判断2：`待查找父类`是否是Object。
      - 是，重置`当前查找类`为`待查找类D`，回到判断1
      - 否，进行判断3
        - 判断3：`待查找父类`是否包含其他子类，且子类满足`待查找类D`的父类或父类的父类。
          - 是，则暂时跳过该 `待查找父类` 的查找，将`父类`的下一个满足是`待查找类D`的条件的子类取出放入到`查找列表__mro__`
          - 否，则将`待查找父类`取出放入到`查找列表__mro__`
        - 准备从`当前查找类`继续向上查找它的父类。回到判断2

## 1.2. 环境配置

```bash
conda info --envs # 查看环境
conda list  # 查看当前环境conda install安装的软件

### 1. 环境创建与软件安装
# -n/--name 参数后面跟一个名字
# conda create -n myenv
conda create --name test_py3   # 创建一个环境, 名为test_py3
conda activate test_py3  # 激活使用test_py3环境
conda install python=3.6  # 安装python并指定版本
conda deactivate # 退出当前环境

# 等同于
# 基于 python2.7 创建一个名为test_py2 的环境
conda create --name test_py2 python=2.7
# 基于 python3.6 创建一个名为test_py3 的环境，并安装python3.6
conda create --name test_py3 python=3.6

### 2. 环境的使用
# 激活 test 环境， 即可使用不同版本的python
conda activate test_py2  # python2环境
conda activate test_py3  # python3环境

### 3. 删除环境（不要乱删啊）
conda remove -n test_py3  # 移除环境
conda remove -n test_py3 --all  # 移除环境，包括环境下的所有其他文件
```


## 1.3. 安装软件
从conda网页内查找：http://bioconda.github.io/conda-recipe_index.html
- conda search PACKAGENAME：运行命令查找是否存在
- conda 安装R语言以及R包示例

### 1.3.1. 示例

#### 1.3.1.1. 创建单独环境
```python
conda info --envs # 查看环境
conda create -n R3.6 # 创建名为R3.6的环境
source activate R3.6  
conda list           # 查看当前安装的软件
conda install r-base # 安装R语言
conda install r-stringi # R包 以 r- 开头 
conda deactivate     # 退出当前环境
```

#### 1.3.1.2. 安装指定版本
- conda install numpy=1.11：即安装能模糊匹配到numpy版本为1.11
- conda install numpy==1.11：即精确安装numpy为1.11的版本

```bash
conda install R=3.6
```

---

参考
- conda 安装R语言及其R包 - 简书  
  https://www.jianshu.com/p/a5e572bc5da5


## 1.4. Conda环境更名

比如，想把环境 rcnn 重命名成 tf

第1步

```bash
conda create -n tf --clone rcnn  # 将rcnn克隆为tf
conda remove -n rcnn --all
```


## 1.5. conda环境的迁移

参考：[conda环境迁移到其他机器上_ysq319的博客-CSDN博客_conda 环境迁移](https://blog.csdn.net/ysq319/article/details/102773615)

原环境：首先在conda的终端激活自己想要迁移的环境，然后生成自己的环境文件
```bash
conda activate your_env
conda env export > your_env.yaml
pip freeze > requirements.txt
```
新环境：在另一台机器上的conda终端克隆迁移的环境即可
```bash
conda env create -f your_env.yaml
pip install -r requirements.txt
```

> 注意：在环境移植的过程中，如果想要在不联网的情况下直接复制别的机器或者自己的环境，可以将env下面对应的环境直接进行拷贝，（只适用于anacoda大版本相近。anaconda2与3应该是不行的因为对应路径就已经有了变化），直接将整个环境复制然后全部拷贝到新环境的路径文件夹中。
