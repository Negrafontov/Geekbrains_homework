'use strict';
//  Написать функцию, преобразующую число в объект.
function numberToObject(number) {
    if (number >= 0 && number <= 999) {
        if (number >= 100) {
            var hund = Math.floor((number / 100) % 100)
        }
        else {
            var hund = 0
        }
        if (number >= 10) {
            var doz = Math.floor((number / 10) % 10)
        }
        else {
            var doz = 0
        }
        var uni = number % 10
        var object = {
            hundreds: hund,
            dozens: doz,
            units: uni
        };
        return object;
    }
    else {
        console.log("Число должно от 0 до 999");
        var object = {

        };
        return object;
    }
}
numberToObject(1200);
numberToObject(10);
// Продолжить работу с интернет-магазином.
var good1 = {
    price: 100,
    quantity: 4
}
var good2 = {
    price: 150,
    quantity: 1
}
var good3 = {
    price: 200,
    quantity: 3
}
var good4 = {
    price: 300,
    quantity: 2
}
var basket = [good1, good2, good3, good4];

function countBasketPrice(basketArray) {
    var totalPrice = 0;
    basketArray.forEach(element => {
        totalPrice += element.price * element.quantity;
    });
    alert(totalPrice);
}
countBasketPrice(basket);