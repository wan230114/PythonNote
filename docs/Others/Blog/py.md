
标签（空格分隔）： Python3探索

@[toc]

---
## 一、基本概念
### 1. mro序列
- MRO是一个有序列表L，在类被创建时就计算出来。
-  通用计算公式为：


		mro(Child(Base1，Base2)) = [ Child ] + merge( mro(Base1), mro(Base2),  [ Base1, Base2] )
		（其中Child继承自Base1, Base2）
		

 - 如果继承至一个基类：class B(A)
    这时B的mro序列为


			mro( B ) = mro( B(A) )
			= [B] + merge( mro(A) + [A] )
			= [B] + merge( [A] + [A] )
			= [B,A]


 - 如果继承至多个基类：class B(A1, A2, A3 ...)
	这时B的mro序列 

			mro(B)  = mro( B(A1, A2, A3 …) )
			= [B] + merge( mro(A1), mro(A2), mro(A3) ..., [A1, A2, A3] )
			= ...
 
 
- 计算结果为列表，列表中至少有一个元素即类自己，如上述示例[A1,A2,A3]。merge操作是C3算法的核心。

  

### 2. 表头和表尾：
- **表头：** 
    列表的第一个元素

- **表尾：**
	列表中表头以外的元素集合（可以为空） 
	
- 示例
列表：[A, B, C]
表头是A，表尾是B和C
### 3. 列表之间的+操作
+操作：
		
	[A] + [B] = [A, B]
	（以下的计算中默认省略）

