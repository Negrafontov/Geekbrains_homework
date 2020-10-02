result = 0
quiting = False
q_position = 0


def check(current_list):
    global quiting, q_position
    for el in current_list:
        try:
            q_position = current_list.index('q')
            quiting = True
            return q_position, quiting
        except ValueError:
            pass


def my_func(current_list):
    global result
    for num, el in enumerate(current_list):
        result = result + int(current_list[num])
    return result


while True:
    user_input = input('Пожалуйста, введите несколько чисел, разделенных пробелом. Если вы хотите завершить ввод, '
                       'введите "q".')
    my_list = user_input.split()
    check(my_list)
    if quiting is True:
        for i in range(q_position):
            result = result + int(my_list[i])
        print(result)
        break
    else:
        my_func(my_list)
    print(result)