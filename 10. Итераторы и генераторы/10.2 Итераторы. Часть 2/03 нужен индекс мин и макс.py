"""
Реализуйте функцию get_min_max(), которая принимает один аргумент:

    data — список произвольных объектов, сравнимых между собой

Функция должна возвращать кортеж, в котором первым элементом является индекс минимального элемента в списке data,
    вторым — индекс максимального элемента в списке data. Если список data пуст, функция должна вернуть значение None.

Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть индексы первого по порядку элемента.
"""


def get_min_max(data_):
    return (min(enumerate(data_), key=lambda x: x[1])[0],
            max(enumerate(data_), key=lambda x: x[1])[0]) if data_ else None


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = [2, 3, 8, 1, 7]

print(get_min_max(data))

# TEST_2:
print('\nтест 2')
data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))

# TEST_3:
print('\nтест 3')
data = [9]

print(get_min_max(data))

# TEST_4:
print('\nтест 4')
data = []

print(get_min_max(data))

# TEST_5:
print('\nтест 5')
data = [9, 9, 9, 9, 9]

print(get_min_max(data))

# TEST_6:
print('\nтест 6')
data = list(range(1, 101))

print(get_min_max(data))

# TEST_7:
print('\nтест 7')
data = list(range(1, 101))[::-1]

print(get_min_max(data))

# TEST_8:
print('\nтест 8')
data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58,
        -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30]

print(get_min_max(data))

# TEST_9:
print('\nтест 9')
data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5,
        75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96]

print(get_min_max(data))
