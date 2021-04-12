'use strict';
// задание 1
var a = 1, b = 1, c, d;
c = ++a; alert(c);           // 2 префиксная форма инкрементирования
d = b++; alert(d);           // 1 постфиксная форма инкрементирования
c = (2 + ++a); alert(c);      // 5 после первого выражения а = 2 и префиксная форма инкрементирования
d = (2 + b++); alert(d);      // 4 поле первого выражения b = 2 и  постфиксная форма инкрементирования
alert(a);                    // 3 после предыдущих выражений а = 3 (дважды инкрементировалось)
alert(b);                    // 3 после предыдущих выражений b = 3 (дважды инкрементировалось)
// задание 2
var a1 = 2;
var x = 1 + (a1 *= 2);
alert(x);                   // х = 5; умножение а1 на 2, потом сложение с единицой
// задание 3
var a2 = -10, b2 = 0;
if (a2 >= 0 && b2 >= 0)
    alert(a2 - b2);
else if (a2 < 0 && b2 < 0)
    alert(a2 * b2)
else if ((a2 >= 0 && b2 < 0) || (a2 < 0 && b2 >= 0))
    alert(a2 + b2)
// задание 4 
var a3 = 14;
max = 15;
dif = max - a3;
switch (a3) {
    case 0:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 1:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 2:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 3:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 4:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 5:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 6:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 7:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 8:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 9:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 10:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 11:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 12:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 13:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 14:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
    case 15:
        while (dif >= 0) {
            alert(a3++);
            dif--;
        }
        break;
}
// задание 5
function addition(num1, num2) {
    var result = num1 + num2;
    return result;
}
function subtraction(num1, num2) {
    var result = num1 - num2;
    return result;
}
function multiplication(num1, num2) {
    var result = num1 * num2;
    return result;
}
function division(num1, num2) {
    var result = num1 / num2;
    return result;
}
// задание 6
function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case 'addition':
            return addition(arg1, arg2);
        case 'subtraction':
            return subtraction(arg1, arg2);
        case 'multiplication':
            return multiplication(arg1, arg2);
        case 'division':
            return division(arg1, arg2);
    }
}
var a4 = 4, b4 = 2; op1 = 'addition', op2 = 'subtraction', op3 = 'multiplication', op4 = 'division';
alert(mathOperation(a4, b4, op1));
alert(mathOperation(a4, b4, op2));
alert(mathOperation(a4, b4, op3));
alert(mathOperation(a4, b4, op4));
// задание 7
alert(null == 0);       // Значения null и undefined равны друг другу, но не чему бы то ни было еще. При явном преобразовании в число null принимает значение 0.
alert(+null == 0);
// задание 8
function power(val, pow) {
    if (pow != 1) {
        return val *= power(val, pow - 1);
    }
    else {
        return val;
    }
}
a5 = 2;
alert(power(a5, 4));
