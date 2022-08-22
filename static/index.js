function select(obj, target){
    tab_buttons = document.getElementsByClassName("todo-item-parent")
    for(let j = 0; j < tab_buttons.length; j++){
        if(tab_buttons[j].classList.contains(target)){
            tab_buttons[j].classList.remove("off")
            let activeElements = document.getElementsByClassName("active")
            console.log(activeElements)
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