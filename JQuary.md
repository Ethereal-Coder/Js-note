### 页面加载事件

- 页面中所有的内容加载完毕后才触发

  ```javascript
  window.onload=function () { };
  $(window).load(function () { });
  ```

- 页面中的基本的标签加载完毕后就可以触发
  ```javascript
  $(document).ready(function () { });
  ```

- 页面中基本的标签加载后就执行

  ```javascript
  jQuery(function () { });
  $(function () { });
  ```

### JQuery对象与DOM对象互转

-  DOM对象转jQuery对象:

  `$(DOM的对象)----->jQuery对象`

  ```javascript
  var btnObj= document.getElementById("btn");
  btnObj.onclick=function () {
  	this.style.backgroundColor="red";
  };
  //----------
  $(btnObj).click(function () {
  	$(this).css("backgroundColor","red");
  });
  ```

 -  jQuery对象转DOM对象:

    1. `$("#btn")[0]---->DOM对象`

    2. `$("#btn").get(0)---DOM对象`

       ```js
       var btnObj=document.getElementById("btn");//DOM对象
       var obj= $(btnObj).get(0);//DOM对象
       obj.onclick=function () {
       	this.style.backgroundColor="green";
       };
       //---------------
       var btnObj=document.getElementById("btn");//DOM对象
       var obj= $(btnObj)[0];//DOM对象
       obj.onclick=function () {
       	this.style.backgroundColor="green";
       };
       ```

       ```javascript
       $("#btn").click(function () {  //$("#btn") ---> jQuery对象
       	$(this).css("backgroundColor","yellow");
        });
       //-------------
       $("#btn").onclick=function () {
       	this.style.backgroundColor="red";
       };
       //--------------
       $("#btn").get(0).onclick=function () {
       	this.style.backgroundColor="red";
       };
       ```


### 网页开关灯实现-CSS

```javascript
//点击按钮设置body的背景颜色,实现网页开关灯的效果
//DOM的方式来操作
window.onload=function () {
  //获取按钮,注册点击事件,设置body的背景颜色
  document.getElementById("btn").onclick=function () {
    //判断--->按钮的value值如果是关灯,则body的背景颜色为黑色
    if(this.value=="关灯"){
      document.body.style.backgroundColor="black";
      this.value="开灯";
    }else{
      document.body.style.backgroundColor="white";
      this.value="关灯";
    }
    //如果按钮的value值为开灯，则body的背景颜色为白色
  };
};
```

```javascript
//页面的加载事件
$(function () {
  //获取按钮,注册点击事件
  $("#btn").click(function () {
    //.val()方法--->获取按钮的value属性的值
    //.val("内容");是设置按钮的value属性的值
    if($(this).val()=="关灯"){
      $("body").css("backgroundColor","black");
      $(this).val("开灯");
    }else{
      $("body").css("backgroundColor","white");
      $(this).val("关灯");
    }
  });
});
```

### JQuery中的选择器

```java
DOM中获取元素的方式:
  document.getElementById("id的值");根据id获取元素,一个
  document.getElementsByTagName("标签的名字");根据标签的名字获取元素,多个
  document.getElementsByName("name属性的值");根据name属性的值获取元素,多个
  document.getElementsByClassName("类样式的名字");根据的是类样式的名字来获取元素,多个
  ...

jQuery获取元素的方式:通过各种选择器来获取元素
  根据id来获取--->id选择器  ---->$("#id的值");一个
  根据标签的名字来获取---标签选择器--->$("标签的名字");多个
  根据类样式的名字获取--->类选择器--->$(".类样式的名字");多个
  ...
```



#### id选择器

```html
<script>
  //点击按钮,设置层中的显示内容为:这是一个层,同时设置这个层的背景颜色(id选择器)

  //页面加载的事件
  $(function () {
    //获取按钮--根据id选择器获取,调用点击事件的方法
    $("#btn").click(function () {
      //设置div中的显示内容
      $("#dv").text("这是一个有颜色的div");//相当于DOM中的innerText或者是textContent
      $("#dv").css("backgroundColor","yellow");//设置元素的样式
    });
  });
</script>
```



