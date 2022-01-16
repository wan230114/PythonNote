
计算机的基础简介及Linux的基本概念

---
# 0. 计算机基础简介

## 0.1. 计算机发展史
```
史前，     --- 算筹：木条类。  
公元八世纪  --- 算盘（十进制）：存储数据并计算。  
二战，     --- 手摇计算机：破译密码  
1946年，   --- 第一台计算机诞生，每秒5000次运算，电信号（二进制）  
```

---
## 0.2. 计算机的组成

- 硬件：  
  - 处理器（CPU）  
    - ARM, AMD
      - A11（33亿个晶体管，7纳米几乎无法再降）（频率3.3GHZ，几乎无法上升详细可以了解量子力学）
      - A12/麒麟980（69亿个晶体管，7纳米）
      - A13（85亿个晶体管，7纳米）
      - 麒麟990（103亿晶体管）
      - A14（150亿个晶体管，5纳米）  
    - X86, Intel
      - I3、I5、I7  
  - 运行内存RAM（存储数据）（容量，字节为单位）  
  - 主板（总线设备）  
  - 外部存储设备 (硬盘，U盘，TF卡等)  
  - 输入输出设备(显示屏，键盘，鼠标等)  
- 软件：   
  - 操作系统  
  - 应用软件（用户级）  

---
## 0.3. 计算机数据表示

1 byte = 8 bit  
(1 字节 = 8 位)

- 每 1 bit(位) 由二进制 0 或 1 组成  
- 每 1 byte(字节) 有 2^8 = 256 种组合
- 256种组合刚好对应的是16进制的所有数(00~FF)，此为字节最基本的表述方式

---
### 0.3.1. 进制

说明：  
- 二进制 0~1  
- 十进制 0~9  
- 八进制 0~7  
- 十六进制 0~9,A~F  
  (`…, 9>9, 10>A, 11>B, 12>C, 13>D, 14>E, 15>F`)  

注意：所有的数都从0开始
> 特别注意：十六进制数`F`代表十进制数为`15`，属于从`0`到`F`数的第16位。

**进制的互相转换** 

进制转换问题，可以拆解为一个根本问题：**某一个数包含了几个这样的进制单位数**

使用公式表示如下：
```
二进制数1100100  
N:  1  1  0  0  1  0  0  
n:  6  5  4  3  2  1  0  
说明：
N--对应位置的数字，a--进制数， n--具有几个单位量级  

二 --> 十： ∑ ( N * a^n ）  上标:n=0  下标:n
二 --> 八： 以二进制每三位为节点  
二 --> 十六： 以二进制每四位为节点  
十 --> 二： 取余法，以预转换的进制数为除数，除到结果为0为止（证明过程：提取法）  
```

---
示例：

> 简单理解方式，每一位数包含了几个进制数，从个位算起。  
> **十进制 <--> 二进制:**  
> `(100)10 = (1100100)2 = 0*2^0 + 0*2^1 + 1*2^2 + 0*2^3 + 0*2^4 + 1*2^5 + 1*2^6`  
> **十进制 <--> 八进制:**   
> `(100)10 = (144)8 = 4*8^0 + 4*8^1 + 1*8^2`  
> **十进制 <--> 十六进制:**   
> `(100)10 = (64)16 = 4*16^0 + 6*16^1`  

---
示例2：

十进制 --> 二进制  
> 例：13转换为二进制？   
> 13/2  =   6…1  
> 6/2       =   3…0  
> 3/2       =   1…1  
> 1/2       =   0…1  
> 所以二进制是1101  

十进制 --> 十六进制  
> 例：18转换为十六进制？  
> 
> 方法1：  
> 18/16 = 1…2  
> 1/16  = 0…1  
> 十六进制表示12  
>   
> 方法2：  
> 18转二进制：  
> 18/2 = 9…0  
> 9/2  = 4…1  
> 4/2  = 2…0  
> 2/2  = 1…0  
> 1/2  = 0…1  
> 所以二进制是10010，即00010010  
> 转换为十六进制：  
> 0010…2  
> 0001…1  
> 十六进制表示12  

十六进制 --> 十进制  
> FF的十进制数是多少？  
> `= 15*16^0 + 15*16^1 = 255`


---
## 0.4. 操作系统简介
三个主流系统：   
- Windows、（图形用户界面GUI最早）  
    - Win3.1、win3.2、win95、win98、win me、win2000、Win_xp、win 7、win 10  
