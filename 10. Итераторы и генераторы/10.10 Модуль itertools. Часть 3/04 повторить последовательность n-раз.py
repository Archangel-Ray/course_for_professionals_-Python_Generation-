"""
Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    times — натуральное число

Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable,
    зацикленных times раз.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
from itertools import tee, chain


def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(*ncycles([1, 2, 3, 4], 3))

# TEST_2:
print('\nтест 2')
iterator = iter('bee')

print(*ncycles(iterator, 4))

# TEST_3:
print('\nтест 3')
iterator = iter([1])

print(*ncycles(iterator, 10))

# TEST_4:
print('\nтест 4')
iterator = ncycles(iter('b'), 1)

print(next(iterator))

# TEST_5:
print('\nтест 5')
iterator = ncycles(iter('g'), 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_6:
print('\nтест 6')
iterator = ncycles(iter([10, 10, 10, 10, 10]), 5)

print(*iterator)

# TEST_7:
print('\nтест 7')
print(list(ncycles([], 5)))
