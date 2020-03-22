# WEB框架

## Django: Python Web应用开发框架

Django是一个开放源代码的Web应用框架，由Python写成。采用了MVC的软件设计模式，即模型M，视图V和控制器C。

它最初是被开发来用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站的，即是CMS（内容管理系统）软件。并于2005年7月在BSD许可证下发布。这套框架是以比利时的吉普赛爵士吉他手Django Reinhardt来命名的。

Django 应该是最出名的Python框架，GAE甚至Erlang都有框架受它影响。Django是走大而全的方向，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台。

Django提供的方便，也意味着Django内置的ORM跟框架内的其他模块耦合程度高。应用程序必须使用Django内置的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利；理论上可以切换掉其ORM模块，但这就相当于要把装修完毕的房子拆除重新装修，倒不如一开始就去毛胚房做全新的装修。Django的卖点是超高的开发效率，其性能扩展有限；采用Django的项目，在流量达到一定规模后，都需要对其进行重构，才能满足性能的要求。

## Flask：一个用Python编写的轻量级Web应用框架

Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2 模板引擎。 Flask使用BSD授权。 Flask也被称为“microframework”，因为它使用简单的核心，用extension增加其他功能。
Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术。   Flask 很有趣

配置简单
特性
1. 内置开发用服务器和debugger
2. 集成单元测试（unit testing）
3. RESTful request dispatching
4. 使用Jinja2模板引擎
5. 支持secure cookies（client side sessions）
6. 100% WSGI 1.0兼容
7. Unicode based
8. 详细的文件、教学
9. Google App Engine兼容
10. 可用Extensions增加其他功能

## Tornado：异步非阻塞IO的Python Web框架

Tornado的全称是Torado Web Server，从名字上看就可知道它可以用作Web服务器，但同时它也是一个Python Web的开发框架。最初是在FriendFeed公司的网站上使用，FaceBook收购了之后便开源了出来。

作为Web框架，是一个轻量级的Web框架，类似于另一个Python web 框架Web.py，其拥有异步非阻塞IO的处理方式。

作为Web服务器，Tornado有较为出色的抗负载能力，官方用nginx反向代理的方式部署Tornado和其它Python web应用框架进行对比，结果最大浏览量超过第二名近40%。

此外，它的源代码也是Python开发者学习与研究的绝佳材料。

以下是Tornado的Hello World示例程序。


## Web2py：全栈式Web框架

Web2py是一个为Python语言提供的全功能Web应用框架，旨在敏捷快速的开发Web应用，具有快速、安全以及可移植的数据库驱动的应用，兼容Google App Engine。  Web2py目录结构

## Bottle: 微型Python Web框架

Bottle是一个简单高效的遵循WSGI的微型python Web框架。说微型，是因为它只有一个文件，除Python标准库外，它不依赖于任何第三方模块。  特性
1. Routing：把请求映射到函数，建立简洁动态的URLs
2. Templates：采用内置模板引擎，同时还支持 mako, jinja2, cheetah 等第三方模板
3. Utilities：便捷地读取表单数据、上传文件、 cookies、HTTP头信息和其它 HTTP相关的元数据
4. Server：内置HTTP开发服务器，并且支持 paste, fapws3, bjoern, Google App Engine, Cherrypy 或者其它任何WSGI HTTP 服务器
示例

运行上面的代码，访问http://localhost:8080/hello/bottle试试。  下载和安装
通过

或者

安装最新稳定版，或者下载bottle.py (不稳定)到你的工程目录。Bottle运行于Python 2.5+ and 3.x环境下。

## webpy: 轻量级的Python Web框架

