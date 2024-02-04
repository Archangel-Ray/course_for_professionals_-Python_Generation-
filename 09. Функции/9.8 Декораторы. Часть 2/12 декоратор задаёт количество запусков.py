"""
Реализуйте декоратор retry, который принимает один аргумент:

    times — натуральное число

Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка.
    Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать
    исключение MaxRetriesException.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                # noinspection PyBroadException
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            raise MaxRetriesException

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))

# TEST_2:
print('\nтест 2')


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()

# TEST_3:
print('\nтест 3')


@retry(6)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_4:
print('\nтест 4')


@retry(7)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_5:
print('\nтест 5')


@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_6:
print('\nтест 6')


@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_7:
print('\nтест 7')


@retry(9)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(10, 20))
except Exception as e:
    print(type(e))

# TEST_8:
print('\nтест 8')


@retry(10)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(10, 30))
except Exception as e:
    print(type(e))

# TEST_9:
print('\nтест 9')


@retry(100)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(40, 10))
except Exception as e:
    print(type(e))

# TEST_10:
print('\nтест 10')


@retry(1)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(40, 20))
except Exception as e:
    print(type(e))

# TEST_11:
print('\nтест 11')


@retry(10)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c


try:
    print(calculate(1, 2, c=3))
except Exception as e:
    print(type(e))

# TEST_12:
print('\nтест 12')


@retry(3)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c


try:
    print(calculate(b=1, a=2, c=3))
except Exception as e:
    print(type(e))

# TEST_13:
print('\nтест 13')


@retry(4)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c


try:
    print(calculate(b=2, a=2, c=3))
except Exception as e:
    print(type(e))

# TEST_14:
print('\nтест 14')


@retry(99)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c


try:
    print(calculate(10, b=1, c=2))
except Exception as e:
    print(type(e))

# TEST_15:
print('\nтест 15')


@retry(99)
def calculate(a, b, c):
    """Calculate something"""
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c


print(calculate.__name__)
print(calculate.__doc__)
try:
    print(calculate(2000, b=1, c=4))
except Exception as e:
    print(type(e))
