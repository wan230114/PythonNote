Python爬虫精进  
前言  
对应前一部，本书旨在探索更深层次的一些基本原理问题，以帮助更深入的理解Python编程。  
  
  
# 1. 概述
  
  
## 1.1. 初识爬虫
  
到底什么是爬虫呢？  
  
### 1.1.1. 概念
  
爬虫，从本质上来说，就是利用程序在网上拿到对我们有价值的数据。  
  
### 1.1.2. 应用
  
  
#### 1.1.2.1. 个人
  
爬虫能做很多事，能做商业分析，也能做生活助手，比如：分析北京近两年二手房成交均价是多少？深圳的Python工程师平均薪资是多少？北京哪家餐厅粤菜最好吃？等等。  
  
#### 1.1.2.2. 商业
  
**搜索引擎**  
  
这是个人利用爬虫所做到的事情，而公司，同样可以利用爬虫来实现巨大的商业价值。比如你所熟悉的搜索引擎——百度和谷歌，它们的核心技术之一也是爬虫，而且是超级爬虫。    
  
以百度为例，你在搜索的时候仔细看，会发现每个搜索结果下面都有一个百度快照。  
      
点击百度快照，你会发现网址的开头有baidu这个词，也就是说这个网页属于百度。  
   
这是因为，百度这家公司会源源不断地把千千万万个网站爬取下来，存储在自己的服务器上。你在百度搜索的本质就是在它的服务器上搜索信息，你搜索到的结果是一些超链接，在超链接跳转之后你就可以访问其它网站了。  
  
图示：  
  
![图 1](img/Crawler_20200519_10_54_15.png)    
  
![图 2](img/Crawler_20200519_10_55_36.png)    
  
  
#### 1.1.2.3. 从数据帝走向人工智能
  
爬虫还让这些搜索巨头有机会朝着人工智能的未来迈进，因为人工智能的发展离不开海量的数据。而每天使用这些搜索网站的用户都是数以亿计的，产生的数据自然也是难以计量的。  
  
从搜索巨头到人工智能巨头，这是一条波澜壮阔的路。而我们应该看到，事情的源头，却是我们今日所书写的“爬虫”。  
  
现在，我们对爬虫有了初步的印象，知道了爬虫能做什么，那我们接下来来看看，爬虫是如何做到这些事的。  
  
## 1.2. 爬虫原理
  
### 1.2.1. 浏览器的工作原理
  
在网站上有几篇文章。假设，我们想收藏首页的文章标题和文章摘要，我们可能会复制粘贴到本地文档。其实这个过程，是一个人和浏览器在交流的过程.更完整的交流过程是下图这样的：  
首先，我们在浏览器输入网址（也可以叫URL）。然后，浏览器向服务器传达了我们想访问某个网页的需求，这个过程就叫做“请求”。  
紧接着，服务器把你想要的网站数据发送给浏览器，这个过程叫做“响应”。  
所以浏览器和服务器之间，先请求，后响应，有这么一层关系。  

![图 3](img/Crawler_20200519_10_58_07.png)  

当服务器把数据响应给浏览器之后，浏览器并不会直接把数据丢给你。因为这些数据是用计算机的语言写的，浏览器还要把这些数据翻译成你能看得懂的样子，这是浏览器做的另一项工作“解析数据”。  
紧接着，我们就可以在拿到的数据中，挑选出对我们有用的数据，这是“提取数据”。  
最后，我们把这些有用的数据保存好，这是“存储数据”。  
以上，就是浏览器的工作原理，是人、浏览器、服务器三者之间的交流过程。  
可这和爬虫有什么关系呢？  
  
### 1.2.2. 爬虫的工作原理
  
其实，爬虫可以帮我们代劳这个过程的其中几步，请看下图：  

![](img/Crawler_20200519_10_58_37.png)  
   
