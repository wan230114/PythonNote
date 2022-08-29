

# 2. Linux 文件操作命令

---
## 2.1. 文件(夹)及文本操作

### 2.1.1.  常用文件目录操作

#### ls 查看文件及各类属性

选项

```bash
ls [选项] [文件名或文件路径名]
-s   列表形式显示所有“文件”
-l   列表形式显示所有“文件及文件夹”，以及详细信息
-a   显示所有文件
-h   文件大小显示单位
-r   逆序
-t   按时间排序，从新到旧
```

```bash
ls -a   # 当前全部文件(夹)（包括隐藏文件 “`.文件名`”：以.开头的文件）

ls -la    # 以列表形式显示当前全部文件(夹)
ls -l -a  # 同上
ls -a -l  # 同上

ls -lrt   # 按照时间逆序排序。最下面显示最新文件

ls /usr/  # 查看指定文件夹
```

其中, 
```shell
(dev) [chenjun@junmac: 15:36:54 "/etc"]
$ ls -l /etc/
total 912
-rw-r--r--   1 root  wheel     515  1  1  2020 afpovertcp.cfg
lrwxr-xr-x   1 root  wheel      15  1  1  2020 aliases -> postfix/aliases
-rw-r-----   1 root  wheel   16384  1  1  2020 aliases.db
drwxr-xr-x  10 root  wheel     320  1 16 12:47 apache2
drwxr-xr-x  18 root  wheel     576  1  1  2020 asl
-rw-r--r--   1 root  wheel    1051  1  1  2020 asl.conf
```

文件类型
```bash
b  块设备文件
c  字符设备文件
d  目录 
-  普通文件
l  链接
s  套接字
p  管道
```


### pwd 查看当前工作路径位置：

```bash
pwd        # 命令
echo $PWD  # $PWD代表一个变量名为PWD的变量
```

## cd 目录的切换

```bash
cd [目录/路径]
cd 文件夹  #进入目录
cd .      #进入当前目录
cd ..     #进入上级目录
cd ../../Me  #进入上上级目录下的Me目录
cd -      #切换到之前工作的文件夹。方便两个文件夹来回切换
cd ~      #进入用户主目录（等同于ls /home/用户名）
```

## mkdir创建单/多个文件夹

mkdir 文件夹名1 文件夹名2 …
常用参数：-p

```bash
mkdir a b c d
mkdir -p a/b/c/d	# 常用选项-p，逐级创建即使存在的文件夹
mkdir -p a/{b1,b2,b3}	# {}可以批量创建不同名文件夹
```

技巧：利用↑↓箭头更改修改的一点变量，dddd,ddda,dddb…不用进入到文件夹内部

## rmdir删除空文件夹

rmdir [选项]
常用参数：-p

```bash
rmdir a b c d
rmdir –p a/bb/ccc/dddd	#是mkdir逆过程
```

	tree显示目录树
tree
tree day01
	touch创建未存在文件，更新已存在文件时间
touch  (路径)文件名
touch ***
	rm删除命令
rm [选项] 文件/文件夹
选项：
-f  强制删除文件或目录。 （不提示，强制删除（或者说直接删除））
-i  删除既有文件或目录之前先询问用户。（提示，对单个文件(夹)删除否灵活操作），
-r  将指定目录下的所有文件及子目录一并处理。（删除文件夹下全部）
-v  显示指令执行过程。
rm *.txt   #删除后缀名为.txt的文件
rm –rf haha   #删除haha的所有文件及文件夹
rm “a b”	#双引号可以把包含特殊字符(如空格)的识别为整体
	cp复制文件或文件夹
cp [选项] 源文件(夹) 目标文件(夹)
选项：
-a ：复制文件夹全部内容，属性时间链接等
-f ：强行复制文件或目录，不论目标文件或目录是否已存在。
-i : 覆盖既有文件之前先询问用户。
-p ：保留源文件或目录的属性。 
-P ：保留源文件或目录的路径。 
-r ：将指定目录下的文件与子目录一并处理。 
-l ：对源文件建立硬连接，而非复制文件。
-s ：对源文件建立符号连接，而非复制文件。
-v ：显示指令执行过程。
-d ：复制软链接，只复制软链接而不复制原文件
高级示例：
	1、复制test目录结构于当前目录，目录创建不变，然后所有文件都为软链接
cp -rs /xxx/xxx/test ./
	mv移动或重命名文件(夹)
mv 源文件(夹) 目标文件(夹)
-f若目标文件或目录与现有的文件或目录重复，则直接覆盖现有的文件或目录。 
-i覆盖前先行询问用户。 
-u在移动或更改文件名时，若目标文件已存在，且其文件日期比源文件新，则不覆盖目标文件。 
-v执行时显示详细的信息。
sudo mv new_service.sh /etc/init.d/
### 2.1.2.  解压缩gzip/tar/zip
	gzip/ gunzip对“文件”进行打包/解包，打包后原文件变为“原文件.gz”
gzip 文件名
选项：
-d 
gzip test.txt
gzip -d test.txt.gz
	tar对“文件(夹)”解压
tar [选项] 压缩后文件名 [待操作文件(夹)路径]
选项:
-c  创建包      -x  解压包
-z  用gzip/gunzip对包进行打包 / 解包
-v  显示当前操作细节
-f  文件名       正在操作的文件名
-c  路径        改变解压缩路径（只对解包有效）

tar  cvf  文件名    #打包
tar  xvf  文件名    #解包
tar  cvfz  文件名   目录/文件    #打包并压缩
tar  xvfz  文件名   目录/文件    #解包并解压
tar  vfz  

tar –czvf day01.tar.gz linux/day01 
tar –xzvf day01.tar.gz
	zip / unzip 压缩与解压缩
FileName.zip
解压：unzip FileName.zip
压缩：zip FileName.zip 待压缩路径
	bzip
基础格式: bzip2 [Options] file1 file2 file3
指令选项：(默认功能为压缩)
-c　　　　　　　//将输出写至标准输出
-d　　　　　　　//进行解压操作
-v　　　　　　　//输出压缩/解压的文件名和压缩比等信息
-k　　　　　　　//在压缩/解压过程中保留原文件
-digit　　　　 //digit部分为数字(1-9)，代表压缩速度，digit越小，则压缩速度越快，但压缩效果越差，digit越大，则压缩速度越慢，压缩效果越好。默认为6.

### 2.1.3.  ln 文件链接
	ln：建立链接
ln [选项] [源文件或目录] [目标文件或目录]
选项：
-b 删除，覆盖以前建立的链接
-d 允许超级用户制作目录的硬链接
-f 强制执行
-i 交互模式，文件存在则提示用户是否覆盖
-n 把符号链接视为一般目录
-s 软链接(符号链接)【注意事项：源文件(夹)链接必须写绝对路径，否则找不到】
 例子：
ln -s file1 file2
ln file file2
软链接与硬链接区别：
硬链接：新建的文件是已经存在的文件的一个别名，当原文件删除时，	 新建的文件仍然可以使用.
	 硬链接只能链接文件

软链接：也称为符号链接，新建的文件以“路径”的形式来表示另一个	文件，和Windows的快捷方式十分相似，新建的软链接可以指向	不存在的文件
	 软链接可以链接文件和目录

## 2.2. 文本查看命令
### 2.2.1.  cat / tac 从（第一行/最后一行）开始显示文本内容
cat 文件路径1文件路径2…
选项：
-n 或 --number：由 1 开始对所有输出的行数编号。
-b 或 --number-nonblank：和 -n 相似，只不过对于空白行不编号。
-s 或 --squeeze-blank：当遇到有连续两行以上的空白行，就代换为一行的空白行。
...
cat -nb 文件     #查看文本，对非空行显示行号
高级用法：
# 把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里：
cat -b textfile1 textfile2 >> textfile3




