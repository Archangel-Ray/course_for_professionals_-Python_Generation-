"""
Реализуйте декоратор returns, который принимает один аргумент:

    datatype — тип данных

Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype.
    Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) is datatype:
                return result
            raise TypeError

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@returns(int)
def add(a, b):
    return a + b


print(add(10, 5))

# TEST_2:
print('\nтест 2')


@returns(int)
def add(a, b):
    return a + b


try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))

# TEST_3:
print('\nтест 3')


@returns(list)
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))

# TEST_4:
print('\nтест 4')


@returns(list)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))

# TEST_5:
print('\nтест 5')


@returns(tuple)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2, 3], [4, 5, 6]))
except TypeError as e:
    print(type(e))

# TEST_6:
print('\nтест 6')


@returns(int)
def add(a, b):
    return a + b


print(add(a=10, b=5))
