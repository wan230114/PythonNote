<h1>Office高级玩法</h1>

标签（空格分隔）： 我的工具

---

<span id="top"></span>
近期更新日志 [[全部日志]](#jump)

|      更新时间      | 更新内容                                               |
| :----------------: | :----------------------------------------------------- |
| 2018-4-2 14:55:52  | 创建文档，目录，将所有零散信息整合过来，完成第一步操作 |
| 2018-4-27 11:08:02 | 【1.1.1 通配符的使用】内容补充及修改                   |
> 目录
> 
> [TOC]

# 1. Word篇

## 1.1. 查找替换类操作
### 1.1.1. 通配符的使用

#### 1.1.1.1. 正则匹配选择序号数字
- 方法一：手动定义匹配规则
```
查找"`【<[0123456789]@】.`"
即可快速选中所有的"`【1】.`"，"`【2】.`"，"`【13】.`"

    示例原文：
    【1】. 223
    【2】. 342ed23
    【13】. 1231rwe
```

- 方法二：利用软件内置特殊符号
```
查找"`【^#】.`"，"`^#`"代表任意数字
此方法只能选择0~9，如"`【13】.`"则无法选中
```

- 特殊符号替换方法
```
查找输入框：
    ^e ······ 表示要查找的尾注
    ^p ······ 换行符
    ^l ······ 换行符连续

替换输入框：
    ^&表示上面查找的内容
```
应用：
- 替换特定内容为自动编号
 - 原理：复制插入域编号，替换内容选择来自剪切板内容 
 - 原文：将不连续编号替换成连续编号：Word查找替换高级玩法(09)_Word联盟
http://www.wordlm.com/html/5634.html

## 1.2. 域代码
域代码末尾，加入\#"0.0”


# 2. Excel篇
## 2.1. 文件及标签的合并处理
### 2.1.1. 批量将多个excel中的多个工作簿合并到一个excel中

- 合并多文件
> 1. 将要合并的excel放到一个文件夹中，在这个目录中新建一个excel。
> 2. 打开新建的excel。
> 3. 按alt+F11，插入一个模块。【也可以右击工作簿标签，点击选择<查看代码>】
> 4. 将下面的代码（附1，合并多文件）复制进去。
> 5. 按快捷键F5直接运行。【点击菜单栏“运行”，再点击“运行子过程”。】
> 搞定。

附1：多文件合并到单文件代码：  
【注1：第20行FileName = Dir(path & "\*.xls", vbNormal)中 \*.xls的后缀可以根据实际文件后缀更改，比如csv,xlsx。】  
【注2：待复制的工作簿标签名字不能太长，否则程序出错】  

```
Sub CombineFiles()
    Dim path            As String
    Dim FileName        As String
    Dim LastCell        As Range
    Dim Wkb             As Workbook
    Dim WS              As Worksheet
    Dim ThisWB          As String
    
    
    Dim MyDir As String
    MyDir = ThisWorkbook.path & "\"
    'ChDrive Left(MyDir, 1) 'find all the excel files
    'ChDir MyDir
    'Match = Dir$("")
    
    ThisWB = ThisWorkbook.Name
    Application.EnableEvents = False
    Application.ScreenUpdating = False
    path = MyDir
    FileName = Dir(path & "\*.xls", vbNormal)
    Do Until FileName = ""
        If FileName <> ThisWB Then
            Set Wkb = Workbooks.Open(FileName:=path & "\" & FileName)
            For Each WS In Wkb.Worksheets
                Set LastCell = WS.Cells.SpecialCells(xlCellTypeLastCell)
                If LastCell.Value = "" And LastCell.Address = Range("$A$1").Address Then
                Else
                    WS.Copy After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count)
                End If
            Next WS
            Wkb.Close False
        End If
        FileName = Dir()
    Loop
    Application.EnableEvents = True
    Application.ScreenUpdating = True
    
    Set Wkb = Nothing
    Set LastCell = Nothing
End Sub
```

- 合并多标签
> 1. 打开任意多标签excel文件
> 2. 添加一个新标签页，
> 3. 按alt+F11，插入一个模块。【也可以右击工作簿标签，点击选择<查看代码>】
> 4. 将下面的代码（附2，合并多标签）复制进去。
> 5. 按快捷键F5直接运行。【点击菜单栏“运行”，再点击“运行子过程”。】
- 合并多标签方法2：
> 1. 在excel中：数据-->新建查询-->从工作簿-->转换数据-->追加查询-->上载数据，实现单个文件多个标签页合并（可自动对齐表头，也十分方便）

附2：单文件合并到单个标签的代码：
```
Sub 合并当前工作簿下的所有工作表()
Application.ScreenUpdating = False
For j = 1 To Sheets.Count
    If Sheets(j).Name <> ActiveSheet.Name Then
        X = Range("A65536").End(xlUp).Row + 1
        Sheets(j).UsedRange.Copy Cells(X, 1)
    End If
Next
Range("B1").Select
Application.ScreenUpdating = True
MsgBox "当前工作簿下的全部工作表已经合并完毕！", vbInformation, "提示"
End Sub
```

引用：  
[[引用原文1：批量将多个excel中的多个工作簿合并到一个excel中_老石头_新浪博客]][1]  
[[引用原文2：如何快速合并单个excel表中的多个sheet的工作页-百度经验]][2]  

  [1]: http://blog.sina.com.cn/s/blog_4a40fa550100oy9y.html
  [2]: https://jingyan.baidu.com/article/19020a0ad8080d529d28422a.html

## 2.2. Excel标记颜色
Excel一次妙用技巧：  
最前面插入三列，  
第一列：筛选存在问题  a  
第二列：筛选的基因  1  
第三列：标注每一个开始的基因  1  

给特征加入底纹：  
| 描述                     | 作用区域   | 语法                               |
| ------------------------ | ---------- | ---------------------------------- |
| 构树所用基因             | `(=$F:$F)` | `=IF(COUNTIF($A$1:$A$165,F1),1,0)` |
| 给每一次开头的基因标颜色 | `(=$A:$F)` | `=IF($C1=1,1,0)`                   |
| 结构域为A等级            | `(=$G:$V)` | `=IF($M1="A",1,0)`                 |
| 结构域为B等级            | `(=$G:$V)` | `=IF($M1="B",1,0)`                 |

# 3. 附
### 3.1. 附件分享

### 3.2. 更新日志
全部更新日志 <span id="jump"></span> [⤴](#top)
|      更新时间      | 更新内容                      |
| :----------------: | :---------------------------- |
| 2018-2-11 22:36:27 | 3.3.1 Python File next() 方法 |
