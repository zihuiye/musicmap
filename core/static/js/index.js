$("#musicmap").css('height',$(window).height()-50);
$(window).resize(function() {
  $("#musicmap").css('height',$(window).height()-50);
});
//显示对话框的函数
function showModal(){
  $('#exampleModal').modal()
}
//检查url地址的正确性，并提取musicid
function checkurl(){
  var urlExp=/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- .\/?%&=]*)?/;
  //var urlExp=/(((^https?:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)$/g
  var urlExpObj=new RegExp(urlExp);
  var id;
  if(urlExpObj.test($("#music-url").val())){
    var songExpObj = new RegExp("(^|&)id=([^&]*)(&|$)");
    id = $("#music-url").val().match(/[^\?]+\?id=([^#|&]*)/,'$1')[1];
    $("#musicid").attr("value",id);
    var musicplayer = '<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id='+id+'&auto=0&height=66"></iframe>'
    $("#player").html(musicplayer);
  }else{
    $("#player").text('不是正确的网址,请检查!');
  }
  console.log(urlExpObj.test($("#music-url").val()));
  console.log($("#music-url").val());

}
//在地图上添加地标标签
function addMusicMarker(name,lat,lng,email,datetime,text,filename){
  var sContent =
    "<div>"+
    "<h5>"+"上传者："+email+"</h5>"+
    "<h5>"+"上传时间："+datetime+"</h5>"+
    "<p>"+"留言："+text+"</p>"+
    "<h4>"+name+"</h4>"+
  	'<audio src="/media/'+filename+'" controls="controls">' +
  	"</div>";
    var point = new BMap.Point(lng,lat);
    var marker = new BMap.Marker(point);
    var infoWindow = new BMap.InfoWindow(sContent);
    map.addOverlay(marker);
    marker.addEventListener("click", function(){
    	   this.openInfoWindow(infoWindow);
    	   //图片加载完毕重绘infowindow
    	  //  document.getElementById('imgDemo').onload = function (){
    		//    infoWindow.redraw();   //防止在网速较慢，图片未加载时，生成的信息框高度比图片的总高度小，导致图片部分被隐藏
    	  //  }
    	});
}


// 百度地图API功能
var map = new BMap.Map("musicmap");    // 创建Map实例
map.centerAndZoom('香港', 11);  // 初始化地图,设置中心点坐标和地图级别
map.addControl(new BMap.MapTypeControl());   //添加地图类型控件
map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放



//创建右键菜单 添加右击事件
map.addEventListener("rightclick",function(e){
    var geoc = new BMap.Geocoder();
    geoc.getLocation(e.point, function(rs){
			var addComp = rs.addressComponents;
      $("#location").val(addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber);
      $("#lat").val(e.point.lat);
      $("#lng").val(e.point.lng);
			console.log(addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber);
		  console.log(e.point.lng + "," + e.point.lat);
	});
});
//设置菜单的内容
var menu = new BMap.ContextMenu();
var txtMenuItem = [
		{
			text:'这此添加音乐',
			callback:function(){showModal()}
		}
	];
for(var i=0; i < txtMenuItem.length; i++){
	menu.addItem(new BMap.MenuItem(txtMenuItem[i].text,txtMenuItem[i].callback,100));
}
map.addContextMenu(menu);

var moved = false;
var zoomed = false;
var longpress = false;

map.addEventListener("touchmove",function(e){
  moved = true;
});

map.addEventListener("resize",function(e){
  zoomed = true;
});

map.addEventListener("touchend",function(e) {
  if ( longpress && !moved && !zoomed){
    var geoc = new BMap.Geocoder();
    geoc.getLocation(e.point, function(rs){
      var addComp = rs.addressComponents;
      $("#location").val(addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber);
      $("#lat").val(e.point.lat);
      $("#lng").val(e.point.lng);
      console.log(addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber);
      console.log(e.point.lng + "," + e.point.lat);
    });
    showModal();
  }
  longpress = false;
  moved = false;
  zoomed = false;
});

map.addEventListener("longpress",function(e){
  longpress=true;
});

//加载完之后取数据库中的音乐数据并添加到地图中
$(document).ready(function(){
  $.ajax({url:"music",
    type:"get",
    dataType:"json",
    success:function(data){
      for (var i = 0; i < data.length; i++) {
        addMusicMarker(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][9]);
      }
      console.log(data);
    },
  });
});
