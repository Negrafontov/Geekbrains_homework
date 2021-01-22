# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
first_letter = input('Пожалуйста, введите строчную букву латинского алфавита')
second_letter = input('Пожалуйста, введите еще одну строчную букву латинского алфавита')

if first_letter == 'a':
    first_number = 1
elif first_letter == 'b':
    first_number = 2
elif first_letter == 'c':
    first_number = 3
elif first_letter == 'd':
    first_number = 4
elif first_letter == 'e':
    first_number = 5
elif first_letter == 'f':
    first_number = 6
elif first_letter == 'g':
    first_number = 7
elif first_letter == 'h':
    first_number = 8
elif first_letter == 'i':
    first_number = 9
elif first_letter == 'j':
    first_number = 10
elif first_letter == 'k':
    first_number = 11
elif first_letter == 'l':
    first_number = 12
elif first_letter == 'm':
    first_number = 13
elif first_letter == 'n':
    first_number = 14
elif first_letter == 'o':
    first_number = 15
elif first_letter == 'p':
    first_number = 16
elif first_letter == 'q':
    first_number = 17
elif first_letter == 'r':
    first_number = 18
elif first_letter == 's':
    first_number = 19
elif first_letter == 't':
    first_number = 20
elif first_letter == 'u':
    first_number = 21
elif first_letter == 'v':
    first_number = 22
elif first_letter == 'w':
    first_number = 23
elif first_letter == 'x':
    first_number = 24
elif first_letter == 'y':
    first_number = 25
else:
    first_number = 26

if second_letter == 'a':
    second_number = 1
elif second_letter == 'b':
    second_number = 2
elif second_letter == 'c':
    second_number = 3
elif second_letter == 'd':
    second_number = 4
elif second_letter == 'e':
    second_number = 5
elif second_letter == 'f':
    second_number = 6
elif second_letter == 'g':
    second_number = 7
elif second_letter == 'h':
    second_number = 8
elif second_letter == 'i':
    second_number = 9
elif second_letter == 'j':
    second_number = 10
elif second_letter == 'k':
    second_number = 11
elif second_letter == 'l':
    second_number = 12
elif second_letter == 'm':
    second_number = 13
elif second_letter == 'n':
    second_number = 14
elif second_letter == 'o':
    second_number = 15
elif second_letter == 'p':
    second_number = 16
elif second_letter == 'q':
    second_number = 17
elif second_letter == 'r':
    second_number = 18
elif second_letter == 's':
    second_number = 19
elif second_letter == 't':
    second_number = 20
elif second_letter == 'u':
    second_number = 21
elif second_letter == 'v':
    second_number = 22
elif second_letter == 'w':
    second_number = 23
elif second_letter == 'x':
    second_number = 24
elif second_letter == 'y':
    second_number = 25
else:
    second_number = 26

if first_number > second_number:
    difference = first_number - second_number - 1
elif first_number < second_number:
    difference = second_number - first_number - 1
else:
    difference = 0

print('Первая введенная буква в алфавите находится в положении: {}'.format(first_number))
print('Вторая введенная буква в алфавите находится в положении: {}'.format(second_number))
print('Кол-во букв между введенными буквами: {}'.format(difference))