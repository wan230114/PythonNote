当前模块在网络上已经比较全面了，所以暂时不放精力在此处整理笔记

## 语法规则速查笔记

不再过多赘述，网络教程已经十分详细：[Python 正则表达式 | 菜鸟教程](https://www.runoob.com/python/python-reg-expressions.html)

摘录于《Python核心编程》

- **符号**
  - `literal`： 匹配文本字符出的字曲值literal。  示例: `foo`
  - `re1|re2`： 匹配正则表达式`re1`或者`re2`。  示例: `foo|bar`
  - `.`： 匹配任何字符(除了\n之外)。  示例: `b.b`
  - `^`： 匹配字符串起始部分。  示例: `^Dear`
  - `$`： 匹配字符串终止部分。  示例: `/bin/*sh$`
  - `*`： 匹配0次或者多次前面出现的正则表达式。  示例: `[A-Za-z0-9]*`
  - `+`： 匹配1次或者多次前面出现的正则表达式。  示例: `[a-z]+\.com`
  - `?`： 匹配0次或者1次前面出现的正则表达式(非贪婪模式)。  示例: `goo?`
  - `{N}`： 匹配N次前面出现的正则表达式。  示例: `[0-9]{3}`
  - `{M,N}`： 匹配M~N次前面出现的正则表达式。  示例: `[0-9]{5.9}`
  - `[...]`： 匹配来自字符集的任意单一字符。  示例: `[abcde]`
  - `[..x-y..]`： 匹配x~y范围中的任意单一字符。  示例: `[0-9],[A-Za-z]`
  - `[^...]`： 不匹配此字符集中出现的任何一个字符，包括某一范围的字符(如果在此字符集中出现)。  示例: `[^abcde],[^A-Za-z0-9]`
  - `(*|+|?|{})?`： 用于匹配上面频繁出现/重复出现符号的非贪婪版本(`*`、`+`、`？`、`{}`)。  示例: `.*?[a-z]`
  - `(...)`： 匹配封闭的正则表达式，然后另存为子组。  示例: `([0-9){3})?,f(oo|u)bar`
- **特殊字符**
  - `\d`： 匹配任何十进制数字，与`[0-9]`一致(`\D` 与`\d` 相反，不匹配任何非数值型的数字)。  示例: `data\d+.txt`
  - `\w`： 匹配任何字母数字字符，与`[A-Za-z0-9_]`相同(`\W` 与之相反)。  示例: `[A-Za-z_]\w+`
  - `\s`： 匹配任何空格字符，与[\n\t\r\v\f]相同(\S 与之相反)。  示例: `of\sthe`
  - `\b`： 匹配任何单词边界(\B 与之相反)。  示例: `\bThe\b`
  - `\N`： 匹配已保存的子组 N(参见上面的(…))。  示例: `price: \16`
  - `\c`： 逐字匹配任何特殊字符 c(即，仅按照字面意义匹配，不匹配特殊含义)。  示例: `\., \\, \*`
  - `\A`(`\Z`)： 匹配字符串的起始(结束)(另见上面介绍的^和$)。  示例: `\ADear`
- **扩展表示法**
  - `(?iLmsux)`： 在正则表达式中嵌入一个或者多个特殊“标记”参数(或者通过函数/方法)。  示例: `(?x)，(？ im)`
  - `(?:…)`： 表示一个匹配不用保存的分组。  示例: `(?:\w+\.)*`
  - `(?P<name>…)`： 像一个仅由 name 标识而不是数字 ID 标识的正则分组匹配。  示例: `(?P<data>)`
  - `(?P=name)`： 在同一字符串中匹配由`(?P<name>)`分组的之前文本。  示例: `(?P=data)`
  - `(?#…)`： 表示注释，所有内容都被忽略。  示例: `(?#comment)`
  - `(?=…)`： ***正向前视断言***：此位置`…`后面匹配。  示例: `(?=.com)`
  - `(?!…)`： ***负向前视断言***：此位置`…`后面不匹配。  示例: `(?!.net)`
  - `(?<=…)`： ***正向后视断言***：此位置`…`前面匹配。  示例: `(?<=800-)`
  - `(?<!…)`： ***负向后视断言***：此位置`…`前面不匹配。  示例: `(?<!192\.168\.)`
  - `(?(…)Y|N )`： 如果分组所提供`…`存在，就与Y匹配；否则与N匹配。注：`|N` 是可选项。  示例: `(?(1)y|x)`



---
示例：

| 正则表达式模式 | 匹配的字符串 |
|---------|--------|
| `[dn]ot?` | 第一位是d或者n，第二位o，第三位与第四位表示t可以有0次或1次 |
| `[0-9]{15,16}` | 匹配15或者16个数字（例如信用卡号码） |
| `</?[^>]+>` | 匹配全部有效的（和无效的）HTML 标签 |

## 讲解

```python
import re
# - `(?iLmsux)`： 在正则表达式中嵌入一个或者多个特殊“标记”参数(或者通过函数/方法)。  示例: `(?x)，(？ im)`
# - `(?:…)`： 表示一个匹配不用保存的分组。  示例: `(?:\w+\.)*`
re.findall(r"aaa123(?:bbb|ccc)*", "aaa123aaa\naaa123bbb\naaa123ccc")  # ['aaa123', 'aaa123bbb', 'aaa123ccc']
# - `(?P<name>…)`： 像一个仅由 name 标识而不是数字 ID 标识的正则分组匹配。  示例: `(?P<data>)`
# - `(?P=name)`： 在同一字符串中匹配由`(?P<name>)`分组的之前文本。  示例: `(?P=data)`
# - `(?#…)`： 表示注释，所有内容都被忽略。  示例: `(?#comment)`
# - `(?=…)`： ***正向前视断言***：此位置`…`后面匹配。  示例: `(?=.com)`
# - `(?!…)`： ***负向前视断言***：此位置`…`后面不匹配。  示例: `(?!.net)`
# - `(?<=…)`： ***正向后视断言***：此位置`…`前面匹配。  示例: `(?<=800-)`
# - `(?<!…)`： ***负向后视断言***：此位置`…`前面不匹配。  示例: `(?<!192\.168\.)`
# - `(?(…)Y|N )`： 如果分组所提供`…`存在，就与Y匹配；否则与N匹配。注：`|N` 是可选项。  示例: `(?(1)y|x)`

```

(?:...) 解决子组问题：

```python
import re
text = r"""
![图 1](a.png)
![图 1](b.png ':size=450')
![图 1](b.png ':size=450x50%' )
![图 1](c.png ':size=45%x50%')'"""
pattern = r'''!\[.*?\]\((.*?)(?: +["']:size=([\d%]*)x*([\d%]*)["'])* *\)'''
#                            (?:                                  )* 
# 表示一个大分组的查找次数可为0-n次，避免无法查找到时无法匹配
tihuan = r'''<img src="\1" width="\2" height="\3" />'''
print(*re.findall(pattern, text), sep='\n')
print(re.sub(pattern, tihuan, text))
```

---
示例：扩展表示法

待补充：

```python
import re

data = """
110101199003079227
110101199003077360
110101199003072906
110101199003074688
110101199003073626
511025199103070696
511025199203071592
511025199303073934
511025199503070135
511025199503070274
"""

print(re.findall('(?(511025)\d*|\d)', data))
```

## re 模块：核心函数和方法

```python
compile(pattern，flags=0)

match(pattern，string，flags=0)   # 只匹配字符串的开始
search(pattern，string，flags=0)  # 匹配整个字符串
findall(pattern，string [, flags] )
finditer(pattern，string [, flags] )
split(pattern，string，max=0)
```


示例： 匹配全文，忽略换行符

```python
import re
# re.compile(pattern, re.DOTALL).findall(doc)
doc = '1221\n312213\n512215'
REGEX1 = re.compile('1.*\s*1')
REGEX2 = re.compile('1.*1', re.DOTALL)
print(REGEX1.findall(doc))
print(REGEX2.findall('1221\n312213\n512215'))
```

运行结果：
```
['1221', '1221', '1221']
['1221\n312213\n51221']
```


一些高级示例：

```python
re.findall(
    "(?:胚胎|肿瘤)(?:干细胞)*|干细胞|器官",
    "胚胎干细胞1, 肿瘤干细胞2, 这是胚胎或肿瘤方面的干细胞研究, 用于器官移植方面")
# OUT: ['胚胎干细胞', '肿瘤干细胞', '胚胎', '干细胞', '器官']

re.sub("(这是)(关键词)(,)", r"\1**\2**\3",
       "\n这是关键词, 我需要两侧增加特殊字符")
# OUT: '\n这是**关键词**, 我需要两侧增加特殊字符'

Pattern, tihuan = r'(<img.* )title=":size=([\d%]*)x*([\d%]*)">', r'\1 width="\2" height="\3"'
re.sub(Pattern, tihuan, r'<img alt="" src="./images/RNA_process.png" title=":size=550">')
re.sub(Pattern, tihuan, r'<img alt="" src="./images/RNA_process.png" title=":size=500x100">')
re.sub(Pattern, tihuan, r'<img alt="" src="./images/RNA_process.png" title=":size=50%x10%">')

import re
pattern, tihuan = r'(<img.*?) title=":size=([\d%]*)x*([\d%]*)">', r'\1 width="\2" height="\3"'
re.sub(pattern, tihuan,  r'aaa\n<p><img alt="" src="./images/RNA_process.png" title=":size=50%x10%"></p>')
```


```python
import re
print(re.findall(r"--(?:abc|123)", "--abcde--12345"))
print(re.findall(r'(?<=").+?(?=")', 'word1:"hello", word2:"world"'))
print(re.findall(r'"(.+?)"', 'word1:"hello", word2:"world"'))
print(re.findall(r".+(?<=re)", "res:result"))
print(re.findall(r"(?<=re).+", "res:result"))
```

