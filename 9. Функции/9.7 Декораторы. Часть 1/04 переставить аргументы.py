"""
Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func
    в обратном порядке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
            а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""


def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))

# TEST_2:
print('\nтест 2')


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))

# TEST_3:
print('\nтест 3')


@reverse_args
def operation(a, b, c):
    return a // b + c


print(operation(10, 20, 80))

# TEST_4:
print('\nтест 4')


@reverse_args
def operation(a, b):
    return a // b


print(operation(90, 0))

# TEST_5:
print('\nтест 5')


@reverse_args
def operation(a, b):
    return a // b


try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

# TEST_6:
print('\nтест 6')


@reverse_args
def operation(a, b, name):
    return a // b + name


print(operation(10, 90, name=1))

# TEST_7:
print('\nтест 7')


@reverse_args
def operation(a, b, value=10):
    return a // b + value


try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

# TEST_8:
print('\nтест 8')


@reverse_args
def operation(a, b, value=10):
    return a // b - value


print(operation(70, 70, value=70))
