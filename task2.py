user_input = int(input('Пожалуйста, введите количество секунд, которое необходимо пересчитать в часы и минуты'))
minutes = user_input // 60
hours = minutes // 60
seconds = user_input % 60
if minutes >= 60:
    minutes = minutes % 60
print('{}:{}:{}'.format(hours, minutes, seconds))