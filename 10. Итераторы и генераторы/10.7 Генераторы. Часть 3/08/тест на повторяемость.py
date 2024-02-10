"""
Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность элементов итерируемого
    объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
from typing import Hashable


def unique(iterable):
    hasheble = {}
    not_hash = set()

    def internal(element):
        if isinstance(element, Hashable):
            if element not in hasheble:
                hasheble[element] = True
                return True
        else:
            if element in not_hash:
                not_hash.add(element)
                return True
        return False

    return (x for x in iterable if internal(x))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))

# TEST_2:
print('\nтест 2')
iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))

# TEST_3:
print('\nтест 3')
data = map(abs, range(-100, 100))

print(*unique(data))

# TEST_4:
print('\nтест 4')
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*unique(data))

# TEST_5:
print('\nтест 5')
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*unique(data))

# TEST_6:
print('\nтест 6')
data = map(str.lower, 'STEPIK')

print(*unique(data))

# TEST_7:
print('\nтест 7')
data = map(str.lower, 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

print(*unique(data))

# TEST_8:
print('\nтест 8')
data = ['bee', 'geek', 'stepik', 'python']

print(*unique(data))

# TEST_9:
print('\nтест 9')
print(list(unique([])))
