from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


def generated_to_list(some_list):
    new_list = []
    for el in some_list:
        new_list.append(el)
    return new_list


generated_list = [el for el in range(100, 1001) if el % 2 == 0]
print(*(el for el in range(100, 1001) if el % 2 == 0))

my_list = generated_to_list(generated_list)

print(reduce(my_func, my_list))