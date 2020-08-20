
[JS计算元素的距离-问答-阿里云开发者社区-阿里云](https://developer.aliyun.com/ask/76988?spm=a2c6h.13159736)

document.getElementById('xx').getBoundingClientRect().top
题主要的是这个哈，刚好前阵子也用到过记得。

## 记一次解决目录自动随内容滚动的问题过程

```js
$(function(){
  document.scroll(function() {
    tocify_item_list_group_item = document.getElementsByTagName("li")
    for (var i=0,len=tocify_item_list_group_item.length; i<len; i++)
    { 
        if (tocify_item_list_group_item[i].className == "tocify-item list-group-item active"){
            $("#TOC").scrollTop(tocify_item_list_group_item[i].getBoundingClientRect().top);
        }    
    }
  });
});
```

滚动时触发
[.scroll()——元素滚动时触发，或元素发生滚动的时候执行的函数 - 念念念不忘 - 博客园](https://www.cnblogs.com/SongHuiJuan/p/6871763.html)
```js
// [.scroll()——元素滚动时触发，或元素发生滚动的时候执行的函数 - 念念念不忘 - 博客园](https://www.cnblogs.com/SongHuiJuan/p/6871763.html)
x=0;
$(function(){
  $("div").scroll(function() { //当div发生滚动的时候执行
    $("span").text(x+=1);  //div发生滚动数字就+1
  });
  $("button").click(function(){
    $("div").scroll(); //点击按钮触发滚动事件
  });
});
```

多次滚动只触发一次
```js
(function() {
    var finished = true;
    function loadData() {
        //xxxx
        finished = true;
    }
    dom.onscroll = function() {
        if(finished && this.scrollHeight - this.clientHeight == this.scrollTop) {
            finished = false;
            loadData();
        }
    }
})();
```

只监听最后一次滚动
[Javascript监听滚动条滚动停止 - 知乎](https://zhuanlan.zhihu.com/p/146166159?from_voters_page=true)
```js
let t1 = 0;
let t2 = 0;
let timer = null; // 定时器

// scroll监听
document.onscroll = function() {
  clearTimeout(timer);
  timer = setTimeout(isScrollEnd, 1000);
  t1 = document.documentElement.scrollTop || document.body.scrollTop;
}

function isScrollEnd() {
  t2 = document.documentElement.scrollTop || document.body.scrollTop;
  if(t2 == t1){
    console.log('滚动结束了')
  }
}
```

整合
```html
<script type="text/javascript">
    $(function () {
        $(window).scroll(function () {
            var tocify_item_list_group_item = document.getElementsByTagName("li")
            var tocify_item_list_group_item_offset = 0
            for (var i = 0, len = tocify_item_list_group_item.length; i < len; i++) {
            if (tocify_item_list_group_item[i].className == "tocify-item list-group-item active") {
                tocify_item_list_group_item_offset = tocify_item_list_group_item[i].getBoundingClientRect().top;
                break
            }
            };
            $("#TOC").scrollTop(tocify_item_list_group_item_offset)
        });
    });

    // let t1 = 0;
    // let t2 = 0;
    // let timer = null; // 定时器

    // // scroll监听
    // document.onscroll = function () {
    //   clearTimeout(timer);
    //   timer = setTimeout(isScrollEnd, 10);
    //   t1 = document.documentElement.scrollTop || document.body.scrollTop;
    // }

    // function isScrollEnd() {
    //   t2 = document.documentElement.scrollTop || document.body.scrollTop;
    //   if (t2 == t1) {
    //     // console.log('滚动结束了')
    //     var tocify_item_list_group_item = document.getElementsByTagName("li")
    //     var tocify_item_list_group_item_offset = 0
    //     for (var i = 10, len = tocify_item_list_group_item.length; i < len; i++) {
    //       if (tocify_item_list_group_item[i].className == "tocify-item list-group-item active") {
    //         tocify_item_list_group_item_offset = tocify_item_list_group_item[i].getBoundingClientRect().top;
    //         break
    //       }
    //     };
    //     $("#TOC").scrollTop(tocify_item_list_group_item_offset)
    //   }
    // }

    // var x = 1;
    // var winH = $(window).height();//页面的高度
    // var timer = null
    // $(window).on("scroll", function () {
    //   clearTimeout(timer);
    //   scrollTop = $(window).scrollTop(); //滚动条距离顶部的距离
    //   offSetTop = $(".container>.fl>.box:last").offset().top;//在页面中的位置
    //   //console.log(offSetTop < (winH + scrollTop));
    //   if (isVisible(".container>.fl>.box:last")) {
    //     x = ++x;
    //     var ddiv = `<div class = "box"> ${x} </div>`;
    //     timer = setTimeout(function () {
    //       $(".container>.fl").append(ddiv);
    //       console.log("出现在视野里");
    //     }, 1000);
    //   };
    // });

    // function isVisible(el) {
    //   if ($(el).offset().top < (winH + scrollTop))
    //     return true;
    // };
</script>

```

最终解决方案
```html
    <!-- 解决tocify无法自动滚动的问题 -->
    <script type="text/javascript">
      var tocify_item_list_group_item_offset = 0
      function scroll_menu() {
        var tocify_item_list_group_item = document.getElementsByTagName("li")
        for (var i = 0, len = tocify_item_list_group_item.length; i < len; i++) {
          if (tocify_item_list_group_item[i].className == "tocify-item list-group-item active") {
            $("#TOC").scrollTop(0)
            tocify_item_list_group_item_offset = tocify_item_list_group_item[i].getBoundingClientRect().top;
            // console.log(tocify_item_list_group_item_offset)
            break
          }
        };
        // console.log(tocify_item_list_group_item)
        // console.log(i, tocify_item_list_group_item[i])
        // console.log(tocify_item_list_group_item_offset)
        $("#TOC").scrollTop(tocify_item_list_group_item_offset - 100)
      }

      function debounce(fun, t, immediate) {
        var timeout;
        //返回真正的scroll事件的事件处理程序
        return function (event) {
          var that = this, arg = arguments;
          var later = function () {
            timeout = null;
            if (!immediate) fun.apply(that, arguments);
          };
          var callNow = immediate && !timeout;//这一句位置很重要
          clearTimeout(timeout);
          timeout = setTimeout(later, t);
          if (callNow) {
            fun.apply(that, arguments);
          }
        }
      };

      var myEfficientFn = debounce(function () {
        // 滚动中的真正想要执行的代码
        scroll_menu()
        // console.log('ok' + new Date());
      }, 10, false);

      // 绑定监听
      window.addEventListener('scroll', myEfficientFn);

    </script>

```