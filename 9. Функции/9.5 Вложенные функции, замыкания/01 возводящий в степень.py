"""
Реализуйте функцию power(), которая принимает один аргумент:

    degree — целое число

Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x и
    возвращает значение x в степени degree.

Примечание 1. Рассмотрим пример из первого теста. Вызов power(2) возвращает функцию, которая принимает в качестве
                аргумента число и возводит его во вторую степень. Функция присваивается переменной square. Далее
                полученная функция вызывается с аргументом 5 и возвращает значение 52=25.
"""


def power(degree):
    return lambda x: x ** degree


# INPUT DATA:

# TEST_1:
print('\nтест 1')
square = power(2)
print(square(5))

# TEST_2:
print('\nтест 2')
print(power(3)(3))

# TEST_3:
print('\nтест 3')
result = power(4)(2)
print(result)

# TEST_4:
print('\nтест 4')
result = power(2)(4)
print(result)

# TEST_5:
print('\nтест 5')
result = power(0)(-1)
print(result)

# TEST_6:
print('\nтест 6')
result = power(-2)(2)
print(result)

# TEST_7:
print('\nтест 7')
result = power(-2)(0.25)
print(result)

# TEST_8:
print('\nтест 8')
result = power(17)(17)
print(result)

# TEST_9:
print('\nтест 9')
result = power(1)(-2948492393)
print(result)

# TEST_10:
print('\nтест 10')
result = power(2)(-2948492393)
print(result)
