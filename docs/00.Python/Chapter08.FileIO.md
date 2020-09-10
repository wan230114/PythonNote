# 8. 文件FILE及编码

---
导读：
> 如何理解文件是什么？  
> 如何理解位(bit)、字节(byte)、字符、编码之间的关系？  
> 编码是什么？为什么会有不同编码？  
> utf-8和gbk编码的文件区别是什么？  
> 字节串是什么，与二进制文件有什么关系？  
> Python在Linux下和Windows下读文件区别？  

学习前准备：

文件准备： 运行以下代码, 生成文件 test_file.txt , 以便后续学习运行使用

```python
with open('demo_Chapter08/test_file.txt', 'wb') as fo:
    for i in range(0, 64, 8):
        fo.write((''.join(['%02d'%xx for xx in range(i, i+8)])
                  +'\r\n').encode())
```

## 8.1. 基本概念

文件是什么，如何理解不同的文件类型？

### 8.1.1. 文件

什么是文件？各种格式之间有什么区别？

可以用一句话概括：
- 文件是存储字节串的容器；编码只是文件转换为人类能看懂的翻译规则；后缀名只是告诉了该系统中如何对这个文件的这些字节串进行解码(后缀名常用于区分文件格式，文件类型)。


---
#### 8.2.1.1. 数据存储基础

**数据的存储基础：** 

- 位：数据存储的最小单位。在计算机中的二进制数系统中，位，简记为b，也称为比特，每个0或1就是一个位(bit)。
- 字节：用于计量存储容量的一种计量单位。大多数计算中，1字节(B,byte) = 8位(b, bit)，由 8个位 (8个`0`或`1`) 组成了一个字节。能表示0-255这256个信息，1字节刚好与两位十六进制数对应，从`00`到`ff`。以下关于文件的描述都默认8位=1字节。

