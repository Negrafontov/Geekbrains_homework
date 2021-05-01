'use strict';
//  Продолжаем реализовывать модуль корзины
var good1 = {
    price: 100,
    quantity: 0
}
var good2 = {
    price: 150,
    quantity: 0
}
var good3 = {
    price: 200,
    quantity: 0
}
var good4 = {
    price: 300,
    quantity: 0
}

var basket = [good1, good2, good3, good4];

function countPrice(basketArray) {
    var totalPrice = 0;
    basketArray.forEach(element => {
        totalPrice += element.price * element.quantity;
    });
    return (totalPrice);
}
function countQuantity(basketArray) {
    var totalQuantity = 0;
    basketArray.forEach(element => {
        totalQuantity += element.quantity;
    });
    return (totalQuantity);
}

function total() {
    alert("В корзине: " + countQuantity(basket) + " товаров на сумму " + countPrice(basket) + " рублей")
}

document.write("<div><li onclick='good1.quantity += 1, total()'>Добавить товар 1</li><li onclick='good2.quantity += 1, total()'>Добавить товар 2</li><li onclick='good3.quantity += 1, total()'>Добавить товар 3</li><li onclick='good4.quantity += 1, total()'>Добавить товар 4</li></div>")