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
    
    function render() {
        $('#todo-list').html(this.todoTemplate(todos));
        $('#main').toggle(todos.length > 0);
        $('#toggle-all').prop('checked', this.getActiveTodos().length === 0);
        this.renderFooter();
        $('#new-todo').focus();
    }

    $('#new-todo').on('keyup', function (event) {
        var input = $(event.target);
        var val = input.val().trim();

        if (event.which !== 13 || !val) {
            return;
        }

        todos.push(new Todo(new Date().getTime(),val,false));


        input.val('');

        render();
    });
    $('#toggle-all').on('change', this.toggleAll.bind(this));
    $('#footer').on('click', '#clear-completed', this.destroyCompleted.bind(this));
    $('#todo-list')
        .on('change', '.toggle', this.toggle.bind(this))
        .on('dblclick', 'label', this.editingMode.bind(this))
        .on('keyup', '.edit', this.editKeyup.bind(this))
        .on('focusout', '.edit', this.update.bind(this))
        .on('click', '.destroy', this.destroy.bind(this));
});