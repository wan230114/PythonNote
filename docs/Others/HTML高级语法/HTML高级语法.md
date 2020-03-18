
# 1. 插入视频
## 1.1. video标签
语法示例
```
<video src="./附件/movie.ogg" controls="controls">
your browser does not support the video tag
</video>
```
<video src="Others/HTML高级语法/附件/movie.ogg" controls="controls">
your browser does not support the video tag
</video>

定义界面大小：
```
<video id="video" width="680" controls="" preload="none">
    <source id="mp4"  src="http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4" type="video/mp4">
</video>
```
<video id="video" width="680" controls="" preload="none">
    <source id="mp4"  src="http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4" type="video/mp4">
</video>

---

# 2. 按钮事件

## 2.1. 选择文件
```html
<script language=javascript>
    var result=document.getElementById("result");
    var file=document.getElementById("file");
    //将文件以文本形式进行读入页面
    function readAsText()
    {
        var file = document.getElementById("file").files[0];
        var reader = new FileReader();
        //将文件以文本形式进行读入页面
        reader.readAsText(file);
        reader.onload = function(f)
        {
            var result=document.getElementById("result");
            //在页面上显示读入文本
            result.innerHTML=this.result;
        }
    }
</script>

<h3>请选择要读取的文本文件：</h3>
<input type="file" id="file" />
<input type="button" value="读取文本文件" onclick="readAsText()"/>

<div name="result" id="result">
    这里用来显示读取结果
</div>
```

<script language=javascript>
    var result=document.getElementById("result");
    var file=document.getElementById("file");
    //将文件以文本形式进行读入页面
    function readAsText()
    {
        var file = document.getElementById("file").files[0];
        var reader = new FileReader();
        //将文件以文本形式进行读入页面
        reader.readAsText(file);
        reader.onload = function(f)
        {
            var result=document.getElementById("result");
            //在页面上显示读入文本
            result.innerHTML=this.result;
        }
    }
</script>

<h3>请选择要读取的文本文件：</h3>
<input type="file" id="file" />
<input type="button" value="读取文本文件" onclick="readAsText()"/>

<div name="result" id="result">
    这里用来显示读取结果
</div>


## 2.2. 调用python程序
```html
<script language="javascript">     
function exec1(command) 
{     
    var ws = new ActiveXObject("WScript.Shell");      
    ws.run(command);
}     
</script>   

<div id="header">
<h1>打开python命令行</h1>
</div>

<div id="nav">
    打开python命令行 
    <input type="button" value="运行 python" οnclick="exec1('python')" />  
    调用python在这里 
    <br/> 
</div>
```

<script language="javascript">     
function exec1(command) 
{     
    var ws = new ActiveXObject("WScript.Shell");      
    ws.run(command);
}     
</script>   

<div id="nav">
    打开python命令行 
    <input type="button" value="运行 python" οnclick="exec1('python')" />  
    调用python在这里 
    <br/> 
    <iframe src="/Others/HTML高级语法/now_time.txt" name=iframe1 width='100%' height='100' frameborder='1' ></iframe>
</div>