### 2.2.2.  more / less分页显示文本内容
more 文件路径      # 空格翻页，q退出
less 文件路径      # 上下翻页
### 2.2.3.  head / tail取出文件前面/后面几行
head 文件        # 默认显示前面10行
head -n num 文件   #显示指定行数
head -c num 显示文件前num个字符
tail与head用法完全相同
### 2.2.4.  nl
nl [选项] 文件
选项：
-w 数字      # 表示显示行数占据的位数
## 2.3. 文件信息查看
### 2.3.1.  wc 统计文本
	wc统计文本文件行数、字数、列数
wc [-clw][--help][--version][文件...]
选项：
-   从标准输入设备读取数据
l   只显示行数
c   只显示字节数
w   只显示字数

## 2.4. 查找文件或文本
### 2.4.1.  whereis查找
whereis [文件夹或文件]
### 2.4.2.  find查找文件
find：	递归查找文件和子目录
find  路径 ... 表达式
-name: 表达式（可以是通配符“*”与“？”）？任意单个字符  *任意多个字符
-user： 属主
-group：属组
-atime：n（n天之前访问的文件） -n（前n天之后访问的文件）	+n（前n天之前访问的文件）
-print：输出查找结果
常用：
find  路径 –name "文件名"
如：
从根目录下查找名为Novogene的文件，并打印到终端
find / -name Novogene -print 
find / -name "passwd"
找出当前文件夹下所有的软链接文件，打印其中指向文件夹的软链接：
find ./ -type l|xargs -i sh -c "if [ \"\`ls {}/ 2>/dev/null \`\" ] ; then echo {} ;fi"
### 2.4.3.  grep查找文件文本中的内容
grep：	查找含有某字符串的行
用法：
grep [参数] <字符串/正则表达式> <文件名或路径>
选项
-n：   显示匹配的行号
-num： 显示匹配行前后各num的行
-i：   不区分大小写
-r:    查找文件夹下所有文件
-f     
-v     反转查找【？】
-vf    
-x     输出精确匹配的
-xvf   

正则表达式：(又称为模式)
.   匹配任意个字符
^   匹配行开头
%   匹配行结尾 
[]  匹配[]中任意一个字符，如[a-z]。

```bash
$ echo https://www.baidu.com/baidu.html|grep -Po "(?<=www.).*(?=.com)"
baidu
```

	示例：
```bash
# 以下示例中，选项的位置前后无所谓
grep "^Novogene" filename
grep "root" /etc/passwd
grep "root" –n /etc/passwd    #显示行号
grep "tedu" –nr /etc    #显示太多的错误信息（-r搜索所有文件）
grep "tedu" -nr /etc 2> /dev/null    #输出重定向，减少错误信息
```
选项-x对比测试
```bash
$grep -x 100 <(echo 11100;echo 100)
100
$grep 100 <(echo 11100;echo 100)
11100
100
```

高级用法：
1、模式匹配对比两个文件。输出匹配的以及不匹配的【原理不太懂？】
grep -f file1 file2    #使用file1里面每一行去匹配file2里面每一行，有则打印
grep -v 是反转查找
$cat file1
1
2
3
4
4
5
$cat file2
2
4
99
999

$grep -f file1 file2   # 用file1的每一行去匹配file2，在file2中匹配到则输出
2
4
$grep -vf file1 file2   # 用file1的
99
999
$grep -v file2 file1   # 为何参数无效？
1
2
3
4
4
5
【显示后者特有的】
$grep -vf file1 file2  #无结果

$grep -vf file2 file1  # 用file2去匹配file1中没有的
1
3
5

应用场景，样品间变异信息比较，样品间基因ID的筛选等等



### 2.4.4.  awk高级命令
该命令内的运行环境是c语言
#### 2.4.4.1.  基本组成
	语法总结：
awk [选项] '执行语句' 文件
执行语句：
{语句}       #对读取文件(或管道)输入中的每一行都执行这个脚本。
BEGIN{...}  #在读取文件前执行
END{...}    #在读取文件后执行
选项：
-F X   X为分隔符，把一行按指定分隔符分开，没有此选项默认为空格【问题：必须$1,$2？】
-v ARG=test  传入参数，创建变量

特殊符号：
$0
$[1-9]*  
$NF
NR  代表行号
NF  代表列数

特殊参数：
OFS="\t"  输出分隔符

判断语句：
if(判断表达式){语句}else{语句}
if(判断表达式){语句1; 语句2; 语句3}
if(判断表达式)语句

判断表达式:
&&  且
||  或


print   带换行符打印
printf  不带换行符打印

匹配：
匹配开头
'/^xxx/'
不匹配开头
'!/^xxx/'

正则匹配一行出现字段
$ echo -e " gene \n nc_gene \n exon"|awk '$1 ~/gene/'
 gene
 nc_gene

支持多个条件匹配
awk -F ':' '/oo/ {print $1,$4} /user1/ {print $1,$6}' test.txt


