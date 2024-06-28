let listOfButtonsImages = document.querySelectorAll('.edit-image')

for (let count = 0; count < listOfButtonsImages.length; count++){
    let button = listOfButtonsImages[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_text = document.querySelector(".input-text")
            input_text.textContent = "Change image:"
            input_text.style.top = 65
            let input_image = document.querySelector(".input-data")
            input_image.type = "file"
            input_image.name = "image"
            input_image.accept = "image/*"
            input_image.style.display = "flex"

            // input_image.hidden = false
            document.querySelector('.submit-change').value = `image-${button.id}`
        }
    )  
}

let listOfButtonsNames = document.querySelectorAll('.edit-title')


for (let count = 0; count < listOfButtonsNames.length; count++){
    let button = listOfButtonsNames[count]
    console.log(14124134)
    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_text = document.querySelector(".input-text")
            input_text.textContent = "Change text:"
            input_text.style.top = 65
            let input_image = document.querySelector(".input-data")
            input_image.type = "text"
            input_image.name = "name"
            input_image.style.display = "flex"
            document.querySelector('.submit-change').value = `name-${button.id}`
        }
    )
}
let listOfButtonsPrices = document.querySelectorAll('.edit-price')


for (let count = 0; count < listOfButtonsPrices.length; count++){
    let button = listOfButtonsPrices[count]
    console.log(14124134)
    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_text = document.querySelector(".input-text")
            input_text.textContent = "Change Price:"
            input_text.style.top = 65
            let input_image = document.querySelector(".input-data")
            input_image.type = "text"
            input_image.name = "price"
            input_image.style.display = "flex"
            document.querySelector('.submit-change').value = `price-${button.id}`
        }
    )
}
let listOfButtonsDiscounts = document.querySelectorAll('.edit-discount')


for (let count = 0; count < listOfButtonsDiscounts.length; count++){
    let button = listOfButtonsDiscounts[count]
    console.log(14124134)
    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            document.querySelector('.modal-form').style.height = '350px'
            document.querySelector('.modal-form').style.display = 'flex'
            let input_text = document.querySelector(".input-text")
            input_text.textContent = "Change Discount:"
            input_text.style.top = 65
            let input_image = document.querySelector(".input-data")
            input_image.type = "text"
            input_image.name = "discount"
            input_image.style.display = "flex"
            document.querySelector('.submit-change').value = `discount-${button.id}`
        }
    )
}

let NewProductButton = document.querySelector(".add-product-b")
NewProductButton.addEventListener(
    type = "click",
    listener = (event) => {
        let elements = document.querySelectorAll(".input-data-new")
        document.querySelector('.modal-window').style.display = 'flex'
        document.querySelector('.modal-form').style.height = '750px'
        document.querySelector('.modal-form').style.display = 'flex'
        for (let count = 0; count < elements.length; count++) {
            let element = elements[count]
            element.style.display = "flex"
        }
        
        let elementsp = document.querySelectorAll(".text-data-new")
        let y = 0
        for (let count = 0; count < elementsp.length; count++) {
            let element = elementsp[count]
            element.style.display = "flex"
            element.style.top = y
            y += 109
        }
        document.querySelector('.submit-change').value = `newProduct-0`

    }
)