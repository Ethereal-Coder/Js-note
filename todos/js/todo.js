$(function () {
    $(document).onkeyup(function (event) {
        if (event.keyCode === 13) {
            if ($(".new-todo").value) {
                $(".todo-list")
            } else {
                alert("input null")
            }
        }
    });
});
