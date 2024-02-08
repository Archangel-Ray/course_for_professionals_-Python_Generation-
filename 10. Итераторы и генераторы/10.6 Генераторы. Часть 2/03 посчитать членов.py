"""
Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является конечным.
"""


def count_iterable(iterable):
    return sum(1 for _ in iterable)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(count_iterable([1, 2, 3, 4, 5]))

# TEST_2:
print('\nтест 2')
numbers = iter([1, 2, 3, 4, 5, 6, 7])

print(count_iterable(numbers))

# TEST_3:
print('\nтест 3')
data = tuple(range(432, 3845, 17))

print(count_iterable(data))

# TEST_4:
print('\nтест 4')
data = map(abs, range(-200, 400, 11))

print(count_iterable(data))

# TEST_5:
print('\nтест 5')
data = filter(lambda x: x % 13, range(101, 982))

print(count_iterable(data))

# TEST_6:
print('\nтест 6')
data = zip('beegeek', 'stepik')

print(count_iterable(data))

# TEST_7:
print('\nтест 7')
data = zip('', '')

print(count_iterable(data))

# TEST_8:
print('\nтест 8')
data = filter(None, range(100_000_001))

print(count_iterable(data))
