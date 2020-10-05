my_list = [10, 23, 4, 56, 4, 657, 2, 3, 11]


def generator(some_list):
    for num, el in enumerate(some_list):
        if el > some_list[num - 1]:
            yield el
        else:
            pass


def generated_to_list(some_list):
    new_list = []
    for el in some_list:
        new_list.append(el)
    return new_list


generated_list = generator(my_list)
new_list = generated_to_list(generated_list)
print(my_list)
print(new_list)