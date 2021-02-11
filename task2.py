# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def array_generation():
    size = 10
    min_item = 0
    max_item = 49.99
    array = [float(format(random.uniform(min_item, max_item), '.2f')) for _ in range(size)]
    print(array)
    return array


def merging(first_array, second_array):
    sorted_array = []
    first_array_index = 0
    second_array_index = 0

    for i in range(len(first_array) + len(second_array)):
        if first_array_index < len(first_array) and second_array_index < len(second_array):
            if first_array[first_array_index] <= second_array[second_array_index]:
                sorted_array.append(first_array[first_array_index])
                first_array_index += 1
            else:
                sorted_array.append(second_array[second_array_index])
                second_array_index += 1
        elif first_array_index == len(first_array):
            sorted_array.append(second_array[second_array_index])
            second_array_index += 1
        elif second_array_index == len(second_array):
            sorted_array.append(first_array[first_array_index])
            first_array_index += 1

    return sorted_array


def merge_sorting(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left_part = merge_sorting(array[:middle])
    right_part = merge_sorting(array[middle:])

    return merging(left_part, right_part)


print(merge_sorting(array_generation()))
