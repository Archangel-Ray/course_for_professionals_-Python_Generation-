"""
Реализуйте функцию print_operation_table(), которая принимает три аргумента в следующем порядке:

    operation — функция, характеризующая некоторую бинарную операцию
    rows — натуральное число
    cols — натуральное число

Функция должна составлять и выводить таблицу из rows строк и cols столбцов,
    в которой элемент со строкой n и столбцом m имеет значение operation(n, m).

Примечание 1. Нумерация строк и столбцов в таблице начинается с единицы.

Примечание 2. Элементы в строках таблицы должны быть разделены одним пробелом, причем выравнивать таблицу необязательно.

Примечание 3. Бинарная операция — математическая операция, принимающая два аргумента и возвращающая один результат.
"""
from operator import mul


def print_operation_table(operation, rows, cols):
    for n in range(1, rows + 1):
        for m in range(1, cols + 1):
            print(operation(n, m), end=' ')
        print()


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print_operation_table(lambda a, b: a * b, 5, 5)

# TEST_2:
print('\nтест 2')
print_operation_table(pow, 5, 4)

# TEST_3:
print('\nтест 3')
print_operation_table(pow, 5, 10)

# TEST_4:
print('\nтест 4')
print_operation_table(mul, 5, 10)
