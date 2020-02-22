# Markdown及HTML常用命令

@[toc]

标签（空格分隔）： JUN-code

---


# 1. 常用代码
```
空格：
    &nbsp;
色彩：
    <font color=""></font>
链接跳转：
    页内：
    跳转链接：[内容](#jump)
    跳转锚点：<span id="jump"></span>
插入：
    目录：[TOC]
超链接：
    文字超链接：[不如](http://bruce-sha.github.io "不如的博客")
    图片超链接(markdown中)：![GitHub Mark](http://**** "GitHub Mark")
    图片超链接：<img src="http://****" width="128" height="96" />
    网址超链接：<http://ibruce.info>
```

# 2. 文字
## 2.1. 基本
```
*我是斜体*  
**我是粗体**  
~~我是删除线~~

- 我是序号（无编号）  
  - 我是二级序号（无编号）
    - 我是三级序号（无编号）

1. 我是序号（有编号）  
   1. 我是二级序号（有编号）
      1. 我是三级序号（有编号）

> 我是段落引用1  
> 我是段落引用2  
```

*我是斜体*  
**我是粗体**  
~~我是删除线~~

- 我是序号（无编号）  
  - 我是二级序号（无编号）
    - 我是三级序号（无编号）

1. 我是序号（有编号）  
   1. 我是二级序号（有编号）
      1. 我是三级序号（有编号）

> 我是段落引用1  
> 我是段落引用2  

## 2.2. 色彩

```
<font color="#00ff00">测试文本内容</font>
```
<font color="#00ff00">测试文本内容</font>


```
<font face="仿宋" color="red" size="3">测试文本（仿宋字体，红色，3号大小）</font>
```

<font face="仿宋" color="red" size="3">测试文本（仿宋字体，红色，3号大小）</font>

## 2.3. 特殊字符
| <描述> | <语法>   |
| ------ | -------- |
| 空格   | `&nbsp;` |
| 换行符 | `<br>`   |

## 2.4. 常用html标签语法
```
<h3>测试文本：三级标题</h3>
```
<h3>测试文本：三级标题</h3>


# 3. 图片样式定义
## 3.1. html语法

数值定义大小：
```
<img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" width="128" height="96" />
```
<img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" width="128" height="96" />

百分比定义图片大小：
```
<img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" width="20%" height="60" />
```
<img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" width="20%" height="60" />

居中：
```
<div align=center>
<img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" />
</div>
```
<div align=center>
<img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" />
</div>

## 3.2. markdown语法
```
![](http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg)
```
![](http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg)


# 4. 表格
## 4.1. html表格

```html
<table>
    <tr>
        <td>1</td>    <td>2</td>    <td>3</td>   
    </tr>
    <tr>
        <td>4</td>    <td>5</td>    <td>6</td>   
    </tr>
</table>
```
<table>
    <tr>
        <td>1</td>    <td>2</td>    <td>3</td>   
    </tr>
    <tr>
        <td>4</td>    <td>5</td>    <td>6</td>   
    </tr>
</table>


## 4.2. markdown表格

```html
| 1   | 2          |      3      |          4 |
| --- | :--------- | :---------: | ---------: |
| 1   | ---居左--- | ----居中--- | ---居右--- |
| 11  | 22         |     33      |         44 |
```

| 1   | 2          |      3      |          4 |
| --- | :--------- | :---------: | ---------: |
| 1   | ---居左--- | ----居中--- | ---居右--- |
| 11  | 22         |     33      |         44 |


# 5. 自定义渲染显示样式

## 5.1. markdown中的CSS标签定义

### 5.1.1. 标题栏样式定义

加粗：font-weight:bold;

```html
h1{
    color:#272727;
    background:#FF9224;
    font-family:黑体;
    font-size: 30px;
}
h2{
    color:#272727;
    background:#FFD306;
    font-family:黑体;
    font-size: 25px;
}
h3{
    color:#272727;
    background:#C2FF68;
    font-family:黑体;
    font-size: 20px;
}
h4{
    color:#272727;
    font-weight:bold;
    font-family:黑体;
    font-size: 18px;
}
```

