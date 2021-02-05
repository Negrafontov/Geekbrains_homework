# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’].
from collections import deque


def key_finder(val, conv_dict):
    for key, value in conv_dict.items():
        if val == value:
            return key


def addition(first_numb, second_numb, conv_dict):
    addition_number = deque()
    if len(first_numb) >= len(second_numb):
        higher = first_numb
        lower = second_numb
    else:
        higher = second_numb
        lower = first_numb
    spam_numb = 0
    for i in range(1, len(lower) + 1):
        current_numb = conv_dict[lower[len(lower) - i]] + conv_dict[higher[len(higher) - i]] + spam_numb
        if current_numb // 16 != 0:
            spam_numb = 1
            addition_number.appendleft(key_finder(current_numb % 16, conv_dict))
        else:
            spam_numb = 0
            addition_number.appendleft(key_finder(current_numb, conv_dict))
    if len(higher) != len(lower):
        eggs = len(higher) - len(lower)
        for i in range(1, eggs + 1):
            if spam_numb != 0:
                current_numb = conv_dict[higher[eggs - i]] + spam_numb
                if current_numb // 16 != 0:
                    spam_numb = 1
                    addition_number.appendleft(key_finder(current_numb % 16, conv_dict))
                else:
                    spam_numb = 0
                    addition_number.appendleft(key_finder(current_numb, conv_dict))
            else:
                current_numb = conv_dict[higher[eggs - i]]
                addition_number.appendleft(key_finder(current_numb, conv_dict))
    if spam_numb != 0:
        addition_number.appendleft(key_finder(spam_numb, conv_dict))
    return addition_number


def multiplication(first_numb, second_numb, conv_dict):
    multiplication_number = deque()
    multiplication_spam = deque()
    if len(first_numb) >= len(second_numb):
        higher = first_numb
        lower = second_numb
    else:
        higher = second_numb
        lower = first_numb
    spam_numb = 0
    for i in range(1, len(higher) + 1):
        current_numb = (conv_dict[lower[len(lower) - 1]] * conv_dict[higher[len(higher) - i]]) + spam_numb
        if current_numb // 16 != 0:
            spam_numb = current_numb // 16
            multiplication_number.appendleft(key_finder(current_numb % 16, conv_dict))
        else:
            spam_numb = 0
            multiplication_number.appendleft(key_finder(current_numb, conv_dict))
    if spam_numb != 0:
        multiplication_number.appendleft(key_finder(spam_numb, conv_dict))
        spam_numb = 0
    number_of_zeros = 1
    for i in range(2, len(lower) + 1):
        multiplication_spam.clear()
        for e in range(number_of_zeros):
            multiplication_spam.appendleft('0')
        eggs = len(higher) - 1
        while eggs >= 0:
            current_numb = (conv_dict[lower[len(lower) - i]] * conv_dict[higher[eggs]]) + spam_numb
            if current_numb // 16 != 0:
                spam_numb = current_numb // 16
                multiplication_spam.appendleft(key_finder(current_numb % 16, conv_dict))
            else:
                spam_numb = 0
                multiplication_spam.appendleft(key_finder(current_numb, conv_dict))
            eggs -= 1
        if spam_numb != 0:
            multiplication_spam.appendleft(key_finder(spam_numb, conv_dict))
            spam_numb = 0
        multiplication_number = addition(multiplication_number, multiplication_spam, conv_dict)
        number_of_zeros += 1
    if spam_numb != 0:
        multiplication_number.appendleft(key_finder(spam_numb, conv_dict))
    return multiplication_number


conversion_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

first_number = list(input('Пожалуйста, введие первое число в шестнадцетеричной системе счисления'))
second_number = list(input('Пожалуйста, введие второе число в шестнадцетеричной системе счисления'))

print(addition(first_number, second_number, conversion_dict))
print(multiplication(first_number, second_number, conversion_dict))