### 3. merge操作：
- merge操作流程图：
![这里写图片描述](https://img-blog.csdn.net/20180808132005424?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE0Njc1NTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
- merge操作示例：

	    如计算merge( [E,O], [C,E,F,O], [C] )
	    有三个列表 ：  ①      ②          ③
	
	    1 merge不为空，取出第一个列表列表①的表头E，进行判断                              
	       各个列表的表尾分别是[O], [E,F,O]，E在这些表尾的集合中，因而跳过当前当前列表
	    2 取出列表②的表头C，进行判断
	       C不在各个列表的集合中，因而将C拿出到merge外，并从所有表头删除
	       merge( [E,O], [C,E,F,O], [C]) = [C] + merge( [E,O], [E,F,O] )
	    3 进行下一次新的merge操作 ......

## 二、实战测试
### 1. 计算实例1
示例：（多继承UML图，引用见参考）
![多继承UML图：](https://img-blog.csdn.net/20160912114102701?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
备注：O==object

**如何计算mro(A) ？**
    
    mro(A) = mro( A(B,C) )
    
    原式= [A] + merge( mro(B),mro(C),[B,C] )
    
      mro(B) = mro( B(D,E) )
             = [B] + merge( mro(D), mro(E), [D,E] )  # 多继承
             = [B] + merge( [D,O] , [E,O] , [D,E] )  # 单继承mro(D(O))=[D,O]
             = [B,D] + merge( [O] , [E,O]  ,  [E] )  # 拿出并删除D
             = [B,D,E] + merge([O] ,  [O])
             = [B,D,E,O]
        
      mro(C) = mro( C(E,F) )
             = [C] + merge( mro(E), mro(F), [E,F] )
             = [C] + merge( [E,O] , [F,O] , [E,F] )
             = [C,E] + merge( [O] , [F,O]  ,  [F] )  # 跳过O，拿出并删除
             = [C,E,F] + merge([O] ,  [O])
             = [C,E,F,O]
            
    原式= [A] + merge( [B,D,E,O], [C,E,F,O], [B,C])
        = [A,B] + merge( [D,E,O], [C,E,F,O],   [C])
        = [A,B,D] + merge( [E,O], [C,E,F,O],   [C])  # 跳过E
        = [A,B,D,C] + merge([E,O],  [E,F,O])
        = [A,B,D,C,E] + merge([O],    [F,O])  # 跳过O
        = [A,B,D,C,E,F] + merge([O],    [O])
        = [A,B,D,C,E,F,O]

### 2. 实例代码测试
对于以上计算，用代码来测试。
```python
class D: pass
class E: pass
class F: pass
class B(D,E): pass
class C(E,F): pass
class A(B,C): pass

print("从A开始查找：")
for s in A.__mro__:
	print(s)

print("从B开始查找：")
for s in B.__mro__:
	print(s)

print("从C开始查找：")
for s in C.__mro__:
	print(s)
```
结果：

	从A开始查找：
	<class '__main__.A'>
	<class '__main__.B'>
	<class '__main__.D'>
	<class '__main__.C'>
	<class '__main__.E'>
	<class '__main__.F'>
	<class 'object'>
	从B开始查找：
	<class '__main__.B'>
	<class '__main__.D'>
	<class '__main__.E'>
	<class 'object'>
	从C开始查找：
	<class '__main__.C'>
	<class '__main__.E'>
	<class '__main__.F'>
	<class 'object'>


## 三、总结 
每次判断如何读取都要这么麻烦计算吗？可有简单方法？
我对此做了一个简单总结。
### 1. 规律总结

<br>

**如何快速判断查找规律？**  

简单的八个字总结就是：“从一至顶，有子先出”。
一句话解释就是，从`当前查找类`的`第一个待查找父类`一直向上查找，当遇到父类还有其他子类时，且子类也是`当前查找类`的父类或父父类，则优先查找其子类，直到到达查找顶端Object类（跳过Object类），再查找`下一个待查找父类`。重复至结束所有查找。

<br>

**查找规律文字描述：**
- 取出查找类：将`当前查找子类`放入到`查找列表__mro__`，准备从`当前查找子类`向上查找它的父类
- 判断父类是否到顶端object处：
	- 若父类未到达object：
		-  判断`父类`是否包含其他子类，且子类满足是之前查找的某个元素的父类或父类的父类。
		 	- 若`父类`无其他子类，则将`父类`取出放入到`查找列表__mro__`，准备继续查找它的`父类`
			- 若`父类`有其他子类，则暂时跳过该 `父类` 的查找，将`父类`的下一个子类取出放入到`查找列表__mro__`
	- 若父类到达Object：
	 	- 判断这个子类的所有父类是否遍历完毕。
		 	- 是，则取出object，放入到`查找列表__mro__`，查找结束
		 	- 否，开始下一个父类的相同方式查找。

**查找规律流程图：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200325130631167.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE0Njc1NTM=,size_16,color_FFFFFF,t_70)
其实整个过程可以浓缩为一个入栈出栈的过程，代码可以用递归实现。但实现的流程图并不容易绘制出来，如果您有更好的想法，请留言我们大家一起共同交流。

### 2. 规律测试
#### 实例2：
对于如下继承：
![这里写图片描述](https://img-blog.csdn.net/20180806032538657?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE0Njc1NTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
通过如下判断模式：

代码测试：
```python
class A1: pass
class A2: pass
class A3: pass
class B1(A1,A2): pass
class B2(A2): pass
class B3(A2,A3): pass
class C1(B1): pass
class C2(B1,B2): pass
class C3(B2,B3): pass
class D(C1, C2, C3): pass

print("从D开始查找：")
for s in D.__mro__:
	print(s)

print("从C3开始查找：")
for s in C3.__mro__:
	print(s)
```
结果参考：
<img src="https://img-blog.csdnimg.cn/20200325095552696.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE0Njc1NTM=,size_16,color_FFFFFF,t_70" width = 75%>

- 规律解释：

| 当前类 | 最底层D的未查找的父类列表 | 预查找的父类 | 预查找父类是否是object          | 预查找父类是否还有的子类? 同时又是底层查找类的父类 | 实际取出的类 |
|--------|---------------------------|--------------|---------------------------------|----------------------------------------------------|--------------|
| D      | C1, C2, C3                | C1           | -                               | -                                                  | C1           |
| C1     | C2, C3                    | B1           | -                               | 有，C2                                             | C2           |
| C2     | C3                        | B1           | -                               | -                                                  | B1           |
| B1     | C3                        | A1           | -                               | -                                                  | A1           |
| A1     | C3                        | object       | 是，但最底层D还有父类C3未取出   | -                                                  | C3           |
| C3     | -                         | B2           | -                               | -                                                  | B2           |
| B2     | -                         | A2           | -                               | 是，B3                                             | B3           |
| B3     | -                         | A2           | -                               | -                                                  | A2           |
| A2     | -                         | object       | 是，最底层D已经没有父类未取出了 | 是，A3                                             | A3           |
| A3     | -                         | object       | 是                              | -                                                  | object       |

#### 实例3：
```python
r"""
    O
 /  |  \
A1  A2  A3
|   | \ |
|   |  \|
B1  B2  B3
| \ | \  
|  \|  \
C1  C2  C3
 \  |   /
    D
"""

class A1: pass
class A2: pass
class A3: pass

class B1(A1):pass
class B2(A2):pass
class B3(A2,A3):pass

class C1(B1):pass
class C2(B1, B2):pass
class C3(B2):pass

class D(C1, C2, C3):pass

print(*D.__mro__, sep='\n')
```
运行结果：
```python
<class '__main__.D'>
<class '__main__.C1'>
<class '__main__.C2'>  # C2是C1父类的子类，优先查找
<class '__main__.B1'>
<class '__main__.A1'>
<class '__main__.C3'>  # D还有父类C3待查找，暂时跳过Object
<class '__main__.B2'>
<class '__main__.A2'>
<class 'object'>   # B3、A3不是D的父类，所以不加入查找列表
```

## 四、参考
python多重继承C3算法 - CSDN博客
https://blog.csdn.net/fmblzf/article/details/52512145
【Python】C3算法 - foreverlove~ - 博客园
https://www.cnblogs.com/bashaowei/p/8508276.html