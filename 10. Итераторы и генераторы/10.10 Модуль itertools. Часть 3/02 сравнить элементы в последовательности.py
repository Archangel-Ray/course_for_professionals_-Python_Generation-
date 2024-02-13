"""
Реализуйте функцию is_rising(), которая принимает один аргумент:

    iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию,
    или False в противном случае.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством,
                а также содержит не менее двух элементов.
"""
from itertools import tee, starmap  # pairwise


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def is_rising(iterable):
    return all(starmap(lambda x, y: x < y, pairwise(iterable)))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(is_rising([1, 2, 3, 4, 5]))

# TEST_2:
print('\nтест 2')
iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

# TEST_3:
print('\nтест 3')
iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

# TEST_4:
print('\nтест 4')
iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))

# TEST_5:
print('\nтест 5')
iterator = iter(list(range(100, 201)) + [200])

print(is_rising(iterator))

# TEST_6:
print('\nтест 6')
iterator = iter([10]*50)

print(is_rising(iterator))
