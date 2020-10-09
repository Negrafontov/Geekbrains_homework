with open("task4.txt", 'r') as old_file:
    content = old_file.readlines()
    print(content)
    for num, el in enumerate(content):
        content_list = el.split(' ')
        if num == 0:
            with open("task4_new.txt", 'w') as new_file:
                content_list[0] = 'Один'
                new_file.writelines(content_list)
        else:
            with open("task4_new.txt", 'a') as new_file:
                if content_list[0] == 'Two':
                    content_list[0] = 'Два'
                    new_file.writelines(content_list)
                elif content_list[0] == 'Three':
                    content_list[0] = 'Три'
                    new_file.writelines(content_list)
                elif content_list[0] == 'Four':
                    content_list[0] = 'Четыре'
                    new_file.writelines(content_list)