#### 标签选择器

```html
<script>
  //点击按钮,设置多个p标签中显示内容为:我们都是p(标签选择器)

  //页面的加载事件
  $(function () {
    //获取按钮,调用点击事件,获取所有的p,设置内容
    $("#btn").click(function () {
      //获取所有的p--->标签选择器
      $("p").text("我们都是p");
    });
  });
</script>
```



#### 类选择器

```html
<script>
  //点击按钮,设置页面上应用cls类样式的元素的背景颜色(类选择器)
  //页面加载的事件
  $(function () {
    //获取按钮,调用点击事件,获取所有应用了cls类样式的元素
    $("#btn").click(function () {
      //类选择器来获取元素
      $(".cls").css("backgroundColor","green");
    });
  });
</script>
```



#### 标签+类选择器

```html
<script>
  //点击按钮设置页面上应用cls类样式li标签的背景颜色
  //页面加载的事件
  $(function () {
    //获取按钮,注册点击事件
    $("#btn").click(function () {
      //获取应用cls类样式的li标签
      //标签+类样式的选择器
      $("li.cls").css("backgroundColor","yellow");
    });
  });
</script>
```



#### 多条件选择器

```html
<script>

  //点击按钮,设置页面中的span标签,li标签,div标签的背景颜色

  $(function () {
    //通过多条件选择器获取元素,统一设置背景颜色
    $("#btn").click(function () {
      $("span,p,li,div").css("backgroundColor","yellow");
    });
  });
</script>
```



#### 层次选择器

```javascript
$(function () {
  //获取div中的相关元素
  $("#btn").click(function () {
    //获取的是div中所有的p标签元素
    $("#dv p").css("backgroundColor","red");
    //获取的是div中直接的子元素
    $("#dv>p").css("backgroundColor","red");
    //获取的是div后面的第一个p标签元素
    $("#dv+p").css("backgroundColor","red");
    //获取的是div后面所有直接的兄弟元素p标签元素
    $("#dv~p").css("backgroundColor","red");
  });
});
```

```html
<script>
  //页面加载后获取ul标签中的所有的li标签
  $(function () {
    //根据层次选择器获取li
    $("#uu>li").mouseover(function () {
      //鼠标进入
      $(this).css("backgroundColor","red");
    });
    $("#uu>li").mouseout(function () {
      //鼠标离开
      $(this).css("backgroundColor","");
    });
  });

  $(function () {
    $("#btn").click(function () {
      // *就是所有的元素
      $("#dv *").css("backgroundColor","yellow");
    });
  });
</script>
```

```html
<script>
  $(function () {
    $("#btn").click(function () {
      //偶数的li
      $("#uu>li:even").css("backgroundColor","yellow");//偶数的li
      $("#uu>li:odd").css("backgroundColor","red");//奇数的li
    });
  });
</script>
```

```html
<script>
  $(function () {
    //找到id为u1的下面的li里面的ul里面的li全部隐藏
    $("#u1>li>ul>li").hide();
    //找到id为ul的直接的子元素li,注册鼠标点击的事件
    $("#u1>li").click(function () {
      //siblings
      $(this).siblings("li").children("ul").find("li").hide(500);
      //当前的li中的ul中的所有的li显示
      $(this).children("ul").find("li").show(500);
    });
  });
</script>
```



#### 索引选择器

```javascript
//获取ul中的索引为4的li标签元素
$("#uu>li:eq(4)").css("backgroundColor","red");
//获取ul中的索引大于4的所有的li标签元素
$("#uu>li:gt(4)").css("backgroundColor","red");
//获取ul中的索引小于4的所有的li标签元素
$("#uu>li:lt(4)").css("backgroundColor","red");
```



### 常用方法1

#### .val()

