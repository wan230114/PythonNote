# 1. pandas数据分析
- 基础知识
- 统计分析基础
- Jupyter notebook介绍
- 数据预处理

## 1.1. 简介

目录：
* [1. pandas数据分析](#_1-pandas数据分析)
  * [1.1. 简介](#_11-简介)
  * [1.2. pandas介绍](#_12-pandas介绍)
* [2. pandas的核心数据结构](#_2-pandas的核心数据结构)
  * [2.1. Series](#_21-series)
    * [2.1.1. Series创建](#_211-series创建)
    * [2.1.2. Series查看](#_212-series查看)
  * [2.2. Dataframe](#_22-dataframe)
    * [2.2.1. Dataframe创建](#_221-dataframe创建)
    * [2.2.2. Dataframe查看](#_222-dataframe查看)
    * [2.2.3. DataFrame更新修改数据](#_223-dataframe更新修改数据)
    * [2.2.4. DataFrame增添数据](#_224-dataframe增添数据)
    * [2.2.5. DataFrame删除某列或某行数据](#_225-dataframe删除某列或某行数据)
    * [2.2.6. 对DataFrame数据进行排序](#_226-对dataframe数据进行排序)
* [3. 数据描述与统计](#_3-数据描述与统计)
  * [3.1. 数值型特征的描述性统计](#_31-数值型特征的描述性统计)
  * [3.2. 类别型特征的描述性统计](#_32-类别型特征的描述性统计)
* [4. 数据的IO —— 文件读取与写入](#_4-数据的io--文件读取与写入)
  * [4.1. 文本文件](#_41-文本文件)
    * [4.1.1. 文本文件读取](#_411-文本文件读取)
    * [4.1.2. 文本文件写入](#_412-文本文件写入)
  * [4.2. Excel文件](#_42-excel文件)
    * [4.2.1. Excel文件读取](#_421-excel文件读取)
    * [4.2.2. Excel文件写入](#_422-excel文件写入)
  * [4.3. 扩展：数据库数据](#_43-扩展数据库数据)
    * [4.3.1. sql读取](#_431-sql读取)
    * [4.3.2. sql存储](#_432-sql存储)
    * [4.3.3. 其他](#_433-其他)
* [5. 常用操作](#_5-常用操作)


常用的参考文档：
- 查询API调用接口：https://pandas.pydata.org/pandas-docs/stable/reference/index.html

学习思维导图：

![](img/pandas01.png)

![](img/pandas02.png)

![](img/pandas03.png)


## 1.2. pandas介绍

名称：Python Data Analysis Library 或 pandas  

介绍：是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。  

定义1：pandas提供了大量能使我们快速便捷地处理数据的函数和方法。Python长期以来一直非常适合数据整理和准备，你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。

定义2：pandas是python里面分析结构化数据的工具集，基础是numpy，图像库是matplotlib

应用：做数据分析的相关工作，我们会见到各个方面的数据，可以是产品的用户体验数据，可以是产品的质量监测数据，也可以是证券市场数据，也可以是资本市场数据等等。这些数据杂乱无章，而且随着时代发展，数据量越来越庞大，单纯的Excel操作渐渐开始捉襟见肘。  
http://pandas.pydata.org/pandas-docs/version/0.23/


> - 结构化数据：  
> 是数据的数据库(即行数据,存储在数据库里,可以用二维表结构来逻辑表达实现的数据)
> - 非结构化数据：  
> 包括所有格式的办公文档、文本、图片、HTML、各类报表、图像和音频/视频信息等等
> - 半结构化数据：  
> 所谓半结构化数据，就是介于完全结构化数据（如关系型数据库、面向对象数据库中的数据）和完全无结构的数据（如声音、图像文件等）之间的数据，XML、json就属于半结构化数据。它一般是自描述的，数据的结构和内容混在一起，没有明显的区分。

# 2. pandas的核心数据结构
先导：什么是数据结构？？  
入门：pandas数据结构介绍
1. 查改增删DataFrame数据
2. 描述分析DataFrame数据
3. pandas获取数据

---

什么是数据结构？？？  
- 最简单的答案是，当你有几千几万个数据点时，每一个存放数据点的位置之间的排列关系就是数据结构。
- 数据结构是计算机存储、组织数据的方式。
- 数据结构是指相互之间存在一种或多种特定关系的数据元素的集合。通常情况下，精心选择的
- 数据结构可以带来更高的运行或者存储效率。数据结构往往同高效的检索算法和索引技术有关。


## 2.1. Series
Series可以理解为一个一维的数组，只是index可以自己改动。类似于定长的有序字典，有Index和value。

### 2.1.1. Series创建
创建的方法统一为：  
`pd.Series(data, index=)`  
打印的时候按照index赋值的顺序；
index参数默认从0开始的整数，也是Series的绝对位置，即使index被赋值之后，绝对位置不会被覆盖。
Series可以通过list, ndarry, dict创建。

示例：
```python
import pandas as pd
import numpy as np
# 1.Series创建
# 1) 通过列表创建
s1 = pd.Series([3, -5, 7, 4], index=("A", "B", "C", "D"))
# 2) 通过ndarray创建
s2 = pd.Series(np.array([3, -5, 7, 4]), index=["A", "B", "C", "D"])
# 3) 通过字典创建
s3 = pd.Series({"A": 3, "B": -5, "C": 7, "D": 4})

print("Series数据类型：", type(s1))
print(s1)
```

```
Series数据类型： <class 'pandas.core.series.Series'>
A    3
B   -5
C    7
D    4
dtype: int64
```

### 2.1.2. Series查看
索引与切片：  
(1) 通过index对应的标签；  
(2) 通过绝对位置查看。   
    如果通过绝对位置查看，会使用s[XXX]，XXX可以是绝对位置的数字，列表，或者表达式 等

注：切片时可以使用标签，但不可将标签与绝对位置混用

```python
import pandas as pd

s1 = pd.Series([3, -5, 7, 4], index=("A", "B", "C", "D"))
# 2. Series查看之索引与切片
print("查看第一个值：", s1[0])
print("查看第一个值：", s1["A"])
print(s1[0:3])
print(s1["A":"C"])
print(s1[s1>3])
```

运行结果：
```
查看第一个值： 3
查看第一个值： 3
A    3
B   -5
C    7
dtype: int64
A    3
B   -5
C    7
dtype: int64
C    7
D    4
dtype: int64
```

## 2.2. Dataframe
DataFrame是一个类似于表格的数据类型。

### 2.2.1. Dataframe创建

DataFrame 可以理解为一个二维数组，index有两个维度，可更改。  

**DataFrame 统一的创建形式为：**  
  - `pd.DataFrame(data, columns=, index=)`, 其中columns为列的索引，index为行的索引。index或者columns如果不进行设置则默认为0开始的整数  
  - **参数：**  
    - data(方框内数据)： numpy ndarray (structured or homogeneous), dict, or DataFrame  
    - index(行索引)： Index or array-like  
    - columns(列索引)： Index or array-like  
    - dtype(data的数据类型)： dtype, default None  

**Dataframe的常见属性：**

|  函数   |        返回值        |
| ------- | -------------------- |
| values  | 元素                 |
| index   | 索引                 |
| columns | 列名                 |
| dtypes  | 类型                 |
| size    | 元素个数             |
| ndim    | 维度数               |
| shape   | 数据形状（行列数目） |

示例1：
```python
import pandas as pd
data = [['Belglum', 'Brussels', 11190846],  # 比利时 布鲁塞尔
        ['Indla', 'New Delhi', 1303171035],  # 印度 新德里
        ['Brazil', 'Brasilia', 207847528]]  # 巴西 巴西利亚
colname = ["Country", "Capital", "Population"]

# array-like方式创建
print('array-like方式创建')
df = pd.DataFrame(data=data,  # 还可为data=np.array(data),
                  index=[1, 2, 3],
                  columns=colname)
print(type(df))
print(df)

# 使用字典创建
d = [dict(zip(colname, row)) for row in data]
print('\n字典方式创建')
print(*d, sep='\n')
df = pd.DataFrame(data=d, index=[1, 2, 3])
print(type(df))
print(df)
```

运行结果：
```
array-like方式创建
<class 'pandas.core.frame.DataFrame'>
   Country    Capital  Population
1  Belglum   Brussels    11190846
2    Indla  New Delhi  1303171035
3   Brazil   Brasilia   207847528

字典方式创建
{'Country': 'Belglum', 'Capital': 'Brussels', 'Population': 11190846}
{'Country': 'Indla', 'Capital': 'New Delhi', 'Population': 1303171035}
{'Country': 'Brazil', 'Capital': 'Brasilia', 'Population': 207847528}
<class 'pandas.core.frame.DataFrame'>
   Country    Capital  Population
1  Belglum   Brussels    11190846
2    Indla  New Delhi  1303171035
3   Brazil   Brasilia   207847528
```

示例2：使用pd的日期范围函数作为索引
```python
import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randn(6, 4),
                  index=pd.date_range("20081221", periods=6),
                  columns=list("abcd"))
print(df)
```

运行结果：
```
                   a         b         c         d
2008-12-21 -0.056629  0.250498  0.177238 -1.004025
2008-12-22  1.503906 -1.483001 -1.523983  2.226657
2008-12-23  0.323661 -0.922841 -0.059312  0.591360
2008-12-24  0.289682  0.577375 -0.888769 -0.178762
2008-12-25 -1.396149 -0.197316 -0.503946  0.211741
2008-12-26  0.232540  1.290481  0.127118 -1.675073
```


### 2.2.2. Dataframe查看

1. 列数据访问：
     - 对单列数据的访问：  
       - DataFrame的单列数据为一个Series。根据DataFrame的定义可以 知晓DataFrame是一个带有标签的二维数组，每个标签相当每一列的列名。
       - `df.a`
       - `df['a']`
     - 对多列数据访问：
       - 访问DataFrame多列数据可以将多个列索引名称视为一个列表
       - `df[['a','b']]` 

2. 行数据访问
   - 访问某几行 `df[s:e]`, s和e分别是行索引的位置
   - 取开头或结尾：`head`和`tail`

示例：
```python
import pandas as pd
data = [['Belglum', 'Brussels', 11190846],  # 比利时 布鲁塞尔
        ['Indla', 'New Delhi', 1303171035],  # 印度 新德里
        ['Brazil', 'Brasilia', 207847528]]  # 巴西 巴西利亚
# DataFrame创建
df = pd.DataFrame(data=data,
                  index=[1, 2, 3],
                  columns=["a", "b", "c"])

print("列访问")
print(df.a)            # 访问第一列, 返回Series
print(df['a'])         # 访问第一列, 返回Series
print(df[['a']])       # 访问第一列, 返回DataFrame
print(df[['a', 'b']])  # 访问第一列和第二列, 返回DataFrame

print("行访问")
print(df[0:2])     # 访问第一行和第二行
print(df[::-1])    # 倒序访问
print(df.head(2))  # 访问第一行和第二行
```

---
查看访问DataFrame中的数据——通用方法：

1. loc,iloc方法介绍  
    - 使用loc方法和iloc实现多列切片，其原理的通俗解释就是将多列的列名或者位置作为一个列表或者数据传入。使用loc，iloc方法可以取出DataFrame中的任意数据。
    - loc方法：
      - loc方法是针对DataFrame索引名称的切片方法，要求传入并须为索引名称。如果传入的不是索引名称，那么切片操作将无法执行 。利用loc方法，能够实现所有单层索引切片操作。
      - loc方法使用方法如下：
      - `DataFrame.loc[行索引名称或条件, 列索引名称]`
        - loc内部可以传入条件表达式，结果会返回满足表达式的所有值。
        - 多行或多列可以用切片或列表表示。在loc使用的时候内部传入的行索引名称如果为切片一个区间，则前后均为闭区间；

    - iloc方法：
      - iloc和loc区别是iloc接收的必须是行索引和列索引的位置。
      - iloc方法的使用方法如下：
      - `DataFrame.iloc[行索引位置, 列索引位置]`
        - 同样可以用切片或列表表示。iloc方法使用时 内部传入的行索引位置或列索引位置为区间时，则为前闭后开区间。

    loc更加灵活多变，代码的可读性更高，iloc的代码简洁，但可读性不高。具体在数据分析工作 中使用哪一种方法，根据情况而定，大多数时候建议使用loc方法。 

    特别的，当loc和iloc只取单个数据时，可用at和iat方法代替。

    示例：
    ```python
    import pandas as pd
    data = [['Belglum', 'Brussels', 11190846],  # 比利时 布鲁塞尔
            ['Indla', 'New Delhi',  1303171035],  # 印度 新德里
            ['Brazil', 'Brasilia',  207847528]]  # 巴西 巴西利亚
    # DataFrame创建
    df = pd.DataFrame(data=data,
                    index=[1, 2, 3],
                    columns=["a", "b", "c"])
    #
    # 1) 统一都取1和2行, a和b列
    print(df.loc[1:2, "a":"b"])  # 闭区间
    print(df.iloc[0:2, 0:2])     # 开区间
    # 条件表达式
    print(df.loc[df.index<3, "a":"b"])
    print(df.loc[df.c!=207847528, "a":"b"])
    # 列表指定取行和列
    print(df.loc[[1,2], ["a","b"]])
    print(df.loc[1:2,   ["a","b"]])
    print(df.iloc[[0,1], [0,1]])
    #
    # 2) 取单个数据
    print(df.loc[1,"a"], df.iloc[0,0])  # Belglum Belglum
    print(df.at[1,"a"], df.iat[0,0])    # Belglum Belglum
    # 取出单列数据时的；类型区别
    print(type(df.loc[1]))    # <class 'pandas.core.series.Series'>
    print(type(df.loc[1:1]))  # <class 'pandas.core.frame.DataFrame'>
    ```

2. 切片方法之ix
   - ix方法更像是loc和iloc两种切片方法的融合。ix方法在使用时既可以接收索引名称也可以接收索引位置。其使用方法如下。
   - `DataFrame.ix[行索引的名称或位置或者条件, 列索引名称或位置]`
   - 使用ix方法时有个注意事项，第一条，当索引名称和位置存在部分重叠时，ix默认优先识别名称。
   -  控制ix方法需要注意以下几点。
      -  使用列索引名称，而非列索引位置。主要用来保证代码可读性。
      -  使用列索引位置时，需要注解。同样保证代码可读性。
      -  除此之外ix方法还有一个缺点，就是在面对数据量巨大的任务的时候，其效率会低于loc和iloc方法，所以在日常的数据分析工作中建议使用loc和iloc方法来执行切片操作。

### 2.2.3. DataFrame更新修改数据

更改DataFrame中的数据，原理是将这部分数据提取出来，重新赋值为新的数据。
需要注意的是，数据更改直接针对DataFrame原数据更改，操作无法撤销，如果做出更改，需要对更改条件做确认或对数据进行备。

示例：

```python
import pandas as pd
df = pd.DataFrame([['小华', 20], ['小明', 19]],
                  index=[1, 2], columns=['name', 'age'])
print(df)
# 更新一个数据
df.iloc[0, 1] = 21
df.iat[1, 1] = 21
print(df)
# 更新一行
df[0:1] = ["小花", 23]
print(df)
# 更新一列
df.age = [-1, -1]
print(df)
```

运行结果：
```
  name  age
1   小华   20
2   小明   19
  name  age
1   小华   21
2   小明   21
  name  age
1   小花   23
2   小明   21
  name  age
1   小花   -1
2   小明   -1
```

### 2.2.4. DataFrame增添数据

列增加：
   - 索引赋值：
     - df原对象新增的一列：
       - `df[new_col_index] = [values...]`
       - `df[new_col_index] = {'fiels1':values,'fiels2':values...}`
     - 值是相同的可直接赋值一个常量。 如 `df[new_colums] = values`
   - insert增加：
     - `df.insert(num, colums_name, [values...])`，df原对象新增一列
   - reindex改动：
     - `df1 = df.reindex(columns=[name1, name2, ...])`，返回挑选列的df新对象，若列不存在与原df中则创建没有的列，值默认为空

行增加：
   - 索引赋值：`df.loc[row_index] = [x1, x2, ...]`
   - append增加：`df3 = df1.append(df2, ignore_index=True)`，在df1基础上增加或合并能被解析为df对象的新数据df2，ignore_index控制是否重新建立索引，默认为False

示例：列增加
```python
import pandas as pd
df = pd.DataFrame([['hua', 20], ['ming', 19]],
                  index=[1, 2], columns=['Name', 'Age'])
print('【原始df】\n', df)

# 增加列: 索引直接增加
df['Score'] = [87, 99]
print('【1列Score增加】\n', df)

# 增加列: insert
df.insert(1, 'Gender', ["M","F"])
print('【1列Gender增加】\n', df)

# 增加列：reindex，返回df新对象，增加的列数值为空
df1 = df.reindex(columns=['Name', 'Gender', 'City', 'Adress', 'Age', 'Score'])
print('【n列增删】\n', df1)
```

```
【原始df】
    Name  Age
1   hua   20
2  ming   19
【1列Score增加】
    Name  Age  Score
1   hua   20     87
2  ming   19     99
【1列Gender增加】
    Name Gender  Age  Score
1   hua      M   20     87
2  ming      F   19     99
【n列增删】
    Name Gender  City  Adress  Age  Score
1   hua      M   NaN     NaN   20     87
2  ming      F   NaN     NaN   19     99
```

示例：行增加
```python
import pandas as pd
df = pd.DataFrame([['hua', 20]], columns=['Name', 'Age'])
print('【原始df】\n', df)

# 增加行, loc指定索引添加
df.loc[3] = ['hu', 22]
print('【行增加】\n', df)

# 增加n行, append：将会返回新df, append合并两个表
row = {'Name': 'juan', 'Age': 14}
df1 = df.append([row, row], ignore_index=True)
df2 = df.append(pd.DataFrame([row, row]), ignore_index=True)
print('【df1】\n', df1)
print('【df2】\n', df2)
```

```
【原始df】
   Name  Age
0  hua   20
【行增加】
   Name  Age
0  hua   20
3   hu   22
【df1】
    Name  Age
0   hua   20
1    hu   22
2  juan   14
3  juan   14
【df2】
    Name  Age
0   hua   20
1    hu   22
2  juan   14
3  juan   14
```

### 2.2.5. DataFrame删除某列或某行数据

删除某列或某行数据需要用到pandas提供的方法drop，drop方法的用法如下:  
- `drop(labels, axis=0, level=None, inplace=False, errors='raise')`  
- axis为0时表示删除行，axis为1时表示删除列。

常用参数如下所示。

| 参数名称 |                        说明                         |
| -------- | --------------------------------------------------- |
| labels   | 接收string或array。代表删除的行或列的标签。无默认。 |
| axis     | 接收0或1。代表操作的轴向。默认为0。                 |
| levels   | 接收int或者索引名。代表标签所在级别。默认为None。   |
| inplace  | 接收boolean。代表搡作是否对原数据生效。默认为False. |

示例：
```python
import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(6).reshape(-1, 3), 
                  columns=["x", "y", "z"])
print("【df】\n", df)
df1 = df.drop(labels=0, axis=0)  # 删除第一行的数据
df2 = df.drop(labels='z', axis=1)  # 删除z列的数据
df3 = df.drop(labels='x', axis=1, inplace=True)  # 删除z列的数据，原对象操作，不返回新df对象
print("【df1】\n", df1)
print("【df2】\n", df2)
print("【df3】\n", df3)
print("【df】\n", df)
```

```
【df】
    x  y  z
0  0  1  2
1  3  4  5
【df1】
    x  y  z
1  3  4  5
【df2】
    x  y
0  0  1
1  3  4
【df3】
 None
【df】
    y  z
0  1  2
1  4  5
```

### 2.2.6. 对DataFrame数据进行排序

- `df.sort_index(axis=,ascending=)`
  - axis为0/1的参数，表示按行/按列排序；
  - ascending为boolean参数，False表示降序，True表示升序。
- `df.sort_values(by=，ascending=)`
  - by表示按哪一个columns参数排序。
  - ascending同上

```python
import numpy as np
import pandas as pd

name = ["Tony", "Tony", "Tony", "Hellen", "Hellen"]
score = np.random.randint(60, 200, 5)

df = pd.DataFrame(data=np.dstack((name, score)).reshape(-1, 2),
                  index=[3, 2, 1, 0, 4],
                  columns=['name', 'score'])
df1 = df.sort_index()
print(df1)
df2 = df.sort_values(by='score', ascending=False)
print(df2)

myself = dict(zip([71,84,74,99], range(4)))
df3 = df.sort_values(by='score', key=lambda col: col.str.lower())
print(df3)

#%%
# df = df.sort_values(by=['name'])
L_index = []
for i, tmp in df.groupby("name"):
    print(i)
    Indexs = tmp["score"].astype("float").sort_values().index.values
    print(Indexs)
    L_index.extend(Indexs)
df.loc[L_index]

#%%
def myf(x):
    print("x:", x)
    return x

# 原理渗透, x 为 services, xx 才为每一列的每一个元素
d = dict(((x[1],x[0]) for x in enumerate(df["name"].drop_duplicates().values)))
df.sort_values(["name"], key=(lambda x: x.map(lambda xx:d[xx])))

```

```
     name score
0  Hellen    91
1    Alon    65
2   Patty    86
3    Tony    79
4   Bella    60
     name score
0  Hellen    91
2   Patty    86
3    Tony    79
1    Alon    65
4   Bella    60
```

### 一些示例：

---
```python
# 将负数改为-，将正数改为+, 修改列名2-->strand
import pandas as pd
df = pd.DataFrame([[0,0,1],[0,0,-1],[0,0,1]])
print("before:\n%s" % df)
df.loc[df[2] == -1, 2] = "-"
df.loc[df[2] == 1, 2] = "+"
df.rename(columns={2: "strand"}, inplace=True)
print("changed:\n%s" % df)
```

```
before:
   0  1  2
0  0  0  1
1  0  0 -1
2  0  0  1
changed:
   0  1  2
0  0  0  +
1  0  0  -
2  0  0  +
```

---
将第一列和最后一列调换顺序【待补充】
```python
import pandas as pd
df = pd.DataFrame({"a":[0,0,0],"b":[0,0,0],"c":[1,-1,1]})
print(df)
df.insert(0, "add1", [6,6,6])
df
# df_c = df["c"]
# df = df.drop('c',axis=1).insert(0, "c", df_c)
# print(df)
```


---
# 3. 数据描述与统计

## 3.1. 数值型特征的描述性统计
pandas描述性统计方法描述分析DataFrame数据

基于NumPy中的描述性统计函数
   - 数值型数据的描述性统计主要包括了计算数值型数据的完整情况、最小值、均值、中位 数、最大值、四分位数、极差、标准差、方差、协方差和变异系数等。
   - pandas库基于NumPy，自然也可以用这些函数对数据框进行描述性统计。
   - pandas还提供了更加便利的方法来计算均值，如`detail['amounts'].mean()`。
   - pandas还提供了一个方法叫作describe，能够一次性得出数据框所有数值型特征的非空值数 目、均值、四分位数、标准差。

在NumPy库中一些常用的统计学函数如下表所示。

| 函数名称  |  说明  | 函数名称 |  说明  |
| --------- | ------ | -------- | ------ |
| np.min    | 最小值 | np.max   | 最大值 |
| np.mean   | 均值   | np.ptp   | 极差   |
| np.median | 中位数 | np.std   | 标准差 |
| np.var    | 方差   | np.cov   | 协方差 |

在Pandas库中一些常用的统计学函数如下表所示。

| 方法名称 |   说明   | 方法名称 |     说明     |
| -------- | -------- | -------- | ------------ |
| min      | 最小值   | max      | 最大值       |
| mean     | 均值     | ptp      | 极差         |
| median   | 中位数   | std      | 标准差       |
| var      | 方差     | cov      | 协方差       |
| sem      | 标准误差 | mode     | 众数         |
| skew     | 样本偏度 | kurt     | 样本峰度     |
| quantile | 四分位数 | count    | 非空值数目   |
| describe | 描述统计 | mad      | 平均绝对离差 |

> ps:
> - 平均绝对离差指的是各观察值与平均值的 距离总和，然后取其平均数
> - 偏度含义是统计数据分布偏斜方向和程度 的度量，是统计数据分布非对称程度的数 字特征。
> - 峰度，表征概率密度分布曲线在平均值处 峰值高低的特征数，反映了峰部的尖度。

示例：
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(50).reshape(10, 5), columns=list('abcde'))
print('\ndf：', df, 
      '\ndf.describe()：', df.describe(),
      '\ndf.sem()：', df.sem(), sep='\n')
```

```
df：
    a   b   c   d   e
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
4  20  21  22  23  24
5  25  26  27  28  29
6  30  31  32  33  34
7  35  36  37  38  39
8  40  41  42  43  44
9  45  46  47  48  49

df.describe()：
               a          b          c          d          e
count  10.000000  10.000000  10.000000  10.000000  10.000000
mean   22.500000  23.500000  24.500000  25.500000  26.500000
std    15.138252  15.138252  15.138252  15.138252  15.138252
min     0.000000   1.000000   2.000000   3.000000   4.000000
25%    11.250000  12.250000  13.250000  14.250000  15.250000
50%    22.500000  23.500000  24.500000  25.500000  26.500000
75%    33.750000  34.750000  35.750000  36.750000  37.750000
max    45.000000  46.000000  47.000000  48.000000  49.000000

df.sem()：
a    4.787136
b    4.787136
c    4.787136
d    4.787136
e    4.787136
dtype: float64
```

## 3.2. 类别型特征的描述性统计

描述类别型特征的分布状况，可以使用频数统计表。pandas库中实现频数统计的方法为`value_counts`。

`describe` 方法除了支持传统数值型以外，还能够支持对数据进行描述性统计，四个统计量分别为：
- 列非空元素的数目
- 类别的数目
- 数目最多的类别
- 数目最多类别的数目

示例：
```python
import pandas as pd
import numpy as np

ss = pd.Series(['Tokyo', 'Nagoya', 'Nagoya', 'Osaka', 'Tokyo', 'Tokyo'])
# 东京 名古屋 大阪
# value_counts 直接用来计算series里面相同数据出现的频率
print('\nss.value_counts()：', ss.value_counts(), 
      '\nss.describe()：', ss.describe(), sep='\n')
```

```
ss.value_counts()：
Tokyo     3
Nagoya    2
Osaka     1
dtype: int64

ss.describe()：
count         6
unique        3
top       Tokyo
freq          3
dtype: object
```

# 4. 数据的IO —— 文件读取与写入

## 4.1. 文本文件
### 4.1.1. 文本文件读取

（从文件中读取数据）

文本文件是一种由若干行字符构成的计算机文件，它是一种典型的顺序文件。

如：csv是一种逗号分隔的文件格式，因为其分隔符不一定是逗号，又被称为字符分隔文件，文
件以纯文本形式存储表格数据（数字和文本）。

文本文件读取
- 使用read_table来读取文本文件。

注：
> 一些重要参数：  
> float_precision="round_trip"：保持读取后的数值不变化。

```python
pandas.read_table(filepath_or_buffer, sep='\t', 
                  header='infer', names=None, index_col=None,
                  dtype=None, engine=None, nrows=None)
```
- 使用read_csv函数来读取csv文件。

```python
pandas.read_csv(filepath_or_buffer, sep=',', 
                header='infer', names=None, index_col=None,
                dtype=None, engine=None, nrows=None)
```

read_table和read_csv常用参数及其说明。

| 参数名称 |                                             说明                                             |
| -------- | -------------------------------------------------------------------------------------------- |
| filepath | 接收string。代表文件路径。无默认。该字符串可以是一个URL。有效的URL方案包括http, ftps3和file |
| sep      | 接收string。代表分隔符。read_csv默认为〃,〃，readable默认为制表符〃[Tab]〃。                 |
| header   | 接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。                       |
| names    | 接收array。表示列名。默认为None。                                                            |
| indexcol | 接收int、sequence或False。表示索引列的位置，取值为sequence则代表多重索引。默认为 None。      |
| dtype    | 接收dict。代表写入的数据类型（列名为key,数据格式为values)。默认为None。                      |
| engine   | 接收c或者python。代表数据解析引擎。默认为c。                                                 |
| nrows    | 接收int。表示读取前n行。默认为None。                                                         |

注：
- read_table和read_csv函数中的sep参数是指定文本的分隔符的，如果分隔符指定错误，在读取数据的时候，每一行数据将连成一片。
- header参数是用来指定列名的，如果是None则会添加一个默认的列名。
- encoding代表文件的编码格式，常用的编码有utf-8、utf-16、gbk、gb2312、gb18030等。如果编码指定错误数据将无法读取，IPython解释器会报解析错误。

### 4.1.2. 文本文件写入

文本文件储存 涉及xlrd openpyxl库的安装

文本文件的存储和读取类似，结构化数据可以通过pandas中的to_csv函数实现以csv文件格
式存储文件。
```python
DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='',
                columns=None, header=True, index=True,
                index_label=None,mode='w',encoding=None)
```

|   参数名称   |                         说明                          |
| ------------ | ----------------------------------------------------- |
| path_or_buf  | 接收string。代表文件路径。无默认。                    |
| sep          | 接收string。代表分隔符。默认为",〃。                  |
| na_rep       | 接收string。代表缺失值。默认为""。                    |
| columns      | 接收list。代表写出的列名。默认为None。                |
| header       | 接收boolean,代表是否将列名写出。默认为True。          |
| index        | 接收boolean,代表是否将行名（索引)写出。 默认为True。  |
| index labels | 接收sequence。表示索引名。默认为None。                |
| mode         | 接收特定string。代表数据写入模式。默认为w。           |
| encoding     | 接收特定string。代表存储文件的编码格式。默 认为None。 |

## 4.2. Excel文件
### 4.2.1. Excel文件读取

pandas提供了read_excel函数来读取"xls","xlsx"两种Excel文件。

```python
pandas.read_excel(io, sheetname=0, header=0, 
                  index_col=None, names=None, dtype=None)
```

| 参数名称  |                                            说明                                            |
| --------- | ------------------------------------------------------------------------------------------ |
| io        | 接收string。表示文件路径。无默认。                                                         |
| sheetname | 接收string、int。代表excel表内数据的分表位置。默认为0。                                    |
| header    | 接收int或sequence。表示将某行数据作为列名。默认为infer,表示自动识别。                      |
| names     | 接收int、sequence或者False。表示索引列的位置，取值为sequence则代表多重索引。默认 为 None。 |
| index col | 接收int、sequence或者False。表示索引列的位置，取值为sequence则代表多重索引。默认 为 None。 |
| dtype     | 接收diet。代表写入的数据类型（列名为key,数据格式为values)。默认为None。                    |

### 4.2.2. Excel文件写入

将文件存储为Excel文件，可以使用to_excel方法。其语法格式如下。
```python
DataFrame.to_excel(excel_writer=None, sheetname=None'', 
                   na_rep='', header=True, index=True,
                   index_label=None, mode='w', encoding=None)
```
to_csv方法的常用参数基本一致，区别之处在于指定存储文件的文件路径参数名称为excel_writer，并且没有sep参数，增加了一个sheetnames参数用来指定存储的Excel sheet的名称，默认为
sheet1。

## 4.3. 扩展：数据库数据
### 4.3.1. sql读取
- pandas提供了读取与存储关系型数据库数据的函数与方法。除了pandas库外，还需要使用SQLAlchemy库建立对应的数据库连接。SQLAlchemy配合相应数据库的Python连接工具（例如MySQL数据库需要安装mysqlclient或者pymysql库），使用create_engine函数，建立一个数据库连接。
- creat_engine中填入的是一个连接字符串。在使用Python的SQLAlchemy时，MySQL和Oracle数据库连接字符串的格式如下：
  `数据库产品名+连接工具名：//用户名:密码@数据库IP地址:数据库端口号/数据库名称?charset=`

数据库数据编码
```python
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqldb://root@localhost:3306/shop)
```

-  `read_sql_table` 只能够读取数据库的某一个表格，不能实现查询的操作。

```python
pandas.read_sql_table(table_name, con, schema=None, index_col=None,
                      coerce_float=True, columns=None)
```

- `read_sql_query` 则只能实现查询操作，不能直接读取数据库中的某个表。

```python
pandas.read_sql_query(sql, con, index_col=None, coerce_float=True)
```

- `read_sql` 是两者的综合，既能够读取数据库中的某一个表，也能够实现查询操作。

```python
pandas.read_sql(sql, con, index_col=None, coerce_float=True, columns=None)
```

pandas三个数据库数据读取函数的参数几乎完全一致，唯一的区别在于传入的是语句还是表名。

|     参数名称      |                                            说明                                            |
| ----------------- | ------------------------------------------------------------------------------------------ |
| sql or table_name | 接收string。表示读取的数据的表名或者sql语句。无默认。                                      |
| con               | 接收数据库连接。表示数据库连接信息。无默认                                                 |
| index_col         | 接收int，sequence或者False。表示设定的列作为列名，如果是一个数列则是多重索引。默认为None。 |
| coerce_float      | 接收boolean。将数据库中的decimal类型的数据转换为pandas中的float64类型的数据。默认为True。  |
| columns           | 接收list。表示读取数据的列名。默认为None。                                                 |

### 4.3.2. sql存储

数据库数据读取有三个函数，但数据存储则只有一个to_sql方法。
```python
DataFrame.to_sql(name, con, schema=None, if_exists='fail', 
                 index=True, index_label=None, dtype=None)
```

|  参数名称   |        说明          |
| ----------- | -------------------  |
| name        | 接收string。代表数据库表名。无默认。 |
| con         | 接收数据库连接。无默认。             |
| if_exists   | 接收fail，replace，append。fail表示如果表名存在则不执行写入操作；replace表示如果存在，将原数据库表删除，再重新创建；append则表示在原数据库表的基础上追加数据。默认为fail。 |
| index       | 接收boolean。表示是否将行索引作为数据传入数据库。默认True。    |
| index_label | 接收string或者sequence。代表是否引用索引名称，如果index参数为True此参数为None则使用默认名称。如果为多重索引必须使用sequence形式。默认为None。  |
| dtype       | 接收dict。代表写入的数据类型（列名为key，数据格式为values）。默认为None。 |

### 4.3.3. 其他
扩展：其他格式
- HDF5: HDF5 是一种层次化的格式（hierarchical format），经常用于存储复杂的科学数据。例如 MATLAB 就是用这个格式来存储数据。在存储带有关联的元数据（metadata）的复杂层次化数据的时候，这个格式非常有用，例如计算机模拟实验的运算结果等等，
- pandas还提供一个直接读取h5文件的函数： pd.HDFStore
- Json: 通过json模块转换为字典，再转换为DataFrame，pd.read_json
- MongoDB数据库：需要结合相应的数据库模块，如：pymongo，再通过游标把数据读出来，转换为DataFrame

# Pandas数据分析与可视化



# 附：常用操作


消掉打印不完全中间的省略号
```python
# 核心代码，设置显示的最大列、宽等参数，
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
```

## 表内操作

列增加

```python
df = pd.DataFrame([["a1", 1], ["a2", 2]])
df["new_colums"] = [1, 2]
df.loc[:,"new_colums"] = [1, 2]
```

列调换
```python
df.insert(1,'调换',df.pop('A'))  #改变某一列的位置。如：先删除A列，然后在原表data中第1列插入被删掉的列。
```

表纵向连接：
```python
import pandas as pd
L1 = ["a1", "a2", "a3"]
L2 = ["b1", "b2", "b3"]
df1 = pd.DataFrame([L1, L1, L1])
df2 = pd.DataFrame([L2, L2, L2])
pd.concat([df1, df2], axis=0)
pd.concat([df1, df2], axis=0, ignore_index=True)
pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], axis=1, ignore_index=True)
```

## 数据cleane

表去重：
```python
import pandas as pd
df = pd.DataFrame(
  [["a1", 1],
   ["a1", 1],
   ["a1", 2],
   ["a1", 2],
   ["a2", 1],
   ]
)
df.drop_duplicates()  # inplace=True
```

表去NA：
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(
  [["a1", np.nan],
   ["a1", 1],
   ["a1", 1],
   [np.nan, np.nan],
   ["a2", 1],
   ]
)
df.dropna()  # 删除行中出现na的数据, how{‘any’, ‘all’}, default ‘any’
df.dropna(how="any")
df.dropna(how="all")

```

表格多行压缩单行（按某列唯一压缩）
```python

def collapse(df, name):
    L = []
    for k, x in df.groupby(name):
        name = set(name)
        L_tmp = []
        for col in x:
            if col not in name:
                # L_tmp.append(','.join([str(xx) for xx in x[col].values]))
                L_tmp.append(x[col].values)
            else:
                L_tmp.append(x[col].iloc[0])
        L.append(L_tmp)
    return pd.DataFrame(L, columns=df.columns)


df_test = pd.DataFrame(
    [["a1", "aa1",  "A", 1],
        ["a2", "aa2",  "B1", 1],
        ["a2", "aa2",  "B2", 2],
        ["a3", "aa3",  "C1", 1],
        ["a3", "aa3",  "C2", 2],
        ["a3", "aa3",  "C2", 3],
     ], columns=["name1", "name2", "type", "value"]
)
collapse(df_test, ["name1", "name2"])

```

```python
def de_collapse(pd2, names):
    # 注意Pandas版本必须 > 1.3.0, 才能使用explode多行一起解压
    for x1, x2 in zip(pd.__version__.split("."), [1, 3, 0]):
        if int(x1) < x2:
            print("pandas version:", pd.__version__, "< 1.3.0, check error.")
            break
    else:
        print("pandas version:", pd.__version__, "> 1.3.0, check ok.")
    for name in names:
        df2[name] = df2[name].map(lambda x: x.split(","))
    return df2.explode(names)


# 解压：
df2 = collapse(df, "name")
de_collapse(df2, ["type", "value"])
```

```python
# 官方测试代码
## New in version 1.3.0: Multi-column explode
import numpy as np
df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
                   'B': 1,
                   'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})
df
df.explode(list('AC'))
#%%
help(pd)
```
## 表间操作


## 表补齐

```python
import pandas as pd
df = pd.DataFrame(
  [["a1", 1],
   ["a1", None],
   ["a2", 1],
   ]
)
df
df.where(df.notnull(), "NA")  # 将Nan补为字符串"NA"，方便后续表格写入文件
```

## 表过滤查询

```python
import pandas as pd
df = pd.DataFrame({"a": ["AA", "AA", "AAA", "BB", "CC"], "b": [11, 22, 33, 44, 55]})
# 查询（单个值）
df.query('a == "AA" & b > 20')
df.loc[(df.a == "AA") & (df.b > 20)]
df.loc[~((df.a == "AA") & (df.b > 20))]  # ~ 代表非
df.loc[~(df.a == "AA") & (df.b > 20)]  # ~ 代表非
# 查询（多个值）
df[df.a.isin(["AA", "BB"])]
df[df.a.isin(["AA", "BB"]) & (df.b > 20)]
# 查询（包含某个词：字符串关键词查找）
df[df["a"].str.contains('AA|C')]
```

```python
# 查询方式效率比较
import pandas as pd
import time
df = pd.DataFrame({"a": range(0, 300000000, 1), "b": range(0, 600000000, 2)})
t = time.time(); df.query('a < 500000 & b < 500000'); print(time.time() - t)
t = time.time(); df.loc[(df.a < 500000) & (df.b < 500000)]; print(time.time() - t)
t = time.time(); df.loc[(df["a"] < 500000) & (df["b"] < 500000)]; print(time.time() - t)
```

## 数据描述

```python
import pandas as pd
df = pd.DataFrame({"a": [1, 20, 1, 1, 1, 20]})
df
pd.value_counts(df.a)
```

## read_csv / read_table 的一些细节补充

```python
"""
存在NA的一列，都会被转换为浮点数
* python – Pandas：为什么数值浮点数的默认列类型？ - 程序园 : http://www.voidcn.com/article/p-hxculmiy-bvn.html
* Pandas 缺失值的认定 | Pandas 教程 - 盖若 : https://www.gairuo.com/p/pandas-missing-data
* 整型中的缺失值。由于 NaN 是浮点型，因此一列甚至缺少一个整数的整数列都将转换为浮点。
"""

# %%
print("""c1	c2	c3	c4
5	6	7	8
9	NA	11	NA
13	14	15	16
17	18	19	20
""", file=open("./mat.tsv", "w"))

# %%
# ! 结论：NA列会将数据类型自动转为float
import pandas as pd
df = pd.read_table("./mat.tsv")
print(df.dtypes)
df

# %%
# ! 解决方案探索
import numpy as np
se = pd.Series([1, 2, np.nan, 4], dtype="str")
print(se.dtypes)
print(se)

# %%
# ! 二次读取的解决方案：
# ! 先读第一行，将所有列指定为str，根据需求手动改类型，二次读取。
colnames = pd.read_table("./mat.tsv", nrows=1).columns
dtype = {x: "str" for x in colnames}
dtype.update({"c1": "int"})
df=pd.read_table("./mat.tsv", dtype=dtype)
print(df.dtypes)
print(df.isna())
df
## ! 注，该方案不会改变原始数据是NA的为字符串。
## 如需将NA也识别为字符串，需指定参数，keep_default_na=False
```


```python
# %%

# 数据生成
print("""c1	c2	c3	c4
5	6	7	8
9	NA	11	NA
13	14	15	16
17	18	19	20
""", file=open("./mat.tsv", "w"))

# %%
import pandas as pd


def pd_read_table_str(infile, dtype={}, **kwargs):
    # ! 二次读取的解决方案：先读第一行，将所有列指定为str，根据需求手动改类型，二次读取。
    colnames = pd.read_table(
        infile, nrows=1, keep_default_na=False, **kwargs).columns
    dtypes = {x: "str" for x in colnames}
    dtypes.update(dtype)
    # dtype.update({"c1": "int"})  # 根据需要更改
    df = pd.read_table(infile, dtype=dtypes, keep_default_na=False, **kwargs)
    # 如需将NA也识别为字符串，需指定参数，keep_default_na=False
    return df


df = pd_read_table_str("./mat.tsv", dtype={"c3":"int"})
df = pd_read_table_str("./mat.tsv", dtype={"c3":"int"}, header=None)
df
# df.dtypes
#%%
```

## read_fwf

```python
#%%
import pandas as pd
import io

TESTDATA = """\
    A       B   C
name1      12   1
name2  123124   0
"""

df = pd.read_table(io.StringIO(TESTDATA))  # 无法识别
df

df = pd.read_fwf(io.StringIO(TESTDATA))  # 正常识别
df

```


## 利用 groupby 

```python
import pandas as pd
import numpy as np
df_all = pd.DataFrame([0,0,0,0,1,1,1,1,1,1], columns=["filter"])
Lnum = np.array([[x[0], len(x[1])]
                  for x in df_all[["filter"]].groupby("filter")])

list(zip(Lnum[:, 0], Lnum[:, 1], Lnum[:, 1]/Lnum[:, 1].sum()))

```


## apply的使用

apply 用于 DataFrame
map 用于 Series

```python
import pandas as pd
import numpy as np
df_all = pd.DataFrame(
  np.arange(15).reshape(-1, 3),
  columns=["x1", "x2", "x3"]
).astype("str")
print(df_all.dtypes)
df_all["newcol"] = df_all[["x1", "x3"]].apply(lambda x: ';'.join(x), axis=1)
df_all
```


## 去重示例，保留相同列1和最大的一行

```python
import pandas as pd

def drop_dup_col1(a_new):
    L_del_index = []
    for x in a_new.iloc[:,0][a_new.iloc[:,0].duplicated()].drop_duplicates():
        df_filter = a_new[a_new.iloc[:,0] == x]
        L_del_index.extend(df_filter.iloc[:, 1:].sum(axis=1).sort_values(
            ascending=False).iloc[1:].index)
    return a_new.drop(index=L_del_index)

a_new = pd.DataFrame([
    ["a", 1, 2, 3, 4],
    ["a", 1, 2, 3, 5],
    ["a", 1, 2, 3, 3],
    ["b", 1, 2, 3, 3],
])
drop_dup_col1(a_new)
```

```python
import pandas as pd

df_test = pd.DataFrame(
    [["a1", "aa1",  "A", 1],
        ["a2", "aa2",  "B1", 1],
        ["a2", "aa2",  "B2", 2],
        ["a3", "aa3",  "C1", 1],
        ["a3", "aa3",  "C2", 2],
        ["a3", "aa3",  "C2", 3],
     ], columns=["name1", "name2", "type", "value"]
)


```
