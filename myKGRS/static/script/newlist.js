var bannerimg = $(".head .banner>div");
var smallbutton = $(".smallbutton>li");
var index = 0;
var dingshiqi;
zidong();
zhiding();
function imgqie(index){
	$.each(bannerimg,function(i,val){
		$(this).removeClass("show");
		$(this).addClass("hide");
		$(smallbutton[i]).addClass("btnstylehide");
	})
	$(bannerimg[index]).addClass("show");
	$(smallbutton[index]).removeClass("btnstylehide");
	$(smallbutton[index]).addClass("btnstyleshow");
}
function zidong(){
	dingshiqi=setInterval(function(){
		if(index==bannerimg.length-1){
			index=0;
			imgqie(index);
		}else{
			index++;
			imgqie(index);
		}
	},4000)
}
function zhiding(){
	$.each(smallbutton,function(i,val){
		$(val).click(function(){
			clearInterval(dingshiqi);
			index=i;
			imgqie(index);
			zidong();
		})
	})
}