```javascript
$("#txt").val("哈哈,我又变帅了");
console.log($("#txt").val());
/*
 * .val()方法，小括号中写内容就是设置元素的value属性
 * .val()方法,小括号中什么也不写,获取元素的value属性的值
 * 就是元素的value属性
* */
```



#### .css()

```javascript
//.css();方法,该方法如果只是设置一个样式的属性和值,那么这个方法写两个参数,第一个参数是属性,第二个参数是值
$("#dv").css("backgroundColor","yellow");
//.css();方法,里面可以直接写键值对的方式
$("#dv").css({"width":"300px","height":"200px","backgroundColor":"yellow"});
```



#### .html()

```javascript
//.html();小括号中可以直接写标签的字符串内容,就是设置div中的元素内容
//.html();小括号中什么也没有,表示的时候获取div中的元素内容
$("#dv").html("<p>这是一个p标签</p>");
console.log($("#dv").html());
//.html()方法相当于DOM中的innerHTML
```



#### .text()

```javascript
//.text();如果小括号中写内容,就是设置文字内容
//如果.text();小括号什么也不写,表示的是获取这个元素中的文字内容
$("#dv").text("这是一个div");//设置
console.log($("#dv").text());//获取
//.text()方法相当于DOM中的innerText
```



### 操作类样式

```javascript
$(function () {
  //获取按钮,点击按钮,为div添加一个类样式
  $("#btn").click(function () {
    $("#dv").addClass("cls");//在addClass方法中类样式的名字前面没有点(.)
    $("#dv").addClass("cls").addClass("cls2");

    //另一种写法,addClass添加样式的时候.多个类样式的名字中间用空格隔开
    $("#dv").addClass("cls cls2");
  });

  $("#btn2").click(function () {
    //移除一个元素的类样式
    $("#dv").removeClass("cls");
    //移除div的所有的类样式,removeClass方法中什么也不写移除的是当前元素的所有的类样式
    $("#dv").removeClass();
  });
  
  //点击按钮查询这个div是否应用了cls类样式
  $("#btn3").click(function () {
    var result=$("#dv").hasClass("cls");
    console.log(result);
  });
});
```



### 网页开关灯实现-Class

```javascript
//页面加载后点击按钮实现开关灯的效果
$(function () {
  $("#btn").click(function () {
    //先判断body是否应用了某个类样式,如果应用了就移除,如果没有应用就让body应用这个类样式
    if($("body").hasClass("cls")){
      //应用了--移除该类样式
      $("body").removeClass("cls");
      $(this).val("关灯");

    }else{
      //没有应用--让body添加这个类样式
      $("body").addClass("cls");
      $(this).val("开灯");
    }
  });

  //更简单的代码
  $("#btn").click(function () {
    $("body").toggleClass("cls");//切换类样式
  });

});
```



### CSS方法与类样式区别

```javascript
/*
*
* .css()
* .css("属性","属性值");
* .css("属性","属性值").css("属性","属性值");
* .css({"属性":"属性值","属性":"属性值"});
* addClass()
* addClass("类样式名字");添加一个类样式
* addClass("类样式名字1 类样式名字2");
* removeClass()
* removeClass("类样式名字");移除类样式
* removeClass();移除的是当前元素中所有的类样式
* hasClass();判断当前元素是否应用了某个类样式
* toggleClass();切换元素的类样式的
*
* */
```



### 链式编程

```javascript
//获取列表中每个li,当鼠标进入后,当前的li有高亮显示,点击的时候可以让当前被点击的li的字体变大,字体的颜色改变,改变字体
$(function () {
  $("#uu>li").mouseover(function () {
    $(this).css("backgroundColor","red").siblings("li").css("backgroundColor","");
  }).click(function () {
    $(this).css("fontSize","50px").css("color","green").css("fontFamily","全新硬笔行书简");
  });
});

```

