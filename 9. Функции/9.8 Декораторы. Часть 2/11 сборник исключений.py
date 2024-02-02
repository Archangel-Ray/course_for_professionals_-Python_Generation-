"""
Реализуйте декоратор ignore_exception, который принимает произвольное количество
    позиционных аргументов — типов исключений, и выводит текст:

Исключение <тип исключения> обработано

если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.

Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def ignore_exception(*exception_types):
    def decorator(func_):
        @functools.wraps(func_)
        def wrapper(*args, **kwargs):
            try:
                return func_(*args, **kwargs)
            except Exception as E:
                if type(E) in exception_types:
                    print(f"Исключение {type(E).__name__} обработано")
                else:
                    raise E

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)

# TEST_2:
print('\nтест 2')
min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))

# TEST_3:
print('\nтест 3')


@ignore_exception()
def func():
    """func docs"""
    raise ValueError


try:
    func()
except Exception as e:
    print(type(e))

# TEST_4:
print('\nтест 4')


@ignore_exception(TypeError)
def func():
    """func docs"""
    raise ValueError


try:
    func()
except Exception as e:
    print(type(e))

# TEST_5:
print('\nтест 5')


@ignore_exception(ValueError, TypeError, NameError)
def func():
    """func docs"""
    raise ValueError


print(func.__name__)
print(func.__doc__)

try:
    func()
except Exception as e:
    print(type(e))

# TEST_6:
print('\nтест 6')


@ignore_exception(ValueError, TypeError, NameError)
def func():
    """func docs"""
    raise NameError


try:
    func()
except Exception as e:
    print(type(e))

# TEST_7:
print('\nтест 7')


@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def func():
    """func docs"""
    raise ZeroDivisionError


try:
    func()
except Exception as e:
    print(type(e))

# TEST_8:
print('\nтест 8')


@ignore_exception(ValueError, NameError, ZeroDivisionError, TypeError)
def func(a, b, c):
    """func docs"""
    raise NameError


try:
    func(1, 2, c=10)
except Exception as e:
    print(type(e))

# TEST_9:
print('\nтест 9')


@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    return 'beegeek'


print(beegeek())
