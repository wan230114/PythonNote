# 2. Django中的路由及应用配置
## 2.1. URL 介绍
url 即统一资源定位符 Uniform Resource Locator

- 作用: 用来表示互联网上某个资源的地址。
- 说明: 互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。

- URL的一般语法格式为：
  - <https://www.djangoproject.com/download/>

    ```
    protocol :// hostname[:port] / path [?query][#fragment]

    如:
    http://tts.tmooc.cn/video/showVideo?meuId=657421&version=AID201908#s
    ```

- 说明:
    - protocol（协议）
        - http 通过 HTTP 访问该资源。 格式 `HTTP://`
        - https 通过安全的 HTTPS 访问该资源。 格式 `HTTPS://`
        - file 资源是本地计算机上的文件。格式: `file:///`
        - ...
    - hostname（主机名）
        - 是指存放资源的服务器的域名系统(DNS) 主机名、域名 或 IP 地址。
    - port（端口号）
        - 整数，可选，省略时使用方案的默认端口；
        - 各种传输协议都有默认的端口号，如http的默认端口为80。 HTTPS 443
    - path（路由地址）
        - 由零或多个“/”符号隔开的字符串，一般用来表示主机上的一个目录或文件地址。路由地址决定了服务器端如何处理这个请求
    - query(查询) 
        - 可选，用于给动态网页传递参数，可有多个参数，用“&”符号隔开，每个参数的名和值用“=”符号隔开。
    - fragment（信息片断）
        - 字符串，用于指定网络资源中的片断。例如一个网页中有多个名词解释，可使用fragment直接定位到某一名词解释。
    - 注: [] 代表其中的内容可省略

<font face="仿宋">

> 拓展： 地址栏的自动补全
> - settings.py里  APPEND_SLASH  可以设置是否自动补全“/”
>     - APPEND_SLASH  -> 自动补全 “/”
> 
> - 案例：
>     - url(r'^page1/$', xx) , 访问浏览器时 , 地址栏输入 127.0.0.1:8000/page1 , 此时 django接到请求后返回301【永久重定向】, 并在响应头中指定重定向地址为 /page1/ ，从而出现自动补全 “/” 效果
> 
> - 若要关闭此功能，可将 `APPEND_SLASH = False`
> 

</font>

## 2.2. Django 中的路由配置
- settings.py 中的`ROOT_URLCONF` 指定了主路由配置列表urlpatterns的文件位置
- urls.py 主路由配置文件
    ```python
    # file : <项目名>/urls.py
    from django.conf.urls import url, include

    urlpatterns = [
        # 此处配置主路由
        url(r'^admin/', admin.site.urls),
        # ...

        # 路由分法，下一节应用细述
        url(r'^music/', include('music.urls'))
    ]
    ```
    > urlpatterns 是一个路由-视图函数映射关的列表,此列表的映射关系由url函数来确定

- url() 函数
    - 用于描述路由与视图函数的对应关系
    - 模块
        - `from django.conf.urls import url`
    - 语法: 
        - url(regex, views, name=None)
        - 参数：
            1. regex: 字符串类型，匹配的请求路径，允许是正则表达式
            2. views: 指定路径所对应的视图处理函数的名称
            3. name: 为地址起别名，在模板中地址反向解析时使用
    
    > 每个正则表达式前面的r表示`'\'`不转义的原始字符串


### 2.2.1. 带有分组的路由和视图函数
（元组位置传参）
- 在视图函数内，可以用正则表达式分组 `()` 提取参数后用函数位置传参传递给视图函数

- 一个分组表示一个参数,多个参数需要使用多个分组,并且使用/隔开
    -   - http://127.0.0.1:8000/year/2018
        - http://127.0.0.1:8000/year/2019
        - http://127.0.0.1:8000/year/????  # 四位数字


### 2.2.2. 带有命名分组的路由和视图函数
（字典关键字传参）
- 在url 的正则表达式中可以使用命名分组(捕获分组)
- 说明:
    - 在视图函数内，可以用正则表达式分组 `(?P<name>pattern)` 提取参数后用函数关键字传参传递给视图函数  
