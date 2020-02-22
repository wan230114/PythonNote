# 3. 请求和响应
## 3.1. HTTP协议的请求和响应
- 请求是指浏览器端通过HTTP协议发送给服务器端的数据
- 响应是指服务器端接收到请求后做相应的处理后再回复给浏览器端的数据

![请求和向应](images/request_response.png)

### 3.1.1. HTTP 请求
- 根据HTTP标准，HTTP请求可以使用多种请求方法。

- HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法(最常用)

- HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法。

- HTTP1.1 请求详述

| 序号 | 方法 | 描述 |
|:-:|:-:|:-|
| 1 | GET | 请求指定的页面信息，并返回实体主体。 |
| 2 | HEAD | 类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头 |
| 3 | POST | 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。 |
| 4 | PUT | 从客户端向服务器传送的数据取代指定的文档的内容。 |
| 5 | DELETE | 请求服务器删除指定的页面。 |
| 6 | CONNECT | HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。 |
| 7 | OPTIONS | 允许客户端查看服务器的性能。 |
| 8 | TRACE | 回显服务器收到的请求，主要用于测试或诊断。 |

### 3.1.2. 视图函数(view)
- 基本概念：视图函数是用于接收一个浏览器请求并通过HttpResponse对象返回数据的函数。此函数可以接收浏览器请求并根据业务逻辑返回相应的内容给浏览器
- 视图处理的函数的语法格式:
    ```python
    # file : <项目名>/views.py
    from django.http import HttpResponse
    def xxx_view(request[, 其它参数...]):
        return HttpResponse对象
    # 参数: 
    #   request用于绑定HttpRequest对象，
    #   通过此对象可以获取浏览器的参数和数据
    ```
- 示例:
    - 视图处理函数 `views.py`
        ```python
        # file : <项目名>/views.py
        from django.http import HttpResponse
        def page1_view(request):
            html = "<h1>这是第1个页面</h1>"
            return HttpResponse(html)
        ```

#### 3.1.2.1. HttpRequest对象
- 视图函数的第一个参数是HttpRequest对象
- 服务器接收到http协议的请求后，会根据请求数据报文创建HttpRequest对象
- HttpRequest属性
    - path：字符串，表示请求的路由信息
    - path_info: URL字符串
    - method：字符串，表示HTTP请求方法，常用值：'GET'、'POST'
    - encoding：字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为'utf-8'
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
    - GET：QueryDict查询字典的对象，包含get请求方式的所有数据
    - POST：QueryDict查询字典的对象，包含post请求方式的所有数据
    - FILES：类似于字典的对象，包含所有的上传文件信息
    - COOKIES：Python字典，包含所有的cookie，键和值都为字符串
    - session：似于字典的对象，表示当前的会话，
    - body: 字符串，请求体的内容(POST或PUT)
    - environ: 字符串,客户端运行的环境变量信息
    - scheme : 请求协议('http'/'https')
    - request.get_full_path() : 请求的完整路径
    - request.get_host() : 请求的主机
    - request.META : 请求中的元数据(消息头)
        - request.META['REMOTE_ADDR']  : 客户端IP地址


### 3.1.3. HTTP 响应
- 当浏览者访问一个网页时，浏览者的浏览器会向网页所在服务器发出请求。当浏览器接收并显示网页前，此网页所在的服务器会返回一个包含HTTP状态码的信息头用以响应浏览器的请求。
- HTTP状态码的英文为HTTP Status Code。
- 下面是常见的HTTP状态码：
    - 200 - 请求成功
    - 301 - 资源（网页等）被永久转移到其它URL
    - 404 - 请求的资源（网页等）不存在
    - 500 - 内部服务器错误

#### 3.1.3.1. HTTP状态码分类
HTTP状态码由三个十进制数字组成，第一个十进制数字定义了状态码的类型，后两个数字没有分类的作用。HTTP状态码共分为5种类型：

