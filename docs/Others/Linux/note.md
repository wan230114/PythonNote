# 一些杂烩
## awk的一些高级用法

### 文件的匹配判断

需求：判断 test2.txt 中第一列的内容在 test1.txt 中。

说明：
- FNR和NR的特性，当扫描第一个文件时，FNR与NR相同。
- 先对第一个文件进行扫描，将每行的内容以键值对的形式保存到a数组中，
- 再对第二个文件进行扫描，判断所检查的列的内容是否在数组a中，
- 然后按照自己的需求打印结果即可。

实例：
```bash
{
echo -e "
chr1 1 2 A
chr1 1 3 AAA
chr1 3 4 AAAA
chr1 5 6 BB
chr1 7 8 CC
chr1 7 9 CCC
"|awk NF|sed 's# #\t#g' >datas.txt

echo "
AA
BB
"|awk NF >keys.txt

head datas.txt
head keys.txt
}
# 以下展示两种用法
# 注，awk是将第一个文件读入内存，去第二个文件里面遍历查询。

# 1. 按datas.txt的顺序打印，此法多用于特定列的查找

# 1） 完全匹配
# 使用时，将 $4 改为自己需要查找的列号

awk -F '\t' 'NR==FNR{a[$1]=$1;next}NR!=FNR{if($4 in a)print $0}' keys.txt datas.txt

# 2） 不完全匹配
# 失效笔记： awk 中 "/"x"/" 不生效。 因此这个不生效 awk '{print}' keys.txt | while read patten; do
# 另类解决方案:
{
# 使用时，将 $4 改为自己需要查找的列号
NRs=""
IFS=$'\n'  # 因为for循环以环境变量IFS的值作为分隔符，而IFS的默认值是“<space/空格>”“<tab/制表符>”“<newline/新行>”, 此处设置为\n
# step1: 将匹配的行号存入变量NRs
# 程序1使用了管道,管道中的while是在子shell中运行的,并不能返回到父shell中。 此处必须使用for循环, 而不能使用 `| while read x; do ... done`
for patten in $(cat keys.txt); do
    res="`awk -v patten=$patten '$4~patten{print NR}' datas.txt`"
    if [ "$res" ]; then
        NRs+="$res
"
    fi
done
# step2: 打印所有匹配keys.txt的行
awk -F "\t" 'NR==FNR{a[$0]=$0;next}NR!=FNR{if(FNR in a)print $0}' <(echo "$NRs" | awk NF | sort -n | uniq) datas.txt
}

# 2. 按keys.txt的顺序打印，此法多用于查找并保留顺序合并
# 注: 此方法，当 datas.txt 数据过大时谨慎使用，内存可能无法支撑
# 文件1 行存入数组a                文件2 $0/$1 查找a
awk 'NR==FNR{a[$4]=$0;next}NR!=FNR{if($0 in a)print a[$0]}' datas.txt keys.txt
awk 'NR==FNR{a[$4]=$0;next}NR!=FNR{if($0 in a)print a[$0]}' datas.txt keys.txt
awk 'NR==FNR{a[$4]=$0;next}NR!=FNR{if($0 in a)print $0"\t"a[$0]}' datas.txt keys.txt

```


案例：

```bash
# AHJ2GCAFX3-2203290743-234.pe.Mutation_new.txt 过滤 列 Entrez Gene ID 中的存在值
colnum=`cat AHJ2GCAFX3-2203290743-234.pe.Mutation_new.txt | head -1 | sed 's#\t#\n#g' | cat -n | grep "Entrez Gene ID" | awk '{print $1}'`
cat AmCare-334-carrier-20220517.txt | sed -e 's/[[:space:]][[:space:]]*/ /g'  | grep -oP '(?<="id":").*?(?=")' >tmp_keys.txt
awk -F "\t" -v colnum=$colnum 'NR==FNR{a[$1]=$1;next}NR!=FNR{if(NR==1){print}else if($colnum in a){print}}'  tmp_keys.txt  AHJ2GCAFX3-2203290743-234.pe.Mutation_new.txt >AHJ2GCAFX3-2203290743-234.pe.Mutation_new-filter.txt
\rm tmp_keys.txt
```


### awk 的数值计算范围

结论： [-99999999999999999999999, 99999999999999999999999]

