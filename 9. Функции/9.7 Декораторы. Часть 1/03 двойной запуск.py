"""
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
            а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@do_twice
def beegeek():
    print('beegeek')


beegeek()

# TEST_2:
print('\nтест 2')


@do_twice
def beegeek():
    print('beegeek')


print(beegeek())

# TEST_3:
print('\nтест 3')


@do_twice
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_4:
print('\nтест 4')


@do_twice
def beegeek():
    print('beegeek')


beegeek()
beegeek()
beegeek()

# TEST_5:
print('\nтест 5')


@do_twice
def beegeek(a, b, sep):
    print(a + b + sep)


beegeek(1, 2, sep=10)

# TEST_6:
print('\nтест 6')


@do_twice
def beegeek(*args, **kwargs):
    print('beegeek' * sum(args + tuple(kwargs.values())))


beegeek(1, 1, 1, sep=1, end=2, step=3)
