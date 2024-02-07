"""
Вам доступна генераторная функция matrix_by_elem(), которая принимает в качестве аргумента матрицу произвольной
    размерности и возвращает генератор, порождающий последовательность элементов переданной матрицы.

Перепишете данную функцию с использованием конструкции yield from, чтобы она выполняла ту же задачу.

Примечание 1. Под матрицей подразумеваются исключительно вложенные списки.
"""


def matrix_by_elem(matrix_):
    for row in matrix_:
        yield from row


# INPUT DATA:

# TEST_1:
print('\nтест 1')
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix))

# TEST_2:
print('\nтест 2')
matrix = [[1, 2, 3],
          [4, 5, 6]]

print(list(matrix_by_elem(matrix)))

# TEST_3:
print('\nтест 3')
matrix = [[1, 2, 3, 5, 6, 7, 8],
          [9, 10, 11, 12, 13, 14, 15]]

print(list(matrix_by_elem(matrix)))

# TEST_4:
print('\nтест 4')
matrix = [[1, 2, 3, 5, 6, 7, 8],
          [9, 10, 11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20, 21, 22]]

print(tuple(matrix_by_elem(matrix)))
