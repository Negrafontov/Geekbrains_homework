with open("task5.txt", 'w+') as task_file:
    task_file.write('1 2 3 4 5 6 7 8 9')
    task_file.seek(0)
    result = 0
    for num, el in enumerate(task_file.readlines()[0].split(' ')):
        result = result + int(el)
    print(result)