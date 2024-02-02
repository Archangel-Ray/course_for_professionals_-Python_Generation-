"""
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения,
    а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:

    TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
    TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def trace(func_):
    @functools.wraps(func_)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func_.__name__}() с аргументами: {args}, {kwargs}')
        res = func_(*args, **kwargs)
        print(f'TRACE: возвращаемое значение {func_.__name__}(): {res.__repr__()}')
        return res

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')

# TEST_2:
print('\nтест 2')


@trace
def sub(a, b, c):
    """прекрасная функция"""
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)

# TEST_3:
print('\nтест 3')


@trace
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)

# TEST_4:
print('\nтест 4')


@trace
def add(a, b, c):
    """docs"""
    return a + b + c


print(add(1, 2, 3))
print(add.__name__)
print(add.__doc__)

# TEST_5:
print('\nтест 5')


@trace
def add(a, b, c):
    """docs"""
    return a + b + c


print(add(b=3, c=3, a=3))
print(add.__name__)
print(add.__doc__)

# TEST_6:
print('\nтест 6')


@trace
def concat(a, b):
    """concat two strings"""
    return a + b


print(concat('bee', b='geek'))
print(concat.__name__)
print(concat.__doc__)

# TEST_7:
print('\nтест 7')


@trace
def func(nums):
    """прекрасная функция"""
    return list(i ** 2 for i in nums)


print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6])

# TEST_8:
print('\nтест 8')


@trace
def func(nums, degree=3):
    """прекрасная функция"""
    return list(i ** degree for i in nums)


print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6], degree=5)
