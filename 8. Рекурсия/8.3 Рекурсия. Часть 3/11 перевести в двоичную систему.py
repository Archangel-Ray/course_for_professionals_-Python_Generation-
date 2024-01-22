"""
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:

    number — неотрицательное целое число

Функция должна возвращать строковое представление числа number в двоичной системе счисления.
"""


def to_binary(number):
    ans = []

    def func(n):
        if n:
            func(n // 2)
            ans.append(str(n % 2))

    func(number)

    return ''.join(ans) if ans else 0


# INPUT DATA:

# TEST_1:
print(to_binary(15))

# TEST_2:
print(to_binary(0))

# TEST_3:
print(to_binary(1))

# TEST_4:
print(to_binary(256))

# TEST_5:
print(to_binary(2))

# TEST_6:
print(to_binary(1025))

# TEST_7:
print(to_binary(3427))

# TEST_8:
print(to_binary(131445))

# TEST_9:
print(to_binary(532))
