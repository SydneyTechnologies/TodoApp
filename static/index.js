function select(obj, target){
    tab_buttons = document.getElementsByClassName("todo-item-parent")
    for(let j = 0; j < tab_buttons.length; j++){
        if(tab_buttons[j].classList.contains(target)){
            tab_buttons[j].classList.remove("off")
            let activeElements = document.getElementsByClassName("active")
            console.log(activeElements.length)
            Array.from(activeElements).forEach(element => {
                element.classList.remove('active')
            });
            obj.classList.add('active')
        }
        else{
            tab_buttons[j].classList.add("off")
        }
    }
}

const starting_item = "todo_list"
task_button = document.getElementById("todo_button")
select(task_button, starting_item)