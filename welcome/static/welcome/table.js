function displayResultTable(response) {
    response = JSON.stringify(response);
    let json = JSON.parse(response);
    
    ioVarTable(json);
    summaryForModelTable(json);
    coefTable(json);

    styleTables();

    let toElement = document.querySelector('.tables-area');
    toElement.scrollIntoView();
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
    if (json['regression_type'] === 'simple_linear' || 
        json['regression_type'] === 'simple_polynominal' ||
        json['regression_type'] === 'multiple_linear' ||
        json['regression_type'] === 'multiple_polynominal') {
        summaryForMoreTypes(json);
    }
    else if (json['regression_type'] === 'simple_logistical') {
        summaryForSimpleLogistical(json);
    }
}
function summaryForMoreTypes(json) {
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
function summaryForSimpleLogistical(json) {
    let table = document.querySelector(".summary-table");
    let caption = table.createCaption()
    caption.textContent = 'Сводка для модели'
    const headersList = ['Модель',
                         'Псевдо R - квдрат',
                         'Log-Likelihood',
                         'LL-null', 
                         'AIC',
                         'BIC']

    createHeadForTable(table, headersList)
    fillBody(json, table, 'summary');
}

function coefTable(json){
    if (json['regression_type'] === 'simple_linear' || 
        json['regression_type'] === 'simple_polynominal' ||
        json['regression_type'] === 'multiple_linear' ||
        json['regression_type'] === 'multiple_polynominal') {
        coefForMoreTypes(json);
    }
    else if (json['regression_type'] === 'simple_logistical') {
        coefForSimpleLogistical(json);
    }
    
}
function coefForMoreTypes(json) {
    let table = document.querySelector(".coef-table");
    let caption = table.createCaption();
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
function coefForSimpleLogistical(json) {
    let table = document.querySelector(".coef-table");
    let caption = table.createCaption();
    caption.textContent = 'Коэффициенты'
    const headersList = ['Модель',
                         'B',
                         'Стандартная ошибка', 
                         'Бета',
                         'z',
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

function styleTables() {
    document.querySelector('.tables-area').style.borderTop = "1px solid #95989c";
    let tables = document.querySelectorAll('.table');
    for(let item of tables) {
        item.style.border = "1px solid #95989c";
    }
    let infoBlocks = document.querySelectorAll('.info');
    for(let item of infoBlocks) {
        item.style.display = "block";
    }

    getDependentVar();
    getPredictors();
}

function getDependentVar() {
    let radioItems = document.querySelectorAll('.radio-item');
    let dependent = document.querySelectorAll('.dependent');

    for(let item of dependent) {
        for (let radio of radioItems) {
            if (radio.checked == true) {
                item.innerHTML = radio.value;
            }
        }
    }
}

function getPredictors() {
    let checkboxes = document.querySelectorAll('.checkbox');
    let predictors = document.querySelectorAll('.predictors');
    
    for(let item of predictors) {
        item.innerHTML = "";
    }

    let checkResult = [];

    for(let item of predictors) {
        for (let checkbox of checkboxes) {
            if (checkbox.checked == true) {
                checkResult.push(checkbox.value)
            }
        }

        for(let i = 0; i < checkResult.length; i++) {
            if(i == checkResult.length - 1) {
                item.innerHTML += checkResult[i];
            } else {
                item.innerHTML += checkResult[i] + ', ';
            }
        }

        checkResult = [];
    }
}

