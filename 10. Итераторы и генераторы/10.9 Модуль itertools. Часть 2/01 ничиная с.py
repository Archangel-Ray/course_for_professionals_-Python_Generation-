"""
Реализуйте функцию drop_while_negative(), которая принимает один аргумент:

    iterable — итерируемый объект, элементами которого являются целые числа

Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable,
    начиная с первого неотрицательного числа.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""
from itertools import dropwhile


def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [-3, -2, -1, 0, 1, 2, 3]

print(*drop_while_negative(numbers))

# TEST_2:
print('\nтест 2')
iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

print(*drop_while_negative(iterator))

# TEST_3:
print('\nтест 3')
iterator = iter([-3, -2, -1, -4, -5, -6])

print(list(drop_while_negative(iterator)))

# TEST_4:
print('\nтест 4')
iterator = iter([0, 1, 2, 3, 4, 5, 6, 7])

print(list(drop_while_negative(iterator)))

# TEST_5:
print('\nтест 5')
iterator = iter([-1, -2, -3, -4, -5, -6, 7])

print(*drop_while_negative(iterator))

# TEST_6:
print('\nтест 6')
iterator = iter([-1, 2, 3, 4, 5, 6, 7, 8])

print(*drop_while_negative(iterator))

# TEST_7:
print('\nтест 7')
iterator = iter([1])

print(*drop_while_negative(iterator))

# TEST_8:
print('\nтест 8')
iterator = iter([-1])

print(list(drop_while_negative(iterator)))

# TEST_9:
print('\nтест 9')
iterator = iter([])

print(list(drop_while_negative(iterator)))