**关于字节的一些换算单位：**
- 字节(Byte)=8位(bit)
- 1KB( Kilobyte，千字节)=1024B
- 1MB( Megabyte，兆字节)=1024KB
- 1GB( ... 


---
#### 8.2.1.2. 文件储存的信息本质

**文件存储的信息本质：**
- 文件的本质都是二进制流，八个位组成的“字节”为文件存储的基本单位。
- 文件的存储，是由一系列字节组合的字节串存储。
- 文件的编码与解码规则，则是将文件中一个字节或多个连续字节翻译成一个有意义的值。存储的数据本身没有任何意义，“编码规则”、“翻译规则”则是人为规定，使字节的各类特定组合对应了人们理解的不同信息，而让文件有了意义。
- 文件类型(文件格式)，常使用后缀名来区分。后缀名也没有任何意义，后缀名只是告诉了该系统中如何对该文件内容的字节串进行解码。一个文件的后缀名是可随意改的，不由计算机确认翻译规则，由我们人为指定也是可以的。 

Ps: 从字节的规定，到翻译规则的建立，到如何让操作系统自动解析，所有的规则规定，如同语言，文化一样，语言与文化本质上就是同化更多人。

**文件的存储特点：**  
- 文件中的数据是以字节为单位进行顺序存储的；
- 文件又是数据存储的一个单位；
- 文件通常用来长期存储数据；

**二进制文件是什么，与文本文件有什么关系？**  
- **二进制文件的组成同样是由 不同8个位组成的字节，再由不同字节组合而成的字节串。** 文本文件只是二进制文件中的一种特例，为了与文本文件相区别，人们又把除了文本文件以外的文件称为二进制文件。[——百度百科](https://baike.baidu.com/item/%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6)


---

实验1-1：  
> 打开 sublime text 软件，将以下代码复制到软件终端，选择以十六进制保存 `文件 > 以...编码保存(保存编码方式) > 选最后一行以十六进制保存`，文件名命名为`test.bmp`，之后便可以双击打开该文件，可以看到一个 `8像素 x 5像素` 包含横线的背景为灰色的图像。（示例中，从aa开始的每三个字节`aaaaaa` 代表一组RGB色彩，如三原色，Red170, Green170, Blue170组合成了灰色；而`000000`代表黑色）

```
424d ae00 0000 0000 0000 3600 0000 2800
0000 0800 0000 0500 0000 0100 1800 0000
0000 7800 0000 7412 0000 7412 0000 0000
0000 0000 0000 aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aa00 0000 0000 0000
0000 0000 0000 0000 0000 00aa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa 
```

实验1-2：  
> 运行以下脚本，亦可以生成一个同实验1相同的图像文件`test.bmp`。

```python
text = """
424d ae00 0000 0000 0000 3600 0000 2800
0000 0800 0000 0500 0000 0100 1800 0000
0000 7800 0000 7412 0000 7412 0000 0000
0000 0000 0000 aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aa00 0000 0000 0000
0000 0000 0000 0000 0000 00aa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa
aaaa aaaa aaaa aaaa aaaa aaaa aaaa 
"""
L = [xx for x in text.split() for xx in (x[:2], x[2:])]
L_bytes = [int('0x'+xx, 16) for xx in L]
print(*zip(L, L_bytes))

codes = bytes(L_bytes)
with open('demo_Chapter08/test.bmp', 'wb') as fo:
    print(codes)
    fo.write(codes)
```

图像展示：

<!-- ![](demo_Chapter08/test.bmp) -->

<div align=center>
<img src="docs/00.Python/demo_Chapter08/test.bmp"  width="50" align="middle" style='border:0px solid black'>
</div>

### 8.1.2. 编码

**编码是什么？怎么理解编码与文件的关系？**
- 文件本质并无差异，都是字节串文件，差异在于打开文件后的编码(翻译)规则。 如：打开文本文件显示时被各类编码规则(`gbk`, `utf8`等)转码显示于屏幕。打开图片文件时，被RGB颜色组合翻译规则显示为图片。文本文件和图片文件的信息本质都是一样的，他们都由基本字节组合而成。

**Unicode是什么，ascII、gbk、utf8是什么，他们是什么联系？**
- Unicode 是「字符集」。
- UTF-8 是「编码规则」。是Unicode的实现方式，UTF-8 最大的一个特点，就是它是一种变长的编码方式。它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度。GBK与UTF-8类似，也是变长编码方式，但他们并不完全兼容。  

**常见的utf-8和gbk编码规则是什么，他们区别是什么？**
- 它们是特别的可用于中文的一套文本编码规则。 gbk为汉字标准特有，常见于Windows系统，2字节编码1汉字。而utf8是国际通用标准，常见于Linux系统，3字节编码1汉字。    

关于编码的深入理解，更多详情，可看一篇博文：[字符编码笔记：ASCII，Unicode 和 UTF-8 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html)


---
#### 8.2.2.1. 汉字编码

国标系列:
```
GB18030(二字节或四字节编码, 共27533个汉字)
  GBK(二字节编码, 共21003个汉字)
    GB2312(二字节编码, 共个6763汉字)
(Windows 常用)
```

国际标准:
```
UNICODE32(UNICODE16) < ---> UTF - 8
  (Linux, Mac OS X, IOS, Android等常用)
有趣的是，这套标准里，3/4都是中亚文，
【问题：ASCii和这些编码是什么关系？是否为包含关系？】
```

---
示例1：Python中的十六进制数转码
```python
# 如文件中的十六进制原码： `61 62 63 31 32 33 e4b8ad e69687`
# 通过utf-8转码： `a b c 1 2 3 中 文`
>>> b'\x61 \x62 \x63 \x31 \x32 \x33 \xe4\xb8\xad \xe6\x96\x87'.decode('utf-8')
'a b c 1 2 3 中 文'

# 十六进制数如何理解？61表示ascii的编码规则对应字母a。
## Python中，默认打印十进制，61(16)对应97(10)。
>>> print(97, 0b01100001, 0x61, "该十进制表示的ascii字母是：", b'\x61')
97 97 97 该进制数61表示的ascii字母是： b'a'
```

---
示例2：同一字节串的不同解码方式对比
```python
# 不同解码方式获得不同结果，utf8一个汉字用3字节表示，gbk一个汉字用2字节表示
>>> b'\xe7\xa8\x8b\xe5\xba\x8f'.decode('utf8')
'程序'
>>> b'\xe7\xa8\x8b\xe5\xba\x8f'.decode('gbk')
'绋嬪簭'
```

---
示例3：问题: “十个汉字占多少个字节”这句话存储的文件占多少个字节？

```python
# 不同编码，不同结果。
# utf-8     30
# gbk(ANSI) 20
```


### 8.2.3. 不同系统平台的编码问题
---
#### 8.2.3.1. Python下读取文件的编码错误问题

（可暂时跳过，等学习到编码规则后在进行此节学习）

问题描述

为什么Python在`open("utf8.file")`在Linux下能正常open并read包含汉字的utf8文件，而把该文件放在Windows却报错？  
- 系统的编码不同open函数默认为系统编码，win --> gbk，linux --> utf-8。  

有时候在Windows下打开带中文的utf-8编码的文件出现报错：

```python
>>> with open('mod-run.sh') as fi:
... 	data = fi.read()
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
UnicodeDecodeError: 'gbk' codec can't decode byte 0xb4 in position 183: illegal multibyte sequence
```

解释：(Python读取文件的平台兼容性问题)
- `open(filename, encoding=None)`，当encoding参数未指定时，Python会自动根据所处系统选用解码方式。Windows下自动使用gbk，Linux下自动使用utf8。
- 因此：
  - Windows下正常读取“gbk编码(ANSI)”文件，却不能正常读取“utf-8编码”文件
  - Linux下不能正常读取“gbk编码(ANSI)”文件，却能正常读取“utf-8编码”文件
- 读取出错时都返回 `UnicodeDecodeError` 错误

---
探索实例：

<br>

**step1: 准备文件**

方式1：使用记事本另存为

1. 打开Windows自带程序记事本，新建记事本，复制粘贴以下文本内容： 
    ```
    abcde12345
    这句中文占了几个字节
    ```
2. 点击 文件>另存为 `test_f_utf8.txt` ，选择编码utf-8编码保存

3. 点击 文件>另存为 `test_f_gbk.txt` ，选择编码ANSI编码保存(也称作gbk编码)

   ps: 更改文件编码的方法:  
   记事本(Windows下) > 文件 > 另存为 > 选择修改编码


方式2：直接运行以下代码生成这两个文件

```python
doc = ["abcde12345", "这句中文占了几个字节"]

with open('test_f_utf8.txt', 'wb') as fo:
    doc_utf8 = [x.encode('utf8') for x in doc]
    fo.write(b'\r\n'.join(doc_utf8))

with open('test_f_gbk.txt', 'wb') as fo:
    doc_gbk = [x.encode('gbk') for x in doc]
    fo.write(b'\r\n'.join(doc_gbk))
```

通过查看文件大小：
```
-rw-r--r-- 1 JUN 197121    42 4月  11 22:03 myfile1.txt
-rw-r--r-- 1 JUN 197121    32 4月  11 22:03 myfile2.txt
```

可以发现 `test_f_gbk.txt` 比 `test_f_utf8.txt` 正好少10个字节，原因正如我们前文所说，utf8汉字是由三个字节编码的，而gbk汉字是由两个字节编码的。少掉的这10个字节，正好是这不同编码的10个汉字导致的。

<br>

**step2: 准备脚本：**

```python
open("test_read.py", 'wb').write((r"""
import traceback


def open_file(filename):
    try:
        f = open(filename, 'rt')
        print("\n打开的文件是：" + filename)
        s = f.read()
        print("读取文件成功! 文件中的内容是:")
        print(s)
    except Exception:
        print("读取文件" + filename + "失败! 错误信息是：")
        traceback.print_exc()


open_file("test_f_utf8.txt")
open_file("test_f_gbk.txt")

""").encode('utf8'))
```

**step3: 执行测试**

- Windows下运行脚本，运行结果：

    ```
    打开的文件是：test_f_utf8.txt
    读取文件test_f_utf8.txt失败! 错误信息是：
    Traceback (most recent call last):
      File "test_read.py", line 8, in open_file
        s = f.read()
    UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 20: illegal multibyte sequence

    打开的文件是：test_f_gbk.txt
    读取文件成功! 文件中的内容是:
    abcde12345
    这句中文占了几个字节
    ```

- linux下运行脚本，结果则相反，运行结果：

    ```
    打开的文件是：test_f_utf8.txt
    读取文件成功! 文件中的内容是:
    abcde12345
    这句中文占了几个字节

    打开的文件是：test_f_gbk.txt
    读取文件test_f_gbk.txt失败! 错误信息是：
    Traceback (most recent call last):
      File "test_read.py", line 8, in open_file
        s = f.read()
      File "/root/miniconda3/lib/python3.7/codecs.py", line 322, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd5 in position 12: invalid continuation byte
    ```

- 解决方案
> 1. 二进制读取
> 2. try分别尝试转码

示例：解码打开
```python
import traceback

def open_file(filename):
    try:
        # 二进制打开文件
        f = open(filename, 'rb')
        print("\n打开的文件是：" + filename)
        s = f.read()
        print("读取文件成功! 文件中的内容是:")
        print(s)
        print('字节长度：', len(s))
        # 转码
        try:
            text = s.decode('utf8')
            print('使用utf8解码:')
        except Exception as e:
            text = s.decode('gbk')
            print('使用gbk解码:')
        print(text)
    except Exception as e:
        print("读取文件" + filename + "失败! 错误信息是：")
        traceback.print_exc()

open_file("test_f_utf8.txt")
open_file("test_f_gbk.txt")
```

---
#### 8.2.3.3. Python中 “换行符” 的处理
各种操作系统的换行符:

|         系统         | 换行符 |
| :------------------: | :----: |
|     Linux换行符:     |  `'\n'`  |
|    Window换行符:     | `'\r\n'` |
| 旧的Macintosh换行符: |  `'\r'`  |
|  新的Mac Os 换行符:  |  `'\n'`  |

说明: 
- 在文件文件模式下
  - 在读入Python内部时，会自动将`"当前使用操作系统的换行符"`统一转换为字符`"\n"`
  - 在从Python内存中写入文件时，又会将`"\n"`转换成`“对应使用操作系统的换行符”`

  如：Windows下，如果以"文本"方式打开一个文件，那么在读字符的时候，系统会把所有的`"\r\n"`序列转成`"\n"`，在写入时把`"\n"`转成`"\r\n"`

---
这个知识有什么用呢？

因为这个你便能理解为什么有时候会出现这些情况：
- 在Windows下在使用 `"rt"`模式读取文件时， `"\r\n"` 会被自动转换处理为 `"\r"`。
  - Windows下有时使用Python统计文件字符串长度会与存储字节大小不一致。
  - Windows下有时使用Python打开一个文件，再原封不动的写入新文件，新文件大小会变小，再用记事本打开这个新文件会消失换行符连成一片。
- Linux下面创建的文件，在Windows下面用记事本打开会所有行连成一行；而Windows中创建的文件在Linux下读取出来却能自动换行。因为Linux下创建的文件换行符是`"\n"`，而Windows是读取`"\r\n"`作为换行。

---
示例：
```python
with open('test_f_gbk.txt', 'rt', encoding='gbk') as fi, \
      open('test_f_gbk.txt.new', 'wt', encoding='gbk') as fo:
    s = fi.read()
    n = fo.write(s)
    print('写入字符数：', n)  # ____
print(len(s), len(s.encode('gbk')))  # ____ ____

with open('test_f_gbk.txt', 'rb') as fi:
    s1 = fi.read()
with open('test_f_gbk.txt.new', 'rb') as fi:
    s2 = fi.read()
print(len(s1), len(s2))  # ____ ____
print(s1 == s2)
```

---
示例：
```python
print('rt模式：')
with open("./test_f_utf8.txt", encoding='utf8') as fi:
     text = fi.read()
     print(repr(text), "长度：%s" % len(text), 
           repr(text.encode()), "长度：%s" % len(text.encode()),
           sep='\n')

print('\nrb模式：')
with open("./test_f_utf8.txt", 'rb') as fi:
     text = fi.read()
     print(repr(text), 
            "长度：%s" % len(text), 
            repr(text.decode('utf8')), 
            "长度：%s" % len(text.decode('utf8')),
            sep='\n')
```

### 8.2.4. 文件与MD5值

文件的MD5值实际上是对文件的字节码进行MD5算法加密所获得的唯一码

示例：
- 文件准备：
test.txt 内容为：
```
hello
```

Linux下直接执行：
```shell
echo hello >test.txt
```

或Python执行：
```python
open('test.txt', 'w').write('hello')
```


Linux下通过命令：
```shell
$ md5sum test.txt 
5d41402abc4b2a76b9719d911017c592  test.txt
```

Python3下计算MD5：
```python
import hashlib
objMD5 = hashlib.md5()
with open('test.txt','rb') as fi:
    data = fi.read()
    objMD5.update(data)
    print(objMD5.hexdigest())
```

## 8.3. Python中的编码说明
### 8.3.1. Python 的内部(内存)编码

Python3的字符串内部都是用UNICODE来存储字符的。可以理解为操作过程中，内存的字符集是Unicode表示，当输出或写入文件时才调用指定的编码方式utf8/gbk等。

't'  文本模式(默认)

1. 默认文件中存储的数据为字符数据，以行为单位分隔，在 Python 内部统一用`'\n'`作为换行符进行分隔

### 8.3.2. python文件的编码注释
python 编码 encode 字符串:
- 'gb2312'
- 'gbk'
- 'gb18030'
- 'utf-8'
- 'ascii'

（在python 源文件第一行或第二行写入如下内容是告诉解释执行器此文件的编码类型是什么）

  如:
```python
# -*- coding: gbk -*-
# 设置python文件读取的编码格式为gbk
```
或
```python
# -*- coding: utf-8 -*-
# 设置python文件读取的编码格式为utf-8
```

### 8.3.3. 字节串 bytes
- 引入：
回顾问题:
之前学的容器类型:  
str, list, tuple, dict, set, frozenset

序列:  
list, str, tuple, bytes, bytearray

- 意义：  
所有字符转码为字节作为通信传输。  
存储以字节为单位的数据

---
#### 8.3.3.1. 概念
何为字节串？
- 由多个字节组合而成的序列

何为字节？  
```
B ... Byte    表示字节
b ... bit     表示位
```
- 字节（Byte ）是计算机信息技术用于计量存储容量的一种计量单位。作为一个单位来处理的一个二进制数字串，是构成信息的一个小单位。最常用的字节是八位的字节，即它包含八位的二进制数。——《百度百科》  
- 位（bit）是储存信息的最小单位，只能储存0或者1
- `1B == 8b` (`1Byte == 8bit`)

说明:
- 字节串是不可变的字节序列
- 字节是0~255之间的整数

---
#### 8.3.3.2. 字节串的创建

- python:字节串创建的三种方式  

  1. `b'字面值'` 直接生成
  2. `bytes()` 使用函数生成
  3. `"str".encode()` 转码

      ```python
      # 1) b''直接生成
      print(b'zifuchuang')
      # 2) bytes()函数
      print(bytes('zifuchuang',encoding='utf-8'))
      # 3) 字符串转换
      print('zifuchuang'.encode('utf-8'))
      ```

- 说明：
  - 字面值只能是字母、数字、英文符号等256个ascii的值，或者十六进制码表示的值，如`'\x09'`

- 字节串的构造函数 bytes
  - 格式：

    ```python
    # 1) 生成一个空的字节串 等同于 b''
    bytes()
    
    # 2) 生成n个值为零的字节串
    bytes(整形数int)
    
    # 3) 用可迭代对象初始化一个字节串
    # 将可迭代对象中整型数按照ascii转码并拼接
    bytes(包含整型数int的可迭代对象)

    # 4) 用字符串的转换编码生成一个字节串
    bytes(字符串, encoding='utf-8')
    ```

说明：
1. Python中对于字节串是默认显示翻译后的字符。

    示例: 使用`\x09\x0a`与`\t\n`表示相同字节串，最后表示为翻译后
    ```python
    print(repr('\x09\x0a\x0b'))  # '\t\n\x0b'
    print(repr('\t\n\x0b'))  # '\t\n\x0b'
    ```
2. 字节串的创建必须使用范围内的数，`b'字面值'`、整形数int、整型数int构成的可迭代对象，其中的整型数int必须在`[0, 256)`范围内，因为1个字节有8位，每个位有`0`和`1`两种组合，共计`2^8=256`个组合。

    示例：查看所有可输入的字节码
    ```python
    seed = 8
    for i in range(0, 256, seed):
        print('%03d-%03d bytes:'%(i, i + seed - 1, ),
              bytes(range(i, i + seed)))
    ```
    运行结果：
    ```
    000-007 bytes: b'\x00\x01\x02\x03\x04\x05\x06\x07'
    008-015 bytes: b'\x08\t\n\x0b\x0c\r\x0e\x0f'
    016-023 bytes: b'\x10\x11\x12\x13\x14\x15\x16\x17'
    024-031 bytes: b'\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
    032-039 bytes: b' !"#$%&\''
    040-047 bytes: b'()*+,-./'
    048-055 bytes: b'01234567'
    056-063 bytes: b'89:;<=>?'
    064-071 bytes: b'@ABCDEFG'
    072-079 bytes: b'HIJKLMNO'
    080-087 bytes: b'PQRSTUVW'
    088-095 bytes: b'XYZ[\\]^_'
    096-103 bytes: b'`abcdefg'
    104-111 bytes: b'hijklmno'
    112-119 bytes: b'pqrstuvw'
    120-127 bytes: b'xyz{|}~\x7f'
    128-135 bytes: b'\x80\x81\x82\x83\x84\x85\x86\x87'
    136-143 bytes: b'\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f'
    144-151 bytes: b'\x90\x91\x92\x93\x94\x95\x96\x97'
    152-159 bytes: b'\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f'
    160-167 bytes: b'\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7'
    168-175 bytes: b'\xa8\xa9\xaa\xab\xac\xad\xae\xaf'
    176-183 bytes: b'\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7'
    184-191 bytes: b'\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf'
    192-199 bytes: b'\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7'
    200-207 bytes: b'\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf'
    208-215 bytes: b'\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7'
    216-223 bytes: b'\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf'
    224-231 bytes: b'\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7'
    232-239 bytes: b'\xe8\xe9\xea\xeb\xec\xed\xee\xef'
    240-247 bytes: b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7'
    248-255 bytes: b'\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
    ```
  
---
示例1：`b'字面值'`创建
```python
# 创建空字节串的字面值:
print(b'', b"", b'''''', b"""""", B"")

# 创建非空字节串的字面值:
# 创建"AB"的字节串
a = b'AB'
b = b'\x41\x42'
print(a == b, a, b)
# 创建"你好"的字节串
print(b"\xd5\xe2")
print(b"\xd5\xe2".decode('gbk'))
```

---
示例2：`bytes()`函数
```python
# bytes(int), 批量创建b'\x00'
print(bytes(1))  # b'\x00'
print(bytes(5))  # b'\x00\x00\x00\x00\x00'
```
```python
# bytes([int, int, ...]), 创建"你好"的字节串
a = b"\xd5\xe2"
b = bytes([213, 226])
print(a==b, a, a.decode('gbk'))  # True b'\xd5\xe2' 这
```
```python
# bytes('str', encoding="code")
print(bytes('a', encoding='utf-8'))
# b'a'
print(bytes('你好', encoding='gbk'))
# b'\xc4\xe3\xba\xc3'
print(bytes('你好', encoding='utf-8'))
# b'\xe4\xbd\xa0\xe5\xa5\xbd'
```

---
#### 8.3.3.3. bytes、str的区别与转换

字节串与字符串的区别本质:
- bytes --- 存储字节(0-255)
- str --- 存储Unicode字符(0-65535)

字节串与字符串之间的转换方法：
- 编码(encode)
  - str -------------->  bytes

    ```python
    b = s.encode('utf-8')  
    ```

- 解码(decode)
  - bytes------------->  str

    ```python
    s = b.decode('utf-8')
    ```

---
示例：
```python
print('你好'.encode('utf-8')) # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))  # 你好
```


长度：
- 文本模式下，长度为转码后的字符长度
- 二进制模式下，长度为转码前的字节长度

示例：
```python
s = '你好'

e1 = s.encode('gbk')
e2 = s.encode('utf8')

print(len(s), len(e1), len(e2))  # ______
# 2 4 6
```

字符串与字节串长度表示相同信息时，字节长度可能是不一样的：
```python
>>> len('abc123')
6
>>> len(bytes('abc123', encoding='utf-8'))
6

>>> len('你好')
2
>>> len(bytes('你好', encoding='gbk'))
4
>>> len(bytes('你好', encoding='utf-8'))
6
```

---
#### 8.3.3.4. 字节串的运算
```
+  +=  *  *=
<  <=  >  >=  ==  !=
in / not in
索引/切片
```

示例:
```python
b = b'abc' + b'123'
print(b)  # b'abc123'

b += b'ABC'
print(b)  # b'abc123ABC'

print(b'ABD' > b'ABC')  # True

print(65 in b'ABCD')    # True
print(b'A' in b'ABCD')  # True
```

---
#### 8.3.3.5. 用于字节串的函数

字节串存储的本质是ascii编码数值，因而同数值一样，可以进行如下函数操作：（详情见数值一章节）

```python
len(x)
max(x)
min(x)
sum(x)
all(x)
any(x) 
```

### 8.3.4. 字节数组 bytearray
可变的字节序列

---
#### 8.3.4.1. 字节数组的创建
```python
bytearray()  # 创建空的字节数组
bytearray(整数)
bytearray(整型可迭代对象)
bytearray(字符串, encoding='utf-8')
# 注: 以上参数等同于字节串
```

---
#### 8.3.4.2. 字节数组的运算:
```python
+  +=  *  *= 
比较运算:  <  <= > >= == !=
in / not in 
索引　/ 切片(字节数组支持索引和切片赋值，规则与列表相同)
```

```python
>>> ba=bytearray(b'ABCDEF')
>>> ba[::2]=[48,49,50]	# 内容必须是整数，因为代表编码值
>>> ba
bytearray(b'0B1D2F')
```

---
#### 8.3.4.3. bytearray的方法:
|方法|功能|
|-|-|
|B.clear()  | 清空字节数组|
|B.append(n)  | 追加一个字节(n为0-255的整数)|
B.remove(value)  | 删除第一个出现的字节，如果没有出现，则产生|ValueError错误|
|B.reverse()  | 字节的顺序进行反转|
|B.decode(encoding='utf-8')  | # 解码|
|B.find(sub[, start[, end]])  | 查找|
字节数组的方法详见: help(bytearray)

## 8.4. 文件的操作流程
1. 打开文件
2. 读/写文件
3. 关闭文件

任何的操作系统，一个应用程序同时打开文件的数量有最大数限制

### 8.4.1. 打开创建文件对象open
- 函数 open
  - 函数：  
    用于打开一个文件，返回此文件对应的文件流对象，如果打开失败，则会触发OSError错误！
    ```python
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    ```

  - 说明：
    - mode: 操作模式, 缺省参数是`'rt'`, `'t'`默认可以省略。
    - buffering: 设置缓冲, 缺省参数-1，代表按照系统分配缓存。
    - encoding: 解码方式, 缺省时自动根据系统定义解码方式，Windows下是gbk，Linux下是utf8。如果提前知道文件编码类型最好自定义固定。
    - errors: 报错级别
    - newline: 区分换行符
    - closefd: 传入的file参数类型
    - ...

  - 返回：  
    open返回的文件流对象是可迭代对象


---
#### 8.4.1.1. 操作模式
模式(mode)字符的含义：

| 字符 |                                       含义                                       |
| ---- | -------------------------------------------------------------------------------- |
| 'r'  | 以只读方式打开(默认)                                                              |
| 'w'  | 以只写方式打开，删除原有文件内容(如果文件不存在，则创建该文件并以只写方式打开)   |
| 'x'  | 创建一个新文件, 并以写模式打开这个文件,如果文件存在则会产生"FileExistsError"错误 |
| 'a'  | 以只写文件打开一个文件，如果有原文件则追加到文件末尾                             |
| 't'  | 文本文件模式打开 (默认)                                                          |
| 'b'  | 用二进制模式打开                                                                 |
| '+'  | 为更新内容打开一个磁盘文件 (可读可写)                                            |

- 说明：
  - 缺省参数模式是 'rt'
  - 'w+b' 可以实现二进制随机读写，当打开文件时，文件内容将被清零
  - 'r+b' 以二进制读和更新模式打开文件,打开文件时不会清空文件内容
  - 'r+' 以文本模式读和更新模式打开文件,打开文件时不会清空文件内容

注：Unicode/UTF/UCS格式的文件，必须用二进制方式打开和读写。【？待确认】

示例见:
file_write_binary.py
file_read_binary.py

---
文本模式(textmode)和二进制模式(binarymode)的区别：
- 流可以分为两种类型：
  - 文本流
  - 二进制流。
- Python中文件操作的两种模式:
  - `'b'`: 二进制模式, 该模式下写入和读取必须是字节串。
  - `'t'`: 文本模式, 该模式下写入和读取必须是字符串。
- 特性：
  - 文本流是解释性的，最长可达255个字节。  
  - 二进制流是非解释性的，一次处理一个字节，并且不转换字符。
<!-- - 二进制模式的文件操作  
  - 默认的文件中存储的都是以字节为单位的数据，通常有人为规则的格式，需要以字节为单位进行读写 -->

- 补充：Linux中以十六进制方式查看文件内容的命令:
  ```
  xxd 文件名
  ```

### 8.4.2. 读取方法read
以读模式打开文件：
> `file = open('filename', 'r')`，操作模式还可以是`'b'`

读取方法：（按光标读取之后的内容）
- `file.read()` : 一次性读取光标后的所有字符(字节)，  
- `file.read(n)` : n代表读取多少位  
- `file.readline()` : 逐次取出文件一行，每行读取会带最后的换行符'\n'，空行或结束时读取为空字符串''  
- `file.readlines()` : 读取所有行并以“行”为分隔符，生成返回列表  
- 注：
  - f.read()的返回类型:  
    - 对于文本模式('t')打开的文件，返回字符串(str)  
    - 对于二进制模式('b')打开的文件，返回字节串(bytes)  

文件的迭代读取:
> `for line in file: print(line)`

<!-- 注：【此处过去遇到过这样的问题，但验证却无法复现了，很奇怪，还没有尝试过python2和python3区别。此处先行放置，日后再看】
file.readline()  读取的内容等同于  for s in file: s 的第一句
但不同之处在于，它可以精确控制光标，而用for循环读取时，光标被一次性移动至末尾。

---
示例:
```python
with open('test_f_utf8.txt', 'rb') as f:
    print(f.tell())
    for line in f:
        print(line)
        print(f.tell())
with open('test_f_utf8.txt', 'rb') as f:
    print(f.tell())
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
        print(f.tell())
``` -->


### 8.4.3. 写入write
文本文件的写操作:
- 写文件模式有:
  - `open(filename, 'w')`
  - `open(filename, 'x')`
  - `open(filename, 'a')`

- 写入方法：
  - `f.write(x)`: 对于文本模式,x必须为字符串; 对于二进制模式,x必须为字节串
  - 
- 写入文件的编码问题探索
经探索：
文本模式写入：
	Python在 Windows 下默认写入的txt文件编码为 gbk
	Python在  Linux  下默认写入的txt文件编码为 utf-8
二进制模式下：
	使用二进制模式写入的文件，能保持其文件原有的编码。

---
示例： test_f_utf8.txt 文件的内容原封不动复制到 test_f_utf8.txt.copy

```python
f = open('test_f_utf8.txt', 'rb')
f2=open('test_f_utf8.txt.copy','wb')
print("打开文件成功!")

s = f.read()
print("读取文件成功!")
print("文件中的内容是:", s)

f2.write(s)
print("写入文件成功!")
```

结果：写入的新文件myfile2.txt  --编码也为gbk

### 8.4.4. 关闭close

`F.close()`

关闭，释放系统资源

示例见:
   01_fileopen.py

### 8.4.5. 二进制操作模式
- F.tell() 方法:  
  作用: 返回当前文件读写位置

- F.seek()设置文件当前位置  
  作用: 改变当前文件的读写位置

```python
F.seek(offset[, whence])
F.seek(偏移量, 相对位置)
    偏移量:
        大于0的数代表向文件尾方向移动
        小于0代表向文件头方向移动
    相对位置:
        0 代表从文件头开始偏移
        1 代表从当前位置开始偏移
        2 代表从文件尾开始偏移
```
示例：
```python
file.seek(0)  # 光标归位
```

### 8.4.6. 应用实例

示例1：F.read()读取文本内容
```
#data.bin
e4b8 ad00 00
```

```python
#file_read_binary.py
file = open('data.bin', 'rb')

b = file.read(1)  # 读取一个字节
print("第一个字节是:", b)

b = file.read() # 读取所有的字节
print('其它所有字节是: ', b)
file.close()
```

结果：
```
第一个字节是: b'\xe4'
其它所有字节是:  b'\xb8\xad\x00\x00'
```

---
示例2：while + readline()读取文本内容

```python
# 此示例示意以文本文件模式读取myfile.txt中的内容
try:
    f = open("test_f_utf8.txt")
    print('打开文件成功!')
    # 读取文件内容
    while True:
        s = f.readline()
        if s == '':
            print('已经读取到了文件末尾')
            break
        print("读到这一行是:", s)
    f.close()
except OSError:
print("打开文件失败")
```

- 示例3：F.readlines()用法



### 8.4.7. python 文件方法总结

|           方法            | 返回 | 输入 |                           说明                            |
| ------------------------- | ---- | ---- | --------------------------------------------------------- |
| F.read(size=-1)           | str  | int  | 从一个文件流中最多读取size个字符，并将光标从文件流后移    |
| F.readline()              | str  | /    | 读取一行数据, 如果到达文件尾则返回空行                    |
| F.readlines(max_chars=-1) | list | /    | 返回每行字符串的列表,max_chars为最大字符(或字节)数        |
| F.write(text)             | int, | str  | 写一个字符串到文件流中，返回写入的字符数                  |
| F.writelines(lines)       | None | list | 每行字符串的列表                                          |
| F.flush()                 | None | /    | 把写入文件对象的缓存内容写入到磁盘                        |
| F.close()                 | None | /    | 关闭文件(关闭后文件不能再读写会发生ValueError错误)        |
| 二进制流操作方法：        |      |      |                                                           |
| F.tell()                  | int  | /    | 返回当前文件流的绝对位置                                  |
| F.seek(offset, whence=0)  | int  | int  | 改变数据流的位置，返回新的绝对位置                        |
| F.readable()              | bool | /    | 判断这个文件是否可读,可读返回True,否则返回False           |
| F.writable()              | bool | /    | 判断这个文件是否可写,可写返回True,否则返回False           |
| F.seekable()              | bool | /    | 返回这个文件对象是否支持随机定位                          |
| F.truncate(pos = None)    | int  | int  | 剪掉自pos位置(默认为当前位置)之后的数据，返回新的文件长度 |


## 8.5. with语句
简化try open文件
注意事项：
1、with语句命名空间
with open(file) as fi:
    test = 'hello'
print(test)  # 正常显示
8.6.  原理理解
8.6.1.  读取的原理
问题引入：
for迭代文件对象，与next()方法读取下一行，以及readline()读取下一行都有区别吗？
【无区别，原理本质都是通过光标读取下一行，在深入一点为指针】
四字总结：
光标移位
【无论是单独语句，还是表达式中（读取，条件判断等）只要往下面走，光标都会移位！！】

- 示例1：
文件：t.txt
```
1
2
3
4
5
6
```
脚本：t.py
```python
# t.py
fi = open('t.txt')
for i in fi:
    print('--' + i, end='')
    if i.startswith('3'):
        next(fi)
        data=fi.readline()
        print(data, end='')
```

运行结果：
```
--1
--2
--3
5
--6
```

- 示例2：文件读取光标问题
另外，还发现一些问题：

1、使用for和使用next()迭代文件对象，都会直接让光标直接移至文件末尾，因为无法在文件读取中获取其当前光标位置。
而使用file.readline()则会让光标按行移动。

2、光标读取后不会归位，重复使用相同迭代器(文件对象)得小心。关于迭代器和可迭代对象见前面章节：数据的迭代与生成

如：
文件：in.txt
```
1
2
3
4
5
```
脚本：test.py
```python
fi = open('in.txt')
for line in fi:
   print(line.strip())

for line in fi:
   print(line.strip())
```
脚本：test2.py
```python
fi = open('in.txt')
print(fi.readlines())
print(fi.readlines())
print(fi.readlines())
```
运行：
```bash
$ python3 test.py
1
2
3
$ python3 test2.py
['1\n', '2\n', '3\n']
[]
[]
```
