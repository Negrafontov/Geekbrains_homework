'use strict';
// Создать функцию, генерирующую шахматную доску.
function chess() {
    var columns = ["A", "B", "C", "D", "E", "F", "G", "H"];
    document.write("<table border='1' width='400' height='400'>");
    for (var i = 0; i <= 8; i++) {
        if (i == 0) {
            document.write("<td></td>");
        }
        else {
            document.write("<td>" + columns[(i - 1)] + "</td>");
        }
    }
    for (var i = 1; i <= 8; i++) {
        document.write("<tr>");
        document.write("<td>" + i + "</td>");
        for (var j = 1; j <= 8; j++) {
            if ((i + j) % 2 != 0) {
                document.write("<td bgcolor='white'></td>");
            }
            else {
                document.write("<td bgcolor='black'></td>");
            }
        }
        document.write("</tr>");
    }
    document.write("</table>");
};
// Сделать генерацию корзины динамической
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

var fullBasket = [good1, good2, good3, good4];
var emptyBasket = [];

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

document.write("<div>");
var basket = fullBasket;
if (basket.length > 0) {
    document.write("<h4>" + "В корзине: " + countQuantity(basket) + " товаров на сумму " + countPrice(basket) + " рублей" + "</h4>");
}
else {
    document.write("<h4>" + "Корзина пуста" + "</h4>");
}
document.write("</div>");
