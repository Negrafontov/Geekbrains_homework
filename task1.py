from sys import argv

script_name, hours, per_hour, award = argv


def my_func(hours, per_hour, award):
    payment = (int(hours) * int(per_hour)) + int(award)
    return str(payment)


print('Зарпалата составила: ' + my_func(hours, per_hour, award))