#### 2.4.4.2.  示例：
1、打印文件所有内容
awk '{print $0}' 文件
2、打印文件1和4列内容
awk '{print $1,$4}' aa
cat file | cut –f 2  # 只输出第二列内容
3、只打印文件2~3行的内容
awk '{if(NR>=2 && NR<=3) print $1}' 文件
4、读取文件前执行内容
awk 'BEGIN{count=0;print "---开始计数---"} {count=count+1;print "第"count"行",$0}  END{print "总行数有：",count}' 文件
seq 40|xargs -n 4|awk 'BEGIN{n=0}{if($1%3==0)n+=1}END{print n*10}'
5、只打印最后一列的内容
awk '{print $NF}' 文件
6、只打印第5列匹配到文件keys.txt的内容
awk -F"\t" 'NR==FNR{a[$1]=$0}NR>FNR{if($5 in a) print $0}'  keys.txt  file.xls
只打印第5列匹配到“keyword”的行
awk '$5~/keyword/{print $0}' file
7、采用指定分隔符分割，输出
awk '{OFS="\t";print $3,$5,$9,$6}' file
8、过滤文件中第一列不等于“-”和第19列不为空的行
awk -F '\t' '($1!="-" && $19!=""){OFS="\t"; print $1,$19;}' file
9、打印第一行，并且之后遇到的所有#开头的都不打印
awk '{if(NR==1)print $0}!/^#/{print$0}' file
关联数组、加入循环等。。。
10、awk中执行shell语句
awk '{system("mkdir "$2";echo cd "$2";echo ln -s "$1"/13.function_filter/fun_stat/*.result ./;echo cd -")}' list |bash
11、奇偶行合并为一行
ls `pwd`/*/clean_data/*_*.clean.fq.gz|awk '{if (NR%2){printf $0;}else{print "\t"$0}}' >../../../annotion/00.data/read.lst
12、引用外部变量
$num=1000; echo ceshi|awk -v NUM=$num '{print NUM"\t"$0}'
1000	ceshi

#### 2.4.4.3.  【高级操作】
##### 2.4.4.3.1.  去除空行
grep -v '^$' file
cat file |tr -s '\n'
sed '/^$/d' file
awk NF test.txt  # 目前get到的最快方法

主要是判断下，某一行是否为空，或者长度是否为0，如果是的话，就不要打印。
awk '{if($0!="")print}' file
awk '{if(length($0)!=0) print $0}' file
awk '!/^$/ {print $0}' file 
awk 'length($0) > 0 {print $0}' file
awk 'BEGIN{RS="\n+";ORS="\n"}{print}' file
awk 'BEGIN{RS="\n+"}{print}'
##### 2.4.4.3.2.  匹配开头
匹配no或so开头的行
awk '/^(no|so)/' file
统计文件３中的序列个数（此方法比wc好的地方在于不统计末尾换行符）
awk '/^(A|G|T|C|N)/' file2 |awk 'BEGIN{l=0}{l+=length}END{print l}'
匹配第一列为"Biological Process"的行输出
awk  -F"\t" '{if($1=="Biological Process"){print $0}}' file

将当前文件夹内所有的*list.txt交换第一行和第二行输出到新文件*list.txt
ls *list.txt|xargs -i sh -c """awk  '{print \$2\"\\t\"\$1}' {}>{}.new"""

奇数偶数行分别重命名
awk '{if (NR%2==1) print "mv "$1"_1.adapter.list.gz "$2;else print "mv "$1"_2.adapter.list.gz "$2}' ../run-P101SC18051999-02/rawDataHiseqPath.lst|sed 's#.fq.gz#.adapter.list.gz#'|xargs -i sh -c "{}"

seq 1 9| xargs -n 3 |awk '{printf "start"; for(i=1;i<=NF;i++){printf $i"---"};print "end"}'
1
2
3
4
5
6
7
8
9
### 2.4.5.  cut分割文本

示例：
cut -d : -f 1    # 用:分割每一行，并显示第一块区域
### 2.4.6.  paste合并列

paste old.name new.name

## 2.5. 对比文件
【都只能对比排序好的文件？？】
### 2.5.1.  diff比较文件或者目录
比较两个文件的不同
diff [选项] 文件1 文件2            #如果文件1和文件2相同，没有提示
diff 目录1 目录2         # 比较两个目录
diff -r  目录1  目录2    # 比较两个目录每个文件的每一行，文件过大过多时运行较慢
选项：
-a：只逐行比较文本文件；
-b：忽略空格；
-B：忽略空行；
-c：显示全部内容，并标出不同之处；
示例：
高级用法，比较两个目录的文件名差异
diff <(ls 目录1) <(ls 目录2)

### 2.5.2.  comm对已排序的文件进行比较
用法：
comm [-123] file1 file2
选项
-1   不显示只在第1个文件里出现过的列。【不显示1列】
-2   不显示只在第2个文件里出现过的列。【不显示2列】
-3   不显示只在第1和第2个文件里出现过的列。【不显示3列】
示例：
$ cat 1
a
b
c
d
$ cat 2
a
c
e

【理解：1列放file1特有，2列放file2特有，3列放共有】
$ comm 1 2
a
b
c
d
	  e
$ comm -1 1 2
	  a
	  c
e
$ comm -2 1 2
	  a
b
	  c
d
$ comm -3 1 2
b
d
	  e
### 2.5.3.  uniq：比较相邻的行，显示不重复的行
uniq 文件
	-i ：忽略大小写
	-c ：计数
sort与uniq组合使用

## 2.6. 文本编辑修改
### 2.6.1.  sed文本编辑增删改
sed [-hnV][-e<script>][-f<script文件>][文本文件]
参数说明：
-e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件。
-f<script文件>或--file=<script文件> 以选项中指定的script文件来处理输入的文本文件。
-h或--help 显示帮助。
-n或--quiet或--silent 仅显示script处理后的结果。
-V或--version 显示版本信息。
动作说明：
a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)～
c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！
d ：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；
i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；
p ：打印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～
s ：取代，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦！
示例1：替换
文件：
$ cat test.txt 
hello hello
haha
hello hello hello
输出显示每行第一个“hello”替换为“你好”
sed 's#hello#你好#' test.txt
输出显示每行所有的“hello”替换为“你好”（加入g参数）
sed 's#hello#你好#g' test.txt
修改文件内容第一个“hello”替换为“你好”
sed -i 's#hello#你好#' test.txt
示例2：以行为单位的新增/删除
将 /etc/passwd 的内容列出并且列印行号，同时，请将第 2~5 行删除！
[root@www ~]# nl /etc/passwd | sed '2,5d'
1 root:x:0:0:root:/root:/bin/bash
6 sync:x:5:0:sync:/sbin:/bin/sync
7 shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
.....(后面省略).....
示例3：行首行末增加内容
在每行的头添加字符，比如"HEAD"，命令如下：
sed 's/^/HEAD&/g' test.file
在每行的行尾添加字符，比如“TAIL”，命令如下：
sed 's/$/&TAIL/g' test.file
示例4：不打印文件最后一行
sed '$d' test.file
### 2.6.2.  tr命令转换或删除文件中的字符。
tr 指令从标准输入设备读取数据，经过字符串转译后，将结果输出到标准输出设备。

语法
tr [-cdst][--help][--version][第一字符集][第二字符集]  
tr [OPTION]…SET1[SET2] 
参数说明：

-c, --complement：反选设定字符。也就是符合 SET1 的部份不做处理，不符合的剩余部份才进行转换
-d, --delete：删除指令字符
-s, --squeeze-repeats：缩减连续重复的字符成指定的单个字符
-t, --truncate-set1：削减 SET1 指定范围，使之与 SET2 设定长度相等
--help：显示程序用法信息
--version：显示程序本身的版本信息
应用：
	去除空行打印文件
cat file |tr -s '\n'

### 2.6.3.  sort：对文件排序
（首字符向后，依次按ASCII码值进行比较，升序输出）
用法：
sort [参数] file
	-r：降序输出
	-n：以数值来排序，避免10<2
-V：忽略字母
	-o：输出到新文件
	-t: 指定分隔符
	-k: 指定哪一列
示例：
```bash
$cat 2
line1
line3
line4
line2
$sort 2
line1
line2
line3
line4
$sort -r 2
line4
line3
line2
line1
$ cat a.txt 
chr2
chr1
chr11
chr12
$ sort a.txt 
chr1
chr11
chr12
chr2
$ sort -n a.txt 
chr1
chr11
chr12
chr2
$ sort -V a.txt 
chr1
chr2
chr11
chr12
```
高级用法：
复制代码代码示例:
sort -t $'\t' -k 1n,1 -k 2n,2 -k4rn,4 -k3,3 <my-file>
解释如下：
-t $'\t'：指定TAB为分隔符
-k 1, 1: 按照第一列的值进行排序，如果只有一个1的话，相当于告诉sort从第一列开始直接到行尾排列
n:代表是数字顺序，默认情况下市字典序，如10<2
r: reverse 逆序排列，默认情况下市正序排列
-b 忽略每行前面开始出的空格字符。
-c 检查文件是否已经按照顺序排序。
-d 排序时，处理英文字母、数字及空格字符外，忽略其他的字符。
-f 排序时，将小写字母视为大写字母。
-i 排序时，除了040至176之间的ASCII字符外，忽略其他的字符。
-m 将几个排序好的文件进行合并。
-M 将前面3个字母依照月份的缩写进行排序。
-n 依照数值的大小排序。
-o <输出文件> 将排序后的结果存入指定的文件。
-r 以相反的顺序来排序。
-t <分隔字符> 指定排序时所用的栏位分隔字符。
+<起始栏位>-<结束栏位> 以指定的栏位来排序，范围由起始栏位到结束栏位的前一栏位。

最终的linux命令如下：
sort -t $'\t' -k 1n,1 -k 2n,2 -k4rn,4 -k3,3 my-file
	按第一列(优先)和第三列排序，输出到新文件（同名则覆盖）
sort -t $'\t' -k1,1 -k3,3 myfile -o newfile
忽略第一行：
(临时方法：把第一行和其他数据分为两个文件，再把数据排序追加到第一行的文件)
tail -n +2 Linux_exercise_1.data > flash; head -n 1 Linux_exercise_1.data > Linux_exercise_1.sort.data; sort -t $'\t' -k1,1 -k3,3 flash >> Linux_exercise_1.sort.data; rm flash


## 2.7. 文本编辑器
### 2.7.1.  VIM文件文本编辑操作
Vim 键盘图
 
Linux vi 命令用法详解：功能强大的纯文本编辑器 
http://man.linuxde.net/vi
vi编辑器提供了丰富的内置命令，有些内置命令使用键盘组合键即可完成，有些内置命令则需要以冒号“：”开头输入。常用内置命令如下：
Ctrl+u 向文件首翻半屏；
Ctrl+d 向文件尾翻半屏；
Ctrl+f 向文件尾翻一屏；
Ctrl+b 向文件首翻一屏；
Esc    从编辑模式切换到命令模式；
ZZ     命令模式下保存当前文件所做的修改后退出vi
:行号   光标跳转到指定行的行首；
:$     光标跳转到最后一行的行首；
x或X   删除一个字符，x删除光标后的，而X删除光标前的；
D      删除从当前光标到光标所在行尾的全部字符；
dd     删除光标行正行内容；
ndd    删除当前行及其后n-1行；
nyy    将当前行及其下n行的内容保存到寄存器？中，其中？为一个字母，n为一个数字；
p      粘贴文本操作，用于将缓存区的内容粘贴到当前光标所在位置的下方；
P      粘贴文本操作，用于将缓存区的内容粘贴到当前光标所在位置的上方；
/字符串     文本查找操作，用于从当前光标所在位置开始向文件尾部查找指定字符串的内容，查找的字符串会被加亮显示；
？name      文本查找操作，用于从当前光标所在位置开始向文件头部查找指定字符串的内容，查找的字符串会被加亮显示；
a，bs/F/T     替换文本操作，用于在第a行到第b行之间，将F字符串换成T字符串。其中，“s/”表示进行替换操作；
a     在当前字符后添加文本；
A     在行末添加文本；
i     在当前字符前插入文本；
I     在行首插入文本；
o     在当前行后面插入一空行；
O     在当前行前面插入一空行；
:wq    在命令模式下，执行存盘退出操作；
:w     在命令模式下，执行存盘操作；
:w！   在命令模式下，执行强制存盘操作；
:q     在命令模式下，执行退出vi操作；
:q！   在命令模式下，执行强制退出vi操作；
:e文件名    在命令模式下，打开并编辑指定名称的文件；
:n     在命令模式下，如果同时打开多个文件，则继续编辑下一个文件；
:f     在命令模式下，用于显示当前的文件名、光标所在行的行号以及显示比例；
:set number      在命令模式下，用于在最左端显示行号；
:set nonumber     在命令模式下，用于在最左端不显示行号；

应用：
	替换的实例:
	替换所有的abc为bcd
                      :%s/abc/bcd/g
	将文件中所有/usr/bin目录替换成/home
                      :%s/\/usr\/bin/\/home/g
	在每行开头加入一个单词linux 
                      :%s/^/linux/g
	在每个单词后面加上一个s
                      :%s/$*\>/s/g


### 2.7.2.  sublime text 3文本编辑器
编写无格式文本
启动方式：
1命令
subl 
subl 文件(夹)路径 
2点击图标
示例：使用sublime打开文本文件
subl /etc/passwd  #用sublime打开文件

	快捷操作：
	打开或隐藏侧边栏	view --> Side Bar --> Show/Hide side bar
		Ctrl + k + b
	字体放大缩小 Ctrl + “+/-”
	创建多个光标Ctrl + 鼠标左键，取消Esc
	多行注释/取消注释 Ctrl + /
	交替换行 Ctrl + shift + ↑/↓
	多选相同的块 Ctrl + d


# 3.  LINUX系统进程操作
## 3.1. 开胃菜
高级操作

去除当前文件夹中所有文件中的末尾\r符号，并输出到新文件夹all-NEW
mkdir all-NEW; ls |cat|awk '!/^all-NEW/'|xargs -i -n 1 sh -c  "cat {} |sed 's#\r##g' >all-NEW/{}"

监控磁盘运行情况
$echo -e "/TJNAS01/PAG/Plant/\n/TJPROJ1/DENOVO/\n/ifs/TJPROJ3/Plant/"|xargs -i sh -c """df {}|sort|head -1|awk '{print \$3}'|awk '{if(int(\$0) < 5497558138880) print \"磁盘空间不足5T，剩余\"\$0/1024/1024/1024\"T，路径是{}\"}'"""
磁盘空间不足5T，剩余2.05536T，路径是/TJNAS01/PAG/Plant/
磁盘空间不足5T，剩余2.62165T，路径是/TJPROJ1/DENOVO/
磁盘空间不足5T，剩余2.20511T，路径是/ifs/TJPROJ3/Plant/
## 3.2. sh运行命令行
$ sh -c 'echo hello'
hello
## 3.3. 管道
### 3.3.1.  管道符：|
管道用于连接 linux 命令，把前面的Linux命令的输出，作为后面命令的输入
机制理解：
后面的命令类似于处理一个缓存文件
应用：
1、查看系统中是否有vim进程运行
（把 ps aux 命令输出的内容作为 grep 命令的输入。）
ps  aux  |  grep  vim 
2、复制所有图片文件到 /data/images 目录下
ls *.jpg | xargs -n1 -I cp {} /data/images
3、使用xargs下载文件中包含的链接
假如你有一个文件包含了很多你希望下载的 URL，你能够使用 xargs下载所有链接：
cat url-list.txt | xargs wget -c
	4、和while联用
cut -f2 lst.tmp.ID|while read a;do echo rm -rf $a;done

### 3.3.2.  xargs一般是和管道一起使用。
	命令格式：
somecommand |xargs -item  command
参数：
-a file   从文件中读入作为sdtin【？】
-e flag   注意有的时候可能会是-E，flag必须是一个以空格分隔的标志，当xargs分析到含有flag这个标志的时候就停止。
-p        当每次执行一个argument的时候询问一次用户。
-n num    后面加次数，表示命令在执行的时候一次用的argument的个数，默认是用所有的。
-t        表示先打印命令，然后再执行。
-i        或者是-I，这得看linux支持了，将xargs的每项名称，一般是一行一行赋值给 {}，可以用 {} 代替。
-r no-run-if-empty      当xargs的输入为空的时候则停止xargs，不用再去执行了。
-s num     命令行的最大字符数，指的是 xargs 后面那个命令的最大命令行字符数。
-L num     从标准输入一次读取 num 行送给 command 命令。
-l 同 -L。
-d delim 分隔符，     默认的xargs分隔符是回车，argument的分隔符是空格，这里修改的是xargs的分隔符。
-x exit      的意思，主要是配合-s使用。。
-P      修改最大的进程数，默认是1，为0时候为as many as it can ，这个例子我没有想到，应该平时都用不到的吧。

	示例：
-dX分隔符的应用
echo "nameXnameXnameXname" | xargs -dX
输出
name name name name
-n num的应用
	快速分列
$ echo "nameXnameXnameXname" | xargs -dX -n2
name name
name name
$ seq 1 8|xargs -n4
1 2 3 4
5 6 7 8
	应用
1、查看所有文件的属性
ls |xargs file
2、
ls ../Test_data/|awk '{print i$0}' i='../Test_data/' |xargs -i ls {}

### 3.3.3.  `的用法
见培训材料：Linux基础
运行命令，返回字符串

### 3.3.4.  炫酷技巧
	快速备份文件
准备好路径文件，
cat all.path|xargs -i echo "mkdir -p .{} ; ln -s {}/* .{}/" >ln.sh

xargs转换成为字符后，使用|bash再运行
cd results-190708
ls *.list|sed 's#.list##g'|xargs -i echo "echo == {} ==;cat {}.list|wc -l|awk '{print \$0-1}' ;grep ^\> {}_new.cds |wc -l; grep ^\> {}_new.pep |wc -l"|sh >../all.num
ls *.list|sed 's#.list##g'|xargs -i echo "echo == {} ==;diff <(cut -f 10 {}.list|awk '{if (NR>1)print}'|sort|uniq) <(grep ^\> {}_new.pep|tr -d '>'|sort|uniq)"|bash > ../all.num.diff
## 3.4. 进程管理
### 3.4.1.  ps查看进程
ps [选项]
a：显示当前终端的所有进程
u：显示进程的用户名和启动时间等
x: 
j:
f:
(详细知识见多任务编程)
ps  aux
ps -e u|grep wangshuai（查找指定用户的进程）
### 3.4.2.  kill：终止后台进程
用法：
kill [参数] 进程1 进程2 ...
-s：指定发送的信号
-l：指定信号的名称
kill -s 9 8337
		-s 9 制定了传递给进程的信号是９，即强制、尽快终止进程
### 3.4.3.  top 显示运行中的程序
查看运行的程序，获取PID
用法：
top [参数] 
  -u:显示某用户的程序
  -d:调整更新秒数，默认是5秒
  如：
top -d 20 -u wangshuai

	pkill 命令 自己看帮助

任务管理命令：
第1行（运行时间）：系统当前时间，系统运行世界，当前用户数量，最近1分钟，5分钟，15分钟运行的进程数。
第2行（统计进程数）：当前进程总数，睡眠进程总数，运行进程总数，僵死进程数，暂停进程数
第3行（统计CPU）：用户进程占比，系统进程占比，修改NI的进程占比，空闲进程占比
第4行（统计内存MEM）：内存总量，已用内存，空闲内存，共享内存缓冲区内存。
第5行（统计交换区和缓冲区）:交换区总量，已用量，空闲量，告诉缓冲区总量。

PID：进程id    USER：用户    PR：进程优先级
NI：nice值，正负分别表示正负优先级
VIRT：进程使用的虚拟内存总量
RES： 进程使用的物理内存大小
SHR：共享内存大小
S：状态
%CPU：CPU使用占比
%MEM：内存使用占比
任务管理命令：
### 3.4.4.  nohup：投递任务到本地后台
用法：nohup  命令  &
sh work.sh
nohup sh work.sh &
nohup time sh work.sh &
### 3.4.5.  wait：设定阻塞等待前面执行完毕：
示例：
sleep 3  && echo 3 &
sleep 2  && echo 2 &
sleep 1  && echo 1 &
wait
echo 0
输出顺序为1230

示例：
（理解内容：sh/bash区别，阻塞&与wait符号含义，nohup含义对wait无效）
sleep 1 && echo 1 && date &  # 1
sleep 9 && echo 2 && date &  # 3
sleep 3 && echo 3 && date  # 1
sleep 4 && echo 4 && date  # 2

sleep 5 && echo 5 && date & #
sleep 1 && echo 6 && date #
wait

echo 7 && date

#s  p
#1  1
#3  3
#4  x
#...
#7     4
#8     6
#9     2
#12    5
#12.1  7

#1-(1)  2-(9)  3(3)
#4(4)
#5-(5)  6(1)

#wait 等1- 2- 5-执行完继续

#7

#如果没有wait，7在8s打印
#有wait，7在9s打印

你可以做个试验，
nohup sleep 120 && echo 1111 >log_nohup &
然后关闭终端，这个即使关闭，最后也能正常生成log_nohup

但如果没有nohup，直接：
sleep 121 && echo 2222 >log_nohup2 &
然后关闭终端，这个关闭，log_nohup2可能就会没了

关闭前后可以在另一个终端ps xjf查看对应进程是否存在

因为第二个是以连接的bash为父进程创建的子进程sleep，父进程是这个终端，杀掉有可能会被清理掉

而nohup相当于父进程直接托管给系统了，所以关闭终端没有影响，除非服务器关机，或者手动杀掉，所以就没有影响

终端关闭，控制终端连接的进程也就杀掉，有可能会处理下面的子进程

当然，有时候会将子进程直接也托管给系统，比如直接拔网线，中间少了进程信号传递，控制子进程到底杀不杀的信号传递（以区分是人为主动关闭，还是不可抗逆因素），不可抗逆因素的话就可能给系统了。

我猜测很有可能自己主动关闭终端，xshell会发送特殊字符去告诉服务器我是主动关的。

而直接断网就没了告诉服务器的过程


# 4.  常用工具
## 4.1. date日期处理
echo start at time `date +%F'  '%H:%M`


---
# 6.  系统操作

## 6.1. 系统查看
### 6.1.1.  查看Linux系统版本的命令（3种方法）
cat /etc/issue  #此命令也适用于所有的Linux发行版。
cat /etc/redhat-release  #这种方法只适合Redhat系的Linux：
lsb_release -a  #即可列出所有版本信息：

### 6.1.2.  查看内核版本
两种方法：
	uname命令
uname -a  # 显示版本及相关内容
uname -r  # 只显示版本信息
	绝对路径 /proc/version
cat /proc/version
### 6.1.3.  查看发行版本
	查看发行版本
ps：如无此命令，请先安装yum -y redhat-lsb
lsb_release -a
	使用绝对路径
/etc/os-release
/etc/redhat-release
### 6.1.4.  查看主机名
hostname

## 6.2. 用户权限管理
### 6.2.1.  查看用户权限
	查看所有用户
　　(1)在终端里.其实只需要查看 /etc/passwd文件就行了.
　　(2)看第三个参数:500以上的,就是后面建的用户了.其它则为系统的用户.
# 查看命令
cat /etc/passwd |cut -f 1 -d :
	查看当前用户
who        #显示已经登录系统的用户信息
whoami     #查看当前用户名称
id          #查看当前用户所属的组（即创建文件时用户的组）
last       #显示过去有哪些登录的用户
tarena@tedu:~/AID1805/haha/aa$ whoami
tarena
tarena@tedu:~/AID1805/haha/aa$ id
uid=1000(tarena) gid=1000(tarena) 组=1000(tarena),4(adm),24(cdrom), 27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
	权限规则【？】
用户属于某个组；首先判断用户，在判断是否同一个组，再判断其他用户。
所有权限对root的无效。
### 6.2.2.  用户管理命令
useradd 注：添加用户
adduser 注：添加用户
passwd 注：为用户设置密码
usermod 注：修改用户命令，可以通过usermod 来修改登录名、用户的家目录等等;
pwcov 注：同步用户从/etc/passwd 到/etc/shadow
pwck 注：pwck是校验用户配置文件/etc/passwd 和/etc/shadow 文件内容是否合法或完整;
pwunconv 注：是pwcov 的立逆向操作，是从/etc/shadow和 /etc/passwd 创建/etc/passwd ，然后会删除 /etc/shadow 文件;

finger 注：查看用户信息工具
id 注：查看用户的UID、GID及所归属的用户组
chfn 注：更改用户信息工具

su 注：用户切换工具
sudo 注：sudo 是通过另一个用户来执行命令(execute a command as another user)，su 是用来切换用户，然后通过切换到的用户来完成相应的任务，但sudo 能后面直接执行命令，比如sudo 不需要root 密码就可以执行root 赋与的执行只有root才能执行相应的命令;但得通过visudo 来编辑/etc/sudoers来实现;

visudo 注：visodo 是编辑 /etc/sudoers 的命令;也可以不用这个命令，直接用vi 来编辑 /etc/sudoers 的效果是一样的;
sudoedit 注：和sudo 功能差不多;
	管理用户组(group)的工具或命令;
groupadd 注：添加用户组;
groupdel 注：删除用户组;
groupmod 注：修改用户组信息
groups 注：显示用户所属的用户组
grpck
grpconv 注：通过/etc/group和/etc/gshadow 的文件内容来同步或创建/etc/gshadow ，如果/etc/gshadow 不存在则创建;
grpunconv 注：通过/etc/group 和/etc/gshadow 文件内容来同步或创建/etc/group ，然后删除gshadow文件

示例：初始化集群用户操作
1.新建用户 
adduser testuser //新建testuser 用户 
passwd testuser //给testuser 用户设置密码

2.建工作组 
groupadd testgroup //新建test工作组

3.新建用户同时增加工作组 
useradd -g testgroup testuser //新建testuser用户并增加到testgroup工作组

//注：：-g 所属组 -d 家目录 -s 所用的SHELL

4.给已有的用户增加工作组 
usermod -G groupname username

5.临时关闭 
在/etc/shadow文件中属于该用户的行的第二个字段（密码）前面加上就可以了。想恢复该用户，去掉即可 
//或者使用如下命令关闭用户账号： 
passwd testuser –l 
//重新释放： 
passwd testuser –u

6.永久性删除用户账号 
userdel testuser 
groupdel testgroup 
usermod –G testgroup testuser //（强制删除该用户的主目录和主目录下的所有文件和子目录）

7.显示用户信息 
id user 
cat /etc/passwd

补充:查看用户和用户组的方法 
用户列表文件：/etc/passwd 
用户组列表文件：/etc/group 
查看系统中有哪些用户：cut -d : -f 1 /etc/passwd 
查看可以登录系统的用户：cat /etc/passwd | grep -v /sbin/nologin | cut -d : -f 1 
查看用户操作：w命令(需要root权限) 
查看某一用户：w 用户名 
查看登录用户：who 
查看用户登录历史记录：last

引用自：
Linux——CentOS7添加/删除用户和用户组（学习笔记） - bfhxt - 博客园
https://www.cnblogs.com/bfhxt/p/9933201.html
### 6.2.3.  sudo获取超级用户root权限
sudo 命令 [选项] [参数]
选项
-i   切换到root用户
（sudo创建的文件及文件夹是属于root用户和组）
sudo –i    #进入超级权限，输入当前用户密码
不同权限下运行区别：
username@ubuntu:~$
root@ubuntu:~#
### 6.2.4.  su 登录root用户
su
su [用户名]    #进入超级权限，输入管理员密码
### 6.2.5.  exit 退出当前用户登录
exit       #退出用户登陆
## 6.3. 文件及权限管理：
### 6.3.1.  ls查看文件及基本信息
ls命令：
ls -l
查看的权限表示：
- rwx --- --- tarena tarena ???? a.txt
d r-- --- ---
b r-- --- ---
c r-- --- ---
从左到右为：文件标识+用户组权限+___+___+文件名
1文件类型：
d      #文件夹
-      #普通文件
l      #链接文件
c/b	    #设备文件
2文件用户
基础权限：
文件所有者(owner)，又称属主
组(group)，又称属组
其他人(other)
3权限：
r	读权限
w	写权限
x	执行权限
最高权限：rwx rwx rwx
最低权限：--- --- ---
	数字代表的权限
读取的权限等于4，用r表示；
写入的权限等于2，用w表示；
执行的权限等于1，用x表示；
通过4、2、1的组合，得到以下几种权限：
0（没有权限）；
4（读取权限）；
5（4+1 | 读取+执行）；
6（4+2 | 读取+写入）；
7（4+2+1 | 读取+写入+执行）
下面列出常用的linux文件权限：
444 r--r--r--
600 rw-------
644 rw-r--r--
666 rw-rw-rw-
700 rwx------
744 rwxr--r--
755 rwxr-xr-x
777 rwxrwxrwx
### 6.3.2.  chmod 文件权限修改
	修改文件权限的修改：
chmod 权限操作 文件(夹)名
选项：
-R  对目前目录下的所有文件与子目录进行相同的权限变更(即以递回的方式逐个变更)

注：普通用户不能修改root用户的权限
u	用户（属主）	user
g	同组用户		group
o	其它用户		other
a	所有用户
+	
-	

chmod a+rwx a.txt	#所有用户权限加上rwx
chmod u-r a.txt	#用户权限减去r

chmod u+x ./a.sh   让文件所有者有执行权限
chmod 0555 ./a.sh  让所有人有读和执行权限
chmod 0554 ./a.sh  所有者和组成员有读和执行权限，其他人是读权限

### 6.3.3.  chown 所属权限的修改：
chown 用户名 文件         #更改文件所有者
chown 用户名:组名 文件     #同时更改文件所有者和所属组
chgrp 组名 文件            #只更改文件所属组

chown usr1 ./file1 
chown usr1:PAG ./file1 
chgrp PAG ./file1

## 6.4. 磁盘管理
### 6.4.1.  du 查看文件夹大小
du [选项] 文件夹
选项：
-h   以k,m,g为读数
-S   显示文件夹
-s   总计
### 6.4.2.  df 查看磁盘大小
df [选项]
选项：
-h   以k,m,g为读数



---
# 7.  LINUX网络命令
## 7.1. 常规操作
	hostname：显示系统主机名

	ping：测试主机与其他主机连通性
用法：ping [参数] 目标主机名/ip地址 
	-c：ping的次数（默认为无限次）
	-i：ping的间隔（默认为1秒）
	host：查找ip地址
用法：host  主机名/ip地址
	telnet：远程登录
用法：telnet  主机地址
	write：向用户发送消息
write 用户名
	mesg管理信息
mesg y 允许他人向自己终端发送消息
      n 不允许他人向自己终端发送消息
	passwd修改密码
passwd

## 7.2. 远程管理
	ssh远程用户登录
ssh [-p port] user@remote 　　
#port是端口号，不写默认22 ; user是用户名 ；remote是服务器IP地址/域名/别名

	scp远程拷贝
远程拷贝，即在远程服务器和本地登陆机之前实现文件与目录的相互拷贝。
scp [选项] user@remote:A B 　　#将远程或目录A 复制到本地文件或目录B
scp [选项] B user@remote:A 　　#将本地文件或目录B复制到远程文件或目录A
选项：
-P port : 若远程 SSH 服务器的端口不是 22，需要使用大写字母 -P 选项指定端口
-r : 若给出是目录，则 scp 将递归复制该目录下的所有子目录和文件

scp -r root@43.224.34.73:/home/lk /root
scp -r maruixin@192.168.20.196:/TRAIN/RESEQ/CROP/Test_data/ .
scp -r mymenu root@192.168.20.196: /TRAIN/RESEQ/CROP/chenjun
scp /TRAIN/RESEQ/CROP/chenjun/* maruixin@192.168.20.196:/TRAIN/RESEQ/CROP/chenjun



## 7.3. 文件传输
### 7.3.1.  wget下载
wget [选项] [网址]
选项：
-t 0  重试次数
-c   断点续传
wget -r -np -nH -R index.html http://url/including/files/you/want/to/download/


---
# 8.  LINUX系统配置操作
## 8.1. 系统
### 8.1.1.  系统开关机
重启，关机：
shutdown -r now     #重启
shutdown -s now     #关机
重演你的系统启动的所有消息
journalctl -b
### 8.1.2.  查看系统及程序状态
查看当前系统版本： 
查看当前服务运行状态：
systemctl status [服务名] 
通过service调节进程服务的状态：
sudo service xxx status/start/stop/restart 
查看全部服务列表：
sudo service --status-all
## 8.2. 设置自动启动服务
### 8.2.1.  用户登录启动
文件：
你好，这里是 /etc/motd ，所有用户统一显示登录信息，我将统一管理！
目录：
你好，这里是 /etc/profile.d ，我将进行所有用户测试
### 8.2.2.  开机启动脚本
	方法一：/etc/rc.local
开机时会默认执行该文件命令

	方法二：在/etc/init.d目录下添加自启动脚本

### 8.2.3.  开机启动服务设置
查看哪个服务进程启动耗时最长。
    systemd-analyze blame
查看开机启动列表
    systemctl list-unit-files --type=service | grep enabled
    systemctl list-unit-files --type=service
停止服务，关闭开机启动服务，卸载该服务
    sudo systemctl stop bluetooth.service 
    sudo systemctl disable bluetooth.service  
    sudo systemctl mask bluetooth.service
方案：
新版ubuntu 里面都有systemd这个东东了，这个用来配置开始自启动服务。 
写一些脚本，将自启动软件转换成启动服务就ok。 
这个是系统级启动，即使你是user组，用了这个也会帮你开机自启动。
把你要执行的文件放在/etc/init.d/目录下 
然后设置启动级别就可以了吧
比如设置Apache开机启动，可以使用 
update-rc.d apache defaults
解决启动时sudo 
echo password |sudo -S command
### 8.2.4.  定时任务启动
crontab -e
# 磁盘挂起
#*/5 * * * * /PUBLIC/software/RESEQ/software/SGE/setup/cluster_tools/watchDisk/disk_monitor_client.pl
#*/50 * * * * /PUBLIC/software/RESEQ/software/SGE/setup/cluster_tools/watchDisk/disk_monitor_client.pl
#*/5 7-20  * * * /PUBLIC/software/RESEQ/software/SGE/setup/cluster_tools/watchDisk/disk_monitor_client.pl
#*/5 7-8  * * * /PUBLIC/software/RESEQ/software/SGE/setup/cluster_tools/watchDisk/disk_monitor_client.pl

