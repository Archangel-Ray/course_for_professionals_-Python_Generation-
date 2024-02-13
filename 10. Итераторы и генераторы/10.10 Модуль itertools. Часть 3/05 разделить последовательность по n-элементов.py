"""
Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные
    в кортежи по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей,
    то ими становится значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
                располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def grouper(iterable, n):
    it = iter(iterable)
    element = next(it, None)
    while element:
        answer = [element]
        for _ in range(n - 1):
            answer.append(next(it, None))
        yield tuple(answer)
        element = next(it, None)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

# TEST_2:
print('\nтест 2')
iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))

# TEST_3:
print('\nтест 3')
iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))

# TEST_4:
print('\nтест 4')
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 4))

# TEST_5:
print('\nтест 5')
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 5))

# TEST_6:
print('\nтест 6')
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 1))

# TEST_7:
print('\nтест 7')
iterator = iter('beegeek')

print(*grouper(iterator, 5))

# TEST_8:
print('\nтест 8')
iterator = iter('beegeek')

print(*grouper(iterator, 20))