当你决定去某个网页后，首先，爬虫可以模拟浏览器去向服务器发出请求；其次，等服务器响应后，爬虫程序还可以代替浏览器帮我们解析数据；接着，爬虫可以根据我们设定的规则批量提取相关数据，而不需要我们去手动提取；最后，爬虫可以批量地把数据存储到本地。  
这就是爬虫做的事。简化上图，就是爬虫的工作原理了：  
![图 5](img/Crawler_20200519_10_59_04.png)  
   
其实，还可以把最开始的【请求——响应】封装为一个步骤——获取数据。由此，我们得出，爬虫的工作分为四步：  
**第0步：** 获取数据。爬虫程序会根据我们提供的网址，向服务器发起请求，然后返回数据。  
**第1步：** 解析数据。爬虫程序会把服务器返回的数据解析成我们能读懂的格式。  
**第2步：** 提取数据。爬虫程序再从中提取出我们需要的数据。  
**第3步：** 储存数据。爬虫程序把这些有用的数据保存起来，便于你日后的使用和分析。  
这就是爬虫的工作原理啦，无论之后的学习内容怎样变化，其核心都是爬虫原理。  
  
## 1.3. 爬虫伦理
  
就像是两个人在来来往往的相处中，会考虑对方的感受；在互联网的世界中，我们也要考虑一下服务器对爬虫的感受是怎样的。  
我们说过，服务器其实就是一个超级电脑，拥有这个服务器的公司，对爬虫其实也有明确的态度。  
通常情况下，服务器不太会在意小爬虫，但是，服务器会拒绝频率很高的大型爬虫和恶意爬虫，因为这会给服务器带来极大的压力或伤害。  
不过，服务器在通常情况下，对搜索引擎是欢迎的态度（刚刚讲过，谷歌和百度的核心技术之一就是爬虫）。当然，这是有条件的，而这些条件会写在Robots协议。  
Robots协议是互联网爬虫的一项公认的道德规范，它的全称是“网络爬虫排除标准”（Robots exclusion protocol），这个协议用来告诉爬虫，哪些页面是可以抓取的，哪些不可以。  
如何查看网站的robots协议呢，很简单，在网站的域名后加上/robots.txt就可以了。  
我们截取了一部分淘宝的robots协议 （ http://www.taobao.com/robots.txt ）。在截取的部分，可以看到淘宝对百度和谷歌这两个爬虫的访问规定，以及对其它爬虫的规定。  

```
User-agent:  Baiduspider #百度爬虫
Allow:  /article #允许访问 /article.htm
Allow:  /oshtml #允许访问 /oshtml.htm
Allow:  /ershou #允许访问 /ershou.htm
Allow: /$ #允许访问根目录，即淘宝主页
Disallow:  /product/ #禁止访问/product/
Disallow:  / #禁止访问除 Allow 规定页面之外的其他所有页面

User-Agent:  Googlebot #谷歌爬虫
Allow:  /article
Allow:  /oshtml
Allow:  /product #允许访问/product/
Allow:  /spu
Allow:  /dianpu
Allow:  /oversea
Allow:  /list
Allow:  /ershou
Allow: /$
Disallow:  / #禁止访问除 Allow 规定页面之外的其他所有页面

…… # 文件太长，省略了对其它爬虫的规定，想看全文的话，点击上面的链接

User-Agent:  * #其他爬虫
Disallow:  / #禁止访问所有页面
```

协议里最常出现的英文是Allow和Disallow，Allow代表可以被访问，Disallow代表禁止被访问。而且有趣的是，淘宝限制了百度对产品页面的爬虫，却允许谷歌访问。

所以，当你在百度搜索“淘宝网”时，会看到下图的这两行小字。

![图 6](img/Crawler_20200519_11_01_27.png)  

因为百度很好地遵守了淘宝网的robots.txt协议，自然，你在百度中也查不到淘宝网的具体商品信息了。

虽然Robots协议只是一个道德规范，和爬虫相关的法律也还在建立和完善之中，但我们在爬取网络中的信息时，也应该有意识地去遵守这个协议。

## 1.4. html基础
略

# 2. 爬虫库概览
Requests获取数据
BeautifulSoup解析数据

![图 7](img/Crawler_20200519_11_01_56.png)  

