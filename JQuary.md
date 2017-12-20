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

### 网页开关灯实现-Class

### CSS方法与类样式区别

### 链式编程

### 获取兄弟元素

### 常见动画方法

### 动态创建元素

### 常用方法2

### 表单元素相关

### 宽高样式设置

### .offset().left/top

### .scrollLeft()/.scrollTop()

### 事件绑定与解绑

### 事件触发

### 事件对象

### 键盘值获取

### 事件冒泡

### 多库共存

### jQuery UI

