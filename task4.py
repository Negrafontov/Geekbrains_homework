my_list = [22, 23, 22, 4, 5, 67, 4, 68, 67]


def generator(some_list):
    for num, el in enumerate(some_list):
        count = 0
        while True:
            if num == count:
                count += 1
            elif el == some_list[count]:
                break
            elif count == len(some_list) - 1:
                yield el
                break
            else:
                count += 1


def generated_to_list(some_list):
    new_list = []
    for el in some_list:
        new_list.append(el)
    return new_list


generated_list = generator(my_list)
new_list = generated_to_list(generated_list)

print(my_list)
print(new_list)