### 5.1.2. 递增序列

CSS代码：
```
ol {
   list-style-type:none;		
   counter-reset:sectioncounter;
}                      
ol li:before {
   content:"美女" counter(sectioncounter) "： "; 
   counter-increment:sectioncounter;
}
```
HTML代码：
```
<ol>
    <li><img src="http://image.zhangxinxu.com/image/study/s/s128/mm1.jpg" width="128" height="96" /></li>
    <li><img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" width="128" height="96" /></li>
</ol>
```
<ol>
    <li><img src="http://image.zhangxinxu.com/image/study/s/s128/mm1.jpg" width="128" height="96" /></li>
    <li><img src="http://image.zhangxinxu.com/image/study/s/s128/mm3.jpg" width="128" height="96" /></li>
</ol>

## 5.2. 多级标题

```
HTML代码如下：

<ol>  
  <li>列表项  
    <ol>  
      <li>列表项  
        <ol>  
          <li>列表项</li>  
          <li>列表项</li>  
          <li>列表项</li>  
        </ol>  
      </li>  
    </ol>  
  </li>  
</ol>
```

```
ol {padding:0 0 0 20px; margin:0; list-style:none; counter-reset:a;}  
li:before {counter-increment:a; content:counters(a,".")". ";}
```
    <head> 
    <style type="text/css"> 
    h1{color:red} 
    p{color:blue} 
    </style> 
    <head> 
    <style type=”text/css”>P{ color:red }</style>
    ol {list-style-type:none;		
       counter-reset:sectioncounter;}                      
    ol li:before {content:"美女" counter(sectioncounter) "： "; 
       counter-increment:sectioncounter;
    }
    <h1><ol><li>这是一个标题。</li></ol></h1>
    <h2>这是一个标题。</h2>
    <h3>这是一个标题。</h3>

### 5.2.1. CSS标题标签自定义

```
ol {
    /* 开始计数 */
  counter-reset: section;                
  list-style-type: none;
}

li::before {
  counter-increment: section;           
  content: counters(section,".") " ";  
}

ol{
    list-style: none;
    counter-reset: ordered;
}
li:before{
    counter-increment: ordered;
    content: counters(ordered,".")" ";
}
```
```
h1{
    color:#272727;    background:#FF9224;    font-family:黑体;    font-size: 30px;
    counter-reset: ordered;
}
h2{
    color:#272727;    background:#00BB00;    font-family:黑体;    font-size: 25px;
}
h3{
    color:#272727;    background:#C2FF68;    font-family:黑体;    font-size: 20px;
}
h4{
    color:#272727;    font-weight:bold;    font-family:黑体;    font-size: 18px;
}
h1:before{ 
    counter-increment: ordered;   content: counter(chapter)" ";
}
h2:before{
    counter-increment: section;    content: counter(chapter)"."counter(section)" ";
}
h3:before{
    counter-increment: subsec;    content: counter(chapter)"."counter(section)"."counter(subsec)".";
}
```
## 5.3. 其他

### 5.3.1. 框架模板
- bootstrap ace admin HTML5 全新高大尚后台框架_HTML/CSS_第七城市
<http://www.th7.cn/web/html-css/201501/75159.shtml>


# 6. 附：常用色彩代码
 - HTML 颜色 | 菜鸟教程
