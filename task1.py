# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
import sys


def size_of_v1(letter1, letter2, number1, number2, dif):
    total_size = sys.getsizeof(letter1) + sys.getsizeof(letter2) + sys.getsizeof(number1) + sys.getsizeof(number2) + \
                 sys.getsizeof(dif) + sys.getsizeof('Пожалуйста, введите строчную букву латинского алфавита') + \
                 sys.getsizeof('Пожалуйста, введите еще одну строчную букву латинского алфавита') + \
                 sys.getsizeof('Первая введенная буква в алфавите находится в положении: {}'.format(number1)) + \
                 sys.getsizeof('Вторая введенная буква в алфавите находится в положении: {}'.format(number2)) + \
                 sys.getsizeof('Кол-во букв между введенными буквами: {}'.format(dif))
    return total_size


def size_of_v2(letter1_v2, letter2_v2, dif_v2, alph):
    total_size_v2 = sys.getsizeof(letter1_v2) + sys.getsizeof(letter2_v2) + sys.getsizeof(dif_v2) + \
                    sys.getsizeof('Пожалуйста, введите строчную букву латинского алфавита') + \
                    sys.getsizeof('Пожалуйста, введите еще одну строчную букву латинского алфавита') + \
                    sys.getsizeof(f'Первая введенная буква в алфавите находится в положении: '
                                  f'{alphabet[first_letter_v2]}') + \
                    sys.getsizeof(f'Вторая введенная буква в алфавите находится в положении: '
                                  f'{alphabet[second_letter_v2]}') + \
                    sys.getsizeof(f'Кол-во букв между введенными буквами: {difference_v2}') + sys.getsizeof(alph)
    return total_size_v2


def size_of_v3(letter1_v3, letter2_v3, alph_v2):
    total_size_v3 = sys.getsizeof(letter1_v3) + sys.getsizeof(letter2_v3) + sys.getsizeof(alph_v2) + \
                    sys.getsizeof('Пожалуйста, введите строчную букву латинского алфавита') + \
                    sys.getsizeof('Пожалуйста, введите еще одну строчную букву латинского алфавита') + \
                    sys.getsizeof(f'Первая введенная буква в алфавите находится в положении: '
                                  f'{alphabet_v2.index(first_letter_v3)}') + \
                    sys.getsizeof(f'Вторая введенная буква в алфавите находится в положении: '
                                  f'{alphabet_v2.index(second_letter_v3)}') + \
                    sys.getsizeof(f'Кол-во букв между введенными буквами:'
                                  f' {abs(alphabet_v2.index(first_letter_v3) - alphabet_v2.index(second_letter_v3))}')
    return total_size_v3


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

# Вариант 2
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26}
first_letter_v2 = input('Пожалуйста, введите строчную букву латинского алфавита')
second_letter_v2 = input('Пожалуйста, введите еще одну строчную букву латинского алфавита')

if first_letter_v2 > second_letter_v2:
    difference_v2 = alphabet[first_letter_v2] - alphabet[second_letter_v2] - 1
elif first_letter_v2 < second_letter_v2:
    difference_v2 = alphabet[second_letter_v2] - alphabet[first_letter_v2] - 1
else:
    difference_v2 = 0

print(f'Первая введенная буква в алфавите находится в положении: {alphabet[first_letter_v2]}')
print(f'Вторая введенная буква в алфавите находится в положении: {alphabet[second_letter_v2]}')
print(f'Кол-во букв между введенными буквами: {difference_v2}')

# Вариант 3
alphabet_v2 = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
first_letter_v3 = input('Пожалуйста, введите строчную букву латинского алфавита')
second_letter_v3 = input('Пожалуйста, введите еще одну строчную букву латинского алфавита')

print(f'Первая введенная буква в алфавите находится в положении: {alphabet_v2.index(first_letter_v3)}')
print(f'Вторая введенная буква в алфавите находится в положении: {alphabet_v2.index(second_letter_v3)}')
print(f'Кол-во букв между введенными буквами: '
      f'{abs(alphabet_v2.index(first_letter_v3) - alphabet_v2.index(second_letter_v3))}')

print(size_of_v1(first_letter, second_letter, first_number, second_number, difference))  # 830
print(size_of_v2(first_letter_v2, second_letter_v2, difference_v2, alphabet))   # 1432
print(size_of_v3(first_letter_v3, second_letter_v3, alphabet_v2))   # 926

# windows 10 home 64 bit
# Python 3.8.5
# Лучшим вариантом считаю третий (при условии, что я верно все посчитал), потому что он не сильно уступает первому
# в памяти, а вот визуально выглядит намного лучше, да и отработать должен быстрее.
