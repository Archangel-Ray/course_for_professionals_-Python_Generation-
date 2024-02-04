"""
Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во вторую степень.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа int или float.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def square(func_):
    @functools.wraps(func_)
    def wrapper(*args, **kwargs):
        return func_(*args, **kwargs) ** 2

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@square
def add(a, b):
    return a + b


print(add(3, 7))

# TEST_2:
print('\nтест 2')


@square
def add(a, b):
    """прекрасная функция"""
    return a + b


print(add(1, 1))
print(add.__name__)
print(add.__doc__)

# TEST_3:
print('\nтест 3')


@square
def beegeek():
    """beegeek docs"""
    return 99


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)

# TEST_4:
print('\nтест 4')


@square
def func(x):
    """classic f(x)"""
    return (x + 1) ** 3


print(func(7))
print(func.__name__)
print(func.__doc__)

# TEST_5:
print('\nтест 5')


@square
def add(a, b, c, d, e):
    return a + b + c + d + e


print(add(1, 2, 3, 4, 5))
print(add.__name__)
print(add.__doc__)

# TEST_6:
print('\nтест 6')


@square
def add(*args, **kwargs):
    return sum([*args, *kwargs.values()])


print(add(3, 7, x=10, y=30))
