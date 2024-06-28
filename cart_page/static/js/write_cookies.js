
const listbuttonsplus = document.querySelectorAll(".plus-count")
const listbuttonsminus = document.querySelectorAll(".minus-count")
const listp = document.querySelectorAll(".count-of-product")

let h4_count_prdc = document.querySelector(".original-count")
let h4_org_prc = document.querySelector(".original-price-p")
let h4_disc = document.querySelector(".discount-p")
let h4_ttl_prc = document.querySelector(".total-price-p")

let cartValue = document.querySelector(".cart-value")

// console.log(cartValue.textContent)
// console.log(prompt("HelloWrdslfkkkfdwekfd"))

let price_iPhones = 0
let price_Vivos = 0
let total_price = 0
let discount = 0
function counter_price (){
    let cookies1 = document.cookie.split('=')[1].split(' ')
    if (cookies1.length == 1) {
        h4_count_prdc.textContent = `${cookies1.length} товар на суму`
    }
    else {
        if (cookies1.length == 4) {
            h4_count_prdc.textContent = `${cookies1.length}-и товари на суму`
        }
        else {
            h4_count_prdc.textContent = `${cookies1.length} товарів на суму`
        }
    }
    price_iPhones = 0
    price_Vivos = 0
    total_price = 0
    discount = 0
    for (let count = 0; count < cookies1.length; count++) {
        if (cookies1[count] == "1") {
            price_iPhones += 40009
        }
        else {
            price_Vivos += 3095
        }
    }
    for (let count = 0; count < cookies1.length; count++) {
        if (cookies1[count] == "1") {
            discount += 9990
        }
        else {
            discount += 1904
        }
    }

    total_price = `${price_Vivos + price_iPhones} грн`
    h4_org_prc.textContent = total_price
    h4_disc.textContent = `${discount} грн`
    h4_ttl_prc.textContent = total_price
    console.log(total_price)
}
function counter1 (id) {
    let cookies = document.cookie.split('=')[1].split(' ')
    let data = 0
    for (let count = 0; count < cookies.length; count++) {
        if (cookies[count] == id) {
            data++
        }
    }
    try {
        listp[id-1].textContent = data 
    }
    catch {
        listp[id-2].textContent = data 
    }
}
for (let count = 0; count < listbuttonsplus.length; count++) {
    let button = listbuttonsplus[count]
    button.addEventListener(
        type = "click",
        listener = function (event) {
            // Якщо записів до cookie раніше не проводились то даємо перший запис
            if (document.cookie == ''){
                // Ми створюємо файл cookie  з назвою products та додаємо динамічно значення натиснутої кнопки
                document.cookie = `products = ${button.id}; path = / `
                let count11 = document.cookie.split("=")
                cartValue.textContent = count11[1].split(' ').length
                counter_price()                
            }
            else{
                // Отримуємо попередньо записані дані в cookie (products)
                product_id = document.cookie.split('=')[1]
                // перезаписуємо cookie додаючи значення нової натиснутої кнопки
                document.cookie = `products = ${product_id} ${button.id}; path = / `
                counter1(id= button.id)
                let count11 = document.cookie.split("=")
                cartValue.textContent = count11[1].split(' ').length

                counter_price()         
            }
        }
    )
}
for (let count = 0; count < listbuttonsminus.length; count++) {
    let button = listbuttonsminus[count]
    button.addEventListener(
        type = "click",
        listener = function (event) {
            // Якщо записів до cookie раніше не проводились то даємо перший запис
            if (document.cookie != ''){
                product_id = document.cookie.split('=')[1].split(' ')
                product_id.splice(product_id.indexOf(button.id), 1)
                document.cookie = `products = ${product_id.join(" ")}; path = / `
                counter1(id= button.id)
                let count11 = document.cookie.split("=")
                cartValue.textContent = count11[1].split(' ').length
                counter_price()         
            }
        }
    )
}
counter_price()    

let count11 = document.cookie.split("=")
cartValue.textContent = count11[1].split(' ').length




let OrderButton = document.querySelector(".continie-order")
OrderButton.addEventListener(
    type = "click",
    listener = (event) => {
        document.querySelector('.modal-window').style.display = 'flex'

        let elementsp = document.querySelectorAll(".text-data-new")
        let y = 30
        for (let count = 0; count < elementsp.length; count++) {
            let element = elementsp[count]
            element.style.display = "flex"
            element.style.top = y
            y += 125
        }

    }
)