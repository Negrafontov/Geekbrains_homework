'use strict';
// С помощью цикла while вывести все простые числа в промежутке от 0 до 100.
var primes = new Array();
var i = 0;
while (i != 100) {
    if (i == 0 || i == 1) {
        i++;
        continue;
    }
    var limit = i ** 0.5;
    var devider = 2;
    var isPrime = true;
    while ((devider <= limit) && isPrime) {
        if (i % devider == 0) {
            isPrime = false;
        }
        devider++;
    }
    if (isPrime) {
        primes.push(i);
    }
    i++;
}
alert(primes);
// Функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров.
// a) Организовать такой массив для хранения товаров в корзине;
var catalog = new Map();
catalog.set('good1', 100).set('good2', 150).set('good3', 200).set('good4', 300);
var basket = new Map();
basket.set('good1', 4).set('good2', 1).set('good3', 3).set('good4', 2);
// b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
function countBasketPrice(basketMap, catalogMap) {
    var totalPrice = 0;
    for (var [key, value] of basketMap) {
        totalPrice += catalogMap.get(key) * value;
    }
    alert(totalPrice);
}
countBasketPrice(basket, catalog);
// Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла.
for (i = 0; i <= 9; alert(i), i++);
// Нарисовать пирамиду с 20 рядами с помощью console.log
function lineBuilder(len) {
    var line = '';
    while (len != 0) {
        line += 'x';
        --len;
    }
    console.log(line);
}
for (i = 1; i <= 20; i++) {
    lineBuilder(i);
}