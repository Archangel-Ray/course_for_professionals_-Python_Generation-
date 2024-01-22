"""
Реализуйте функцию recursive_sum() с использованием рекурсии, которая принимает два аргумента в следующем порядке:

    a — неотрицательное целое число
    b — неотрицательное целое число

Функция должна возвращать сумму чисел a и b. При вычислении суммы функция:

    не должна использовать циклы
    из всех арифметических операций должна использовать только +1 и −1
"""


def recursive_sum(a, b):
    if b:
        return recursive_sum(a + 1, b - 1)
    return a


# INPUT DATA:

# TEST_1:
print(recursive_sum(10, 22))

# TEST_2:
print(recursive_sum(99, 0))

# TEST_3:
print(recursive_sum(0, 0))

# TEST_4:
print(recursive_sum(1, 1))

# TEST_5:
print(recursive_sum(0, 78))

# TEST_6:
print(recursive_sum(13, 27))

# TEST_7:
print(recursive_sum(74, 11))

# TEST_8:
print(recursive_sum(91, 92))

# TEST_9:
print(recursive_sum(62, 62))
