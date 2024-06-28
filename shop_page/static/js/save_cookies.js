const listButtons = document.querySelectorAll('.buy')
// 
const listButtonsEditTitle = document.querySelectorAll('.edit-title')
const listTitles = document.querySelectorAll(".title")
// 
const listButtonsEditPrice = document.querySelectorAll('.edit-price')
const listPrices = document.querySelectorAll(".cost-original")
// 
const listButtonsEditDiscount = document.querySelectorAll('.edit-discount')
const listDiscounts = document.querySelectorAll(".discount")
// 
const listTotalPrice = document.querySelectorAll(".total-cost")
for (let count = 0; count < listButtonsEditTitle.length; count++) {
    let button = listButtonsEditTitle[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            listTitles[count].textContent = prompt("Укажіть нову назву для товару")
        }
    )
}

for (let count = 0; count < listButtonsEditPrice.length; count++) {
    let button = listButtonsEditPrice[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            listPrices[count].textContent = prompt("Укажіть нову ціну для товару") + ' грн'
            console.log(1488)
        }
    )
}

for (let count = 0; count < listButtonsEditDiscount.length; count++) {
    let button = listButtonsEditDiscount[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            listDiscounts[count].textContent = "Знижка " + prompt("Укажіть нову знижку для товару") + "%"
            console.log(153)
        }
    )
}

for (let count = 0; count < listButtons.length; count++) {
    let button = listButtons[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            if (document.cookie == ''){
                document.cookie = `products = ${button.id}; path = / `
            }
            else{
                product_id = document.cookie.split('=')[1]
                document.cookie = `products = ${product_id} ${button.id}; path = / `
            }
        }
    )
}