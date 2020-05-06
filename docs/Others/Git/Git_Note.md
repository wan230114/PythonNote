GIT
==========================

[TOC]

## 1. GIT简介

1. 什么是GIT

    - git是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件。

2. 代码管理工具的用途

    - * 防止代码丢失，做备份
    - * 项目的版本管理和控制，可以通过设置节点进行跳转
    - * 建立各自的开发环境分支，互不影响，方便合并
    - * 在多终端开发时，方便代码的相互传输

3. git的特点

    - * git是开源的，多在*nix下使用，可以管理各种文件
    - * git是分布式的项目管理工具(svn是集中式的)
    - * git数据管理更多样化，分享速度快，数据安全
    - * git 拥有更好的分支支持，方便多人协调

4. git安装

    - sudo apt-get install git

## 2. GIT使用

![git结构](img/git.jpeg)

![git结构2](img/git.png)

### 2.1. 基本概念

* 工作区：项目所在操作目录，实际操作项目的区域
* 暂存区: 用于记录工作区的工作（修改）内容
* 仓库区: 用于备份工作区的内容
* 远程仓库: 远程主机上的GIT仓库

    - 注意： 在本地仓库中，git总是希望工作区的内容与仓库区保持一致，而且只有仓库区的内容才能和其他远程仓库交互。

### 2.2. 初始配置

    - 配置命令: `git config`  
    - 
    - * 配置所有用户： `git config --system [选项]`  
    - 配置文件位置:  /etc/gitconfig
    - 
    - * 配置当前用户： `git config --global [选项]`  
    - 配置文件位置:  ~/.gitconfig  
    - 
    - * 配置当前项目： `git config  [选项]`  
    - 配置文件位置:  project/.git/config  

1. 配置用户名

    e.g. 将用户名设置为Tedu
    ```
    sudo git config --system user.name Tedu
    ```

2. 配置用户邮箱

    e.g. 将邮箱设置为lvze@tedu.cn
    ```
    git config --global user.email lvze@tedu.cn
    ```

3. 配置编译器

    e.g. 配置编译器为pycharm
    ```
    git config core.editor pycharm
    ```

4. 查看配置信息

    ```
    git config --list
    ```

### 2.3. 基本命令

1. 初始化仓库

    - `git init`   
    - 意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理

2. 查看本地仓库状态

    - `git status`
    - 说明: 初始化仓库后默认工作在master分支，当工作区与仓库区不一致时会有提示。

3. 将工作内容记录到暂存区

    - `git add [files..]`

        e.g. 将 a ，b 记录到暂存区
        ```
        git add  a b
        ```
        e.g. 将所有文件（不包含隐藏文件）记录到暂存区
        ```
        git add  *
        ```

4. 取消文件暂存记录

    -  `git rm --cached [file]` 

5. 将文件同步到本地仓库

    - `git commit [file] -m [message]`
    - 说明: -m表示添加一些同步信息，表达同步内容

        e.g.  将暂存区所有记录同步到仓库区
        ```
        git commit  -m 'add files'
        ```

6. 查看commit 日志记录

    - `git log`  
    - `git log --pretty=oneline`  
    - `git log --oneline -5` 查看最近5次commit的简要信息，输出信息为：简短commitID commit_message

7. 比较工作区文件和仓库文件差异

    - `git diff  [file]`

8. 放弃工作区文件修改

    - `git checkout -- [file]`

9. 从仓库区恢复文件

    - `git checkout [file]`

10. 移动或者删除文件

    - `git  mv  [file] [path]`  
    - `git  rm  [files]`  
    - 注意: 这两个操作会修改工作区内容，同时将操作记录提交到暂存区。

### 2.4. commit节点控制

1. 退回到上一个commit节点

   - `git reset --hard HEAD^`
   - 注意 ： 一个^表示回退1个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致

2. 退回到指定的 commit_id 节点

   - `git reset --hard [commit_id]`

3. 删除中间某个指定的 commit_id 节点
   - `git log --oneline -10`  查看最近10次提交（根据实际情况调节10），找到想要删除的前面一次的 commit_id
   - `git rebase -i commit_id`  自动进入编辑模式，将需要删除的commit_id行最前面由`pick`改为`drop`，保存退出
   - `git push -f`  强制提交


### 2.5. 版本控制


1. 查看所有操作记录

   - `git reflog`
   - 注意:最上面的为最新记录，可以利用commit_id去往任何操作位置

2. 创建标签

   - 标签: 在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。
   - `git tag [tag_name] [commit_id] -m [message]`
   - 说明: commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。

        e.g. 在最新的commit处添加标签v1.0
        ```
        git tag v1.0 -m '版本1'
        ```

3. 查看标签

   - `git tag`  查看标签列表
   - `git show [tag_name]`  查看标签详细信息

4. 去往某个标签节点

   - `git reset --hard [tag]`

