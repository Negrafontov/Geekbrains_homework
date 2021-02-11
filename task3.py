# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
import random


def array_generation(m):
    size = 2*m + 1
    min_item = 0
    max_item = 5
    array = [random.randint(min_item, max_item) for _ in range(size)]
    print(array)
    return array


def finding_median(array):
    for i in range(len(array)):
        before = 0
        after = 0
        even = 0
        for a in range(len(array)):
            if a == i:
                pass
            elif array[i] > array[a]:
                before += 1
            elif array[i] < array[a]:
                after += 1
            else:
                even += 1
        while even != 0:
            if before > after:
                after += 1
                even -= 1
            else:
                before += 1
                even -= 1
        if before == after:
            return array[i]


spam_array = array_generation(int(input('Введите натуральное число')))
print(finding_median(spam_array))
print(sorted(spam_array))   # Использую sorted для проверки, а не для решения, не ругайтесь!

