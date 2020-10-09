with open("task1.txt", 'w') as task_file:
    check = True
    while check is True:
        user_input = input('Пожалуйста, введите текст. Для завершения записи не вводите ничего и жмите enter')
        if user_input == '':
            check = False
            break
        else:
            task_file.write(user_input + '\n')