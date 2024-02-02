"""
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:

    start — неотрицательное целое число
    end — неотрицательное целое число
    char — одиночный символ, по умолчанию равный точке .

Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы в диапазоне индексов
    от start (включительно) до end (не включительно) на символ char.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.

Примечание 2. Гарантируется, что start < end.

Примечание 3. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result[:start] + char * (len(result) - (len(result[:start]) + len(result[end:]))) + result[end:]

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_2:
print('\nтест 2')


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_3:
print('\nтест 3')


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_4:
print('\nтест 4')


@strip_range(1, 2, '-')
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_5:
print('\nтест 5')


@strip_range(100, 200, '=')
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_6:
print('\nтест 6')


@strip_range(0, 300, '=')
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_7:
print('\nтест 7')


@strip_range(0, 4, '=')
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_8:
print('\nтест 8')


@strip_range(0, 1)
def beegeek(word, end=" "):
    """This is... Requiem. What you are seeing is indeed the truth"""
    return word + end


print(beegeek("beegee", end="k"))
print(beegeek.__name__)
print(beegeek.__doc__)
