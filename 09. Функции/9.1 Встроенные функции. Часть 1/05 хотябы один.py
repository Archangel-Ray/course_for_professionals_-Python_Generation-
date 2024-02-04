"""
Реализуйте функцию is_greater(), которая принимает два аргумента в следующем порядке:

    lists — список, элементами которого являются списки целых чисел
    number — целое число

Функция должна возвращать True, если хотя бы в одном вложенном списке из списка lists сумма всех элементов
    больше number, или False в противном случае.

Примечание 1. В задаче удобно воспользоваться функцией any().
"""


def is_greater(lists, number):
    return any(map(lambda x: sum(x) > number, lists))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]

print(is_greater(data, 10))

# TEST_2:
print('\nтест 2')
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

print(is_greater(data, 2))

# TEST_3:
print('\nтест 3')
data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]

print(is_greater(data, 3))

# TEST_4:
print('\nтест 4')
data = [[1, 5, 22, -9], [6, 9, 0, -1, -1], [1, 1, 1], [4, 5, 6, 7], [5, 0, 0, -10, -10]]

print(is_greater(data, 100))

# TEST_5:
print('\nтест 5')
data = [[1, 5, 22, -9], [6, 9, 0, -1, -1], [1, 1, 1], [4, 5, 6, 7], [5, 0, 0, -10, -10]]

print(is_greater(data, 1))

# TEST_6:
print('\nтест 6')
data = [[1, 5, 22, -9], [6, 9, 0, -1, -1], [1, 1, 1], [4, 5, 6, 7], [5, 0, 0, -10, -10]]

print(is_greater(data, 1))

# TEST_7:
print('\nтест 7')
data = [[0]]

print(is_greater(data, 0))

# TEST_8:
print('\nтест 8')
data = [[1, 2, 3, 4, 5, -5, -5]]

print(is_greater(data, 4))

# TEST_9:
print('\nтест 9')
data = [[1, 2, 3, 4, 5, -5, -5]]

print(is_greater(data, 6))

# TEST_10:
print('\nтест 10')
data = [[-1, -2], [-10, -2], [-1, -1, -1, -1], [-20]]

print(is_greater(data, -4))

# TEST_11:
print('\nтест 11')
data = [[-1, -2], [-10, -2], [-1, -1, -1, -1], [-20]]

print(is_greater(data, -2))
