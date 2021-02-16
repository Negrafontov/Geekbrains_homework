# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
import hashlib


def unique_substrings(your_string):
    unique_dict = dict()
    string_hash = hashlib.sha1(your_string.encode('utf-8')).hexdigest()
    for i in range(len(your_string) + 1):
        for e in range(i + 1, len(your_string) + 1):
            substring_hash = hashlib.sha1(your_string[i:e].encode('utf-8')).hexdigest()
            if substring_hash not in unique_dict:
                unique_dict[hashlib.sha1(your_string[i:e].encode('utf-8')).hexdigest()] = your_string[i:e]
    unique_dict.pop(string_hash)
    return unique_dict


string = input('Пожалуйста, введите данные строчного типа')
result = unique_substrings(string)
print(f'Количество уникальных подстрок в строке "{string}" равно {len(result)}')
print(result)
for item in result:
    print(result[item])
