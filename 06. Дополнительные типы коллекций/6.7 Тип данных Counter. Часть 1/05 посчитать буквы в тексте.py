# Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:
#
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# ...
#
# Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и
# их количество должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:
#
# <буква>: <количество>
#
# Примечание 1. Начальная часть ответа выглядит так:
#
# a: 53
# b: 21
# ...
#
# Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.
#
# Примечание 3. Программа должна игнорировать все небуквенные символы.

from collections import Counter

with open('файлы/05/pythonzen.txt') as file:
    counter = Counter()
    for letter in file.read().lower():
        if letter.isalpha():
            counter.update(letter)

for key in sorted(counter):
    print(f'{key}: {counter[key]}')
