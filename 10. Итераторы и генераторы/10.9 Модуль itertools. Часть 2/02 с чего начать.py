"""
Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    obj — произвольный объект

Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable,
    начиная с элемента, не равного obj.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
from itertools import dropwhile


def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))

# TEST_2:
print('\nтест 2')
iterator = iter('bbbbeebee')

print(*drop_this(iterator, 'b'))

# TEST_3:
print('\nтест 3')
iterator = iter('ssssssssssssssssssssssss')

print(list(drop_this(iterator, 's')))

# TEST_4:
print('\nтест 4')
letters = drop_this(iter('stepik'), 'g')

print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))

# TEST_5:
print('\nтест 5')
numbers = drop_this(map(abs, range(100)), -1)

print(*numbers)

# TEST_6:
print('\nтест 6')
iterator = iter([5, 5, 5, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

print(*drop_this(iterator, 5))

# TEST_7:
print('\nтест 7')
print(list(drop_this('b', 'b')))

# TEST_8:
print('\nтест 8')
print(list(drop_this('a', 'b')))

# TEST_9:
print('\nтест 9')
print(list(drop_this([], None)))
