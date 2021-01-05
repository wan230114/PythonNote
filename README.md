<font face="楷体">

<h2>《Python学习之极简笔记——从零到催生AGI》</h2>

> 从Python入门到人工智能的专属知识图谱。包含了从Python基础到高阶使用，以及一些日常探索，只为让零碎知识逐渐整体化。  
> 一个开源的知识图谱，进步与分享必将让世界变得更为美好。让我们在踏实打下基础的同时，逐渐迈向创造通用型人工智能(AGI)。  
> A general knowledge map.  
> —— [陈军](https://github.com/wan230114)（1170101471@qq.com）、[邢鹏伟](https://github.com/pengweixing)（179464967@qq.com）
> 

</font>  

> <font font="等线" size="2">**网站主页：**   
> https://wan230114.github.io/PythonNote  
> https://wan230114.gitee.io/pythonnote   (备用)  
> http://118.89.194.65:8888   (备用网站实时镜像)  
>
> **项目主页：**   
> https://github.com/wan230114/PythonNote  
> https://gitee.com/wan230114/PythonNote  (备用)
>
> **食用方法：**  
> [>> PythonNote使用方法](/docs/Usage.md)</font>

<h3> 笔记总目录 </h3>

<!-- menu -->
* **Python基础部分**
    <!-- menu_base -->
    * [Introduction 前言](/docs/00.Python/Introduction.md)
    * [Chapter01.Python简介](/docs/00.Python/Chapter01.PythonReview.md)
    * [Chapter02.数值](/docs/00.Python/Chapter02.Value.md)
    * [Chapter03.数据容器](/docs/00.Python/Chapter03.DataContainers.md)
    * [Chapter04.流程控制](/docs/00.Python/Chapter04.ProcessControl.md)
    * [Chapter05.数据的遍历访问](/docs/00.Python/Chapter05.DataTraversal.md)
    * [Chapter06.函数function](/docs/00.Python/Chapter06.Function.md)
    * [Chapter07.错误及异常处理](/docs/00.Python/Chapter07.Exception.md)
    * [Chapter08.文件file及编码](/docs/00.Python/Chapter08.FileIO.md)
    * [Chapter09.面向对象](/docs/00.Python/Chapter09.Classes.md)
    * [Chapter10.模块和包](/docs/00.Python/Chapter10.Modules.md)
    * [附录](/docs/00.Python/ChapterN_Appendix.md)
    <!-- menu_base -->
* **Python进阶部分**
    * [Introduction 简介](/docs/00.Python_Advanced/Introduction.md)
    * [Chapter01.网络编程](/docs/00.Python_Advanced/Chapter01.PythonNet.md)
    * [Chapter02.多进程多线程](/docs/00.Python_Advanced/Chapter02.PythonThread.md)
    * [Django框架笔记](/docs/00.Python_Advanced/Django_note/django_all.md)
      * [Chapter01 概述与基本使用](/docs/00.Python_Advanced/Django_note/django01.md)
      * [Chapter02 请求和相应](/docs/00.Python_Advanced/Django_note/django02.md)
* **Python高级部分——数据分析**
    * [Introduction 简介](/docs/01.Datascience/Introduction.md)
    * [Chapter01 Numpy的多维矩阵批量操作方法](/docs/01.Datascience/Datascience_1numpy.md)
    * [Chapter02 Matplotlib绘图工具](/docs/01.Datascience/Datascience_2matplotlib.md)
    * [Chapter03 Pandas与数据分析](/docs/01.Datascience/Datascience_3pandas.md)
* **AI机器学习——入门**
    * [Introduction 简介](/docs/02.AI_ML/Introduction.md)
    * [所有笔记汇总 --> Note 教程](/docs/02.AI_ML/ML.md)
* **AI机器学习——算法进阶篇**
    * [Introduction 简介](/docs/03.AI_ML_机器学习算法集训营/Introduction.md)
    * ***阶段一***
      * [Chapter01 初识人工智能](/docs/03.AI_ML_机器学习算法集训营/Phase1/01_初识人工智能.md)
      * [Chapter02 第一个监督学习算法KNN](/docs/03.AI_ML_机器学习算法集训营/Phase1/02_第一个监督学习算法KNN.md)
* **AI机器学习——公式推导**
    * [Introduction 简介](/docs/01.Datascience/Introduction.md)
    <!-- * ***补充ing*** -->
* **其他笔记**
    * [Markdown 语法](/docs/Others/HTML/Markdown_HTML.md)
    * [HTML 语法](/docs/Others/HTML/HTML高级语法.md)
    * [Git笔记](/docs/Others/Git/Git_Note.md)
    * [docker笔记](/docs/Others/Virtual/docker.md)
    <!-- * [LeetCode](/docs/Others/Python_leetcode/Summary.md) -->
* **附**  
    * [Personal resume](/docs/Interview/me_bio.md)
<!-- menu -->

---

<h3> Python基础主页：</h3>
<br>
<br>


<!-- introduction -->
<h1><center><font color="#42a5f5" face="仿宋">《Python学习之极简笔记——基础部分》</font></center></h1>

<div align=right>
<font face="仿宋">—— 陈 军</br>1170101471@qq.com</font>
</div>
<font face="仿宋">

**当前版本：** v2.0.12

**更新日志：**
> 2019-12-17：v2.0.12【1,2,3】前三章部分语法的逻辑调整，使用实例整理  
> 2019-11-10：v2.0.11【1.6.3】第一章type/id/is的使用，1.5.1|1.6.3结构重排<br>
> 2019-10-23：v2.0.10【10.5.2.2】重新整理并新增os模块路径操作方法<br>
> 2019-10-13：v2.0.9【3.4.2 】集合创建错误示例增加，创建元素不能包含可变对象<br>
> 2019-10-11：v2.0.8【10.5.2 】os模块内容结构调整，增加subprocess示例<br>
> 2019-10-09：v2.0.7【第6章】函数进阶之装饰器示例6.7.4.4增加<br>
> 2019-10-05：v2.0.6【第10章】os模块使用的分类整理<br>
> 2019-09-17：v2.0.5【第10章】action:触发动作补充<br>
> 2019-09-11：v2.0.4【第5章 装饰器】增加一个打印函数运行时间的实例<br>
> 2019-09-09：v2.0.3【3.1.1.2格式化函数】关于字典值传入字符串的一些选择、【10.5.10 argparse参数模块】增加互斥传参方法<br>
> 2019-08-25：v2.0.2【3.4.5集合常用方法】返回值和描述纠错<br>
> 2019-08-18：v2.0.1【10.5.10 argparse解析参数】的标准框架更新<br>
> 2019-08-15：v2.0整体结构和排版优化，第4章与第5章顺序调整，第5章内容重构，三种可迭代对象的解读<br>
> ...<br>
> 2018-06-01：第一次撰写该文档<br>

---

<h2>导航：</h2>

* [写在前面](#写在前面)
* [目录大纲](#目录大纲)

</font>


---

# 写在前面

<center>（一）</center>

这是一个极速变革的枢纽时代，技术疯狂更迭，标准层出不穷，但我们的知识图谱却从未停滞，知识图谱在"熵增"的同时，也在不断"熵减"。这得益于其间千万为这个趋势不断付出的人们，ta们舍弃顶上秀发，用汗珠交织，让这指数增加的海量知识被封装的更有高度、更有序，感谢他们。无数人的努力让这一切复杂事物被逐渐封装为一个个成熟模块，借助于简洁的语法并逐渐走向平民，如今，我们可以很轻松的享受这成果。

这一切的变革，让我们的个体能力越来越强，辅助我们的工具不断迭代升级、日益强大，到有一天，这些工具又是否能强大到自我进化并具有独立思考的能力，我们不得而知。在这个紧要关口，我们十分有幸能驻于此，无法预知未来，但我们可以提前学习与机器交流的语言。科技是把双刃剑，但我们希望将它向好的方向控制，相信我们有能力努力规范和塑造这样的智能未来。

纵观人类的工具史发展，有一些很常见的规律，一切一开始复杂的东西都将会变得越来越简单，比如因为我们在前一代"工具"的基础上进行新一代"工具"的创造，让我们能得以模块化生产，比如机械制造，。而秉承简洁之力的一门编程语言————Python做到了，将大量无需人们关注的操作细节封入看不见的模块，用尽量少的代码量实现更强大的逻辑。这门独具风格的编程语言，随着2016年人机围棋大赛一战而红，它的醒目标语"Life is short, you need Python"伴随着它的开源技术分享、成熟框架风靡全球。这股浪潮让它已连续多次蝉联各类编程语言排行榜榜首，它已成为研究机器智能、神经网络等领域的不二法门。甚至在教育方面，某些中小学已将这门简洁的语言艺术列入课本，热度毋庸置疑。

Python，语言简洁，活跃社区，丰富的共享资料及库等优势，也许在下一门更强大的编程方式活跃之前，可以说，在下一场与计算机对话的方式革命到来之前，它能一直稳坐王位。

通过学习这门简洁的艺术语言，你将会逐渐感受到技术的变革，而不仅仅停留在一串名词的理解上。现在，我想从这门技术入手，带您感受这个时代的极速变迁。


<center> (二) </center>

一门技术的兴起，必然带动无数的副业。教育市场便是其中之一，关于这方面，得承认有了门槛确实能提升质量。但却以身边的经历来看，这些门槛又是否会太高？并且各类信息杂乱。这不禁让我陷入深思。

我愿意花费时间向世界及未来贡献我的一份微薄之力，方便大众用最低的时间成本系统高效的get到灵魂深处。我希望这部电子作品通过不断改进能成为您可以随时搜索查阅的电子版"新华字典"。

在智能时代到来前夕，数据操作技术已逐渐成为我们必不可少的一项本领。此刻，这样的技术学习教程已经泛滥，但我们需要一个系统简明的知识图谱，让它们更加系统亲民，这是本电子文档编辑的另一个初衷所在。

<center>（三）</center>

那么如何理解Python呢，编程又是什么？

简单描述，编程是一门精确记录和重现你做事方法的工具，它能帮助并解放你的记忆力、脑力、劳力，就像实际生产，通过一步步搭建自动化成熟的模块，最终可以铸造一个无人值守的高效工厂。而Python简洁清晰的语法将会成为这些上层设计的一把瑞士军刀。

接下来，让我们一起步入Python殿堂吧！

<div align=right>
<img width="35%" src="docs/00.Python/img/sin.png" alt="封面"/>
</div>

# 目录大纲

<!-- menu_write -->
* [Introduction 前言](/docs/00.Python/Introduction.md)
* [Chapter01.Python简介](/docs/00.Python/Chapter01.PythonReview.md)
* [Chapter02.数值](/docs/00.Python/Chapter02.Value.md)
* [Chapter03.数据容器](/docs/00.Python/Chapter03.DataContainers.md)
* [Chapter04.流程控制](/docs/00.Python/Chapter04.ProcessControl.md)
* [Chapter05.数据的遍历访问](/docs/00.Python/Chapter05.DataTraversal.md)
* [Chapter06.函数function](/docs/00.Python/Chapter06.Function.md)
* [Chapter07.错误及异常处理](/docs/00.Python/Chapter07.Exception.md)
* [Chapter08.文件file及编码](/docs/00.Python/Chapter08.FileIO.md)
* [Chapter09.面向对象](/docs/00.Python/Chapter09.Classes.md)
* [Chapter10.模块和包](/docs/00.Python/Chapter10.Modules.md)
* [附录](/docs/00.Python/ChapterN_Appendix.md)
<!-- menu_write -->

（文章笔记暂未完全转化，原始文档下载链接：https://1drv.ms/w/s!AofyZDsRK31B8m8uzCxonAKFeOEl?e=JWqhA2
）
<!-- introduction -->


---

<font face="仿宋">
以上为《Python学习之极简笔记——基础部分》主页。<br>
更多其他内容，如高级使用，数据分析，机器学习等，见各个子文件夹~
</font>
