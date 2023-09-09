# Напишите программу, которая принимает на вход описание одного объекта
# в формате JSON и выводит все пары ключ-значение этого объекта.
#
# Формат входных данных
# На вход программе подается корректное описание одного объекта в формате JSON.
#
# Формат выходных данных
# Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую
# на отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.
#
# Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.
#
# Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin.

from json import loads
from sys import stdin

string = ""
for line in stdin:
    string += line

for key, value in loads(string).items():
    if type(value) == list:
        print(key, end=': ')
        print(*value, sep=', ')
    else:
        print(f'{key}: {value}')