- 示例:
    - 路由配置文件
        ```python
        # file : <项目名>/urls.py
        # 以下示例匹配
        # http://127.0.0.1:8000/person/weimingze/35
        # http://127.0.0.1:8000/person/shibowen/29
        # http://127.0.0.1:8000/person/xiaowei/9
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
        ]
        ```
    - views.py
        ```python
        from django.http import HttpResponse

        def person_view(request, name, age):
            return HttpResponse("name: %s , age: %s" % (
                name, age))
        ```


> - PyCharm 社区版针对Django项目调试方法
>     1. 添加自己调式配置
>         - 选择 Add Configuration...
>     2. 点击 `+` 号添加一个自己的配置
>         - 选择运行的项目的主模块位置 manage.py
>         - 添加 runserver 命令行参数


## 2.3. Django中的应用 - app
- 应用在Django项目中是一个独立的业务模块,可以包含自己的路由,视图,模板,模型

### 2.3.1. 创建应用app
- 创建步骤
    1. 用manage.py 中的子命令 startapp 创建应用文件夹
    2. 在settings.py 的 INSTALLED_APPS 列表中配置安装此应用

- 创建应用的子命令
    - python3 manage.py startapp 应用名称(必须是标识符命令规则)
    - 如:
        - python3 manage.py startapp music

- Django应用的结构组成
    1. `migrations` 文件夹
        - 保存数据迁移的中间文件
    2. `__init__.py`
        - 应用子包的初始化文件
    3. `admin.py`
        - 应用的后台管理配置文件
    4. `apps.py`
        - 应用的属性配置文件
    5. `models.py`
        - 与数据库相关的模型映射类文件
    6. `tests.py`
        - 应用的单元测试文件
    7. `views.py`
        - 定义视图处理函数的文件

- 配置安装应用
    - 在 settings.py 中配置应用, 让此应用能和整个项目融为一体
        ```python
        # file : settings.py 
        INSTALLED_APPS = [
            ... ...,
            '自定义应用名称'
        ]
        ```
    - 如:
        ```python
        INSTALLED_APPS = [
            # ....
            'user',  # 用户信息模块
            'music',  # 收藏模块
        ]
        ```

### 2.3.2. 应用的分布式路由
- Django中，基础路由配置文件(urls.py)可以不处理用户具体路由，基础路由配置文件的可以做请求的分发(分布式请求处理)。具体的请求可以由各自的应用来进行处理
- 如图:
    - ![](images/urls.png)

```python
# 交给 music 应用去处理(转交给music的urls)
from django.conf.urls import include
# url(r'^music/',include('music.urls')),
http://localhost:8000/music/****

# 交给 music 应用中的 index_views 视图去处理
http://localhost:8000/music/index

# 交给 sport 应用去处理(转交给sport的urls)
http://localhost:8000/sport/****
```

#### 2.3.2.1. include 函数
- 作用:
    - 用于分发将当前路由转到各个应用的路由配置文件的 urlpatterns 进行分布式处理
- 函数格式
    - include('app名字.url模块名')
    > 模块`app名字/url模块名.py` 文件件里必须有urlpatterns 列表
    > 使用前需要使用 `from django.conf.urls import include` 导入此函数


- 练习
    - 建立一个小网站:
        - 输入网址: http://127.0.0.1:8000, 在网页中输出 : 这是我的首页
        - 输入网址: http://127.0.0.1:8000/page1, 在网页中输出 : 这是编号为1的网页
        - 输入网址: http://127.0.0.1:8000/page2, 在网页中输出 : 这是编号为2的网页
        > 提示: 主页路由的正则是  `r'^$'`

        <font color="red">
        
        - 思考
            - /page3  /page4 .... /page100
            - 建立如上一百个网页该怎么办？
        
        </font>


- 练习：
    - 定义一个路由的格式为:
        - http://127.0.0.1:8000/整数/操作字符串/整数

    - 从路由中提取数据，做相应的操作后返回给浏览器
    - 如：
    ```
    输入: 127.0.0.1:8000/100/add/200
        页面显示  结果：300
    输入: 127.0.0.1:8000/100/sub/200
        页面显示  结果：-100
    输入: 127.0.0.1:8000/100/mul/200
        页面显示  结果：20000
    ```

