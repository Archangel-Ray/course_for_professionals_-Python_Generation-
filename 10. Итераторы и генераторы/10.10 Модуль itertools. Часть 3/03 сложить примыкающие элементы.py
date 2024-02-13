"""
Реализуйте функцию max_pair(), которая принимает один аргумент:

    iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.

Примечание 1. Рассмотрим список чисел 1,8,2,4,3 из первого теста. Из данной последовательности можно получить следующие
                пары соседних элементов: 1 и 8, 8 и 2, 2 и 4, 4 и 3. Максимальную сумму имеет вторая пара — 10.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством,
                а также содержит не менее двух элементов.
"""
from itertools import tee, starmap  # pairwise


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def max_pair(iterable):
    return max(starmap(lambda x, y: x + y, pairwise(iterable)))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(max_pair([1, 8, 2, 4, 3]))

# TEST_2:
print('\nтест 2')
iterator = iter([1, 2, 3, 4, 5])

print(max_pair(iterator))

# TEST_3:
print('\nтест 3')
iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(max_pair(iterator))

# TEST_4:
print('\nтест 4')
iterator = iter([10, 11])

print(max_pair(iterator))

# TEST_5:
print('\nтест 5')
iterator = iter([5, 6, 4, 3, 2, 2])

print(max_pair(iterator))

# TEST_6:
print('\nтест 6')
iterator = iter([10, 10, 10, 10, 10, 10, 10, 10, 10])

print(max_pair(iterator))

# TEST_7:
print('\nтест 7')
iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 1])

print(max_pair(iterator))

# TEST_8:
print('\nтест 8')
iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 107])

print(max_pair(iterator))