```javascript
//断链:对象调用方法,返回的不是当前的对象,再调用方法,调用不了,
//解决断链--->恢复到断链之前的一个效果--修复断链
//.end()方法恢复到断链之前的效果
               $(this).prevAll().css("backgroundColor","yellow").end().nextAll().css("backgroundColor","blue");
```



### 获取兄弟元素

```javascript
$("#uu>li").mouseenter(function () {
  //.next();获取的是当前元素的下一个兄弟元素
  $(this).next().css("backgroundColor","green");
  //.nextAll();获取的是当前元素的后面的所有的兄弟元素
  $(this).nextAll().css("backgroundColor","green");
  //.prev();获取的是当前元素的前一个兄弟元素
  $(this).prev().css("backgroundColor","green");
  //.prevAll();获取的是当前元素的前面的所有的兄弟元素
  $(this).prevAll().css("backgroundColor","green");
  //.siblings();获取的是当前元素的所有的兄弟元素(自己除外)
  $(this).siblings().css("backgroundColor","green");
});
```



### 常见动画方法

```javascript
$(function () {
  //点击按钮 隐藏div
  $("#btnHide").click(function () {
    //$("#dv").hide();//隐藏
    //hide方法中可以写参数:参数类型:1.数字类型,2字符串类型
    //1数字类型:1000表示的是毫秒  ---1秒
    //2字符串类型: "slow"  "normal"  "fast"
    $("#dv").hide(1000);
    //$("#dv").hide("normal");
  });
  $("#btnShow").click(function () {
    //$("#dv").show();//显示
    //show方法中可以写参数:参数类型:1.数字类型,2字符串类型
    //1数字类型:1000表示的是毫秒  ---1秒
    //2字符串类型: "slow"  "normal"  "fast"
    //$("#dv").show(1000);
    $("#dv").show("fast");
  });
});
```

```javascript
$(function () {
  //slideUp和slideDown和slideToggle方法中都可以写参数
  //参数:可以写数字类型  1000毫秒---1秒
  //参数:字符串:  slow   normal  fast
  //点击第一个按钮
  $("#btn1").click(function () {
    $("#dv").slideUp(1000);
  });
  //点击第二个按钮
  $("#btn2").click(function () {
    $("#dv").slideDown(1000);
  });
  //点击第三个按钮
  $("#btn3").click(function () {
    $("#dv").slideToggle(1000);
  });

});
```

```javascript
// 淡入淡出
$(function () {
  //slow  normal  fast
  $("#btn1").click(function () {
    $("#dv").fadeIn(1000);
  });
  //点击第二个按钮
  $("#btn2").click(function () {
    $("#dv").fadeOut(1000);
  });
  //点击第三个按钮
  $("#btn3").click(function () {
    $("#dv").fadeToggle(1000);
  });

  $("#btn4").click(function () {
    //一秒钟 透明度达到0.3
    $("#dv").fadeTo(1000,0.3);
  });
});
```

```javascript
$(function () {
  $("#btn1").click(function () {
    //获取div,最后一个图片,隐藏
    $("div>img").last("img").hide(800,function () {
      //arguments.callee相当于递归
      $(this).prev().hide(800,arguments.callee);
    });
  });
  //显示
  $("#btn2").click(function () {
    $("div>img").first("img").show(800,function () {
      //arguments.callee相当于递归
      $(this).next().show(800,arguments.callee);
    });
  });
});
```

```javascript
$(function () {
  //获取.wrap下面的ul中的li,注册鼠标进入和离开的事件
  $(".wrap>ul>li").mouseover(function () {
    //鼠标进入
    $(this).children("ul").stop().show(500);//显示
  });
  $(".wrap>ul>li").mouseout(function () {
    //鼠标离开
    $(this).children("ul").stop().hide(500);//显示
  });
  // .stop() 方法用来停止动画
});
```



### 动态

```javascript
/*
* animate方法
* 参数:
* 1.是键值对---对象
* 2.时间---1000毫秒---1秒
* 3.匿名函数---回调函数
*
* */
$("#dv").animate({"width":"300px","height":"300px","left":"300px"},1000,function () {
  $("#dv").animate({"width":"50px","height":"30px","left":"800px","top":"300px","opacity":0.2},2000);
});
```