webpy的设计理念力求精简（Keep it simple and powerful），源码很简短，只提供一个框架所必须的东西，不依赖大量的第三方模块，它没有URL路由、没有模板也没有数据库的访问。这样的优点是，
框架给开发带来的限制少，可以根据自己的需求进行定制。缺点就是，很多东西都需要自己亲自动手开发。
虽然webpy的作者Aaron H.Swartz，一位伟大的程序员在2013年1月11日自杀身亡，结束了短暂的26年生命。但是，作为一个开源项目，目前还是有很多开发者在持续更新。
webpy非常的简单，语法几乎跟Python一样，以下是一个简单的示例：




# 后端构建
## Falcon：构建云API和网络应用后端的高性能Python框架

Falcon是一个构建云API的高性能Python框架，它鼓励使用REST架构风格，尽可能以最少的力气做最多的事情。  特性
1. 通过URI模板和资源类的路由
2. 通过请求和响应类访问headers和bodies
3. 通过异常基类响应HTTP错误等等  基准测试


## Zerorpc：基于ZeroMQ的高性能分布式RPC框架

Zerorpc是一个基于ZeroMQ和MessagePack开发的远程过程调用协议（RPC）实现。和 Zerorpc 一起使用的 Service API 被称为 zeroservice。Zerorpc 可以通过编程或命令行方式调用。

它允许你：
1. 不用修改代码即可显露python模块
2. 通过命令行远程调用这些模块
如何把你代码中的对象暴露为一个zeroservice？

运行以上代码，在另一个终端，尝试连接这个zeroservice


# 网络编程与多进程
## Diesel：基于Greenlet的事件I/O框架

Diesel提供一个整洁的API来编写网络客户端和服务器。支持TCP和UDP。
你应该使用diesel来编写你的下一个网络应用。得益于Python使得diesel语法非常整洁，发展步伐非常迅速。非阻塞I/O使得diesel非常快速并且容易扩展。greenlets使得diesel有了unwind（to(callbacks(no)))。
nose使得测试变得容易。最后，Flask使得你不需要写一个新的网络框架来使用diesel。 

## Pulsar：Python的事件驱动并发框架

Pulsar是一个事件驱动的并发框架，有了pulsar，你可以写出在不同进程或线程中运行一个或多个活动的异步服务器。  应用
附带以下功能
1. Socket服务器
2. WSGI服务器
3. JSON-RPC
4. Web Sockets
5. 任务队列
6. Shell
7. 测试包
8. django集成  示例

# OLAP框架
## Cubes：轻量级Python OLAP框架
Cubes是一个轻量级Python框架，包含OLAP、多维数据分析和浏览聚合数据（aggregated data）等工具
Cubes的主要特性之一是它的逻辑模型，抽象物理数据并提供给终端用户层。


# 网络爬虫框架
## Scrapy：Python的爬虫框架

网络爬虫，是在网上进行数据抓取的程序，使用它能够抓取特定网页的HTML数据。虽然我们利用一些库开发一个爬虫程序，但是使用框架可以大大提高效率，缩短开发时间。Scrapy是一个使用Python编写的，
轻量级的，简单轻巧，并且使用起来非常的方便。
Scrapy使用了Twisted异步网络库来处理网络通讯。整体架构大致如下（注：图片来自互联网）：


Scrapy主要包括了以下组件：
1. 引擎，用来处理整个系统的数据流处理，触发事务。
2. 调度器，用来接受引擎发过来的请求，压入队列中，并在引擎再次请求的时候返回。
3. 下载器，用于下载网页内容，并将网页内容返回给蜘蛛。
4. 蜘蛛，蜘蛛是主要干活的，用它来制订特定域名或网页的解析规则。
5. 项目管道，负责处理有蜘蛛从网页中抽取的项目，他的主要任务是清晰、验证和存储数据。当页面被蜘蛛解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
6. 下载器中间件，位于Scrapy引擎和下载器之间的钩子框架，主要是处理Scrapy引擎与下载器之间的请求及响应。
7. 蜘蛛中间件，介于Scrapy引擎和蜘蛛之间的钩子框架，主要工作是处理蜘蛛的响应输入和请求输出。
8. 调度中间件，介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。

