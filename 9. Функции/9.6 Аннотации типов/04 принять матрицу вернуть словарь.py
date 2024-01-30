"""
Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая принимает один аргумент:

    matrix — матрица произвольной размерности, элементами которой являются целые или вещественные числа

Функция должна возвращать словарь, ключом в котором является номер строки матрицы,
    а значением — список элементов этой строки.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing.
                Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. Под матрицей подразумеваются исключительно вложенные списки.

Примечание 3. Нумерация строк матрицы в возвращаемом функцией словаре должна начинаться с единицы.

Примечание 4. Элементы матрицы в списке должны располагаться в своем исходном порядке.
"""


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i: x for i, x in enumerate(matrix, 1)}


# INPUT DATA:

# TEST_1:
print('\nтест 1')
matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))

# TEST_2:
print('\nтест 2')
matrix = [[5.1, 6, 7.94]]

print(matrix_to_dict(matrix))

# TEST_3:
print('\nтест 3')
annotations = matrix_to_dict.__annotations__

print(annotations['return'])

# TEST_4:
print('\nтест 4')
matrix = [[3, 66, 71], [8.0, 3.1, 2.88], [13, 22, 76], [19, 21, 22]]

print(matrix_to_dict(matrix))

# TEST_5:
print('\nтест 5')
print(*matrix_to_dict.__annotations__.values())

# TEST_6:
print('\nтест 6')
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

print(matrix_to_dict(matrix))

# TEST_7:
print('\nтест 7')
matrix = [[1, 2, 3, 4, 5, 6, 7, 8]]

print(matrix_to_dict(matrix))