http://www.runoob.com/html/html-colors.html
```Python
代码格式：d
<td><font color="#000000">文本内容</font></td>
```
<table>
<tr>
<td><font color="#000000">███#000000</font></td>
<td><font color="#2F0000">███#2F0000</font></td>
<td><font color="#600030">███#600030</font></td>
<td><font color="#460046">███#460046</font></td>
<td><font color="#28004D">███#28004D</font></td>
</tr><tr>
<td><font color="#272727">███#272727</font></td>
<td><font color="#4D0000">███#4D0000</font></td>
<td><font color="#820041">███#820041</font></td>
<td><font color="#5E005E">███#5E005E</font></td>
<td><font color="#3A006F">███#3A006F</font></td>
</tr><tr>
<td><font color="#3C3C3C">███#3C3C3C</font></td>
<td><font color="#600000">███#600000</font></td>
<td><font color="#9F0050">███#9F0050</font></td>
<td><font color="#750075">███#750075</font></td>
<td><font color="#4B0091">███#4B0091</font></td>
</tr><tr>
<td><font color="#4F4F4F">███#4F4F4F</font></td>
<td><font color="#750000">███#750000</font></td>
<td><font color="#BF0060">███#BF0060</font></td>
<td><font color="#930093">███#930093</font></td>
<td><font color="#5B00AE">███#5B00AE</font></td>
</tr><tr>
<td><font color="#5B5B5B">███#5B5B5B</font></td>
<td><font color="#930000">███#930000</font></td>
<td><font color="#D9006C">███#D9006C</font></td>
<td><font color="#AE00AE">███#AE00AE</font></td>
<td><font color="#6F00D2">███#6F00D2</font></td>
</tr><tr>
<td><font color="#6C6C6C">███#6C6C6C</font></td>
<td><font color="#AE0000">███#AE0000</font></td>
<td><font color="#F00078">███#F00078</font></td>
<td><font color="#D200D2">███#D200D2</font></td>
<td><font color="#8600FF">███#8600FF</font></td>
</tr><tr>
<td><font color="#7B7B7B">███#7B7B7B</font></td>
<td><font color="#CE0000">███#CE0000</font></td>
<td><font color="#FF0080">███#FF0080</font></td>
<td><font color="#E800E8">███#E800E8</font></td>
<td><font color="#921AFF">███#921AFF</font></td>
</tr><tr>
<td><font color="#8E8E8E">███#8E8E8E</font></td>
<td><font color="#EA0000">███#EA0000</font></td>
<td><font color="#FF359A">███#FF359A</font></td>
<td><font color="#FF00FF">███#FF00FF</font></td>
<td><font color="#9F35FF">███#9F35FF</font></td>
</tr><tr>
<td><font color="#9D9D9D">███#9D9D9D</font></td>
<td><font color="#FF0000">███#FF0000</font></td>
<td><font color="#FF60AF">███#FF60AF</font></td>
<td><font color="#FF44FF">███#FF44FF</font></td>
<td><font color="#B15BFF">███#B15BFF</font></td>
</tr><tr>
<td><font color="#ADADAD">███#ADADAD</font></td>
<td><font color="#FF2D2D">███#FF2D2D</font></td>
<td><font color="#FF79BC">███#FF79BC</font></td>
<td><font color="#FF77FF">███#FF77FF</font></td>
<td><font color="#BE77FF">███#BE77FF</font></td>
</tr><tr>
<td><font color="#BEBEBE">███#BEBEBE</font></td>
<td><font color="#FF5151">███#FF5151</font></td>
<td><font color="#FF95CA">███#FF95CA</font></td>
<td><font color="#FF8EFF">███#FF8EFF</font></td>
<td><font color="#CA8EFF">███#CA8EFF</font></td>
</tr><tr>
<td><font color="#d0d0d0">███#d0d0d0</font></td>
<td><font color="#ff7575">███#ff7575</font></td>
<td><font color="#ffaad5">███#ffaad5</font></td>
<td><font color="#ffa6ff">███#ffa6ff</font></td>
<td><font color="#d3a4ff">███#d3a4ff</font></td>
</tr><tr>
<td><font color="#E0E0E0">███#E0E0E0</font></td>
<td><font color="#FF9797">███#FF9797</font></td>
<td><font color="#FFC1E0">███#FFC1E0</font></td>
<td><font color="#FFBFFF">███#FFBFFF</font></td>
<td><font color="#DCB5FF">███#DCB5FF</font></td>
</tr><tr>
<td><font color="#F0F0F0">███#F0F0F0</font></td>
<td><font color="#FFB5B5">███#FFB5B5</font></td>
<td><font color="#FFD9EC">███#FFD9EC</font></td>
<td><font color="#FFD0FF">███#FFD0FF</font></td>
<td><font color="#E6CAFF">███#E6CAFF</font></td>
</tr><tr>
<td><font color="#FCFCFC">███#FCFCFC</font></td>
<td><font color="#FFD2D2">███#FFD2D2</font></td>
<td><font color="#FFECF5">███#FFECF5</font></td>
<td><font color="#FFE6FF">███#FFE6FF</font></td>
<td><font color="#F1E1FF">███#F1E1FF</font></td>
</tr><tr>
<td><font color="#FFFFFF">███#FFFFFF</font></td>
<td><font color="#FFECEC">███#FFECEC</font></td>
<td><font color="#FFF7FB">███#FFF7FB</font></td>
<td><font color="#FFF7FF">███#FFF7FF</font></td>
<td><font color="#FAF4FF">███#FAF4FF</font></td>
</tr><tr>
<td><font color="#000079">███#000079</font></td>
<td><font color="#000079">███#000079</font></td>
<td><font color="#003E3E">███#003E3E</font></td>
<td><font color="#006030">███#006030</font></td>
<td><font color="#006000">███#006000</font></td>
</tr><tr>
<td><font color="#000093">███#000093</font></td>
<td><font color="#003D79">███#003D79</font></td>
<td><font color="#005757">███#005757</font></td>
<td><font color="#01814A">███#01814A</font></td>
<td><font color="#007500">███#007500</font></td>
</tr><tr>
<td><font color="#0000C6">███#0000C6</font></td>
<td><font color="#004B97">███#004B97</font></td>
<td><font color="#007979">███#007979</font></td>
<td><font color="#019858">███#019858</font></td>
<td><font color="#009100">███#009100</font></td>
</tr><tr>
<td><font color="#0000C6">███#0000C6</font></td>
<td><font color="#005AB5">███#005AB5</font></td>
<td><font color="#009393">███#009393</font></td>
<td><font color="#01B468">███#01B468</font></td>
<td><font color="#00A600">███#00A600</font></td>
</tr><tr>
<td><font color="#0000E3">███#0000E3</font></td>
<td><font color="#0066CC">███#0066CC</font></td>
<td><font color="#00AEAE">███#00AEAE</font></td>
<td><font color="#02C874">███#02C874</font></td>
<td><font color="#00BB00">███#00BB00</font></td>
</tr><tr>
<td><font color="#2828FF">███#2828FF</font></td>
<td><font color="#0072E3">███#0072E3</font></td>
<td><font color="#00CACA">███#00CACA</font></td>
<td><font color="#02DF82">███#02DF82</font></td>
<td><font color="#00DB00">███#00DB00</font></td>
</tr><tr>
<td><font color="#4A4AFF">███#4A4AFF</font></td>
<td><font color="#0080FF">███#0080FF</font></td>
<td><font color="#00E3E3">███#00E3E3</font></td>
<td><font color="#02F78E">███#02F78E</font></td>
<td><font color="#00EC00">███#00EC00</font></td>
</tr><tr>
<td><font color="#6A6AFF">███#6A6AFF</font></td>
<td><font color="#2894FF">███#2894FF</font></td>
<td><font color="#00FFFF">███#00FFFF</font></td>
<td><font color="#1AFD9C">███#1AFD9C</font></td>
<td><font color="#28FF28">███#28FF28</font></td>
</tr><tr>
<td><font color="#7D7DFF">███#7D7DFF</font></td>
<td><font color="#46A3FF">███#46A3FF</font></td>
<td><font color="#4DFFFF">███#4DFFFF</font></td>
<td><font color="#4EFEB3">███#4EFEB3</font></td>
<td><font color="#53FF53">███#53FF53</font></td>
</tr><tr>
<td><font color="#9393FF">███#9393FF</font></td>
<td><font color="#66B3FF">███#66B3FF</font></td>
<td><font color="#80FFFF">███#80FFFF</font></td>
<td><font color="#7AFEC6">███#7AFEC6</font></td>
<td><font color="#79FF79">███#79FF79</font></td>
</tr><tr>
<td><font color="#AAAAFF">███#AAAAFF</font></td>
<td><font color="#84C1FF">███#84C1FF</font></td>
<td><font color="#A6FFFF">███#A6FFFF</font></td>
<td><font color="#96FED1">███#96FED1</font></td>
<td><font color="#93FF93">███#93FF93</font></td>
</tr><tr>
<td><font color="#B9B9FF">███#B9B9FF</font></td>
<td><font color="#97CBFF">███#97CBFF</font></td>
<td><font color="#BBFFFF">███#BBFFFF</font></td>
<td><font color="#ADFEDC">███#ADFEDC</font></td>
<td><font color="#A6FFA6">███#A6FFA6</font></td>
</tr><tr>
<td><font color="#CECEFF">███#CECEFF</font></td>
<td><font color="#ACD6FF">███#ACD6FF</font></td>
<td><font color="#CAFFFF">███#CAFFFF</font></td>
<td><font color="#C1FFE4">███#C1FFE4</font></td>
<td><font color="#BBFFBB">███#BBFFBB</font></td>
</tr><tr>
<td><font color="#DDDDFF">███#DDDDFF</font></td>
<td><font color="#C4E1FF">███#C4E1FF</font></td>
<td><font color="#D9FFFF">███#D9FFFF</font></td>
<td><font color="#D7FFEE">███#D7FFEE</font></td>
<td><font color="#CEFFCE">███#CEFFCE</font></td>
</tr><tr>
<td><font color="#ECECFF">███#ECECFF</font></td>
<td><font color="#D2E9FF">███#D2E9FF</font></td>
<td><font color="#ECFFFF">███#ECFFFF</font></td>
<td><font color="#E8FFF5">███#E8FFF5</font></td>
<td><font color="#DFFFDF">███#DFFFDF</font></td>
</tr><tr>
<td><font color="#FBFBFF">███#FBFBFF</font></td>
<td><font color="#ECF5FF">███#ECF5FF</font></td>
<td><font color="#FDFFFF">███#FDFFFF</font></td>
<td><font color="#FBFFFD">███#FBFFFD</font></td>
<td><font color="#F0FFF0">███#F0FFF0</font></td>
</tr><tr>
<td><font color="#467500">███#467500</font></td>
<td><font color="#424200">███#424200</font></td>
<td><font color="#5B4B00">███#5B4B00</font></td>
<td><font color="#844200">███#844200</font></td>
<td><font color="#642100">███#642100</font></td>
</tr><tr>
<td><font color="#548C00">███#548C00</font></td>
<td><font color="#5B5B00">███#5B5B00</font></td>
<td><font color="#796400">███#796400</font></td>
<td><font color="#9F5000">███#9F5000</font></td>
<td><font color="#842B00">███#842B00</font></td>
</tr><tr>
<td><font color="#64A600">███#64A600</font></td>
<td><font color="#737300">███#737300</font></td>
<td><font color="#977C00">███#977C00</font></td>
<td><font color="#BB5E00">███#BB5E00</font></td>
<td><font color="#A23400">███#A23400</font></td>
</tr><tr>
<td><font color="#73BF00">███#73BF00</font></td>
<td><font color="#8C8C00">███#8C8C00</font></td>
<td><font color="#AE8F00">███#AE8F00</font></td>
<td><font color="#D26900">███#D26900</font></td>
<td><font color="#BB3D00">███#BB3D00</font></td>
</tr><tr>
<td><font color="#82D900">███#82D900</font></td>
<td><font color="#A6A600">███#A6A600</font></td>
<td><font color="#C6A300">███#C6A300</font></td>
<td><font color="#EA7500">███#EA7500</font></td>
<td><font color="#D94600">███#D94600</font></td>
</tr><tr>
<td><font color="#8CEA00">███#8CEA00</font></td>
<td><font color="#C4C400">███#C4C400</font></td>
<td><font color="#D9B300">███#D9B300</font></td>
<td><font color="#FF8000">███#FF8000</font></td>
<td><font color="#F75000">███#F75000</font></td>
</tr><tr>
<td><font color="#9AFF02">███#9AFF02</font></td>
<td><font color="#E1E100">███#E1E100</font></td>
<td><font color="#EAC100">███#EAC100</font></td>
<td><font color="#FF9224">███#FF9224</font></td>
<td><font color="#FF5809">███#FF5809</font></td>
</tr><tr>
<td><font color="#A8FF24">███#A8FF24</font></td>
<td><font color="#F9F900">███#F9F900</font></td>
<td><font color="#FFD306">███#FFD306</font></td>
<td><font color="#FFA042">███#FFA042</font></td>
<td><font color="#FF8040">███#FF8040</font></td>
</tr><tr>
<td><font color="#B7FF4A">███#B7FF4A</font></td>
<td><font color="#FFFF37">███#FFFF37</font></td>
<td><font color="#FFDC35">███#FFDC35</font></td>
<td><font color="#FFAF60">███#FFAF60</font></td>
<td><font color="#FF8F59">███#FF8F59</font></td>
</tr><tr>
<td><font color="#C2FF68">███#C2FF68</font></td>
<td><font color="#FFFF6F">███#FFFF6F</font></td>
<td><font color="#FFE153">███#FFE153</font></td>
<td><font color="#FFBB77">███#FFBB77</font></td>
<td><font color="#FF9D6F">███#FF9D6F</font></td>
</tr><tr>
<td><font color="#CCFF80">███#CCFF80</font></td>
<td><font color="#FFFF93">███#FFFF93</font></td>
<td><font color="#FFE66F">███#FFE66F</font></td>
<td><font color="#FFC78E">███#FFC78E</font></td>
<td><font color="#FFAD86">███#FFAD86</font></td>
</tr><tr>
<td><font color="#D3FF93">███#D3FF93</font></td>
<td><font color="#FFFFAA">███#FFFFAA</font></td>
<td><font color="#FFED97">███#FFED97</font></td>
<td><font color="#FFD1A4">███#FFD1A4</font></td>
<td><font color="#FFBD9D">███#FFBD9D</font></td>
</tr><tr>
<td><font color="#DEFFAC">███#DEFFAC</font></td>
<td><font color="#FFFFB9">███#FFFFB9</font></td>
<td><font color="#FFF0AC">███#FFF0AC</font></td>
<td><font color="#FFDCB9">███#FFDCB9</font></td>
<td><font color="#FFCBB3">███#FFCBB3</font></td>
</tr><tr>
<td><font color="#E8FFC4">███#E8FFC4</font></td>
<td><font color="#FFFFCE">███#FFFFCE</font></td>
<td><font color="#FFF4C1">███#FFF4C1</font></td>
<td><font color="#FFE4CA">███#FFE4CA</font></td>
<td><font color="#FFDAC8">███#FFDAC8</font></td>
</tr><tr>
<td><font color="#EFFFD7">███#EFFFD7</font></td>
<td><font color="#FFFFDF">███#FFFFDF</font></td>
<td><font color="#FFF8D7">███#FFF8D7</font></td>
<td><font color="#FFEEDD">███#FFEEDD</font></td>
<td><font color="#FFE6D9">███#FFE6D9</font></td>
</tr><tr>
<td><font color="#F5FFE8">███#F5FFE8</font></td>
<td><font color="#FFFFF4">███#FFFFF4</font></td>
<td><font color="#FFFCEC">███#FFFCEC</font></td>
<td><font color="#FFFAF4">███#FFFAF4</font></td>
<td><font color="#FFF3EE">███#FFF3EE</font></td>
</tr><tr>
<td><font color="#613030">███#613030</font></td>
<td><font color="#616130">███#616130</font></td>
<td><font color="#336666">███#336666</font></td>
<td><font color="#484891">███#484891</font></td>
<td><font color="#6C3365">███#6C3365</font></td>
</tr><tr>
<td><font color="#743A3A">███#743A3A</font></td>
<td><font color="#707038">███#707038</font></td>
<td><font color="#3D7878">███#3D7878</font></td>
<td><font color="#5151A2">███#5151A2</font></td>
<td><font color="#7E3D76">███#7E3D76</font></td>
</tr><tr>
<td><font color="#804040">███#804040</font></td>
<td><font color="#808040">███#808040</font></td>
<td><font color="#408080">███#408080</font></td>
<td><font color="#5A5AAD">███#5A5AAD</font></td>
<td><font color="#8F4586">███#8F4586</font></td>
</tr><tr>
<td><font color="#984B4B">███#984B4B</font></td>
<td><font color="#949449">███#949449</font></td>
<td><font color="#4F9D9D">███#4F9D9D</font></td>
<td><font color="#7373B9">███#7373B9</font></td>
<td><font color="#9F4D95">███#9F4D95</font></td>
</tr><tr>
<td><font color="#AD5A5A">███#AD5A5A</font></td>
<td><font color="#A5A552">███#A5A552</font></td>
<td><font color="#5CADAD">███#5CADAD</font></td>
<td><font color="#8080C0">███#8080C0</font></td>
<td><font color="#AE57A4">███#AE57A4</font></td>
</tr><tr>
<td><font color="#B87070">███#B87070</font></td>
<td><font color="#AFAF61">███#AFAF61</font></td>
<td><font color="#6FB7B7">███#6FB7B7</font></td>
<td><font color="#9999CC">███#9999CC</font></td>
<td><font color="#B766AD">███#B766AD</font></td>
</tr><tr>
<td><font color="#C48888">███#C48888</font></td>
<td><font color="#B9B973">███#B9B973</font></td>
<td><font color="#81C0C0">███#81C0C0</font></td>
<td><font color="#A6A6D2">███#A6A6D2</font></td>
<td><font color="#C07AB8">███#C07AB8</font></td>
</tr><tr>
<td><font color="#CF9E9E">███#CF9E9E</font></td>
<td><font color="#C2C287">███#C2C287</font></td>
<td><font color="#95CACA">███#95CACA</font></td>
<td><font color="#B8B8DC">███#B8B8DC</font></td>
<td><font color="#CA8EC2">███#CA8EC2</font></td>
</tr><tr>
<td><font color="#D9B3B3">███#D9B3B3</font></td>
<td><font color="#CDCD9A">███#CDCD9A</font></td>
<td><font color="#A3D1D1">███#A3D1D1</font></td>
<td><font color="#C7C7E2">███#C7C7E2</font></td>
<td><font color="#D2A2CC">███#D2A2CC</font></td>
</tr><tr>
<td><font color="#E1C4C4">███#E1C4C4</font></td>
<td><font color="#D6D6AD">███#D6D6AD</font></td>
<td><font color="#B3D9D9">███#B3D9D9</font></td>
<td><font color="#D8D8EB">███#D8D8EB</font></td>
<td><font color="#DAB1D5">███#DAB1D5</font></td>
</tr><tr>
<td><font color="#EBD6D6">███#EBD6D6</font></td>
<td><font color="#DEDEBE">███#DEDEBE</font></td>
<td><font color="#C4E1E1">███#C4E1E1</font></td>
<td><font color="#E6E6F2">███#E6E6F2</font></td>
<td><font color="#E2C2DE">███#E2C2DE</font></td>
</tr><tr>
<td><font color="#F2E6E6">███#F2E6E6</font></td>
<td><font color="#E8E8D0">███#E8E8D0</font></td>
<td><font color="#D1E9E9">███#D1E9E9</font></td>
<td><font color="#F3F3FA">███#F3F3FA</font></td>
<td><font color="#EBD3E8">███#EBD3E8</font></td>
</tr>

</table>
