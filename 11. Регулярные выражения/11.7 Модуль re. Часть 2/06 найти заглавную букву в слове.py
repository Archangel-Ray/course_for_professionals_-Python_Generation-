"""
Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое по алфавитному названию начальных
    букв или по начальным звукам слов, входящих в него.

Реализуйте функцию abbreviate(), которая принимает один аргумент:

    phrase — фраза

Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.

Примечание 1. В аббревиатуре должны присутствовать как начальные буквы слов, так и начальные буквы подслов,
                начинающихся с заглавной буквы, например, JavaScript Object Notation -> JSON.
"""
from re import findall


def abbreviate(phrase):
    return "".join(findall(r"\b\w|\B[A-Z]", phrase)).upper()


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(abbreviate('javaScript object notation'))

# TEST_2:
print('\nтест 2')
print(abbreviate('frequently asked questions'))

# TEST_3:
print('\nтест 3')
print(abbreviate('JS game sec'))

# TEST_4:
print('\nтест 4')
print(abbreviate('gaveOver GameStarted happyEnd happyend'))
