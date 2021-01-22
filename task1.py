# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Не совсем понимаю как полноценно выполнить данное задание без использования [], поэтому уповаю на идеального юзера
# ссылка на схемы: https://drive.google.com/file/d/1xX4wHHhhkiWLMDUkxLRBZFzOaEvD3Dh8/view?usp=sharing
print('Дорогой пользователь, Вам необходимо по частям ввести натуральное трехзначное число')
first_digit = int(input('Пожалуйста, введите цифру, обозначающее количество сотен в Вашем числе'))
second_digit = int(input('Пожалуйста, введите цифру, обозначающее количество десятков в Вашем числе'))
third_digit = int(input('Пожалуйста, введите цифру, обозначающее количество единиц в Вашем числе'))
number = first_digit * 100 + second_digit * 10 + third_digit
sum_of_digits = first_digit + second_digit + third_digit
product_of_digits = first_digit * second_digit * third_digit
print('Ваше число: {}'.format(number))
print('Сумма цифр в Вашем числе равна: {}'.format(sum_of_digits))
print('Произведение цифр в Вашем числе равно: {}'.format(product_of_digits))