# 每日磁盘统计
0 8 * * * /ifs/TJPROJ3/Plant/chenjun/software/fileshare/00.get2mail.sh
#*/1 * * * * /ifs/TJPROJ3/Plant/chenjun/software/fileshare/test.sh

# 自动扫盘
0 0 * * 0  /bin/sh /ifs/TJPROJ3/Plant/chenjun/Admin/02.saopan/shell.sh
0 9 * * *  /bin/sh /ifs/TJPROJ3/Plant/chenjun/Admin/02.saopan/get-result.sh


# 集群job上限提醒
#*/20 * * * * /home/chenjun/test.sh
*/20 * * * * source /etc/profile; setjob="1950" ; numjob=`/opt/gridengine/bin/linux-x64/qstat -u chenjun|wc -l`; if (("$numjob" >= "$setjob")); then echo "h `date +%F` $numjob / $setjob"; /PUBLIC/software/public/Python-2.7.6/bin/python /ifs/TJPROJ3/Plant/chenjun/mytools/sendmail.py 1170101471@qq.com -c "Warning, job beyongd your set: $setjob ,now is $numjob."; else echo "l `date +%F` $numjob / $setjob";fi &>/home/chenjun/tmplog/log_jobnums


# 使用方法
# {minute} {hour} {day-of-month} {month} {day-of-week} {full-path-to-shell-script}
# o minute: 区间为 0 – 59
# o hour: 区间为0 – 23
# o day-of-month: 区间为0 – 31
# o month: 区间为1 – 12. 1 是1月. 12是12月.
# o Day-of-week: 区间为0 – 7. 周日可以是0或7.
## 8.3. 软件操作
### 8.3.1.  软件安装与卸载
Ubuntu安装：    
apt-get install systemd libpam-systemd systemd-ui
sudo  dpkg  -i   deb文件名
sudo apt-get update   # 更新源
sudo apt-get install package  # 安装包
sudo apt-get remove package  # 删除包
sudo apt-cache search package  # 搜索软件包
sudo apt-cache show package   # 获取包的相关信息，如说明、大小、版本等
sudo apt-get install package --reinstall   # 重新安装包
sudo apt-get -f install   # 修复安装
sudo apt-get remove package --purge  # 删除包，包括配置文件等
sudo apt-get build-dep package  # 安装相关的编译环境
sudo apt-get upgrade  # 更新已安装的包
sudo apt-get dist-upgrade  # 升级系统
sudo apt-cache depends package  # 了解使用该包依赖那些包
sudo apt-cache rdepends package  # 查看该包被哪些包依赖
sudo apt-get source package   # 下载该包的源代码
sudo apt-get clean && sudo apt-get autoclean  # 清理无用的包
sudo apt-get check  # 检查是否有损坏的依赖
yum安装：
yum install <appname> -y
yum remove <appname>
清除无效的隧道适配器: 
netsh interface teredo set state disable
netsh interface 6to4 set state disable
netsh interface isatap set state disable
## 8.4. 系统常用配置文件
### 8.4.1.  网络
	修改DNS服务器
