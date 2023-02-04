function displayResultTable(response) {
    response = JSON.stringify(response);
    let json = JSON.parse(response);
    
    ioVarTable(json)
    summaryForModelTable(json)
    anovaTable(json)
    coefTable(json)


}
function createHeadForTable(table, headersList) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of headersList) {
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function ioVarTable(json){
    let table = document.querySelector(".iovar-table");
    let caption = table.createCaption()
    caption.textContent = 'Введенные/удаленные переменные'
    const headersList = ['Модель',
                         'Введенные переменные',
                         'Удаленные переменные', 
                         'Метод']
    createHeadForTable(table, headersList)
    
}
function summaryForModelTable(json){
    let table = document.querySelector(".summary-table");
    let caption = table.createCaption()
    caption.textContent = 'Сводка для модели'
    const headersList = ['Модель',
                         'R',
                         'R - квадрат', 
                         'Скорректированный R - квадрат',
                         'Стандартная ошибка оценки']

    createHeadForTable(table, headersList)
}
function anovaTable(json){
    let table = document.querySelector(".anova-table");
    let caption = table.createCaption()
    caption.textContent = 'ANOVA'
    const headersList = ['Модель',
                         'Сумма квадратов',
                         'ст. св.', 
                         'Средний квадрат',
                         'F',
                         'Значимость']

    createHeadForTable(table, headersList)
}
function coefTable(json){
    let table = document.querySelector(".coef-table");
    let caption = table.createCaption()
    caption.textContent = 'Коэффициенты'
    const headersList = ['Модель',
                         'B',
                         'Стандартная ошибка', 
                         'Бета',
                         't',
                         'Значимость']
    
    createHeadForTable(table, headersList)
}



