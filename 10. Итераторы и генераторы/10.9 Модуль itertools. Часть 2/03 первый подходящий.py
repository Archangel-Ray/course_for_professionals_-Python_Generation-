"""
Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()

Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция
    predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного
                в качестве аргумента значения.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
from itertools import dropwhile


def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    return next(dropwhile(lambda x: not predicate(x), iterable), None)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_2:
print('\nтест 2')
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

# TEST_3:
print('\nтест 3')
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))

# TEST_4:
print('\nтест 4')
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))

# TEST_5:
print('\nтест 5')
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_6:
print('\nтест 6')
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 1))

# TEST_7:
print('\nтест 7')
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num == 200))

# TEST_8:
print('\nтест 8')
numbers = iter([])

print(first_true(numbers, lambda num: num == 200))