vim /etc/resolv.conf

## 8.5. 环境变量
### 8.5.1.  简介
何为环境变量？类似于变量，但不同于变量，主要是它的作用范围和生存周期！【总结的到位否？】
	常用的环境变量 
PATH       决定了shell将到哪些目录中寻找命令或程序 
HOME       当前用户主目录 
HISTSIZE 　历史记录数 
LOGNAME    当前用户的登录名 
HOSTNAME 　指主机的名称 
SHELL      当前用户Shell类型 
LANGUGE  　语言相关的环境变量，多语言可以修改此环境变量 
MAIL     　当前用户的邮件存放目录 
PS1      　基本提示符，对于root用户是#，对于普通用户是$
### 8.5.2.  环境变量的作用范围
如何查看变量与环境变量作用范围？
	查看与删除环境变量
env   # 只查看当前用户的变量（env 是环境单词的缩写 environment）
set   # 查看当前终端的变量（终端变量包括了用户变量）
unset [name]   # 可以删除指定的环境变量，当name存在时，删除指定环境变量。
	设置变量的三种方式：
1. 在/etc/profile文件中添加变量【对所有用户生效(永久的)】
2. 在用户目录下的.bash_profile文件中增加变量【对单一用户生效(永久的)】
3. 直接运行export命令定义变量【只对当前shell(BASH)有效(临时的)】
...
### 8.5.3.  用户登录加载环境变量的顺序
linux配置文件执行顺序为：
/etc/profile→
(~/.bash_profile | ~/.bash_login | ~/.profile)→
~/.bashrc →
/etc/bashrc →
~/.bash_logout
### 8.5.4.  命令使用及设置
alias：为命令创建别名
alias l='ls -lh'
unalias：删除别名
history：显示最近执行的命令 
## 8.6. 命令集锦之——系统管理

