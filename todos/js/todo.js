$(function () {

    var todos = [];
    function Todo(tid,title,checkState){
        this.tid = tid;
        this.title = title;
        this.checkState = checkState;
        this.printParams = function(){
            console.log(this.tid);
            console.log(this.title);
            console.log(this.checkState);
        }
    }

    function setUnCheckedNum() {
        var num = 0;
        for (var i = 0;i<todos.length;i++){
            if (todos[i].checkState === false){
                num++;
            }
        }
        $('.todo-count').children('strong').text(num);
    }

    function todoString(todo) {
           return "<li id="+todo.tid+">"+
                "<div class='view'>" +
                    "<input class='toggle' type='checkbox'/>"+
                    "<label>"+todo.title+"</label>"+
                    "<button class='destroy'></button>"
                "</div>"+
                "<input class='edit' type='text' value="+todo.title+"/>"+
            "</li>";

    }

    function getTodoIndex(temp) {
        for (var i=0;i<todos.length;i++){
            if (todos[i].tid == temp){
                return i;
            }
        }
        return -1;
    }
    
    function render(todo) {
        var todoStr = $(todoString(todo));
        // console.log(todoStr.attr("id"));
        $('.todo-list').append(todoStr);
        $('.main').toggle(todos.length > 0);
        $('.toggle-all').prop('checked', todos.length === 0);
        $('.new-todo').focus();
        setUnCheckedNum();
    }

    $(document).keydown(function (e) {
        var keyCode=e.keyCode;//键盘按下后的键对应的键值
        var input = $(e.target);
        var val = input.val().trim();

        if (keyCode!== 13){
            return;
        }else {
            if(!val){
                console.log("请输入内容...");
                alert("请输入内容...");
                return;
            }
        }

        var todo = new Todo(new Date().getTime(),val,false);
        // todo.printParams();
        todos.push(todo);

        input.val('');

        render(todo);

    });

    // $('#toggle-all').on('change', this.toggleAll.bind(this));
    // $('#footer').on('click', '#clear-completed', this.destroyCompleted.bind(this));
    $('.todo-list')
        .on('change', '.toggle', function (e) {
            var ce = e.target;
            var aid = $(ce).closest("li").attr('id');
            var index = getTodoIndex(aid);
            console.log(index);
            console.log($('.toggle').prop('checked'));
            todos[index].checkState = !todos[index].checkState;
            if (todos[index].checkState){
                $(ce).closest("li").addClass('completed');
            }else {
                $(ce).closest("li").removeClass('completed');
            }

            setUnCheckedNum();

        })
        .on('dblclick', 'label', function (e) {

        })
        .on('click', '.destroy', function (e) {
            var aid = $(e.target).closest("li").attr('id');

            $(e.target).closest('li').remove();

            var index = getTodoIndex(aid);
            todos.splice(index,1);

            setUnCheckedNum();
        });
    $('.toggle-all').on('click',function () {
        var flag=$(".toggle-all").prop("checked");
        for (var i=0;i<todos.length;i++){
             todos[i].checkState = flag;
        }
        $('ul>li').each(function (index, element) {
            $(element).children('div').find('.toggle').prop("checked",flag);
            console.log($(element).children('div').find('.toggle').prop("checked"));
            if ($(element).hasClass('completed')){
                if (!flag){
                    $(element).removeClass('completed');
                }
            }else {
                if(flag){
                    $(element).addClass('completed');
                }
            }
        });

        setUnCheckedNum();

    });

    $('.clear-All').on('click',function () {
        // $(".todo-list>li").last("li").hide(800,function () {
        //     $(this).prev().hide(800,arguments.callee);
        // });
        // $(".todo-list>").html("");
        $(".todo-list>li").each(function (index, element) {
            element.remove();
        });
        todos = [];
        setUnCheckedNum();
    });
});