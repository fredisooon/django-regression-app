let valueList = document.getElementById('valueList');
let text = '<span> you have selected : </span>';
let listArray = [];
        
let checkboxes = document.querySelectorAll('.checkbox')
        for(let checkbox of checkboxes){
            checkbox.addEventListener('click', function() {
                if (this.checked == true) {
                    listArray.push(this.value)
                    valueList.innerHTML = text + listArray.join(' / ');
                }
                else {
                    
                }
            })
        }