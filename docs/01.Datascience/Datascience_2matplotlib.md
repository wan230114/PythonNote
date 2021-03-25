# matplotlib概述

# 目录

* [matplotlib概述](#_matplotlib概述)
* [目录](#_目录)
* [1. matplotlib概述](#__1-matplotlib概述)
  * [1.1. matplotlib基本功能](#_11-matplotlib基本功能)
  * [1.2. 包的导入](#_12-包的导入)
* [2. matplotlib基本功能详解](#_2-matplotlib基本功能详解)
  * [2.1. 基本绘图](#_21-基本绘图)
    * [2.1.1. 绘图核心API mp.plot](#_211-绘图核心api-mpplot)
    * [2.1.2. 绘制水平线与垂直线 mp.vlines, mp.hlines](#_212-绘制水平线与垂直线-mpvlines-mphlines)
    * [2.1.3. 设置坐标轴范围  mp.xlim/mp.ylim](#_213-设置坐标轴范围-mpxlimmpylim)
    * [2.1.4. 设置坐标刻度 mp.xticks/mp.yticks](#_214-设置坐标刻度-mpxticksmpyticks)
    * [2.1.5. 设置坐标轴 mp.gca().spines().set_...](#_215-设置坐标轴-mpgcaspinesset_)
    * [2.1.6. 图例 mp.legend](#_216-图例-mplegend)
    * [2.1.7. 特殊点标注绘制 mp.scatter](#_217-特殊点标注绘制-mpscatter)
    * [2.1.8. 备注文本 mp.annotate](#_218-备注文本-mpannotate)
    * [2.1.9. 绘图案例](#_219-绘图案例)
  * [2.2. 图形对象（图形窗口）](#_22-图形对象图形窗口)
    * [2.2.1. 图形窗口创建及选择 mp.figure](#_221-图形窗口创建及选择-mpfigure)
    * [2.2.2. 设置当前窗口的参数 mp.title/mp.xlabel/mp.tick_params/mp.grid](#_222-设置当前窗口的参数-mptitlempxlabelmptick_paramsmpgrid)
    * [2.2.3. 子图](#_223-子图)
      * [2.2.3.1. 矩阵式布局 mp.subplot](#_2231-矩阵式布局-mpsubplot)
      * [2.2.3.2. 网格式布局 mp.subplot(mg.GridSpec(3, 3)[0, :2])](#_2232-网格式布局-mpsubplotmggridspec3-30-2)
      * [2.2.3.3. 自由式布局 mp.axes](#_2233-自由式布局-mpaxes)
    * [2.2.4. 刻度定位器 mp.gca().xaxis.set_major_locator()](#_224-刻度定位器-mpgcaxaxisset_major_locator)
    * [2.2.5. 刻度网格线 mp.gca().grid()](#_225-刻度网格线-mpgcagrid)
    * [2.2.6. 半对数坐标 mp.semilogy](#_226-半对数坐标-mpsemilogy)
    * [2.2.7. 散点图 mp.scatter](#_227-散点图-mpscatter)
    * [2.2.8. 填充 mp.fill_between](#_228-填充-mpfill_between)
    * [2.2.9. 条形图（柱状图） mp.bar](#_229-条形图柱状图-mpbar)
    * [2.2.10. 饼图 mp.axis, mp.pie](#_2210-饼图-mpaxis-mppie)
    * [2.2.11. 等高线图 mp.clabel(mp.contour)](#_2211-等高线图-mpclabelmpcontour)
    * [2.2.12. 热成像图 mp.imshow, mp.colorbar](#_2212-热成像图-mpimshow-mpcolorbar)
    * [2.2.13. 3D图像绘制 mp.gca(projection='3d')](#_2213-3d图像绘制-mpgcaprojection3d)
      * [2.2.13.1. 3D点阵绘制 ax.scatter](#_22131-3d点阵绘制-axscatter)
      * [2.2.13.2. 3D曲面绘制 ax.plot_surface](#_22132-3d曲面绘制-axplot_surface)
      * [2.2.13.3. 3D线框图 ax.plot_wireframe](#_22133-3d线框图-axplot_wireframe)
    * [2.2.14. 极坐标系 mp.gca(projection='polar')](#_2214-极坐标系-mpgcaprojectionpolar)
    * [2.2.15. 简单动画 ma.FuncAnimation(mp.gcf(), func, interval=10)](#_2215-简单动画-mafuncanimationmpgcf-func-interval10)


---
# 1. matplotlib概述

`matplotlib`是python的一个绘图库。使用它可以很方便的绘制出版质量级别的图形。

在这基础上，有二次封装开发，或模仿的包，以下还例举了一些其他的可视化工具：
- `pyecharts`。支持多达400+地图；支持Jupyter Notebook、JupyterLab；可轻松集成至 Flask，Sanic，Django 等主流 Web 框架
- `AutoViz`。数据可视化，大多数都需要把数据读取到内存中，然后对内存中的数据进行可视化。但是，对于真正令人头疼的是一次又一次的开发读取离线文件的数据接口。而AutoViz就是用于解决这个痛点的，它真正的可以做到1行代码轻松实现可视化。它可以同时兼容txt、json、csv等主流离线数据格式，比较适合于机器学习、计算机视觉等涉及离线数据较多的应用场景。
- `Altair`。一款基于Vega 和Vega-Lite开发的统计可视化库。Altair构建在强大的Vega-Lite JSON规范之上，并且具有API简单、友好、一致等诸多优点。

## matplotlib起源和发展

- 一些优秀的拓展包：
  - `Seaborn`：是matplotlib的强大的一个扩展，可以让代码更加简洁，绘图更加丰富。

## 1.1. matplotlib基本功能

    1. 基本绘图 （在二维平面坐标系中绘制连续的线）
       1. 设置线型、线宽和颜色  
       2. 设置坐标轴范围
       3. 设置坐标刻度
       4. 设置坐标轴
       5. 图例
       6. 特殊点****
       7. 备注
    2. 图形对象(图形窗口)~~~~
       1. 子图
       2. 刻度定位器
       3. 刻度网格线
       4. 半对数坐标
       5. 散点图
       6. 填充
       7. 条形图
       8. 饼图
       9. 等高线图
       10. 热成像图
       11. 极坐标系
       12. 三维曲面
       13. 简单动画

包的导入: `import matplotlib.pyplot as mp`

# 2. matplotlib基本功能详解

## 2.1. 基本绘图

### 2.1.1. 绘图核心API mp.plot

绘制一条折线

```python
# 绘制一条折线
import matplotlib.pyplot as mp
xarray = [0, 2, 3]  # xarray: <序列> 水平坐标序列
yarray = [0, 2, 4]  # yarray: <序列> 垂直坐标序列
mp.plot(xarray, yarray)
mp.show()  # 显示图表
```

线型、线宽和
```python
import matplotlib.pyplot as mp
# linestyle: '-' 实线  '--' 虚线  ':' 点线
# linewidth: 线宽 (数字)
# color: <关键字参数> 颜色
#        英文颜色单词 或 常见颜色英文单词首字母 或 #495434 或 (1,1,1) 或 (1,1,1,1)
# alpha: <关键字参数> 透明度
#        浮点数值
xarray = [1, 4, 8, 10]
yarray = [4, 1, 3, 9]
# ":"   0.7透明度  3倍线宽   颜色red
mp.plot(xarray, yarray, linestyle='-', linewidth=3, color='red', alpha=0.7)
mp.show()
```


### 2.1.2. 绘制水平线与垂直线 mp.vlines, mp.hlines

```python
import matplotlib.pyplot as mp
# x轴起点，y轴起点，y轴终点
mp.vlines(8, 2, 10)  # vertical 绘制垂直线  mp.vlines(vval, ymin, ymax, ...)
# y轴起点，x轴起点，x轴终点
mp.hlines(5, 2, 12)  # horizotal 绘制水平线  mp.hlines(xval, xmin, xmax, ...)
mp.show()  #显示图表
```

### 2.1.3. 设置坐标轴范围  mp.xlim/mp.ylim

案例：把坐标轴范围设置为 -π ~ π

```python
import matplotlib.pyplot as mp
# x_limt_min / x_limit_max: <float> x轴范围最小值/x轴范围最大值
# y_limt_min / y_limit_max: <float> y轴范围最小值，y轴范围最大值
y_limt_min, y_limit_max = -2, 14
x_limt_min, x_limit_max = 0, 10
mp.xlim(x_limt_min, x_limit_max)
mp.ylim(y_limt_min, y_limit_max)
mp.show()
```

### 2.1.4. 设置坐标刻度 mp.xticks/mp.yticks

案例：把横坐标的刻度显示为：0, π/2, π, 3π/2, 2π

```python
import matplotlib.pyplot as mp
# x_val_list:  x轴刻度值序列, x_text_list: x轴刻度标签文本序列 [可选]
# y_val_list:  y轴刻度值序列, y_text_list: y轴刻度标签文本序列 [可选]
mp.xticks([1, 2, 3, 4, 5], list("ABCDE") )
mp.yticks([1, 2, 3, 4, 5], list("ABCDE") )
mp.show()
```

### 2.1.5. 设置坐标轴 mp.gca().spines().set_...

坐标轴名：left / right / bottom / top

```python
import matplotlib.pyplot as mp
# 获取当前坐标轴字典，{'left':左轴,'right':右轴,'bottom':下轴,'top':上轴 }
ax = mp.gca()
# 获取其中某个坐标轴
axis = ax.spines['left']  # 坐标轴名：left, right, bottom, top
axis.set_position(('data', 0))
# 设置坐标轴的位置。 该方法需要传入2个元素的元组作为参数
    # type: <str> 移动坐标轴的参照类型  一般为'data' (以数据的值作为移动参照值)
    # val:  参照值
# 设置坐标轴的颜色
axis.set_color('red')  # color: <str> 颜色值字符串
mp.yticks([-1, -0.5, 0.5, 1])
mp.xticks([-2, -1, 1, 2])
mp.show()
```

案例：设置坐标轴至中心。

```python
import matplotlib.pyplot as mp
# 设置坐标轴, 设置顶部右侧线条为无, 设置右下居右
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['bottom'].set_color('red')
mp.yticks([-1, -0.5, 0.5, 1])
mp.xticks([-1, -0.5, 0.5, 1])
mp.show()
```

### 2.1.6. 图例 mp.legend

显示两条曲线的图例，并测试loc属性。

```python
import matplotlib.pyplot as mp
# 再绘制曲线时定义曲线的label

# label: <关键字参数 str> 支持LaTex排版语法字符串
xarray = [0,  2,  4]
yarray = [0,  1,  2]
mp.plot(xarray, yarray)
# label 定义曲线名称，为后续显示图例准备
mp.plot(xarray, yarray, label=r'$y=\frac{1}{2}x$')
# loc 设置图例
mp.legend(loc='best')
mp.show()
```
```
设置图例的位置
loc: <关键字参数> 制定图例的显示位置 (若不设置loc，则显示默认位置)
     ===============   =============
   Location String   Location Code
   ===============   =============
   'best'            0
   'upper right'     1
   'upper left'      2
   'lower left'      3
   'lower right'     4
   'right'           5
   'center left'     6
   'center right'    7
   'lower center'    8
   'upper center'    9
   'center'          10
   ===============   =============
```

***刻度文本的特殊语法*** -- *LaTex排版语法字符串*

注：<font color="#FF0000">红色文字</font>为Python语法：

<center>
<font color="#FF0000" face='consolas'>
r'$x^n+y^n=z^n$'
</font>
</center>

$$
x^n+y^n=z^n
$$

<center>
<font color="#FF0000" face='consolas'>
r'$\int\frac{1}{x} dx = \ln |x| + C$',
</font>
</center>

$$
\int\frac{1}{x} dx = \ln |x| + C
$$

<center>
<font color="#FF0000" face='consolas'>
r'$-\frac{\pi}{2}$'
</font>
</center>

$$
 -\frac{\pi}{2}
$$

### 2.1.7. 特殊点标注绘制 mp.scatter

案例：绘制当x=3π/4时两条曲线上的特殊点。

```python
import matplotlib.pyplot as mp
# xarray: <序列> 所有需要标注点的水平坐标组成的序列
# yarray: <序列> 所有需要标注点的垂直坐标组成的序列
xarray = [1, 2, 3, 4]
yarray = [3, 1, 2, 4]
mp.scatter(xarray, yarray, 
           marker='o',         #点型 ~ matplotlib.markers
           s=60,             #大小
           edgecolor='red',     #边缘色
           facecolor='orange',    #填充色
           zorder=3            #绘制图层编号 （编号越大，图层越靠上）
)
mp.show()
```

*marker点型可参照：help(matplotlib.markers)*

*也可参照附录： matplotlib point样式*



### 2.1.8. 备注文本 mp.annotate

案例：为在某条曲线上的点添加备注，指明函数方程与值。

```python
import matplotlib.pyplot as mp
# 在图表中为某个点添加备注。包含备注文本，备注箭头等图像的设置。
import numpy as np
mp.annotate(
    r'$(\frac{\pi}{4}, 5)$',    #备注中显示的文本内容
    xycoords='data',            #备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(np.pi/4, 0.5),            #备注目标点的坐标
    textcoords='offset points',    #备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(30, 20),            #备注文本的坐标
    fontsize=14,                #备注文本的字体大小
    arrowprops=dict(  #arrowprops字典参数的常用key
        arrowstyle='->', #定义箭头样式
        connectionstyle='angle3' #定义连接线的样式
        ) 
    #使用字典定义文本指向目标点的箭头样式
)
mp.show()
```

**arrowprops参数** 使用字典定义指向目标点的箭头样式

箭头样式（arrowstyle）字符串如下

```
============   =============================================
Name           Attrs
============   =============================================
  '-'          None
  '->'         head_length=0.4,head_width=0.2
  '-['         widthB=1.0,lengthB=0.2,angleB=None
  '|-|'        widthA=1.0,widthB=1.0
  '-|>'        head_length=0.4,head_width=0.2
  '<-'         head_length=0.4,head_width=0.2
  '<->'        head_length=0.4,head_width=0.2
  '<|-'        head_length=0.4,head_width=0.2
  '<|-|>'      head_length=0.4,head_width=0.2
  'fancy'      head_length=0.4,head_width=0.4,tail_width=0.4
  'simple'     head_length=0.5,head_width=0.5,tail_width=0.2
  'wedge'      tail_width=0.3,shrink_factor=0.5
============   =============================================

```

连接线样式（connectionstyle）字符串如下

```
============   =============================================
Name           Attrs
============   =============================================
  'angle'         angleA=90,angleB=0,rad=0.0
  'angle3'         angleA=90,angleB=0`   
  'arc'            angleA=0,angleB=0,armA=None,armB=None,rad=0.0
  'arc3'         rad=0.0
  'bar'         armA=0.0,armB=0.0,fraction=0.3,angle=None
============   =============================================

```

### 2.1.9. 绘图案例
```python
"""
demo02_plot.py  基本绘图案例
"""
import matplotlib.pyplot as mp
import numpy as np

# 绘制正弦图像
# 从0到2π区间拆1000个点
x = np.linspace(-np.pi, np.pi, 1000)
y = np.sin(x)
mp.plot(x, y, linestyle='--', alpha=0.7,
    linewidth=2, color='dodgerblue', 
    label=r'$y=sin(x)$')
# 绘制一条余弦曲线 y=1/2 * cos(x)  
# ":"   0.7透明度  3倍线宽   颜色orangered
y2 = np.cos(x) / 2
mp.plot(x, y2, linestyle=':', alpha=0.7,
    linewidth=3, color='orangered',
    label=r'$y=\frac{1}{2} cos(x)$')

# 修改可视区域
# mp.xlim(0, np.pi)
# mp.ylim(0, 1)

# 修改x坐标轴刻度
xvals = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
xtexts = [r'$-\pi$',r'$-\frac{\pi}{2}$',r'$0$',
          r'$\frac{\pi}{2}$',r'$\pi$']
mp.xticks(xvals, xtexts)

# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
mp.yticks([-1, -0.5, 0.5, 1])

# 绘制两个特殊点
px = [np.pi/2, np.pi/2]
py = [0, 1]
mp.scatter(px, py, marker='o', s=70,
    color='red', label='Points', 
    zorder=3)

# 绘制点的备注
mp.annotate(r'$[\frac{\pi}{2}, 1]$', 
    xycoords='data',
    xy=(np.pi/2, 1),
    textcoords='offset points',
    xytext=(30, 20),
    fontsize=14,
    arrowprops=dict(
        arrowstyle='->',
        connectionstyle='angle3'
    )
)


mp.annotate(r'$[\frac{\pi}{2}, 0]$', 
    xycoords='data',
    xy=(np.pi/2, 0),
    textcoords='offset points',
    xytext=(-50, -50),
    fontsize=14,
    arrowprops=dict(
        arrowstyle='->',
        connectionstyle='angle3'
    )
)

# 显示图例
mp.legend(loc='best')
mp.show()
```


## 2.2. 图形对象（图形窗口）

### 2.2.1. 图形窗口创建及选择 mp.figure

案例：绘制两个窗口，一起显示。
```python
import matplotlib.pyplot as mp
# 手动构建 matplotlib 窗口
mp.figure(
    '文本1',            #窗口标题栏文本
    figsize=(4, 3),        #窗口大小 <元组>
    dpi=120,            #像素密度
    facecolor='green'    #图表背景色
)
mp.show()
```
mp.figure方法不仅可以构建一个新窗口，如果已经构建过title='A'的窗口，又使用figure方法构建了title='A' 的窗口的话，mp将不会创建新的窗口，而是把title='A'的窗口置为当前操作窗口。


### 2.2.2. 设置当前窗口的参数 mp.title/mp.xlabel/mp.tick_params/mp.grid

案例：测试窗口相关参数

```python
import matplotlib.pyplot as mp
# 1) 设置图表标题 显示在图表上方
mp.title('title', fontsize=12)
# 2) 设置水平轴的文本
mp.xlabel('x_label_str', fontsize=12)
# 3) 设置垂直轴的文本
mp.ylabel('y_label_str', fontsize=12)
# 4) 设置刻度参数   labelsize设置刻度字体大小
mp.tick_params(labelsize=8)
# 5) 设置图表网格线  linestyle设置网格线的样式
    #    -  or solid 粗线
    #   -- or dashed 虚线
    #   -. or dashdot 点虚线
    #   :  or dotted 点线
mp.grid(linestyle=':')
# 6) 设置紧凑布局
mp.tight_layout() 
mp.show()
```

示例：
```python
"""
demo03_figure.py  窗口相关测试
"""
import matplotlib.pyplot as mp
mp.figure('Figure Title A',
          facecolor='lightgray')
mp.figure('Figure Title B',
          facecolor='lightblue')
def fig(s):
    mp.figure('Figure Title %s' % s)  # 切换操作窗口
    mp.title('Title %s' % s, fontsize=18)
    mp.xlabel('Time %s' % s, fontsize=14)
    mp.ylabel('Price %s' % s, fontsize=14)
    mp.tick_params(labelsize=10)
    mp.grid(linestyle=':')
    mp.tight_layout()  # 窗口内容紧凑布局
fig('A')
fig('B')
mp.show()
```


### 2.2.3. 子图

#### 2.2.3.1. 矩阵式布局 mp.subplot

绘制矩阵式子图布局相关API：

```python
import matplotlib.pyplot as mp
mp.figure('Subplot Layout', facecolor='lightgray')
# 拆分矩阵
    # rows:    行数
    # cols:    列数
    # num:    编号
# mp.subplot(rows, cols, num)
mp.subplot(3, 3, 1)
mp.subplot(3, 3, 3)
    #    1 2 3
    #    4 5 6
    #    7 8 9 
mp.subplot(3, 3, 5)        #操作3*3的矩阵中编号为5的子图
mp.subplot(336)            #简写
mp.show()
```

案例：绘制9宫格矩阵式子图，每个子图中写一个数字。

```python
"""
demo04_subplot.py  矩阵式子图
"""
import matplotlib.pyplot as mp
mp.figure('Subplot', facecolor='lightgray')
for i in range(1, 10):
    mp.subplot(3, 3, i)
    mp.text(0.5, 0.5, i, ha='center', 
            va='center', size=36, alpha=0.7)
    mp.xticks([])
    mp.yticks([])
mp.tight_layout()
mp.show()
```

#### 2.2.3.2. 网格式布局 mp.subplot(mg.GridSpec(3, 3)[0, :2])

网格式布局支持单元格的合并。

绘制网格式子图布局相关API：

```python
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
mp.figure('Grid Layout', facecolor='lightgray')

# 调用GridSpec方法拆分网格式布局
# rows:    行数
# cols:    列数
# gs = mg.GridSpec(rows, cols)    拆分成3行3列
gs = mg.GridSpec(3, 3)

# 合并0行与0、1列为一个子图表
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()
```

案例：绘制一个自定义网格布局。

```python
"""
demo05_gridsubplot.py  网格式子图布局
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.ion()  # 开启一个画图的窗口
mp.show()
mp.figure('Grid Subplot', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', 
        va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[:2, -1])
mp.text(0.5, 0.5, 2, ha='center', 
        va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, 3, ha='center', 
        va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, 4, ha='center', 
        va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[-1, 1:])
mp.text(0.5, 0.5, 5, ha='center', 
        va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.tight_layout()
mp.show()
```

#### 2.2.3.3. 自由式布局 mp.axes

自由式布局相关API：

```python
import matplotlib.pyplot as mp
# 设置图标的位置，给出左下角点坐标与宽高即可
# left_bottom_x: 左下角点x坐标
# left_bottom_y: 左下角点y坐标
# width:         宽度
# height:         高度
# mp.axes([left_bottom_x, left_bottom_y, width, height])
mp.figure('Flow Layout', facecolor='lightgray')
mp.axes([0.2, 0.5, 0.3, 0.4])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()
```

### 2.2.4. 刻度定位器 mp.gca().xaxis.set_major_locator()

刻度定位器相关API：

```python
import matplotlib.pyplot as mp
# 获取当前坐标轴
ax = mp.gca()
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.NullLocator())
# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
```
常用刻度器如下

| 刻度器                                     | 解释                                                       |
| ------------------------------------------ | ---------------------------------------------------------- |
| mp.NullLocator()                           | 空定位器: 不绘制刻度                                       |
| mp.MaxNLocator(nbins=3)                    | 最大值定位器: 最多绘制nbins+1个刻度                        |
| mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10]) | 定点定位器: 根据locs参数中的位置绘制刻度                   |
| mp.AutoLocator()                           | 自动定位器: 由系统自动选择刻度的绘制位置                   |
| mp.IndexLocator(offset=0.5, base=1.5)      | 索引定位器: 由offset确定起始刻度，由base确定相邻刻度的间隔 |
| mp.MultipleLocator()                       | 多点定位器: 从0开始，按照参数指定的间隔(缺省1)绘制刻度     |
| mp.LinearLocator(numticks=21)              | 线性定位器: 等分numticks-1份，绘制numticks个刻度           |
| mp.LogLocator(base=2)                      | 对数定位器: 以base为底，绘制刻度                           |

案例：绘制一个数轴。

```python
import matplotlib.pyplot as mp
mp.figure('Locators', facecolor='lightgray')
# 获取当前坐标轴
ax = mp.gca()
# 隐藏除底轴以外的所有坐标轴, 将底坐标轴调整到子图中心位置
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.NullLocator())
# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
# 标记所用刻度定位器类名
mp.text(5, 0.3, 'NullLocator()', ha='center', size=12)
mp.show()
```

案例：使用for循环测试刻度器样式：

```python
"""
demo07_locators.py  刻度定位器
"""
import matplotlib.pyplot as mp
import numpy as np
locators = ['mp.NullLocator()', 
            'mp.MultipleLocator(2)', 
            'mp.MaxNLocator(nbins=4)']
mp.figure('Locators', facecolor='lightgray')
for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i+1)
    ax = mp.gca()
    # ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    mp.ylim(-1, 1)
    mp.xlim(1, 10)
    ax.spines['bottom'].set_position(('data', 0))
    # 设置主刻度定位器 与 次刻度定位器
    maloc = eval(locator)
    ax.xaxis.set_major_locator(maloc)
    miloc = mp.MultipleLocator(0.1)
    ax.xaxis.set_minor_locator(miloc)
mp.show()
```


### 2.2.5. 刻度网格线 mp.gca().grid()

绘制刻度网格线的相关API：
```
ax = mp.gca()
#绘制刻度网格线
ax.grid(
    which='',       # 'major'/'minor' <-> '主刻度'/'次刻度' 
    axis='',        # 'x'/'y'/'both' <-> 绘制x或y轴
    linewidth=1,    # 线宽
    linestyle='',   # 线型
    color='',       # 颜色
    alpha=0.5       # 透明度
)
```

案例：绘制曲线 [1, 10, 100, 1000, 100, 10, 1]，然后设置刻度网格线，测试刻度网格线的参数。

```python
import matplotlib.pyplot as mp
import numpy as np
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.subplot(211)

ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
mp.tick_params(labelsize=10)
ax.grid(which='major', axis='both', linewidth=0.75,
        linestyle='-', color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25,
        linestyle='-', color='orange')
mp.plot(y, 'o-', c='dodgerblue', label='plot')
mp.legend()
mp.show()
```

### 2.2.6. 半对数坐标 mp.semilogy

y轴将以指数方式递增。 基于半对数坐标绘制第二个子图，表示曲线：[1, 10, 100, 1000, 100, 10, 1]。

```python
"""
demo09_semilogy.py 半对数坐标系
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Normal & Semilogy', facecolor='lightgray')
mp.subplot(211)
mp.title('Normal', fontsize=20)
mp.ylabel('y', fontsize=14)
y = [1, 10, 100, 1000, 100, 10, 1]
# 设置刻度定位器
ax = mp.gca()
xmaloc = mp.MultipleLocator(1)
ax.xaxis.set_major_locator(xmaloc)
xmiloc = mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(xmiloc)
ymaloc = mp.MultipleLocator(250)
ax.yaxis.set_major_locator(ymaloc)
ymiloc = mp.MultipleLocator(50)
ax.yaxis.set_minor_locator(ymiloc)
# 绘制刻度网格线
ax.grid(which='major', axis='both',
    color='orangered', linewidth=0.75)
ax.grid(which='minor', axis='both',
    color='orangered', linewidth=0.25)
mp.plot(y, 'o-')

# 半对数坐标系
mp.subplot(212)
y = [1, 10, 100, 1000, 100, 10, 1]
# 设置刻度定位器
ax = mp.gca()
xmaloc = mp.MultipleLocator(1)
ax.xaxis.set_major_locator(xmaloc)
xmiloc = mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(xmiloc)
ymaloc = mp.MultipleLocator(250)
ax.yaxis.set_major_locator(ymaloc)
ymiloc = mp.MultipleLocator(50)
ax.yaxis.set_minor_locator(ymiloc)
# 绘制刻度网格线
ax.grid(which='major', axis='both',
    color='orangered', linewidth=0.75)
ax.grid(which='minor', axis='both',
    color='orangered', linewidth=0.25)
mp.semilogy(y, 'o-')  # 用法同 mp.plot()

mp.show()
```


### 2.2.7. 散点图 mp.scatter

可以通过每个点的坐标、颜色、大小和形状表示不同的特征值。

| 身高 | 体重 | 性别 | 年龄段 | 种族 |
| ---- | ---- | ---- | ------ | ---- |
| 180  | 80   | 男   | 中年   | 亚洲 |
| 160  | 50   | 女   | 青少   | 美洲 |

绘制散点图的相关API：
```
mp.scatter(
    x,                     # x轴坐标数组
    y,                    # y轴坐标数组
    marker='',             # 点型
    s=10,                # 大小
    color='',            # 颜色
    edgecolor='',         # 边缘颜色
    facecolor='',        # 填充色
    zorder=''            # 图层序号
)
```

numpy.random提供了normal函数用于产生符合 正态分布 的随机数 

```python
n = 100
# 172:    期望值
# 10:    标准差
# n:    数字生成数量
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)
```

案例：绘制平面散点图。

```python
"""
demo10_scatter.py 散点图
"""
import numpy as np
import matplotlib.pyplot as mp
n = 300
x = np.random.normal(175, 5, n)
y = np.random.normal(65, 10, n)

mp.figure('Persons', facecolor='lightgray')
mp.title('Persons')

d = (x-175)**2 + (y-65)**2
# 设置点的颜色
# mp.scatter(x, y, c='red')  #直接设置颜色
mp.scatter(x, y, s=60, label='Persons',
    c=d, cmap='jet')
mp.legend()
mp.show()
```

*cmap颜色映射表参照附件：cmap颜色映射表: <a href="../img/Datascience/matplotlib_cmap.png">matplotlib_cmap.png</a>*

**一颗AI心**

### 2.2.8. 填充 mp.fill_between

以某种颜色自动填充两条曲线的闭合区域。

```
mp.fill_between(
    x,              # x轴的水平坐标
    sin_x,          # 下边界曲线上点的垂直坐标
    cos_x,          # 上边界曲线上点的垂直坐标
    sin_x<cos_x,    # 填充条件，为True时填充
    color='',       # 填充颜色
    alpha=0.2       # 透明度
)
```

案例：绘制两条曲线： sin_x = sin(x)   cos_x = cos(x / 2) / 2    [0-8π]  

```python
"""
demo01_fill.py  填充
"""
import matplotlib.pyplot as mp
import numpy as np

x = np.linspace(0, 8*np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x/2) / 2
mp.figure('Fill', facecolor='lightgray')
mp.title('Fill')
mp.plot(x, sinx, color='dodgerblue', 
    label='sinx', linewidth=2)
mp.plot(x, cosx, color='orangered', 
    label='cosx', linewidth=2)
# 绘制填充
mp.fill_between(x, sinx, cosx, sinx>cosx, 
    color='dodgerblue', alpha=0.5)
mp.fill_between(x, sinx, cosx, sinx<cosx, 
    color='orangered', alpha=0.5)

mp.legend()
mp.show()
```

### 2.2.9. 条形图（柱状图） mp.bar

绘制柱状图的相关API：

```
mp.figure('Bar', facecolor='lightgray')
mp.bar(
    x,                # 水平坐标数组
    y,                # 柱状图高度数组
    width,            # 柱子的宽度  0.8
    color='',         # 填充颜色
    label='',        #
    alpha=0.2        #
)
```

案例：先以柱状图绘制苹果12个月的销量，然后再绘制橘子的销量。

```python
import matplotlib.pyplot as mp
import numpy as np
apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
mp.figure('Bar' , facecolor='lightgray')
mp.title('Bar', fontsize=20)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.ylim((0, 40))
x = np.arange(len(apples))
mp.bar(x - 0.2, apples, 0.4, color='dodgerblue',label='Apple')
mp.bar(x + 0.2, oranges, 0.4, color='orangered',label='Orange', alpha=0.75)
mp.xticks(x, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
```

### 2.2.10. 饼图 mp.axis, mp.pie

绘制饼状图的基本API：

```
mp.axis('equal')
mp.pie(
    values,         # 值列表        
    spaces,         # 扇形之间的间距列表
    labels,         # 标签列表
    colors,         # 颜色列表
    '%d%%',            # 标签所占比例格式
    shadow=True,     # 是否显示阴影
    startangle=90    # 逆时针绘制饼状图时的起始角度
    radius=1        # 半径
)
```

案例：绘制饼状图显示5门语言的流行程度：

```python
"""
demo03_pie.py  饼状图
"""
import numpy as np

labels=['Python', 'Javascript', 'C++', 
        'Java', 'PHP']
values=[26, 17, 21, 29, 11]
spaces=[0.05, 0.01, 0.01, 0.01, 0.01]
colors=['dodgerblue', 'orangered', 
        'limegreen', 'violet', 'gold']

mp.figure('Pie Chart', facecolor='lightgray')
mp.title('Languages PR')
mp.axis('equal')  # 等轴比例显示正圆
mp.pie(values, spaces, labels, colors, 
    '%.1f%%', shadow=True, startangle=45,
    radius=1)
mp.legend()
mp.show()
```

### 2.2.11. 等高线图 mp.clabel(mp.contour)

组成等高线需要网格点坐标矩阵，也需要每个点的高度。所以等高线属于3D数学模型范畴。

绘制等高线的相关API：
```
cntr = mp.contour(
    x,                     # 网格坐标矩阵的x坐标 （2维数组）
    y,                     # 网格坐标矩阵的y坐标 （2维数组）
    z,                     # 网格坐标矩阵的z坐标 （2维数组）
    8,                     # 把等高线绘制成8部分，在高度上需要分多少阶
    colors='black',        # 等高线的颜色
    linewidths=0.5        # 线宽
)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)

# 填充等高线
mp.contourf(x, y, z, 8, cmap='jet')
```

案例：生成网格坐标矩阵，并且绘制等高线：

```python
import matplotlib.pyplot as mp
import numpy as np
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制等高线图
cntr = mp.contour(x, y, z, 8, colors='black',
                  linewidths=0.5)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
          fontsize=10)
# 颜色填充
mp.contourf(x, y, z, 8, cmap='jet')
mp.show()
```

### 2.2.12. 热成像图 mp.imshow, mp.colorbar

用图形的方式显示矩阵及矩阵中值的大小
1 2 3
4 5 6
7 8 9

绘制热成像图的相关API：

```
# 把矩阵z图形化，使用cmap表示矩阵中每个元素值的大小
# origin: 坐标轴方向
#    upper: 缺省值，原点在左上角
#    lower: 原点在左下角
mp.imshow(z, cmap='jet', origin='low')
# 使用颜色条显示热度值：
mp.colorbar()
```

```python
"""
demo05_imshow.py  热成像图显示矩阵
"""
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), 
                   np.linspace(-3, 3, n))
#  根据一个奇妙的公式算出每个坐标点的高度值z
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# 绘制
mp.figure('Imshow', facecolor='lightgray')
mp.title('Imshow')
mp.grid(linestyle=':')
mp.imshow(z, cmap='jet', origin='lower')
mp.colorbar()
mp.show()
```

### 2.2.13. 3D图像绘制 mp.gca(projection='3d')

 matplotlib支持绘制三维曲面。若希望绘制三维曲面，需要使用axes3d提供的3d坐标系。

```
from mpl_toolkits.mplot3d import axes3d
ax3d = mp.gca(projection='3d')   # class axes3d

# matplotlib支持绘制三维点阵、三维曲面、三维线框图：
ax3d.scatter(..)        # 绘制三维点阵
ax3d.plot_surface(..)    # 绘制三维曲面
ax3d.plot_wireframe(..)    # 绘制三维线框图

# 3d散点图的绘制相关API：
ax3d.scatter(
    x,                 # x轴坐标数组
    y,                # y轴坐标数组
    z,                # z轴坐标数组
    marker='',         # 点型
    s=10,            # 大小
    zorder='',        # 图层序号
    color='',        # 颜色
    edgecolor='',     # 边缘颜色
    facecolor='',    # 填充色
    c=v,            # 颜色值 根据cmap映射应用相应颜色
    cmap=''            # 
)
```

#### 2.2.13.1. 3D点阵绘制 ax.scatter
案例：随机生成3组坐标，服从标准正态分布规则，并且绘制它们。

```python
"""
demo06_3dscatter.py  3维点阵图
"""
import matplotlib.pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d

n = 500
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
mp.figure('3D scatter')
ax3d = mp.gca(projection='3d')
d = x**2 + y**2 + z**2
ax3d.scatter(x, y, z, s=70, c=d, alpha=0.7, cmap='jet')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
mp.tight_layout()
mp.show()
```

#### 2.2.13.2. 3D曲面绘制 ax.plot_surface

3d曲面图的绘制相关API：

```
ax3d.plot_surface(
    x,                     # 网格坐标矩阵的x坐标 （2维数组）
    y,                     # 网格坐标矩阵的y坐标 （2维数组）
    z,                     # 网格坐标矩阵的z坐标 （2维数组）
    rstride=30,            # 行跨距
    cstride=30,         # 列跨距
    cmap='jet'            # 颜色映射
)
```

案例：绘制3d平面图

```python
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('3D', facecolor='lightgray')
mp.title('3D', fontsize=20)

ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制3D平面图
# rstride: 行跨距
# cstride: 列跨距 
ax3d.plot_surface(x,y,z,rstride=20,cstride=40, cmap='jet')
mp.show()
```

#### 2.2.13.3. 3D线框图 ax.plot_wireframe

```
# 绘制3D平面图 
# rstride: 行跨距
# cstride: 列跨距 
ax3d.plot_wireframe(x,y,z,rstride=30,cstride=30, 
    linewidth=1, color='dodgerblue')
```

案例：3d线框图的绘制
```python
"""
demo08_3dwireframe.py  三维线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
#  根据一个奇妙的公式算出每个坐标点的高度值z
z = (1 - x / 2 + x**5 + y**3) * \
    np.exp(-x**2 - y**2)
# 绘制
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface')
ax3d = mp.gca(projection='3d')
ax3d.plot_wireframe(x, y, z, rstride=30,
                    cstride=30, cmap='jet', linewidth=1)
mp.show()
```


### 2.2.14. 极坐标系 mp.gca(projection='polar')

与笛卡尔坐标系不同，某些情况下极坐标系适合显示与角度有关的图像。例如雷达等。极坐标系可以描述极径&rho;与极角&theta;的线性关系。

```python
import matplotlib.pyplot as mp
mp.figure("Polar", facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Porlar', fontsize=20)
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 在极坐标系中绘制曲线：
t = np.linspace(0, 4*np.pi, 1000)  # 准备数据
r = 0.8 * t
mp.plot(t, r)

# 案例，在极坐标系中绘制正弦函数。 y=3 sin(6x)
x = np.linspace(0, 6*np.pi, 1000)
y = 3*np.sin(6*x)
mp.plot(x, y, color='red')
mp.show()
```

### 2.2.15. 简单动画 ma.FuncAnimation(mp.gcf(), func, interval=10)

动画即是在一段时间内快速连续的重新绘制图像的过程。

matplotlib提供了方法用于处理简单动画的绘制。定义update函数用于即时更新图像。

```python
import matplotlib.animation as ma
#定义更新函数行为
def update(number):
    pass
# 每隔10毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：    获取当前窗口
# update：    更新函数
# interval：    间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=10)
mp.show()
```

案例：随机生成各种颜色的100个气泡。让他们不断的增大。

```python
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

#自定义一种可以存放在ndarray里的类型，用于保存一个球
ball_type = np.dtype([
    ('position', float, 2),  # 位置(水平和垂直坐标)
    ('size', float, 1),      # 大小
    ('growth', float, 1),    # 生长速度
    ('color', float, 4)])    # 颜色(红、绿、蓝和透明度)

#随机生成100个点对象
n = 100
balls = np.zeros(100, dtype=ball_type)
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(40, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

mp.figure("Animation", facecolor='lightgray')
mp.title("Animation", fontsize=14)
mp.xticks([])
mp.yticks([])

sc = mp.scatter(
    balls['position'][:, 0], 
    balls['position'][:, 1], 
    balls['size'], 
    color=balls['color'], alpha=0.5)

#定义更新函数行为
def update(number):
    balls['size'] += balls['growth']
    #每次让一个气泡破裂，随机生成一个新的
    boom_ind = number % n
    balls[boom_ind]['size']=np.random.uniform(40, 70, 1)
    balls[boom_ind]['position']=np.random.uniform(0, 1, (1, 2))
    # 重新设置属性
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])
    
# 每隔30毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：    获取当前窗口
# update：        更新函数
# interval：    间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()  # 触发动画
```

使用生成器函数提供数据，实现动画绘制

在很多情况下，绘制动画的参数是动态获取的，matplotlib支持定义generator生成器函数，用于生成数据，把生成的数据交给update函数更新图像：

```
import matplotlib.animation as ma
#定义更新函数行为
def update(data):
    t, v = data
    ...
    pass

def generator():
    yield t, v
        
# 每隔10毫秒将会先调用生成器，获取生成器返回的数据，
# 把生成器返回的数据交给并且调用update函数，执行更新图像函数
anim = ma.FuncAnimation(mp.gcf(), update, generator,interval=10)
```

案例：绘制信号曲线：y=sin(2 * π * t) * exp(sin(0.2 * π * t))，数据通过生成器函数生成，在update函数中绘制曲线。

```python
import numpy as np
import matplotlib.animation as ma


mp.figure("Signal", facecolor='lightgray')
mp.title("Signal", fontsize=14)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue', label='Signal')[0]

x = 0

def update(data):
    t, v = data
    x, y = pl.get_data()
    #x是保存x坐标的ndarray对象
    #y是保存y坐标的ndarray对象
    x = np.append(x, t)
    y = np.append(y, v)
    #重新设置数据源
    pl.set_data(x, y)
    #移动坐标轴
    if(x[-1]>5):
        mp.xlim(x[-1]-5, x[-1]+5)

def y_generator():
    global x
    y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
    yield (x, y)
    x += 0.05

anim = ma.FuncAnimation(mp.gcf(), update, y_generator, interval=20)
mp.tight_layout()
mp.show()
```

## 图形绘制

### 圆

```python
import matplotlib.pyplot as plt

circles = [
    plt.Circle((0, 0), 1, color='#000000', fill=False),
    plt.Circle((0, 0), 0.5, color='#000000', fill=True)
    ]

fig, ax = plt.subplots()

plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)

# plt.grid(linestyle='--')
ax.set_aspect(1)

for circle in circles:
    ax.add_artist(circle)
```


# 图像的输出

【待补充】

# 附

## 一些画图调试技巧

实时显示

```python
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.ion()  # 开启一个画图的窗口
mp.plot([1,2,3], [2,5,6])
mp.figure()
mp.plot([1,2,3], [1,3,2])
mp.show() # 前台画图窗口
```
