"""
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
    являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:

    TypeError, если аргумент не является целым числом
    ValueError, если аргумент является целым числом, но отрицательным или равным нулю

Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных
                аргументов, несоответствующих разным условиям: TypeError, затем ValueError.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        for x in (*args, *kwargs.values()):
            if type(x) is not int:
                raise TypeError
            elif x <= 0:
                raise ValueError
        return func(*args, **kwargs)

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# TEST_2:
print('\nтест 2')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

# TEST_3:
print('\nтест 3')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

# TEST_4:
print('\nтест 4')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(10, 20, 16, 18, '10'))
except Exception as err:
    print(type(err))

# TEST_5:
print('\nтест 5')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(10, 20, '16', 18, '10'))
except Exception as err:
    print(type(err))

# TEST_6:
print('\nтест 6')


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(*range(10, 100)))

# TEST_7:
print('\nтест 7')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(3, 2, 1, -8, 1, 2, 3))
except Exception as err:
    print(type(err))

# TEST_8:
print('\nтест 8')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))

# TEST_9:
print('\nтест 9')


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))

# TEST_10:
print('\nтест 10')


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))

# TEST_11:
print('\nтест 11')


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep='40'))
except Exception as err:
    print(type(err))

# TEST_12:
print('\nтест 12')


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(11, 20.7, 10))
except Exception as err:
    print(type(err))

# TEST_13:
print('\nтест 13')


@takes_positive
def power(a, n):
    return a ** n


try:
    print(power(a="3", n="2"))
except Exception as err:
    print(type(err))
