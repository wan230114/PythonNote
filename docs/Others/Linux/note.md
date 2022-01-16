## awk高级用法

### 文件判断
判断test2.txt 中第一列的内容在test1.txt 中，


说明：
- FNR和NR的特性，当扫描第一个文件时，FNR与NR相同。
- 先对第一个文件进行扫描，将每行的内容以键值对的形式保存到a数组中，
- 再对第二个文件进行扫描，判断所检查的列的内容是否在数组a中，
- 然后按照自己的需求打印结果即可。


实例：
```bash
echo -e "
chr1 1 2 AAA
chr1 3 4 AAAA
chr1 5 6 BB
chr1 7 8 CC
"|awk NF|sed 's# #\t#g' >datas.txt

echo "
AAA
BB
CC
AA
BB
"|awk NF >keys.txt

head datas.txt
head keys.txt

# 以下展示两种用法
# 注，awk是将第一个文件读入内存，去第二个文件里面遍历查询。

# 按datas.txt的顺序打印，此法多用于特定列的查找
awk 'NR==FNR{a[$1]=$1;next}NR!=FNR{if($4 in a)print $0}' keys.txt datas.txt

# 按keys.txt的顺序打印，此法多用于查找并保留顺序合并
# 文件1 行存入数组a                文件2 $0 查找a
awk 'NR==FNR{a[$4]=$0;next}NR!=FNR{if($0 in a)print a[$0]}' datas.txt keys.txt
awk 'NR==FNR{a[$4]=$0;next}NR!=FNR{if($1 in a)print a[$0]}' datas.txt keys.txt
awk 'NR==FNR{a[$4]=$0;next}NR!=FNR{if($1 in a)print $0"\t"a[$0]}' datas.txt keys.txt

```


### awk 的数值计算范围

```bash
echo | awk '{print 9999999999999999999999+1}'
# 10000000000000000000000
echo | awk '{print 99999999999999999999999+1}'
# 99999999999999991611392
```

### awk 从文件和管道同时读入数据

```bash
awk 'ARGIND==1{print NR,FNR,$0}ARGIND==2{print NR,FNR,$0}' <(echo -e "1\n2\n3") <(echo -e "10\n20\n30") 
awk 'ARGIND==1{a=$1; b=$2; c=$3;}ARGIND==2{print $1*a,$2*b,$3*c}' <(echo -e "2 3 4") <(echo -e "10 20 30\n100 200 300")
```


---
## 其他

### case法 替代 if else if

```bash
cho=y
case $cho in  # 判断变量cho的值
    "yes")  # 如果是yes
        echo "Your choose is yes!"  # 则执行程序1
        ;;
    "no")  # 如果是no
        echo "Your choose is no!"  # 则执行程序2
        ;;
    *)  # 如果既不是yes,也不是no
    echo "Your choose is error!"  # 则执行此程序
    ;;
esac
```


### rsync妙用

rsync 参数：
- -a
- -L: 复制文件的真实文件，而不只复制软链接
- -v: 打印当前操作的文件
- -z: 传输时进行压缩提高效率
- --delete: 参数目标目录冗余文件
- -P: 打印当前操作的文件进度

```bash
rsync -avz --delete  ./  gzsc:/work/users/exchange_qts/chenjun/Product-Lines/Product-Lines/
rsync -avzL --delete  Release_Datas_20210429/  nas:/share/external/DEV3301_1/Release_Datas_20210429
#  将dirA的所有文件同步到dirB内，并删除dirB内多余的文件
#  rsync -avz --delete dirA/ dirB/       #源目录和目标目录结构一定要一致！！不能是dirA/* dirB/  或者dirA/ dirB/*  或者 dirA/* dirB/*


# -ravz 已经会自动同步改变的文件, --delete只是额外去删除dir2内“在dir1中不存在”的文件
mkdir dir1 dir2
echo 123 >dir1/1; rsync -ravz dir1/ dir2/; cat dir2/1
echo 323 >dir1/1; rsync -ravz dir1/ dir2/; cat dir2/1
echo 423 >dir1/1; rsync -ravPt dir1/ dir2/; sleep 0.2; touch dir2/1; cat dir2/1

```


# mkfifo

```
NAME(名称）
       mkfifo - 创建FIFO(命名管道）

SYNOPSIS(总览）
       mkfifo [options] file...

       POSIX options(选项）： [-m mode]

       GNU options(选项）（最短格式）： [-m mode] [--help] [--version] [--]

DESCRIPTION(描述)
       mkfifo 使用指定的文件名创建FIFO(也称为"命名管道").

       "FIFO"是一种特殊的文件类型，它允许独立的进程通讯.      一个进程打开FIFO文件进行写操作,而另一个进程对之进行读操作,
       然后数据便可以如同在shell或者其它地方常见的的匿名管道一样流线执行.

       默认情况下,创建的FIFO的模式为0666('a+rw')减去umask中设置的位.
```

```bash
# Define a multi-threaded run channel
mkfifo tmp
exec 9<>tmp
for ((i=1;i<=${THREAD_NUM:=1};i++))
do
    echo >&9 
done
```


```bash
seq 1 10 | xargs -i echo "sleep 1 && echo "{} | xargs -iCMD -P3 bash -c CMD
```

## 用户相关命令


```bash
# 增加用户

# 增加组

# 增加组内某个用户
usermod -aG group_name user_name
# 删除组内某个用户
gpasswd -d root gl
```

## 

```bash
zcat xx.gz
pigz -cd xx.gz
```

```bash
a="col1 test1\tcol2 test2
1\t2
2\t3
3\t4
"
# echo -e "$a" | column -c 1
echo -e "$a" | column -t
echo -e "$a" | column -ts $'\t'

```