### 创建元素

```javascript
/*
*
* DOM中创建元素:
* 1.document.write("标签代码");缺陷:页面加载后创建元素,把页面中原有的内容全部的干掉
* 2.innerHTML
* 3.document.createElement("标签的名字")
*
* jQuery中创建元素的方式:
* 1.$("标签的代码")
* 2.对象.html("标签的代码");
*
* */
```

```javascript
//需求:点击按钮,在div中创建一个超链接
$(function () {
  var i=0;
  $("#btn").click(function () {
    i++;
    //创建元素
    var aObj=$("<a href='http://www.baidu.com'>百度"+i+"</a>");
    //把元素添加到div中
    $("#dv").append(aObj);//把超链接追加到div中
    //把元素插入到某个元素的前面
    $("#dv").prepend(aObj);
    
    //把元素添加到当前元素的后面(兄弟元素来添加)
    $("#dv").after(aObj);
    //把元素添加到当前元素的前面(兄弟元素来添加)
    $("#dv").before(aObj);

  });
});
```

```javascript
$(function () {
  //点击按钮把第一个div中的元素添加到第二个div中
  $("#btn").click(function () {
    // append方法把元素添加到另一个元素中的时候,
    // 有剪切的效果
    $("#dv2").append($("#dv1>p"));
  });
});
```

```javascript
$(function () {
  //第一个按钮:获取按钮添加点击事件,获取第一个下拉框中被选中的option添加到第二个下拉框
  $("#toRight").click(function () {
    $("#se2").append($("#se1>option:selected"));
  });

  //第二个按钮
  $("#toLeft").click(function () {
    $("#se1").append($("#se2>option:selected"));
  });
  //第三个按钮
  $("#toAllRight").click(function () {
    $("#se2").append($("#se1>option"));
  });
  //第四个按钮
  $("#toAllLeft").click(function () {
    $("#se1").append($("#se2>option"));
  });
});
```

```javascript
//需求:点击按钮把一个p标签添加到一个div中
$(function () {
  $("#btn").click(function () {
    //创建p标签
    var pObj= $("<p></p>");
    pObj.text("哈哈哈,我又变帅了");
    //$("#dv").append(pObj);
    //把pObj对象主动的加到div中
    pObj.appendTo($("#dv"));
  });
});
```



```javascript
$(function () {
  //点击按钮创建一个p标签加入到div中
  $("#btn").click(function () {
    $("#dv").html("<p>这是一个p标签</p>");
  });
});
```

```javascript
// 动态创建表格
var datas = [
  {
    name: "传智播客",
    url: "http://www.itcast.cn",
    type: "IT最强培训机构"
  },
  {
    name: "黑马程序员",
    url: "http://www.itheima.com",
    type: "大学生IT培训机构"
  },
  {
    name: "传智前端学院",
    url: "http://web.itcast.cn",
    type: "前端的黄埔军校"
  }];

//页面加载后,点击按钮,遍历数组,获取数组中的元素内容,创建行和列,加入到表格中的tbody中
$(function () {
  $("#btnCreate").click(function () {
    //遍历数组
    for(var i=0;i<datas.length;i++){
      var obj=datas[i];//数组中的每一个对象
      //创建行和列,加入到tbody中
      $("<tr><td><a href="+obj.url+">"+obj.name+"</a></td>      <td>"+obj.type+"</td></tr>").appendTo($("#tbd"));
    }
  });
});


$(function () {
  $("#btnCreate").click(function () {
    var arr=[];
    //遍历数组
    for(var i=0;i<datas.length;i++){
      var obj=datas[i];//数组中的每一个对象
      //创建行和列,加入到tbody中
      arr.push("<tr><td><a href="+obj.url+">"+obj.name+"</a></td>      <td>"+obj.type+"</td></tr>");
    }
    $("#tbd").html(arr);
  });
});
```