使用Scrapy可以很方便的完成网上数据的采集工作，它为我们完成了大量的工作，而不需要自己费大力气去开发。


# 绘图框架
## Kartograph.py：创造矢量地图的轻量级Python框架

Kartograph是一个Python库，用来为ESRI生成SVG地图。Kartograph.py目前仍处于beta阶段，你可以在virtualenv环境下来测试。


# 分布式计算
## Dpark：Python版的Spark


DPark是一个基于Mesos的集群计算框架(cluster computing framework)，是Spark的Python实现版本，类似于MapReduce，但是比其更灵活，可以用Python非常方便地进行分布式计算，并且提供了更多的功能以便更好
的进行迭代式计算。DPark的计算模型是基于两个中心思想的：对分布式数据集的并行计算以及一些有限的可以在计算过程中、从不同机器访问的共享变量类型。这个的目标是为了提供一种类似于global address space
programming model的工具，例如OpenMP，但是我们要求共享变量的类型必须是那些很容易在分布式系统当中实现的，当前支持的共享变量类型有只读的数据和支持一种数据修改方式的累加器(accumulators)。
DPark具有的一个很重要的特性：分布式的数据集可以在多个不同的并行循环当中被重复利用。这个特性将其与其他数据流形式的框架例如Hadoop和Dryad区分开来。  示例
一个word counting程序


上面的脚本可以无修改的在Mesos集群上运行，只需稍微修改一下命令行参数：


# 自动化测试
## Buildbot：基于Python的持续集成测试框架

Buildbot是一个开源框架，可以自动化软件构建、测试和发布等过程。每当代码有改变，服务器要求不同平台上的客户端立即进行代码构建和测试，收集并报告不同平台的构建和测试结果。

## unittest

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.


unittest 和 JUnit类似，可以说是python的标准单元测试框架，所以有时也被人称为 PyUnit。它使用起来和xUnit 家族其他成员类似。 用的人也比较多。兼容 python2 以及python3 。


个人比较喜欢用这个，主要之前用过JUnit，用这个上手就很快。而且属于python自动集成，不用额外的安装包，感觉是该有的都有了，用着方便。

## unittest2
参考文档： https://pypi.python.org/pypi/unittest2

unittest2 is a backport of the new features added to the unittest testing framework in Python 2.7 and onwards.

unittest2 可以说是一个针对 unittest测试框架新特性的补丁。它很大程度上和unittest都类似。然后还添加了一些unittest没有的方法。

## pytest
参考文档：http://pytest.org/latest/

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

看了一下，pytest文档还是蛮详细的。比较关注的一点是，pytest 直接可以通过 @pytest.mark.parametrize 进行参数化，而unittest 则需要借助DDT。

## nose
参考文档： https://nose.readthedocs.org/en/latest/

基于Python的测试驱动开发实战 也有nose的用法： http://python.jobbole.com/81305/

nose extends unittest to make testing easier.

nose扩展了unittest，从而使得测试更容易。

一般可以用unittest方式写用例，写完之后用nose来执行。nose的测试收集方式还是很方便的。

 还有一个特定就是，nose可以采用  @with_setup() 来定义方法的setup和teardown。

##  doctest
参考文档：https://docs.python.org/3/library/doctest.html

Python 各种测试框架简介（一）：doctest  http://my.oschina.net/lionets/blog/268542

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown.

doctest模块会搜索那些看起来像交互式会话的 Python 代码片段，然后尝试执行并验证结果。

doctest 中，如果要写测试用例，只需要在写在以 ''' '''包围的文档注释即可，也就是可以被__doc__这个属性引用到的地方。这点比较特别，跟其他单元测试框架都不一样。但是我觉得这样的话就注定了doctest不适合大型测试，因为做不到代码和测试的分离。



# GUI 开发框架
## Kivy

