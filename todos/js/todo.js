$(function () {

    var todos = [];
    function Todo(tid,title,completed){
        this.tid = tid;
        this.title = title;
        this.completed = completed;
        this.sayHi = function(){
            console.log('Hello,everyBody');
        }
    }

    function todoString(todo) {
           return "<li id="+todo.tid+">"+
                "<div class='view'>" +
                    "<input class='toggle' type='checkbox'/>"+
                    "<label>"+todo.title+"</label>"+
                    "<button class='destroy'></button>"
                "</div>"+
                "<input class='edit' value="+todo.title+"/>"+
            "</li>";

    }
    
    function render(todo) {
        var todoStr = todoString(todo);
        $('#todo-list').append($(todoStr));
        $('#main').toggle(todos.length > 0);
        // $('#toggle-all').prop('checked', this.getActiveTodos().length === 0);
        // this.renderFooter();
        $('#new-todo').focus();
    }

    $(document).keydown(function (e) {
        var keyCode=e.keyCode;//键盘按下后的键对应的键值
        var input = $(e.target);
        var val = input.val().trim();

        if (keyCode !== 13 || !val) {
            return;
        }

        console.log(1);
        var todo = new Todo(new Date().getTime(),val,false);

        todos.push(todo);

        input.val('');

        // render(todo);
        var todoStr =  "<li id="+todo.tid+">"+
            "<div class='view'>" +
            "<input class='toggle' type='checkbox'/>"+
            "<label>"+todo.title+"</label>"+
            "<button class='destroy'></button>"
        "</div>"+
        "<input class='edit' value="+todo.title+"/>"+
        "</li>";
        var aObj=$("<li>百度</li>");
        console.log(2);
        $('#todo-list').append(aObj);
        console.log(3);
        $('#main').toggle(true);
        $('#new-todo').focus();
        console.log(4);


    });

    // $('#new-todo').on('keyup', function (event) {
    //     var input = $(event.target);
    //     var val = input.val().trim();
    //
    //     if (event.which !== 13 || !val) {
    //         return;
    //     }
    //
    //     console.log(1);
    //     var todo = new Todo(new Date().getTime(),val,false);
    //
    //     todos.push(todo);
    //
    //
    //     input.val('');
    //
    //     render(todo);
    // });
    // $('#toggle-all').on('change', this.toggleAll.bind(this));
    // $('#footer').on('click', '#clear-completed', this.destroyCompleted.bind(this));
    // $('#todo-list')
    //     .on('change', '.toggle', this.toggle.bind(this))
    //     .on('dblclick', 'label', this.editingMode.bind(this))
    //     .on('keyup', '.edit', this.editKeyup.bind(this))
    //     .on('focusout', '.edit', this.update.bind(this))
    //     .on('click', '.destroy', this.destroy.bind(this));
});