### 常用方法2

##### 清空元素内容

##### 移除元素

##### 克隆元素

```javascript
$(function () {
  //点击按钮清空div中内容
  $("#btn").click(function () {
    //$("#dv").html("");//清空元素中的内容
    //$("#dv").empty();//清空元素中的内容
    //$("#dv").remove();//移除元素自身---自杀
  });
  $("#btn2").click(function () {
    var spanObj=$("#dv>span").clone();//克隆,复制了这个元素
    spanObj.css("fontSize","50px");
    $("#dv2").append(spanObj);
  });
});
```



### 表单元素相关

##### 设置/获取表单元素的value

```javascript
$(function () {
  //点击按钮把所有的表单的value属性值全部显示出来
  $("#btn").click(function () {
    console.log($(this).val());//显示按钮的value属性值
    console.log($("#txt").val());//显示文本框的value属性值
    console.log($("#rad").val());//显示的单选框的value属性值
    console.log($("#ck").val());//显示的是复选框的value属性值
    console.log($("#sm").val());//显示的是提交按钮的value属性值

    //设置表单元素的value属性值
    $(this).val("这是一个按钮妞");
    $("#txt").val("我是一个开心的按钮");
    $("#rad").val("这是单选");
    $("#ck").val("兴趣来了");
    $("#sm").val("这是sm按钮");

    //获取文本域中的内容:1. .text()方法  2  .val()方法--推荐
    console.log($("#tt").text());

  });
  
  //点击按钮让下拉框中的某个选中
  $("#btn").click(function () {
    $("#se").val("4");//可以改变某一项选中
  });
});
```

##### 自定义属性

```javascript
$(function () {
  //点击按钮,在div中添加一个超链接,设置超链接的title属性和热点文字,地址
  $("#btn").click(function () {
    //获取div,创建超链接
    var aObj=$("<a></a>");
    //attr();可以写两个参数:1参数；属性,2属性值
    //attr();只写了一个参数,获取该元素的这个属性的值
    aObj.attr("title","hello");
    aObj.attr("href","http://www.syh.cn");
    aObj.text("hello syh");
    $("#dv").append(aObj);
    console.log(aObj.attr("href"));

  });
});
```

##### 复选框选中状态获取

```javascript
//点击按钮显示复选框的选中状态
$(function () {
  $("#btn").click(function () {
    // console.log($("#ck").attr("checked"));//无效
    //prop()可以真正的获取元素是否选中的状态
    //console.log($("#ck").prop("checked"));
    //点击按钮让复选框选中,再点按钮让复选框不选中
    var flag=$("#ck").prop("checked");//获取选中状态
    //if(flag){
    //  //选中了
    //  $("#ck").prop("checked",false);
    //}else{
    // //没有选中
    //  $("#ck").prop("checked",true);
    //}
    
   $("#ck").prop("checked",!flag); 
  });
});
```



### 宽高样式设置

```javascript
//点击按钮,获取当前元素的宽和高,再次设置元素的宽和高,设置后元素的宽和高分别是原来的宽和高2倍
$(function () {
  $("#btn").click(function () {
    //获取元素的宽和高
    var width=parseInt($("#dv").css("width"))*2;
    var height=parseInt($("#dv").css("height"))*2;
    //设置样式
    $("#dv").css("width",width+"px");
    $("#dv").css("height",height+"px");
    //通过元素的css()方法可以获取元素的宽和高,但是都是 字符串 类型


    //获取宽和高的属性值---->数字类型
    var width=$("#dv").width()*2;
    var height=$("#dv").height()*2;
    //设置元素的宽和高--->参数可以是 数字 也可以是 字符串
    $("#dv").width(width);
    $("#dv").height(height);

  })
});
```



### .offset().left/top

```javascript
$(function () {
  $("#btn").click(function () {
    //获取left和top的值--->都是数字类型
    console.log($("#dv").offset().left);
    console.log($("#dv").offset().top);、
    
    $("#dv").offset({"left":200,"top":200});
  });
});
```



