"""
Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:

    number — натуральное число

Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.
"""


def print_digits(number):
    if number:
        print(number % 10)
        print_digits(number // 10)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print_digits(12345)

# TEST_2:
print('\nтест 2')
print_digits(7)

# TEST_3:
print('\nтест 3')
print_digits(4868569493888292933)

# TEST_4:
print('\nтест 4')
print_digits(9999999999)