# 3. REQUESTS库：获取网页数据
我们将会利用一个强大的库——requests来获取数据。  

requests库可以帮我们下载网页源代码、文本、图片，甚至是音频。其实，“下载”本质上是向服务器发送请求并得到响应。  

安装
```bash
pip install requests
```

## 3.1.1. requests.get()创建Response对象

语法：
```python
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
res = requests.get(url, headers=headers)
```

参数：
- url ：请求地址
- headers ：访问请求头。默认为Python套接字请求头，通常自定义用于模拟浏览器真实访问。

解释：
- 引入requests库，requests.get()方法向服务器发送了一个请求，括号里的参数是你需要的数据所在的网址，然后服务器对请求作出了响应。我们把这个响应返回的结果赋值在变量res上。

---
实例：

现在，我们试着用requests.get()来下载一个小说——《三国演义》：

```python
import requests 
# 引入requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md') 
# 发送请求，并把响应结果赋值在变量res上
```


---
## 3.2. Response对象的常用属性

| 属性                   | 作用                 |
|----------------------|--------------------|
| response.status_code | 检查请求是否成功           |
| response.content     | 把reponse对象转换为二逬制数据 |
| response.text        | 把reponse对象转换为字符串数据 |
| response.encoding    | 定义response对象的编码    |


**res.status_code获取相应状态码**

常见响应状态码有：

| 响应状态码 | 说明     | 举例  | 说明      |
|-------|--------|-----|---------|
| 1xx   | 请求收到   | 100 | 继续提出请求  |
| 2xx   | 谓求成功   | 200 | 成功      |
| 3xx   | 重定向    | 305 | 应使用代理访问 |
| 4xx   | 客户端错误  | 403 | 禁止访问    |
| 5xx   | 服务器端错误 | 503 | 服务不可用   |

**res.content返回获取二进制数据**

把Response对象的内容以二进制数据的形式返回，适用于图片、音频、视频的下载。
示例：下载图片
```python
import requests    
#发出请求，并把返回的结果放在变量res中    
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')    
#把Reponse对象的内容以二进制数据的形式返回    
pic=res.content
#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。 图片内容需要以二进制wb读写。
photo = open('ppt.jpg','wb')    
#获取pic的二进制内容    
photo.write(pic)     
#关闭文件    
photo.close()
```

**res.text返回获取字符串数据**

response.text，这个属性可以把Response对象的内容以字符串的形式返回，适用于文字、网页源代码的下载。

注：程序会根据操作系统自动进行判断编码规则，有时候会造成乱码

**res.encoding设置编码**
当遇上文本的乱码问题，考虑用res.encoding手动定义编码规则

```python
res.encoding='gbk'
```

# 4. BEAUTIFULSOUP库：解析网页文本

简介

安装：
```bash
pip install BeautifulSoup4
```

## 4.1. BeautifulSoup()创建对象

语法：

```python
from bs4 import BeautifulSoup

bs = BeautifulSoup(markup=None, features=None, ...)
# type：<class 'bs4.BeautifulSoup'>
```
参数：
- markup 要解析的文本字符串, str
- features 解析器, 该参数用来标识解析器，我们要用的是一个Python内置库：`html.parser`。（它不是唯一的解析器，但是比较简单的）

注意：
- `print(bs)`可以直接打印出文本，但它本质是是一个bs对象，非字符串对象

## 4.2. 方法
### 4.2.1. find() / find_all()方法
- 可以操作的bs对象：（PS：Tag继承自Bs，本质上也是Bs【待验证是否正确？】）
  - <class 'bs4.BeautifulSoup'>
  - <class 'bs4.element.Tag'> 

- 用法及输出：

    ```python
    bs.find(标签, 属性="字符串")  # 满足要求的首个数据
    ```
    返回对象：<class 'bs4.element.Tag'>，  
    可直接打印出字符串（非字符串对象，可str转换）  

    ```python
    bs.find_all(标签, 属性="字符串")   满足要求的所有数据的列表
    ```
    返回对象：<class 'bs4.element.ResultSet'>，  
    可当做列表处理，其中该对象其实是封装了Tag对象