### .scrollLeft()/.scrollTop()

```javascript
$(function () {
  $(document).click(function () {
    //获取的卷曲出去的距离----->数字类型
    console.log($(this).scrollLeft()+"===="+$(this).scrollTop());
  });
});
```



### 事件绑定与解绑

##### 事件绑定

```javascript
$(function () {
  //鼠标进入到按钮中背景颜色为红色,离开后颜色为默认,点击按钮,弹出对话框
  //鼠标进入
  $("#btn").mouseover(function () {
    $(this).css("backgroundColor","red");
  });
  //鼠标离开
  $("#btn").mouseout(function () {
    $(this).css("backgroundColor","");
  });
  //点击事件
  $("#btn").click(function () {
    alert("哈哈,我又变帅了");
  });
  //链式编程
  $("#btn").mouseover(function () {
    $(this).css("backgroundColor","red");
  }).mouseout(function () {
    $(this).css("backgroundColor","");
  }).click(function () {
    alert("哈哈,我又变帅了");
  });
  
  //bind()方法:第一个参数是事件名字,第二个参数是事件处理函数-匿名函数
  $("#btn").bind("click",function () {
    alert("我被点了");
  });
  //bind()方法可以为元素同时绑定多个事件
  $("#btn").bind({"click":function(){
    alert("我被点了");
  },"mouseover":function(){
    $(this).css("backgroundColor","red");
  },"mouseout":function(){
    $(this).css("backgroundColor","");
  }});

});
```

```javascript
$(function () {
  //为按钮注册鼠标进入和离开的事件--绑定--bind
  var i=0;
  $("#btn").bind("mouseover mouseout",function () {
    i++;
    console.log(i);
  });
});

$(function () {
  //点击按钮通过bind方式为div中添加一个元素
  $("#btn").bind("click",function () {
    //创建一个p标签,添加到div中
    $("<p>这是一个p</p>").appendTo($("#dv"));
    //方法
    //点击p标签弹出对话框
    //delegate--->绑定事件
    /*
*
* delegate:
* 参数:3个
* 1.要绑定事件的元素---p
* 2.要绑定的事件的名字---click
* 3.绑定事件的处理函数---匿名函数
*
* */
    $("#dv").delegate("p","click",function () {
      alert("我被点了");
    });
  });
});
```

```javascript
//通过on为按钮绑定点击的事件,创建一个p标签加入到div中,通过on的方式为div中的p绑定点击事件
$(function () {
  $("#btn").on("click",function () {
    //创建p添加到div中
    $("#dv").append($("<p>这是一个p</p>"));
    //为div中的p标签绑定事件
    /*
* on方法： 两个参数:1事件的名字,2事件处理函数
* on方法:三个参数: 1,事件的名字, 2.要绑定事件的元素--p,3事件处理函数
* on是父级元素调用,目的:为子级元素去绑定事件
*
* */
    $("#dv").on("click","p",function () {
      alert("我被点了");
    });
  });
});

```

##### 事件解绑

```javascript
$(function () {
  //第一个按钮通过on的方式绑定点击事件
  $("#btn1").on("click",function () {
    alert("我被点了");
  });
  //第二个按钮把第一个按钮的点击事件解绑
  $("#btn2").on("click",function () {
    //off()参数:要解绑的事件的名字
    $("#btn1").off("click");//解绑事件
  });
});

```

```javascript
$(function () {
  //第一个按钮bind绑定事件
  $("#btn1").bind("click",function () {
    alert("我又被点了");
  });
  //第二个按钮unbind解绑事件
  $("#btn2").bind("click",function () {
    $("#btn1").unbind("click");//解绑事件的方法
  });
});
```

```javascript
$(function () {
  //点击第一个按钮为div中p绑定点击事件
  $("#btn1").click(function () {
    $("#dv").delegate("p","click",function () {
      alert("我被点了");
    });
  });
  //点击第二个按钮为div中p解除绑定事件
  $("#btn2").click(function () {
    $("#dv").undelegate("p","click");//解绑
  });
});
```

