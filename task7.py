from functools import reduce


def computation(prev_el, el):
    return prev_el * el


def generated_to_list(some_list):
    new_list = []
    for el in some_list:
        new_list.append(el)
    return new_list


def fact(n):
    for i in range(1, n+1):
        fact_list = [el for el in range(1, i+1)]
        true_fact_list = generated_to_list(fact_list)
        fact_computation = reduce(computation, true_fact_list)
        yield fact_computation


user_input = int(input('Введите число, скрипт покажет все факториалы от 1 до Вашего числа'))

for el in fact(user_input):
    print(str(el) + '!=' + str(el))