23个9, 具体是否依系统而定还需要测试。 

```bash
echo | awk '{print 9999999999999999999999+1}'
# 10000000000000000000000
echo | awk '{print 99999999999999999999999+1}'
# 99999999999999991611392
echo | awk '{print -9999999999999999999999-1}'
# -10000000000000000000000
echo | awk '{print -99999999999999999999999-1}'
# -99999999999999991611392
```

### awk 从文件和管道同时读入数据

```bash
# 使用 <() 直接作为文件灵活去处理
awk 'ARGIND==1{print NR,FNR,$0}ARGIND==2{print NR,FNR,$0}' <(echo -e "1\n2\n3") <(echo -e "10\n20\n30") 
awk 'ARGIND==1{a=$1; b=$2; c=$3;}ARGIND==2{print $1*a,$2*b,$3*c}' <(echo -e "2 3 4") <(echo -e "10 20 30\n100 200 300")

cat <(echo -e "1\n2\n3") | awk '{print NR,FNR,$0}'
# 使用 - 占位，表示文件是从管道接入
cat <(echo -e "1\n2\n3") | awk 'ARGIND==1{print NR,FNR,ARGIND,$0}ARGIND==2{print NR,FNR,ARGIND,$0}' - <(echo -e "10\n20\n30") 
```

### awk 按列名过滤文件

```bash
echo -e 'a\tb\tc\n1\t100\t1000\n2\t150\t2000\n5\t200\t3000' > a.txt
cat a.txt | awk -F '\t' '{
      if(NR==1){
          split($0, header, "\t")
          for (i in header){ colnums[header[i]]=i }
          print
      } else {
          if ($colnums["a"]>=2 &&
              $colnums["b"]>120){ print }
      }
  }' > a2.txt
cat a.txt
cat a2.txt
```

### awk去重以某列重复的行


```bash
echo "\
adc 3 5
a d a
a 3 adf
a d b
a 3 adf" > 2.txt

# 去重第一列重复的行：
# 重复的行取最上面一行记录
cat 2.txt |awk '!a[$1]++{print}'
# adc 3 5
# a d a

# 去重以第一列和第二列重复的行：
cat 2.txt |awk '!a[$1" "$2]++{print}'
# adc 3 5
# a d a
# a 3 adf

# 去除重复的行：
cat 2.txt |awk '!a[$0]++{print}'
# adc 3 5
# a d a
# a 3 adf
# a d b

# 只显示重复行：
cat 2.txt |awk 'a[$0]++{print}'
# a 3 adf
```

---
## 其他

### case法 替代 if else if

```bash
# case法
{
cho=y
case $cho in  # 判断变量cho的值
    "yes")  # 如果是yes
        echo 'Your choose is yes!'  # 则执行程序1
        ;;
    "no")  # 如果是no
        echo 'Your choose is no!'  # 则执行程序2
        ;;
    *)  # 如果既不是yes,也不是no
    echo 'Your choose is error!'  # 则执行此程序
    ;;
esac
}

# 原if：
{
cho=y
if [ "$cho" == "yes" ]; then  # 如果是yes
    echo 'Your choose is yes!'  # 则执行程序1
else if [ "$cho" == "no" ]; then  # 如果是yes
    echo 'Your choose is no!'  # 则执行程序2
else  # 如果既不是yes,也不是no
    echo 'Your choose is error!'  # 则执行此程序
fi
}

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
# 非增量同步，所有更改同步
rsync -avz --delete  ./  gzsc:/work/users/exchange_qts/chenjun/Product-Lines/Product-Lines/
rsync -avzL --delete  Release_Datas_20210429/  nas:/share/external/DEV3301_1/Release_Datas_20210429
#  将dirA的所有文件同步到dirB内，并删除dirB内多余的文件
#  rsync -avz --delete dirA/ dirB/
# 末尾的 / 很关键 !!!!
# 源目录和目标目录结构一定要一致！！不能是dirA/* dirB/  或者dirA/ dirB/*  或者 dirA/* dirB/*  或者 dirA/ dirB , ...
# -ravz 已经会自动同步改变的文件, --delete只是额外去删除dir2内“在dir1中不存在”的文件

mkdir dir1 dir2
echo 123 >dir1/1; rsync -ravz dir1/ dir2/; cat dir2/1
echo 323 >dir1/1; rsync -ravz dir1/ dir2/; cat dir2/1
echo 423 >dir1/1; rsync -ravPt dir1/ dir2/; sleep 0.2; touch dir2/1; cat dir2/1

```