##### 解绑事件细节问题

```javascript
$(function () {
  //为div和p都绑定点击事件
  //            $("#dv>p").click(function () {
  //                alert("p被点了");
  //            });
  $("#dv").delegate("p","click",function () {
    alert("p被点了");
  });
  $("#dv").click(function () {
    alert("div被点了");
  });
  $("#btn1").click(function () {
    // $("#dv").off("click");
    //下面的代码是把子级元素的点击事件解绑了,父级元素的点击事件还存在
    //$("#dv").off("click","**");
    $("#dv").off();//移除父级元素和子级元素的所有的事件
  });
  //如果说父级元素和子级元素都是通过正常的方式绑定事件,如果通过off解绑的时候,父级元素的事件解绑了,子级元素的事件没有解绑
  //但是:如果子级元素是通过父级元素调用delegate的方式绑定的事件,父级元素使用off方式解绑事件,这个时候父级元素和子级元素的相同的事件都会被解绑
});
```



### 事件触发

```javascript
$(function () {
  $("#btn1").click(function () {
    $(this).css("backgroundColor","red");
  });
  //点击第二个按钮调用第一个按钮的点击事件---触发第一个按钮的点击事件
  $("#btn2").click(function () {
    //触发事件--3三种方式
    $("#btn1").click();
    
    //trigget()方法中需要写上触发事件的名字
    $("#btn1").trigger("click");//触发事件
    
    $("#btn1").triggerHandler("click");//触发事件
  });
});
```

```javascript
// 浏览器默认事件

$(function () {
  $("#btn").click(function () {
    //触发文本框的获取焦点的事件
    $("#txt").focus();
    $("#txt").trigger("focus");
    $("#txt").triggerHandler("focus");

    //第一种触发事件的方式和第二种触发事件的方式是相同的,都会触发浏览器默认的事件(光标在文本框中闪烁)
    //第三种触发事件的方式不会触发浏览器的默认事件
  });
});
```

```javascript
// 取消浏览器默认事件  ---> return false
```



### 事件对象

```javascript
$(function () {
  //为div中的按钮绑定事件,获取事件对象中内容
  $("#dv").on("click","input",function (event) {
    //获取函数在调用的时候,有几个参数
    //console.log(arguments[0]);
    console.log(event);
    //event.delegateTarget----->div--->谁代替元素绑定的事件--div
    //event.currentTarget----->input--->真正是谁绑定的事件
    //event.target---->input----触发的事件
  });
});
```



### 键盘值获取

```javascript
$(function () {
  $(document).keydown(function (e) {
    var keyCode=e.keyCode;//键盘按下后的键对应的键值
    switch (keyCode){
      case 65:$("#dv").css("backgroundColor","red");break;
      case 66:$("#dv").css("backgroundColor","green");break;
      case 67:$("#dv").css("backgroundColor","blue");break;
      case 68:$("#dv").css("backgroundColor","yellow");break;
      case 69:$("#dv").css("backgroundColor","black");break;
    }
  });
});
```



### 事件冒泡

```javascript
//事件冒泡:元素中有元素,这些元素都有相同的事件,一旦最里面的元素的事件触发了,外面的所有的元素的相同的事件都会被触发
//元素A中有一个元素B,A和B都有点击事件,B点击事件触发,A点击事件自动触发
//取消事件冒泡
//jQuery中  return false
$(function () {
  $("#dv1").click(function () {
    alert("dv1被点了"+$(this).attr("id"));
  });
  $("#dv2").click(function () {
    alert("dv2被点了"+$(this).attr("id"));
    //$("body").css("backgroundColor","black");
  });
  $("#dv3").click(function () {
    alert("dv3被点了"+$(this).attr("id"));
    return false;//取消事件冒泡
  });
});
```



### 多库共存

### jQuery UI