# 打印当前系统所有用户的“用户名和组”信息，用\t隔开：
awk -F ':' '{print $4}' /etc/group|sed 's#,#\n#g'|awk NF|sort|uniq|xargs -i id {}|awk -F '[()]' '{print $2"\t"$4}'


# 9.  SHELL编程极简介绍
## 9.1. shell脚本的运行
1、作为可执行程序
	文件test.sh第一行需要加解释器
#!/bin/bash
echo "Hello World!"
$ chmod +x ./test.sh
$ ./test.sh
2、作为解释器参数
/bin/sh test.sh
/bin/php test.php

	注释：
单行注释
# echo 1
多行注释：
<<!
echo 1
echo 2
echo 3
!

echo 4

## 9.2. if语句块
### 9.2.1.  “if [ xxx ]”语句
#### 9.2.1.1.  基本语法
	语法
if [ xxx ]; then
    语句1
elif [ xxx ]; then
    语句2
else
    语句3
fi
xxx可以为表达式，如字符串表达式，当不为空表示真
	示例
若有参数则打印ok，否则false，此处的参数可以理解为一个字符串
if [ $1 ]; then
   echo ok
else
   echo false
fi
判断命令是否有输出结果：
if [ "`ps aux|grep frpc|grep -v " grep "`" != "" ]; then 
echo 在运行; 
else 
echo 未运行，准备投递运行 ;
fi
#### 9.2.1.2.  运算符
	判断路径/文件对象是否存在
