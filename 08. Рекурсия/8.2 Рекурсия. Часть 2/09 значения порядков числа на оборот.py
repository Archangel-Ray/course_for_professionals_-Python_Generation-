"""
Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:

    number — натуральное число

Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.
"""


def print_digits(number):
    if number:
        print_digits(number // 10)
        print(number % 10)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print_digits(12345)

# TEST_2:
print('\nтест 2')
print_digits(2077)

# TEST_3:
print('\nтест 3')
print_digits(8)

# TEST_4:
print('\nтест 4')
print_digits(84293825)

# TEST_5:
print('\nтест 5')
print_digits(9999999999)
