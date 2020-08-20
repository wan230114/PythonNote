$(document).ready(function(){
	//1.首先将#goTopBtn隐藏
	$("#goTopBtn").hide();

	//2.给窗口添加事件：滚动时触发
	$(window).scroll(function(){
		//当滚动条的位置处于距顶部0像素以上时，返回顶部按钮出现，否则消失
		if ($(window).scrollTop()>0){
			$("#goTopBtn").fadeIn(1500);
			}
		else{
			$("#goTopBtn").fadeOut(1500);
			}
	});
	
	//3.当点击返回顶部按钮后，回到页面顶部位置
	$("#goTopBtn").click(function(){
		$('body,html').animate({scrollTop:0},1000);
	});
	$(".title").mouseenter(function(){
		$(this).find('img[class="arrow"]').show();
	});
	$(".title").mouseleave(function(){
		$(this).find('img[class="arrow"]').hide();
	});
});
$(document).ready(function(){
		$(function(){
		//纵向，默认，移动间隔2
		$('div.albumSlider').albumSlider();
		//横向设置
		$('div.albumSlider-h').albumSlider({direction:'h',step:3});
	});
});
$(document).ready(function() {
		/*
		*   Examples - images
		*/

		$("a#example1").fancybox();

		$("a#example2").fancybox({
			'overlayShow'	: false,
			'transitionIn'	: 'elastic',
			'transitionOut'	: 'elastic'
		});
		$("a#example3").fancybox({
			'transitionIn'	: 'none',
			'transitionOut'	: 'none'	
		});

		$("a#example4").fancybox({
			'opacity'		: true,
			'overlayShow'	: false,
			'transitionIn'	: 'elastic',
			'transitionOut'	: 'none'
		});

		$("a#example5").fancybox();

		$("a#example6").fancybox({
			'titlePosition'		: 'outside',
			'overlayColor'		: '#000',
			'overlayOpacity'	: 0.9
		});

		$("a#example7").fancybox({
			'titlePosition'	: 'inside'
		});

		$("a#example8").fancybox({
			'titlePosition'	: 'over'
		});

		$("a[rel=example_group]").fancybox({
			'transitionIn'		: 'none',
			'transitionOut'		: 'none',
			'titlePosition' 	: 'over',
			'titleFormat'		: function(title, currentArray, currentIndex, currentOpts) {
				return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
			}
		});

		/*
		*   Examples - various
		*/

		$("#various1").fancybox({
			'titlePosition'		: 'inside',
			'transitionIn'		: 'none',
			'transitionOut'		: 'none'
		});

		$("#various2").fancybox();

		$("#various3").fancybox({
			'width'				: '75%',
			'height'			: '75%',
			'autoScale'			: false,
			'transitionIn'		: 'none',
			'transitionOut'		: 'none',
			'type'				: 'iframe'
		});

		$("#various4").fancybox({
			'padding'			: 0,
			'autoScale'			: false,
			'transitionIn'		: 'none',
			'transitionOut'		: 'none'
		});
	});
$(document).ready(function(){
	//+-替换
	$("#zhankai").toggle(function(){
			$(this).html("<b>展开目录</b>");
			var sq=$(".shouqi");
			for(i=0;i<sq.length;i++){
				sq.eq(i).html(sq.eq(i).html().replace("arrow_up.png","arrow_down.png"))
			}
			$(".lanmu-content").css("display","none")
		},function(){
			$(this).html("<b>收起目录</b>");
			var sq=$(".shouqi");
			for(i=0;i<sq.length;i++){
				sq.eq(i).html(sq.eq(i).html().replace("arrow_down.png","arrow_up.png"))
			}
			$(".lanmu-content").css("display","block")
		})
		
		/*开关*/
		$("#kaiguan").toggle(function(){
			$(this).html("<b>【目录】</b>");
			$("#zhankai").html("")
			$(".mulu").width("60px")
			$("#zhankai").width("0")
			$("#kaiguan").css({"text-align":"left","margin":"0","padding":"padding"})
			$("#main").width("90%");
			$("#left").css({"display":"none"})
		},function(){
			$(this).html("<b>【关闭】</b>");
			$("#zhankai").html("<b>展开目录</b>")
			$(".mulu").width("17.5%")
			$("#main").width("78%")
			$("#left").css({"display":"block"})
		})
		
});
//收起栏目
$(document).ready(function(){
		$(".title").mousedown(function(){
			var re1 = /arrow_down.png/g; 
			var re2 = /arrow_up.png/g; 
			var re3 = /arrow_right.png/g; 
			if($(this).html().match(re1)){
				$(this).html($(this).html().replace("arrow_down.png","arrow_up.png"))
				$(this).next().fadeIn("2500")
				return
			}
			if($(this).html().match(re2)){
				$(this).html($(this).html().replace("arrow_up.png","arrow_down.png"))
				$(this).next().fadeOut("2500")
				return
			}
			if($(this).html().match(re3)){
				$(this).find('a[class="shouqi"]').click();
				return
			}
		})
		$(".lanmu-list a").click(function(){
			$(".lanmu-list a").removeClass("current")
			$(this).addClass("current"); 
		})
});