| 分类 | 分类描述 |
|:-:|-|
| 1** | 信息，服务器收到请求，需要请求者继续执行操作 |
| 2** | 成功，操作被成功接收并处理 |
| 3** | 重定向，需要进一步的操作以完成请求 |
| 4** | 客户端错误，请求包含语法错误或无法完成请求 |
| 5** | 服务器错误，服务器在处理请求的过程中发生了错误 |

### 3.1.4. Django中的响应对象HttpResponse:
- 构造函数格式:  
`HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)`
- 作用:   
向客户端浏览器返回响应，同时携带响应体内容
- 参数:  
    - content：表示返回的内容。
    - status_code：返回的HTTP响应状态码(默认为200)。
    - content_type：指定返回数据的的MIME类型(默认为"text/html")。浏览器会根据这个属性，来显示数据。如果是text/html，那么就会解析这个字符串，如果text/plain，那么就会显示一个纯文本。
        - 常用的Content-Type如下：
            - `'text/html'`（默认的，html文件）
            - `'text/plain'`（纯文本）
            - `'text/css'`（css文件）
            - `'text/javascript'`（js文件）
            - `'multipart/form-data'`（文件提交）
            - `'application/json'`（json传输）
            - `'application/xml'`（xml文件）  
        - 注： 关键字MIME(Multipurpose Internet Mail Extensions)是指多用途互联网邮件扩展类型。

#### 3.1.4.1. HttpResponse 子类

|          类型           |      作用      | 状态码 |
| ----------------------- | -------------- | ------ |
| HttpResponseRedirect    | 重定响         | 301    |
| HttpResponseNotModified | 未修改         | 304    |
| HttpResponseBadRequest  | 错误请求       | 400    |
| HttpResponseNotFound    | 没有对应的资源 | 404    |
| HttpResponseForbidden   | 请求被禁止     | 403    |
| HttpResponseServerError | 服务器错误     | 500    |

ps: 本小节练习见本章节末

### 3.1.5. GET方式传参
- GET请求方式中可以通过查询字符串(Query String)将数据传递给服务器    
- URL 格式: `xxx?参数名1=值1&参数名2=值2...`
    - 如: `http://127.0.0.1:8000/page1?a=100&b=200`
- 服务器端接收参数
    1. 判断 request.method 的值判断请求方式是否是get请求
        ```python
        if request.method == 'GET':
            处理GET请求时的业务逻辑
        else:
            处理其它请求的业务逻辑
        ```
    2. 获取客户端请求GET请求提交的数据
        1. 语法
            ```python
            request.GET['参数名']  # QueryDict
            request.GET.get('参数名','默认值')
            request.GET.getlist('参数名')
            # mypage?a=100&b=200&c=300&b=400
            # request.GET=QueryDict({'a':['100'], 'b':['200','400'], 'c':['300']})
            # a = request.GET['a']
            # b = request.GET['b']  # Error
            ```
        2. 能够产生get请求方式的场合
            1. 地址栏手动输入, 如: http://127.0.0.1:8000/mypage?a=100&b=200
            2. `<a href="地址?参数=值&参数=值">`
            3. form表单中的method为get
                ```html
                <form method='get' action="/user/login">
                    姓名:<input type="text" name="uname">
                </form>
                ```
> 一般查询字符串的大小会受到浏览器的的限制(不建议超过2048字节)


### 3.1.6. POST传递参数

- 客户端通过表单等POST请求将数据传递给服务器端,如:
    <form method='post' action="/login">
        姓名:<input type="text" name="username">
        <input type='submit' value='登陆'>
    </form>

    ```html
    <form method='post' action="/login">
        姓名:<input type="text" name="username">
        <input type='submit' value='登陆'>
    </form>
    ```

- 服务器端接收参数

  - 通过 request.method 来判断是否为POST请求,如:

  ```python
  if request.method == 'POST':
      处理POST请求的数据并响应
  else:
      处理非POST 请求的响应
  ```