- Linux、  
    - 安卓（Android）  
    - Ubuntu（当前学习的操作系统） 
    - CentOs 
    - Redhat  
- Unix（最优秀的操作系统，大型企业、政府等使用，安全稳定高效）  
    - 公司：AIX（IBM）由开源闭源、Solaris（SUN）  
    - IOS（Apple 移动端）  
    - Mac OS X（Apple PC）  


---
### 0.4.1. Linux基本结构（由上到下）

（ 换言之，程序如何调用到最终的硬件？） 

包括以下：  
- 应用程序  
- 标准库  
- Linux操作系统内核  
- 硬件

### 0.4.2. 基于Linux的文件系统

Linux中：一切皆文件！！ 

Linux下文件系统：
- /bin/   常用目录 bin是Binary的缩写, 这个目录存放着最经常使用的命令
- /boot/grub
- /etc/
- /home/  用户主目录，是用户权限下管理分配的不同目录
- /lib/
- ...


扩展阅读：
> http://www.cnblogs.com/happyframework/p/4480228.html
> http://www.pathname.com/fhs/pub/fhs-2.3.html
> 搜索引擎关键字：linux目录结构  和  linux文件系统


---
# 1. Linux基本了解



---
## 1.1. Linux/Unix基本认识
Linux操作系统优势：
- 运行速度快。
- 无多余的图形处理界面
  - 比如有时企业处理事件，Windows5秒，Linux3秒。


---
#### 1.1.1. 连接Linux会话的终端工具

- 本地终端打开会话：  
  - Ubuntu桌面版打开会话连接方法：  
    - 搜索应用程序：终端、gnome-terminal 图标  
    - `Ctrl + Alt + T`  
- ssh远程连接会话
    - 任意命令终端中使用ssh
- 终端会话退出：  
  - 输入exit  
  - `Ctrl + D`  
- 其他第三方终端工具：
  - ...


一些快捷键：
- `Tab`	- 自动补齐。补全路径，命名  
- `↑↓`	- 翻出上/下条命令  
- `Ctrl + L` - 清屏，也可用命令clear  
- `Ctrl + D` - 退出当前交互命令窗口  


---
#### 1.1.2. 会话基本界面

```
[chenjun@ge60centos ~]$ 
 ------- ---------- -   -------------
    |     |         |     |
 用户名  主机名  所在文件夹  待输入的操作命令
```


设置样式的代码环境：

```bash
PS1="\[\e[1;32m\][\u@\h:\[\e[1;36m\] \t \[\e[31m\]\"\w/\"]\n\[\e[32m\]$ \[\e[m\]"
PS1=`echo ${PS1}|sed 's#"\\\\w/"#"$PWD/"#'`  # "~/" --> "/home/user/"
```

---
### 操作命令

操作命令格式： `命令名 [选项] [参数]`

> 注：`[]`的内容代表可选选项或可选参数（可有可无，具体看命令功能或要求）


示例：

```bash
find /var -maxdepth 2 -type d
```

命令解析：
- `/var`：输入路径。代表去/var路径下面去找所有文件或目录
- `-maxdepth 2`：输入最大寻找到几级目录。我们填写的2，代表最大搜索二级目录
- `-type d`：输入搜索类型是什么。我们填写的d，代表只搜索文件类型为目录的。



---
## 1.2. Linux 基本概念

- **隐藏文件**

  如 `ls –a` 查看到的以.开头的文件
  ```bash
  $ ls
  file   folder
  $ ls -a
  .          ..         .file      .hide_file file       folder
  ```

- **文件类型**

  如 `ls -l` 查看到的第一位字符  

  |文件类型|解释|
  |-|-|
  | `b` | 块设备文件 |
  | `c` | 字符设备文件 |
  | `d` | 目录  |
  | `-` | 普通文件 |
  | `l` | 链接 |
  | `s` | 套接字 |
  | `p` | 管道 |

  ```bash
  $ ls -l
  total 0
  -rw-r--r--  1 chenjun  staff   0  1 27 21:40 file
  drwxr-xr-x  2 chenjun  staff  64  1 27 21:38 folder
  ```

- **路径**

  是用来记录一个文件或文件夹的字符串。

  - 绝对路径：  
    以“/”字符开头的路径称为绝对路径。（任何时候，一个文件的绝对路径是唯一的）。
    如：`/` 根目录, `/root` root的home目录
  - 相对路径：  
    如：`./*/`当前目录下的所有目录
  - 特殊符号：  
    如 `~`代表当前登录会话用户的home目录（每次打开会话，默认进入的目录）


