"""
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.

Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.

Примечание 2. Пустая строка является палиндромом, как и строка, состоящая из одного символа.
"""


def is_palindrome(string):
    if not string or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


# INPUT DATA:

# TEST_1:
print(is_palindrome('stepik'))

# TEST_2:
print(is_palindrome('level'))

# TEST_3:
print(is_palindrome('122333221'))

# TEST_4:
print(is_palindrome('b'))

# TEST_5:
print(is_palindrome('beegeek'))

# TEST_6:
print(is_palindrome('redivider'))

# TEST_7:
print(is_palindrome(''))

# TEST_8:
print(is_palindrome('aa'))

# TEST_9:
print(is_palindrome('ab'))

# TEST_10:
print(is_palindrome('abcca'))
