'use strict';
document.write("<div id=0 style= display:><li onclick='basket.push(good1), good1.quantity += 1, total()'>Добавить товар 1</li><li onclick='basket.push(good2), good2.quantity += 1, total()'>Добавить товар 2</li><li onclick='basket.push(good3), good3.quantity += 1, total()'>Добавить товар 3</li><li onclick='basket.push(good4), good4.quantity += 1, total()'>Добавить товар 4</li></div>");
document.write("<div id=1 style= display:none>Состав корзины</div>");
document.write("<div id=2 style= display:none>адрес<input></div>");
document.write("<div id=3 style= display:none>комментарий<input></div>");
document.write("<input type='button' onclick='next(counter); counter += 1' value='Далее'>");
var counter = 1;
function next(counter) {
    document.getElementById(counter).style.display = (document.getElementById(counter).style.display != 'none' ? 'none' : '');
    document.getElementById(counter - 1).style.display = (document.getElementById(counter - 1).style.display != 'none' ? 'none' : '');
    if (counter == 1) {
        if (basket.length == 0) {
            document.getElementById(counter).innerHTML = "Корзина пуста";
        }
        else {
            document.getElementById(counter).innerHTML = "Состав корзины:<br>Товар 1: " + good1.quantity + "<br>Товар 2: " + good2.quantity + "<br>Товар 3: " + good3.quantity + "<br>Товар 4: " + good4.quantity;
        }
    }

};
function countPrice(basketArray) {
    var totalPrice = 0;
    basketArray.forEach(element => {
        totalPrice += element.price;
    });
    return (totalPrice);
};
function countQuantity(basketArray) {
    var totalQuantity = basketArray.length;
    return (totalQuantity);
};
function total() {
    alert("В корзине: " + countQuantity(basket) + " товаров на сумму " + countPrice(basket) + " рублей")
}
var good1 = {
    price: 100,
    quantity: 0
};
var good2 = {
    price: 150,
    quantity: 0
};
var good3 = {
    price: 200,
    quantity: 0
};
var good4 = {
    price: 300,
    quantity: 0
};
var basket = [];
