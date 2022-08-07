## 4. 极简笔记

### 4.1. 初始化

1. 初次使用git， 配置用户基本信息，名字和邮箱

```bash
# Git全局设置：
git config --global user.name "wan230114"
git config --global user.email "1170101471@qq.com"

# 远程身份验证密匙配置：
ssh-keygen -t rsa -C "1170101471@qq.com"   # 按三下enter
cat ~/.ssh/id_rsa.pub   # 将内容复制到 https://github.com/settings/ssh/new 内
```

2. 初次使用仓库 （初始化一个 git 仓库）

```bash
# git clone下载（全部克隆针对新的）
# git clone git@github.com:wan230114/mytools.git

# cd 切换到工程目录
git init
# git remote rm origin
# (你的远程仓库地址，即是码云的项目路径) //和远程仓库进行关联
git remote add origin git@github.com:wan230114/mytools.git
git remote add origin git@github.com:wan230114/Web_Data_Realese.git
# 克隆一个别人的仓库，修改之后提交保存在Git（PS：可以fork操作为自己仓库哦）
git remote rm origin
git remote add origin git@github.com:wan230114/MAPS.git


# 3. 上传文件
# 添加所有文件
git add -A
# "注释内容” //添加注释
git commit -a -m ":seedling: First init."
# git commit -a -m ":seedling: Updata chip && atac."
git push
git push -u origin master        # 上传仓库到云
git push origin master --force   # 强制上传
```

> *PS:*  
> ***`git add .`*** ：他会监控工作区的状态树，使用它会把工作时的所有变化提交到暂存区，包括文件内容修改(modified)以及新文件(new)，但不包括被删除的文件。  
> ***`git add -u`*** ：他仅监控已经被add的文件（即tracked file），他会将被修改的文件提交到暂存区。add -u 不会提交新文件（untracked file）。（git add --update的缩写）  
> ***`git add -A`*** ：是上面两个功能的合集（git add --all的缩写）


删除本地修改：
```bash
# !!! 此步操作需谨慎，可能清空本地代码，最好提前备份整个项目 !!!
git pull --rebase origin master  # 拉取合并代码
```


---
1. 分支管理

```bash
git status      # 查看当前分支及状态
git branch -a   # 查看当前所有分支
git branch rev-master # 创建分支
git checkout master   # 切换分支
git branch -d <分支名>  # 删除分支

# 切换分支文件冲突怎么办
git stash list  # 可以查看隐藏起来的工作现场
```

2. 版本管理

```bash
git log  # 获取commit信息
git rebase -i (commit-id)  # commit-id 为要删除的commit的下一个commit号
```


### 4.2. 技巧：版本回退

```bash
# 1) reset是指将HEAD指针指到指定提交，历史记录中不会出现放弃的提交记录。
# 【使用场景：如commit写错了，上一次的修改还想加点内容，都可以用这个】

# 回退commit,保留源码，默认方式。
git reset --mixed HEAD^

# 回退至某个版本，只回退commit信息
git reset --soft HEAD^

# 彻底回退到某个版本 【慎用！！！！ 此操作将导致你现在新修改的代码消失】
git reset --hard HEAD^

git reset HEAD^
git push origin master -f


# 2) revert是放弃指定提交的修改，但是会生成一次新的提交，需要填写提交注释，以前的历史记录都在；
git revert HEAD
git push origin master


# 技巧：版本回退+创建分支 

# 创建分支, 退回前一个分支
git branch revert-branch HEAD^
# 接下来切换到新的分支:
git checkout revert-branch
# sup:传授一个绝招：从master软恢复到新分支的HEAD。
# 软恢复将改变HEAD的状态，但并不影响工作树。
git reset --soft master
# 查看状态
git status
git commit -m "reverted to initial state."
```

### 4.3. 版本回退的详细语法

通过使用Git版本恢复命令reset，可以回退版本。
- reset命令有3种方式：
  - 此为默认方式，不带任何参数的git reset，即时这种方式，它回退到某个版本，只保留源码，回退commit和index信息　（本地代码貌似不会改变）
    - `git reset –mixed`
  - 回退到某个版本，只回退了commit的信息，不会恢复到index file一级。如果还要提交，直接commit即可
    - `git reset –soft`
  - 彻底回退到某个版本，本地的源码也会变为上一个版本的内容
    - `git reset –hard`

---
以下是一些reset的示例：
```bash
#回退所有内容到上一个版本
git  reset  HEAD^
#回退a.py这个文件的版本到上一个版本
git  reset  HEAD^  a.py
#向前回退到第3个版本
git  reset  –soft  HEAD~3
#将本地的状态回退到和远程的一样
git  reset  –hard  origin/master
#回退到某个版本
git  reset  057d
#回退到上一次提交的状态，按照某一次的commit完全反向的进行一次commit
git  revert  HEAD

#新建old_master分支做备份
git  branch  old_master
#push到远程
git  push  origin  old_master:old_master
#本地仓库回退到某个版本
git  reset  –hard  bae168
#删除远程的master分支
git  push  origin  :master
#重新创建master分支
git  push  origin  master
```

————————————————

版权声明：本文为CSDN博主「夜月独狼」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/YeYueDuLangcy/article/details/84820109



### 4.4. 恢复到远程目录

```bash
# git fetch --all
git fetch
git reset --hard origin/master
git pull  # 可以省略
```

实战：

```bash
git clone https://github.com/wan230114/PythonNote
# git clone https://gitee.com/wan230114/PythonNote
cd PythonNote
echo "#! /usr/bin/bash
git fetch 
git reset --hard origin/master 
git pull " >get_remote.sh
chmod +x get_remote.sh
./get_remote.sh
echo "* * * * * cd $PWD  && ./get_rermote.sh > ./get_rermote.sh.o"
# crontab -e

```


## gitlab 的使用

关键博客:
- [docker下gitlab安装配置使用(完整版) - 简书](https://www.jianshu.com/p/080a962c35b6)
- [GitLab → 搭建中常遇的问题与日常维护_A___LEi的博客-CSDN博客](https://blog.csdn.net/A___LEi/article/details/110476531)
- [GitLab管理员通过账号审核申请的步骤 - web_cnblogs - 博客园](https://www.cnblogs.com/xingfeng-cool/articles/15597366.html)


