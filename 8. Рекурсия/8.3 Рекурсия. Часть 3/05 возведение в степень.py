"""
Реализуйте функцию get_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:

    a — положительное целое число
    n — неотрицательное целое число

Функция должна вычислять значение a в степени n и возвращать полученный результат.

Примечание 1. При решении не используйте оператор возведения в степень **.

Примечание 2. Для построения рекурсивного алгоритма воспользуйтесь следующим рекуррентным соотношением:
(a)n=(a)⋅(a)n−1
"""


def get_pow(a, n):
    if n:
        return a * get_pow(a, n - 1)
    return 1


# INPUT DATA:

# TEST_1:
print(get_pow(5, 2))

# TEST_2:
print(get_pow(99, 0))

# TEST_3:
print(get_pow(2, 10))

# TEST_4:
print(get_pow(99999, 1))

# TEST_5:
print(get_pow(8, 4))

# TEST_6:
print(get_pow(7, 7))

# TEST_7:
print(get_pow(10, 4))

# TEST_8:
print(get_pow(11, 12))
