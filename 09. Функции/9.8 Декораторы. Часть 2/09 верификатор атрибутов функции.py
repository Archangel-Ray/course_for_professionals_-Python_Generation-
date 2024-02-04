"""
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов,
    каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов.
    Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in [*args, *kwargs.values()]:
                if type(arg) not in types:
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@takes(int, str)
def repeat_string(string, times):
    return string * times


print(repeat_string('bee', 3))

# TEST_2:
print('\nтест 2')


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times


try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

# TEST_3:
print('\nтест 3')


@takes(list)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], [3, 4]))
except TypeError as e:
    print(type(e))

# TEST_4:
print('\nтест 4')


@takes(list)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], 3))
except TypeError as e:
    print(type(e))

# TEST_5:
print('\nтест 5')


@takes(str, int, list)
def add(a, b):
    """add docs"""
    return a + b


print(add.__name__)
print(add.__doc__)

try:
    print(add('a', 'b'))
except TypeError as e:
    print(type(e))

# TEST_6:
print('\nтест 6')


@takes(list, int, tuple, str)
def add(a, b):
    """add docs"""
    return a + b


print(add.__name__)
print(add.__doc__)

try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))

# TEST_7:
print('\nтест 7')


@takes(list, int, tuple, str)
def add(a, b):
    """add docs"""
    return a + b


print(add.__name__)
print(add.__doc__)

try:
    print(add(1, b=2))
except TypeError as e:
    print(type(e))

# TEST_8:
print('\nтест 8')


@takes(list, int, float, str)
def add(a, b):
    """add docs"""
    return a + b


print(add.__name__)
print(add.__doc__)

try:
    print(add((1, 2), (3, 4, 5)))
except TypeError as e:
    print(type(e))

# TEST_9:
print('\nтест 9')


@takes()
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek())

# TEST_10:
print('\nтест 10')


@takes(str)
def beegeek(word):
    return word


print(beegeek(word="beegeek"))

# TEST_11:
print('\nтест 11')


@takes(str)
def beegeek(word, repeat):
    return word * repeat


try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))
