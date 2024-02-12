"""
Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    n — натуральное число

Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если итерируемый объект iterable
    содержит менее n элементов, функция должна вернуть значение None.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
from itertools import islice


def take_nth(iterable, n):
    return next(islice(iterable, n - 1, None), None)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))

# TEST_2:
print('\nтест 2')
iterator = iter('beegeek')

print(take_nth(iterator, 4))

# TEST_3:
print('\nтест 3')
iterator = iter('beegeek')

print(take_nth(iterator, 10))

# TEST_4:
print('\nтест 4')
iterator = iter('beegeek')

print(take_nth(iterator, 1))

# TEST_5:
print('\nтест 5')
iterator = tuple('stepik')

print(take_nth(iterator, 6))

# TEST_6:
print('\nтест 6')
iterator = iter('p')

print(take_nth(iterator, 1))

# TEST_7:
print('\nтест 7')
iterator = iter('p')

print(take_nth(iterator, 2))

# TEST_8:
print('\nтест 8')
iterator = iter('beegeek')

print(take_nth(iterator, 7))

# TEST_9:
print('\nтест 9')
iterator = iter('beegeek')

print(take_nth(iterator, 8))

# TEST_10:
print('\nтест 10')
print(take_nth([], 4))
