/**
 * Created by zjq on 16-2-14.
 */
window.onload= function () {
    waterfall('main','box');
    var dataInt={"data":[{"src":"1.jpg"},{"src":"2.jpg"},{"src":"3.jpg"},{"src":"4.jpg"}]};
    //window.onscroll=function(){
    //    if(checkScrollSlide){
    //        var oParent=document.getElementById("main");
    //        //将数据渲染到页面底部
    //        for(var i=0;i<dataInt.data.length;i++){
    //            var oBox=document.createElement('div');
    //            oBox.className='box';
    //            oParent.appendChild(oBox);
    //            var oPic=document.createElement('div');
    //            oPic.className='pic';
    //            oBox.appendChild(oPic);
    //            var oImg=document.createElement('img');
    //            oImg.src="images/"+dataInt.data[i].src;
    //            oPic.appendChild(oImg);
    //        }
    //        waterfall('main','box');
    //    }
    //}
};

function waterfall(parent,box){
    //将main下所有class为box的元素取出来
    var oParent=document.getElementById(parent);
    var oBox=getByClass(oParent,box);
    //设置整个页面显示的列数(页面宽/box的宽)
    var oBoxW=oBox[0].offsetWidth;//每个盒子的宽度
    var cols=Math.floor(document.documentElement.clientWidth/oBoxW);
    //设置main的宽
    oParent.style.cssText='width:'+oBoxW*cols+'px;margin:0 auto';
    var hArr=[];//存放每一列高度的数组
    for(var i=0;i<oBox.length;i++){
        if(i<cols){
            hArr.push(oBox[i].offsetHeight);
        }else{
            //数组中的最小值
            var minH=Math.min.apply(null,hArr);
            //获得最小高度的索引
            var index=getMinhIndex(hArr,minH);
            //更改绝对定位
            oBox[i].style.position='absolute';
            oBox[i].style.top=minH+'px';
            oBox[i].style.left=index*oBoxW+'px';
            //更改高度
            hArr[index]+=oBox[i].offsetHeight;
        }
    }
    //console.log(hArr);
}

function  getByClass(parent,clsName){
    var boxArr=new Array(),
        oElements=parent.getElementsByTagName('*');
    for(var i=0;i<oElements.length;i++){
        if(oElements[i].className==clsName){
            boxArr.push(oElements[i]);
        }
    }
    return boxArr;
}

function getMinhIndex(arr,val){
    for(var i in arr){
        if(arr[i]==val){
            return i;
        }
    }
}
//检测是佛加载
function checkScrollSlide(){
    var oParent=document.getElementById('main');
    var oBox=getByClass(oParent,'box');
    //最后一个盒子距离页面顶部的高度
    var lastBoxH=oBox[oBox.length-1].offsetTop+Math.floor(oBox[oBox.length-1].offsetHeight/2);
    //滚轮滚走的距离+浏览器的可视高度
    var scrollTop=document.body.scrollTop||document.documentElement.scrollTop;
    var height=document.body.clientHeight||document.documentElement.clientHeight;
    return (lastBoxH<scrollTop+height)?true:false;
}
//点击CreateDream弹出对话框
$(document).ready(function(){
    $(".bg-03").click(function(){
        $(".dialog").show();
    });
});