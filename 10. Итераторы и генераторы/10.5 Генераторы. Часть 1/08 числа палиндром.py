"""
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.

Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.
"""


def palindromes():
    counter = 0
    while True:
        counter += 1
        if counter == int(str(counter)[::-1]):
            yield counter

palindrome = palindromes()

for i in range(200):
    print(next(palindrome))