- 使用post方式接收客户端数据

  1. 方法

  ```python
  request.POST['参数名']  # request.POST 绑定QueryDict
  request.POST.get('参数名','')
  request.POST.getlist('参数名')
  ```

- 取消csrf验证,否则Django将会拒绝客户端发来的POST请求

  - 取消 csrf 验证

    - 删除 settings.py 中 MIDDLEWARE 中的 CsrfViewsMiddleWare 的中间件

    ```python
    MIDDLEWARE = [
        ...
        # 'django.middleware.csrf.CsrfViewMiddleware',
        ...
    ]
    ```

### 3.1.7. form 表单的name属性

- 在form表单控件提交数据时，会自动搜索本表单控件内部的子标签的name属性及相应的值，再将这些名字和值以键-值对的形式提交给action指定的服务器相关位置

- 在form内能自动搜集到的name属性的标签的控件有

  ```html
  <input name='xxx'>
  <select name='yyy'></select>
  <textarea name='zzz'></textarea>
  ```

  - 如:
  - 
  <form action="/page1" method="POST">
      <input name="title" type="text" value="请输入">
      <select name="gender">
          <option value=1>男</option>
          <option value=0>女</option>
      </select>
      <textarea name="comment" rows="5" cols="10">附言...</textarea>
      <input type="submit" value="提交">
  </form>

  ```html
  <form action="/page1" method="POST">
      <input name="title" type="text" value="请输入">
      <select name="gender">
          <option value=1>男</option>
          <option value=0>女</option>
      </select>
      <textarea name="comment" rows="5" cols="10">附言...</textarea>
      <input type="submit" value="提交">
  </form>
  ```

## 3.2. 练习
- 练习1:
    - 访问地址: <http://127.0.0.1:8000/sum?start=整数&stop=整数&step整=字>
    - 输出结果为sum(range(start, step, stop)) 和:
    - 如:
        - 输入网址: http://127.0.0.1:8000/sum?start=1&stop=101&step=1
        - 页面显示: 结果: 5050
        - 输入网址: http://127.0.0.1:8000/sum?stop=101&step=2
        - 页面显示: 结果: 2550
        - 输入网址: http://127.0.0.1:8000/sum?start=1&stop=101&step=2
        - 页面显示: 结果: 2500

- 练习2:
    - 访问地址: <http://127.0.0.1:8000/birthday?year=四位整数&month=整数&day=整数>
    - 最终输出: 生日为: xxxx年xx月xx日
    - 如:
        - 输入网址: http://127.0.0.1:8000/birthday?year=2015&month=12&day=11
        - 显示为: 生日为:2015年12月11日

- 练习3：
    - 写一个简单的计算器页面，能够在服务端进行简单加减乘除计算

    - form中的action属性 ->  此次提交的地址

    - ex: `action='/mycal'` -> 提交地址为当前浏览器地址栏的ip+端口+ action, 即 http://127.0.0.1:8000/mycal

    - 示例：
        <form action='/mycal' method='POST'>
            <input type='text' name="x" value="1">
            <select>
                <option value="add"> +加 </option>
                <option value="sub"> -减 </option>
                <option value="mul"> *乘 </option>
                <option value="div"> /除 </option>
            </select>
            <input type='text' name="y" value="2"> = <span>3</span>
            <div>
                <input type="submit" value='开始计算'>
            <div>
        </form>

    - 参考代码
        ```html
        <form action='/mycal' method='POST'>
            <input type='text' name="x" value="1">
            <select name='op'>
                <option value="add" > +加 </option>
                <option value="sub" > -减 </option>
                <option value="mul" > *乘 </option>
                <option value="div" > /除 </option>
            </select>
            <input type='text' name="y" value="2"> = <span>3</span>
            <div>
                <input type="submit" value='开始计算'>
            <div>
        </form>
        ```
