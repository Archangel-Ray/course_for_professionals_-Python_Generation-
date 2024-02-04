"""
Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает два аргумента:

    predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
    iterable — итерируемый объект

Функция должна работать противоположно функции filter(), то есть возвращать итератор, элементами которого являются
    элементы итерируемого объекта iterable, для которых функция predicate вернула значение False.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного
                в качестве аргумента значения.

Примечание 2. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
                в своем исходном порядке.

Примечание 3. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
import string


def filterfalse(predicate, iterable):
    for x in iterable:
        if predicate is None:
            if not x:
                yield x
        elif not predicate(x):
            yield x


# INPUT DATA:

# TEST_1:
print('\nтест 1')
objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))

# TEST_2:
print('\nтест 2')
numbers = (1, 2, 3, 4, 5)

print(*filterfalse(lambda x: x % 2 == 0, numbers))

# TEST_3:
print('\nтест 3')
numbers = [1, 2, 3, 4, 5]

print(*filterfalse(lambda x: x >= 3, numbers))

# TEST_4:
print('\nтест 4')
numbers = range(1, 150, 8)
result = filterfalse(lambda num: num % 8 == 3, numbers)
print(*result)

# TEST_5:
print('\nтест 5')
letters = string.ascii_letters
result = filterfalse(lambda char: ord(char) > 75, letters)
print(*result, sep=',')

# TEST_6:
print('\nтест 6')
objects = [0, 0, 0, True, False, 1788, [], {}, set(), (), '', 0.0, None, 'stepik', dict()]

print(*filterfalse(None, objects))
