new_words = ''


def int_func(word):
    global new_words
    new_words = new_words + word.title() + ' '


user_input = input('Введите несколько слов, разделенных пробелом')
words = user_input.split()
for i in range(len(words)):
    int_func(words[i])
print(new_words)