https://www.oschina.net/p/kivy

Kivy是一个开源工具包能够让使用相同源代码创建的程序能跨平台运行。它主要关注创新型用户界面开发，如：多点触摸应用程序。Kivy还提供一个多点触摸鼠标模拟器。当前支持的平台包括：Linux、Windows、Mac OS X和Android。

Kivy拥有能够处理动画、缓存、手势、绘图等功能。它还内置许多用户界面控件如：按纽、摄影机、表格、Slider和树形控件等。

## Flexx

https://www.oschina.net/p/flexx

Flexx 是一个纯 Python 工具包，用来创建图形化界面应用程序。其使用 Web 技术进行界面的渲染。你可以用 Flexx 来创建桌面应用，同时也可以导出一个应用到独立的 HTML 文档。因为使用纯 Python 开发，所以 Flexx 是跨平台的。只需要有 Python 和浏览器就可以运行。如果是使用桌面模式运行，推荐使用 Firefox 。

## PyQt

https://www.oschina.net/p/pyqt

PyQt是Qt库的Python版本。PyQt3支持Qt1到Qt3。 PyQt4支持Qt4。它的首次发布也是在1998年，但是当时它叫 PyKDE，因为开始的时候SIP和PyQt没有分开。PyQt是用SIP写的。PyQt 提供 GPL版和商业版。

## wxPython

https://www.oschina.net/p/wxpython

wxPython 是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能键全的  GUI 用户界面。 wxPython 是作为优秀的跨平台 GUI 库 wxWidgets 的 Python 封装和 Python 模块的方式提供给用户的。

就如同Python和wxWidgets一样，wxPython也是一款开源软件，并且具有非常优秀的跨平台能力，能够运行在32位windows、绝大多数的Unix或类Unix系统、Macintosh OS X上。

## Tkinter

https://www.oschina.net/p/tkinter

Tkinter（也叫Tk接口）是Tk图形用户界面工具包标准的Python接口。Tk是一个轻量级的跨平台图形用户界面（GUI）开发工具。Tk和Tkinter可以运行在大多数的Unix平台、Windows、和Macintosh系统。

Tkinter 由一定数量的模块组成。Tkinter位于一个名为_tkinter（较早的版本名为tkinter）的二进制模块中 。Tkinter包含了对Tk的低 级接口模块，低级接口并不会被应用级程序员直接使用，通常是一个共享库（或DLL），但是在一些情况下它也被Python解释器静态链接。

## Pywin32

https://www.oschina.net/p/pywin32

Windows Pywin32允许你像VC一样的形式来使用PYTHON开发win32应用。代码风格可以类似win32 sdk，也可以类似MFC，由你选择。如果你仍不放弃vc一样的代码过程在python下，那么这就是一个不错的选择。

## PyGTK —— 图形界面开发包

https://www.oschina.net/p/pygtk

PyGTK让你用Python轻松创建具有图形用户界面的程序.底层的GTK+提供了各式的可视元素和功能,如果需要,你能开发在GNOME桌面系统运行的功能完整的软件.

PyGTK真正具有跨平台性,它能不加修改地,稳定运行各种操作系统之上,如Linux,Windows,MacOS等.除了简单易用和快速的原型开发能力外,PyGTK还有一流的处理本地化语言的独特功能.

## pyui4win —— 快速开发绚丽桌面程序

https://www.oschina.net/p/py-ui4win

pyui4win是一个开源的采用自绘技术的界面库。支持C++和python。用它可以很容易实现QQ和360安全卫士这样的绚丽界面。而且，pyui4win有所见即所得界面设计器，让C++开发人员和python开发人员直接用
设计工具设计界面，而不用关心界面如何生成和运行，可以显著缩短界面开发时间。在pyui4win中，界面甚至可以完全交给美工去处理，开发人员可以只负责处理业务逻辑，把开发人员彻底从繁杂的界面处理中解放出来。

