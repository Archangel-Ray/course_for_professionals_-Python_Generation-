"""
Реализуйте функцию convert(), которая принимает один аргумент:

    number — целое число

Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:

    двоичное представление числа number в виде строки без префикса 0b
    восьмеричное представление числа number в виде строки без префикса 0o
    шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x

Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
"""


def representation(s):
    return s[2:].upper() if s[0] != '-' else '-' + s[3:].upper()


def convert(number):
    return representation(bin(number)), representation(oct(number)), representation(hex(number))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(convert(15))

# TEST_2:
print('\nтест 2')
print(convert(-24))

# TEST_3:
print('\nтест 3')
print(convert(1))

# TEST_4:
print('\nтест 4')
print(convert(0))

# TEST_5:
print('\nтест 5')
print(convert(-132))

# TEST_6:
print('\nтест 6')
print(convert(78))
