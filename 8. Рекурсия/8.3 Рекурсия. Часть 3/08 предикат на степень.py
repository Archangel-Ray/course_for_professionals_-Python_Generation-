"""
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:

    number — натуральное число

Функция должна возвращать значение True, если number является степенью числа 22, или False в противном случае.
"""


def is_power(number):
    if number < 2:
        return True if number == 1 else False
    return is_power(number / 2)


# INPUT DATA:

# TEST_1:
print(is_power(512))

# TEST_2:
print(is_power(15))

# TEST_3:
print(is_power(1))

# TEST_4:
print(is_power(2))

# TEST_5:
print(is_power(100))

# TEST_6:
print(is_power(128))

# TEST_7:
print(is_power(1024))

# TEST_8:
print(is_power(1111111))