if [ -e "/ifs/TJPROJ3/Plant/chenjun/Admin/04.mapXiaji" ]; then cd /ifs/TJPROJ3/Plant/chenjun/Admin/04.mapXiaji; else cd /NJPROJ2/Plant/chenjun/Admin/04.mapXiaji; fi
	数值比较
数值比较运算符：
整数比较

-eq 等于,      如:if [ "$a" -eq "$b" ]
-ne 不等于,    如:if [ "$a" -ne "$b" ]
-gt 大于,      如:if [ "$a" -gt "$b" ]
-ge 大于等于,  如:if [ "$a" -ge "$b" ]
-lt 小于,      如:if [ "$a" -lt "$b" ]
-le 小于等于,  如:if [ "$a" -le "$b" ]
< 小于(需要双括号),        如:(("$a" < "$b"))
<= 小于等于(需要双括号),   如:(("$a" <= "$b"))
> 大于(需要双括号),        如:(("$a" > "$b"))
>= 大于等于(需要双括号),   如:(("$a" >= "$b"))
示例：
$ if [ 1 -eq 1 ]; then echo True; else echo False; fi
True
$ if [ 1 -eq 2 ]; then echo True; else echo False; fi
False
$ if (("123" >= "133"));then echo True;else echo False;fi
False