两台远程服务器之间进行同步：

```bash
# 直接同步报错，原因是不支持
# rsync -avP  vps_sh:/root/test-2.zip .  jun@192.168.3.162:~/
# The source and destination cannot both be remote.

# https://unix.stackexchange.com/questions/183504/how-to-rsync-files-between-two-remotes
# SSH -R 反向端口转发
# 指定了 139.196.159.43:22 源服务的端口。 这里 jun@192.168.3.162 是指目标服务器
# 实现条件为 目标服务器上 先使用秘钥免密码登录后才能进行
ssh -R localhost:50000:139.196.159.43:22 jun@192.168.3.162 # 先登录，然后手动执行 ssh-copy-id -p 50000 root@localhost
ssh -R localhost:50000:139.196.159.43:22 jun@192.168.3.162 'rsync -e "ssh -p 50000 root@localhost" -vuar localhost:/root/test-2.zip ~/target/'

```


# 其他
## mkfifo

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

## 解压速度神器

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


## 执行状态判断调试

```bash
VQSR(){

    {
        sleep 0.1 && echo cmd1 && \
        sleep 0.2 && echo cmd2
    } &

    {
        sleep 0.1 && rm cmd3  # 异常抛出
    } &

    i=0
    for pid in $(jobs -p); do
        ((i++))
        wait $pid
        stat[$i]=$?
        if [ ${stat[$i]} != 0 ]; then return; fi
    done

    ((i++))
    echo cmd4
    stat[$i]=$?
    if [ ${stat[$i]} != 0 ]; then return; fi
}


for i in 8 7; do
    echo -e "\n####################"
    echo max-gaussians=$i
    stat=(0 0 0 0)
    VQSR $i
    sum_stats=$(echo ${stat[*]} | sed 's# #\n#g' | awk '{s += $0} END {print s}')
    echo stat: ${stat[*]}
    echo sum_stats: $sum_stats
    if [ "$sum_stats" == "0" ]; then
        echo all done.;
    else
        echo not ok.;
    fi
done

```


```bash
{
    sleep 0.1 && echo cmd1 && \
    sleep 0.2 && echo cmd2
} &

{
    set -e
    # sleep 0.1 && rm cmd3  # 异常抛出
    rm cmd3  # 异常抛出
    echo cmd4
} &

{
set -exv
rm cmd3.1  # 异常抛出
echo cmd4.1
} &

i=0
for pid in $(jobs -p); do
    ((i++))
    wait $pid
    stat[$i]=$?
done

# 日志打印
echo cmd5: 此处可以打印日志，并在后续依然保持异常抛出

# 异常抛出
echo Run stats: ${stat[*]}
sum_stats=$(echo ${stat[*]} | sed 's# #\n#g' | awk '{s += $0} END {print s}')
max_stats=$(echo ${stat[*]} | sed 's# #\n#g' | awk 'BEGIN{m=0}{if($0>m) m=$0} END {print m}')
if [ "$sum_stats" == "0" ]; then
    echo "All jobs done.";
else
    echo "Some jobs not ok.";
    exit $max_stats
fi

```


转置文件：（未成功实现，日后补充）
```bash
T() {
    for i in `seq $(head -n 1 $1 | awk -F '\t' '{print NF}')`; do awk -v a=$i '{print $a}' $1 | awk  -F '\t' BEGIN{RS=EOF}'{gsub("\n","\t");print}' ; done
}

```

# 出错情景

末尾加入 || cat 即可解决

```bash
seq 1 100 | gzip > a.gz
bash -c $'
set -o pipefail
zcat a.gz  | awk \'{if(NR<=3){print}else{ exit 0 }}\' | wc -l
echo $?
'
# 3
# 0

seq 1 10000000 | gzip > a.gz
bash -c $'
set -o pipefail
zcat a.gz  | awk \'{if(NR<=3){print}else{ exit 0 }}\' | wc -l
echo $?
'
# 3
# 141
```