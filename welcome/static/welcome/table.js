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
    fillBody(json, table, 'io_vars')
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
    fillBody(json, table, 'summary');
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
    fillBody(json, table, 'anova')
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
    
    createHeadForTable(table, headersList);
    fillBody(json, table, 'coefs');
}

function fillBody(json, table, table_name) {
    let body = table.createTBody();
    for (let jsonrow in json[table_name]) {
        let row = body.insertRow();
        for (let info in json[table_name][jsonrow]) {
            let cell = row.insertCell();
            console.log(typeof(json[table_name][jsonrow][info]))
            if (typeof(json[table_name][jsonrow][info]) === 'number') {
                let text = document.createTextNode(json[table_name][jsonrow][info].toFixed(3));
                cell.appendChild(text);
            }
            else {
                let text = document.createTextNode(json[table_name][jsonrow][info]);
                cell.appendChild(text);
            }
        }
    }
}