5. 删除标签

   - `git tag -d  [tag]`


### 2.6. 保存工作区

1.  保存工作区内容

    - `git stash save [message]`
    - 说明: 将工作区未提交的修改封存，让工作区回到修改前的状态

2. 查看工作区列表

    - `git stash  list`
    - 说明:最新保存的工作区在最上面

3. 应用某个工作区

    - `git stash  apply  [stash@{n}]`

4. 删除工作区

    - `git stash drop [stash@{n}]`  删除某一个工作区
    - `git stash clear`  删除所有保存的工作区


### 2.7. 分支管理

- 定义: 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，单独开发，互不干扰。完成开发工作后再进行分支统一合并。

![](img/merge.png)

1. 查看分支情况

    - `git branch`
    - 说明: 前面带 * 的分支表示当前工作分支

2. 创建分支

    - `git branch [branch_name]`
    - 说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支"干净"状态。

3. 切换工作分支

    - `git checkout [branch]`
    - 说明: 2,3可以同时操作，即创建并切换分支
    - `git checkout -b [branch_name]`

4. 合并分支

    - `git merge [branch]`

    - 冲突问题是合并分支过程中最为棘手的问题
    - 当分支合并时，原分支和以前发生了变化就会产生冲突
    - 当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需自己决定commit操作即可。
    - 当合并分支时两个分支修改了同一个文件，则需要手动解决冲突。

5. 删除分支

    - `git branch -d [branch]`  删除分支
    - `git branch -D [branch]`  删除没有被合并的分支

### 2.8. 远程仓库

1. 什么是远程仓库

    - 远程主机上的git仓库。实际上git是分布式结构，每台主机的git仓库结构类似，只是把别人主机上的git仓库称为远程仓库。

2. 共享仓库

    - 在git仓库中bare属性为True的共享仓库可以很好的和远程仓库进行交互

    - 创建步骤：

    * 选择共享仓库目录，将该目录属主设置为当前用户

        ```
        mkdir gitrepo
        chown tarena:tarena gitrepo
        ```

    * 将该目录初始化为git共享目录，下例中tedu为自己取的项目名称，.git为通用结尾后缀

        ```
        cd gitrepo
        git init --bare tedu.git
        ```

    * 将git配置目录与项目目录设置为相同的属主

        ```
        chown -R tarena:tarena tedu.git
        ```

#### 2.8.1. 远程仓库操作命令

所有操作在本地git仓库下进行

1. 添加远程仓库

    ```
    git remote add origin \
        tarena@127.0.0.1:/home/tarena/gitrepo/tedu.git
    ```

2. 删除远程主机

    - `git remote rm [origin]`

3. 查看连接的主机

    - `git remote`
    - 注意: 一个git项目连接的远程主机名不会重复

4. 将本地分支推送给远程仓库

    - 将master分支推送给origin主机远程仓库，第一次推送分支使用-u表示与远程对应分支建立自动关联
    - `git push -u origin  master`

5. 删除远程分支

    - `git branch -a`  查看所有分支
    - `git push origin  [:branch]`  删除远程分支

6. 其他推送方法

    - `git push --force origin`  用于本地版本比远程版本旧时强行推送本地版本
    - `git push origin [tag]`  推送本地标签到远程

7. 从远程获取项目

    - `git clone tarena@127.0.0.1:/home/tarena/gitrepo/tedu.git`
    - 注意： 获取到本地的项目会自动和远程仓库建立连接。且获取的项目本身也是个git项目。

8. 从远程获取代码

    - `git pull`
    - 将远程分支master拉取到本地，作为tmp分支
    - `git fetch origin  master:tmp`  

    - 区别
    - pull将远程内容直接拉取到本地，并和对应分支内容进行合并
    - fetch将远程分支内容拉取到本地，但是不会和本地对应分支合并，可以自己判断后再使用merge合并。

## 3. GitHub使用

1. 介绍

   - github是一个开源的项目社区网站，拥有全球最多的开源项目。开发者可以注册网站在github建立自己的项目仓库。

   - 网址： github.com

   - 代码管理工具：git

2. 获取项目

   * 搜索项目，选择想要的项目

   * 复制git地址

   * 通过clone 下载到本地

3. 创建仓库

   * 右上角+下拉 new repository

   * 填写基本的仓库信息 点击创建

   * 创建新仓库之后github仓库即为远程仓库

4. 删除仓库

   * 右上角头像下拉

   * 选择自己的仓库，选择项目

   * 在settings中最后有删除选项

5. 秘钥添加

   * 在个人主机上使用ssh-keygen获取密钥对（通常在~/.ssh目录下）

   * 将id_rsa.pub（公钥）内容复制，添加到github中

   * 右上角头像下来，settings->SSH and GPG keys->new ssh key,内容粘贴到keys文本框

