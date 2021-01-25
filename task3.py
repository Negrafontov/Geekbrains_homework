# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

def reverse(a):
    global b
    c = a % 10
    b = str(b) + str(c)

    if a // 10 == 0:
        return b
    else:
        a = a // 10
        reverse(a)


b = ''
users_input = int(input('Пожалуйста, введите натуральное число'))
reverse(users_input)
print(b)