- 练习：
    - 访问地址:
        - http://127.0.0.1:8000/birthday/四位数字/一到两位数字/一到两位数字
        - http://127.0.0.1:8000/birthday/一到两位数字/一到两位数字/四位数字
    - 最终输出: 生日为: xxxx年xx月xx日
    - 如:
        输入网址: http://127.0.0.1:8000/birthday/2015/12/11
        显示为: 生日为:2015年12月11日
        输入网址: http://127.0.0.1:8000/birthday/2/28/2008
        显示为: 生日为:2008年2月28日


- 练习：分布式路由
    * 1.访问路径 localhost:8000/news/index
        * 转交给 news 的urls 再找到index_views处理
    * 2.访问路径 localhost:8000/sport/index
        * 转交给 sport 的urls 再找到index_views处理
    * 3.访问路径 localhost:8000/index/index
        * 转交给 index 的urls 再找到index_views处理

    * 需求:
        * 1.访问路径
            * http://localhost:8000/music/
            * 交给 music 应用中的 index_views 视图去处理
            * url(r'^$',index_views)
        * 2.访问路径
            * http://localhost:8000/music/index
            * 交给 music 应用中的 index_views 视图去处理
            * http://localhost:8000/music/show
            * 交给 music 应用中的 show_views 视图去处理

        * news 应用:
        * 1. http://localhost:8000/news/
            * 交给 news 应用中的 index_views 视图去处理

        * 需求
            * 1.http://localhost:8000/
                * 交给 index 应用中的 index_views 视图去处理
            * 2.http://localhost:8000/login
                * 交给 index 应用中的 login_views 视图去处理
            * 3.http://localhost:8000/register
                * 交给 index 应用中的 register_views 视图去处理

            * 只要访问路径不是 music , news , sport 的话, 一律都交给 index 应用去处理

## 2.5. 一个实例搞懂所有路由

**step01: 创建项目和应用**  

创建项目和应用  
```shell
django-admin startproject mywebsite1
cd mywebsite1
python manage.py startapp music
```

设置语言和时区  
[mywebsite1/settings.py]()
```python
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
```


**step02: 修改主路由**  

[mywebsite1/urls.py]()
```python
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 定义路由
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^page1/$', views.page1),
    url(r'^page2/$', views.page2),

    # 元组传参，按位置传参
    url(r'^year/(\d{4})$', views.page_year),
    url(r'^date/(\d{4})/(\d+)/(\d+)$', views.date),
    url(r'^birthday/(\d{4})/(\d{1,2})/(\d{1,2})$', views.birthday),

    # 字典传参，按关键词传参
    url(r'^students1/$', views.students, {'name': 'shibw', 'age': '20'}),
    url(r'^students2/(?P<name>\w+)/(?P<age>\d{1,2})$', views.students),
    url(r'^goods/(?P<id>\d+)$', views.goods),

    # 应用，分布式路由
    url(r'^music/', include('music.urls')),
]
```


[mywebsite1/views.py]()
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse(request.is_ajax())

def page1(request):
    return HttpResponse(request.path)

def page2(request):
    return HttpResponse('这是第二个页面')

#接收参数并显示到页面
def page_year(request,year):
    #year对应正则表达式的第一个分组() 2015
    return HttpResponse('当前的年份：' + year)

#接收多个参数
def date(request,year,month,day):
    return HttpResponse(year+'年'+month+'月'+day+'日')

def birthday(request,year,month,day):
    return HttpResponse('生日为：'+year+'年'+month+'月'+day+'日')

def students(request,name,age):
    return HttpResponse('学生姓名：'+name+' 年龄:'+age)

def goods(request,id):
    return HttpResponse('当前查看的是id为'+id+'的商品')
```


**step03: 应用的路由配置**  
新建定义“应用”的分路由配置  
[music/url.py]()
```python
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$',views.index)
]
```

[music/view.py]()
```python
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('这是Music的首页')
```