### 9.2.2.  “if <命令>”语句
判断ls file命令是否运行成功
if ls file; then
   echo ok
else
   echo false
fi

## 9.3. for语句块
示例
$ for x in `echo 1 2 3`; do echo $x; done
1
2
3

示例：妙用for循环控制进程数
for name in `ls raw-result/`; 
do 
((i++)); 
echo "python3 /ifs/TJPROJ3/Plant/chenjun/mytools/tools_jiqun/getsize.py raw-result/${name} 2 --add >result/${name} &"; 
if [ "$((${i}%3))" == "0" ]; then echo wait; fi;
done|awk '{print}END{print "wait"}'|sh

# 控制最大进程数为3
scan_path=../scan/01.scan_results/02.formatted_results_from_scan_shell_out/
i=0

for name in `ls ${scan_path}`; 
do ((i++)); 
echo "cat ${scan_path}/${name}/*|awk -v numb=${Num_b} '{if(\$5>=numb){OFS=\"\\t\";print \$3,\$5,\$9,\$6}}' >result/${name}_${Numname} &"; 
if [ "$((${i}%3))" == "0" ]; then echo wait; fi;
done|awk '{print}END{print "wait"}'|sh

## 9.4. while语句块

示例：
# handle "$line" done 其中string就是一个多行字符串。
echo "$string"|while read line ; do echo line; done
tail -1000 run-sserver.sh.log.2034|while read x; do echo -e "[url] $x"; echo -e "$x"|awk '{print $NF}'|cut -f 1 -d :|uniq|xargs -i curl https://ip.cn/index.php?ip={};  done
## 9.5. shell的参数传递
linux系统除了提供位置参数还提供内置参数，内置参数如下：　
$#  ----传递给程序的总的参数数目 　
$?  ----上一个代码或者shell程序在shell中退出的情况，如果正常退出则返回0，反之为非0值。 　　
$*  ----传递给程序的所有参数组成的字符串。 　　
$n  ----表示第几个参数，$1 表示第一个参数，$2 表示第二个参数 ...
$0  ----当前程序的名称 　　
$@  ----以"参数1" "参数2" ... 形式保存所有参数 　　
$$  ----本程序的(进程ID号)PID 　　
$!  ----上一个命令的PID
## 9.6. read标准输入
read -p "是否删除以上进程（y/n）？:" val
echo $val
# 10.  附
## 10.1. 博客收藏
### 10.1.1.  实用+必读
shell 语句出错自动退出 - drbinzhao的专栏 - CSDN博客
https://blog.csdn.net/drbinzhao/article/details/8281645?tdsourcetag=s_pctim_aiomsg
Linux set 指令用法 - options - 迎难而上 - CSDN博客
https://blog.csdn.net/u010003835/article/details/79936072
set -u  # 使脚本遇到不存在变量则退出
set -e  # 使脚本出错就退出
set -ue   # 若遇变量不存在或运行报错，则直接退出不再执行后面                                   
set -o pipefail  # 使得管道中的异常状态保持到后面

```bash
ls  1 2 
# ls: 无法访问1: 没有那个文件或目录
# 2
echo $?
# 2
ls  1 2 | xargs echo files:
# ls: 无法访问1: 没有那个文件或目录
# files: 2
echo $?
# 0
set -o pipefail
ls  1 2 | xargs echo files:
# ls: 无法访问1: 没有那个文件或目录
# files: 2
echo $?
# 2
```

# 11.  待整理

1.basename 该命令的作用是从路径中提取出文件名,使用方法为basename NAME [SUFFIX]。 1)从路径中提出出文件名(带后缀),例子如下: 2)从上面命令的用法中可以看到,后缀...
2.dirname 该命令的作用是从路径中提取出目录名,使用方法为 dirname NAME 使用例子如下: 这样就提取出了file...
3.realpath 上面两个命令的结合体: 相对路径输出绝对路径
shell获取文件名和目录名-新人一个-51CTO博客
https://blog.51cto.com/welcomeweb/2163585


验证gz文件是否可以直接cat一块儿，并且对原数据内容没有损失
echo 1234567890 >1.txt
echo 9234567899 >2.txt

gzip -f 1.txt 
gzip -f 2.txt 

zcat 1.txt.gz 2.txt.gz |gzip >all_gzip.txt.gz 
cat 1.txt.gz 2.txt.gz >all_cat.txt.gz

cp all_cat.txt.gz all_cat2.txt.gz
cp all_gzip.txt.gz all_gzip2.txt.gz

gzip -d all_cat2.txt.gz
gzip -d all_gzip2.txt.gz

md5sum all_cat2.txt all_gzip2.txt


单双引号区别

多重赋值
read x1 x2 x3 <<< "1 2 3"

