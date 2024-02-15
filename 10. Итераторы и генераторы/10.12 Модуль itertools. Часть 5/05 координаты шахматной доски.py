"""
Вам доступна программа, которая выводит все обозначения полей шахматной доски в алфавитном порядке через пробел.

Перепишите данную программу с использованием функции product(), чтобы она выполняла ту же задачу.

Примечание 1. Начальная часть ответа выглядит так:

a1 a2 a3 a4 a5 a6 a7 a8 b1 b2 ...
"""
from string import ascii_lowercase
from itertools import product

letters = ascii_lowercase[:8]
digits = [1, 2, 3, 4, 5, 6, 7, 8]

for letter in letters:
    for digit in digits:
        print(letter, digit, sep='', end=' ')

print()
print(*(f"{x[0]}{x[1]}" for x in product(letters, digits)))