---
## 1.3. 基本标识符

### 1.3.1. 各类括号
| 标识符 | 说明 |
|-|-|
|`()`|单小括号。新开运行环境，shell命令替换|
|`(())`|整数扩展。计算数值|
| `[]` | 单中括号。 |
| `[[]]` | 双中括号 |
| `{}` | 花括号。 变量名规定，语句块，以逗号分割的文件列表进行拓展|

```bash
## 1) 单小括号()
a=1; (a=2); echo $a
# 1
a=1; sh -c "a=2"; echo $a
# 1
a=1; a=2; echo $a  # 对比
# 2

ec$(echo ho) 123
# 123
echo 123
# 123


## 2) 双小括号()
a=100
echo $((a++))
echo $a
echo $((++a))
echo $a
((a=a+100))
echo $a


## 5) 花括号
a=100
echo ${a}
{ echo 123; echo 456;} 
touch {a,b}.txt  # 结果为a.txt b.txt。
```

拓展阅读：
> [linux中()、[]、{}、(())、[[]]等各种括号的使用_zjmy的博客-CSDN博客](https://blog.csdn.net/qq_41551450/article/details/92803686)


---
### 1.3.2. 通配符：
**`*`**	—— 匹配0个，1个或多个字符  
**`?`**	—— 匹配1个任意字符

示例：
```bash
touch a aa ab abc 
ls a*	匹配a开头的文件，以此类推
ls a?
ls *a*	含有a的字符，不一定是a在中间
ls *c
ls ?c
...
```

### 1.3.3. 引号

引号常用于表示一段字符串。

- `""` 双引号内部可以嵌入变量等特殊字符
- `''` 单引号则将内部的所有符号都认为是字符串

示例：
```bash
var=3  # 定义一个变量
echo "这是$var"
echo '这是$var'
```

---
## 1.4. 输出重定向符号

|符号|说明|
|-|-|
| **`>` / `>>`**   | “标准输出”重定向到文件，等价于 `1>` / `1>>` |
| **`2>` / `2>>`** | “标准错误输出”重定向到文件 |
| **`&>` / `&>>`** | ”标准输出“和“标准错误输出”都重定向到文件，等价于 **`1>2 2>somefile`** |
| **`<`** | 将文件作为标准输入 |
| **`<()`** | 作为临时文件 |


示例：

```bash
seq 3  # 创建并打印一个1到3的数字
seq 3 >testfile    # 标准输出重定向到文件

cat testfile | sed 2d  # 去除第二行的输出，只打印 1 3
sed 2d < testfile  # 使用标准输入方式来操作

cat <(seq 3)  # 打印一个临时生成的文件，打印 1 2 3
ls -l <(seq 3)   # 看看这个临时文件的信息。/dev/fd/63

find /etc -name "passwd" >log.o 2>log.e 	  # 输出的信息分流到文件
find /etc -name "passwd" >log.o 2>/dev/null	 # 报错信息重新向于无任何打印
find /etc -name "passwd" 1>/dev/null	 # 只看错误信息
find /etc -name "passwd" 2>/dev/null	 # 只看正常信息

find /etc -name "passwd" 1>log.o 2>&1  # 标准和错误的所有输出都重定向到文件log.o
find /etc -name "passwd" &>log.o       # 同上，需注意的是，该种写法在某些系统中不适用，如ubuntu
```


---
PS：

几个特殊的设备文件

- `/dev/stdout`  : 标准输出。一般用于命令程序正常执行的信息打印
- `/dev/stderr`  : 标准错误输出。一般用于命令程序执行时有错误或警告的信息打印
- `/dev/stdin`   : 标准输入
- `/dev/null`    : 丢弃一切写入其中的数据


---
## 1.5. 查看帮助

方法：
- `man 命令名` —— 查看命令帮助，翻页↑↓，退出q键
- `命令名 --help` —— 查看命令帮助，翻页↑↓，退出q键

```bash
man ascii  # Linux下查看ASCⅡ编码表
man ls
man rm
ls --help
```


---
拓展： ASCⅡ编码（由美国国家标准委员会制定）中的常用编码：  
```
字符    十进制   十六进制  
'0'     48      30  
'A'     65      41  
'a'     97      61  
```