注意：
- 属性中的class标签需用class_替换

---
示例：

```python
from bs4 import BeautifulSoup
  
bs = BeautifulSoup(
    ('<p class="books">test1</p>\n'
     '<p class="books">test2</p>\n'
     '<p class="books2">test3</p>'
     ), 
    'html.parser')
items0 = bs.find('p')
items1 = bs.find_all('p')
items2 = bs.find_all(class_='books') #通过定位标签和属性提取我们想要的数据
items3 = bs.find_all('p', class_='books2')
print(items0, items1, items2, items3, sep='\n')
```
运行结果：
```
<p class="books">test1</p>
[<p class="books">test1</p>, <p class="books">test2</p>, <p class="books2">test3</p>]
[<p class="books">test1</p>, <p class="books">test2</p>]
[<p class="books2">test3</p>]
```

## 4.3. Bs对象和Tag对象属性
### text属性
提取文本

```python
bs.text
tag.text
```
返回：字符串对象

### 4.3.2. Tag['属性名']
注意事项：
必须为Tag对象才能操作
查找的属性，必须为当前标签，对于子标签无效。如下：

```python
from bs4 import BeautifulSoup
bs = BeautifulSoup("<p><a href='https://www.pypypy.cn'></a></p>",'html.parser')
tag = bs.find('p')
# print(tag['href'])  # 这样会报错，因为<p>标签没有属性href，href属于<a>标签
print(tag.find('a')['href'])

```

## 操作实例

### 获取菜品列表

实例：
```python
import requests  
from bs4 import BeautifulSoup  
  
res_foods = requests.get('http://www.xiachufang.com/explore/')  # 获取数据  
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')  # 解析数据  
list_foods = bs_foods.find_all('div', class_='info pure-u')  # 查找最小父级标签  
  
tag_a = list_foods[0].find('a')  # 提取第0个父级标签中的<a>标签  
name = tag_a.text[17:-13]  # 菜名，使用[17:-13]切掉了多余的信息  
URL = 'http://www.xiachufang.com' + tag_a['href']  # 获取URL  
  
tag_p = list_foods[0].find('p', class_='ing ellipsis')  # 提取第0个父级标签中的<p>标签  
ingredients = tag_p.text[1:-1]  # 食材，使用[1:-1]切掉了多余的信息  
print(ingredients)  # 打印食材  
```




---
# xpath的基本使用

```python
from lxml import etree
 
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """

def exp(html_data):
    print(type(html_data[0]))
    for i in html_data:
        if type(i) == etree._Element:
            print("  i.text: ", i.text)
        else:
            print("  i:", i)

html = etree.HTML(wb_data)  # 初始化
print(html)  # Element
result = etree.tostring(html)  # 打印字符串
print(result.decode("utf-8"))

# 获取标签a 文本内容
exp(html.xpath('/html/body/div/ul/li/a'))  # [Element, ]
# 获取标签a 文本内容
exp(html.xpath('/html/body/div/ul/li/a/text()'))  # [str, ]
# 获取标签a 属性（网址）
exp(html.xpath('/html/body/div/ul/li/a/@href'))  # [str, ]
# 获取标签a 属性（网址==特定值）的文本内容
exp(html.xpath('/html/body/div/ul/li/a[@href="link2.html"]/text()'))  # [str, ]
# 获取标签a 文本内容， li相对路径下
exp(html.xpath('//li/a'))  # [Element, ]
# 获取标签a 文本内容， li相对路径下
exp(html.xpath('//li/a/text()'))  # [str, ]
# 获取标签a 文本内容， li相对路径下
exp(html.xpath('//li/a//@href'))  # [str, ]
# 获取标签a 文本内容， li相对路径下
exp(html.xpath('//li/a[@href="link2.html"]'))  # [Element,]
# 查找最后一个li标签里的a标签的href属性
exp(html.xpath('//li[last()]/a/text()'))
# 查找倒数第二个li标签里的a标签的href属性
exp(html.xpath('//li[last()-1]/a/text()'))
```