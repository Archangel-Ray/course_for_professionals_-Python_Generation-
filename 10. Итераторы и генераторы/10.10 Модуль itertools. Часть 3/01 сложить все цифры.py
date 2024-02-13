"""
Реализуйте функцию sum_of_digits(), которая принимает один аргумент:

    iterable — итерируемый объект, элементами которого являются натуральные числа

Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.

Примечание 1. Рассмотрим набор чисел 13,20,41,2,2,5 из первого теста. Сумма цифр всех представленных чисел будет равна:
1+3+2+0+4+1+2+2+5=20
"""
from itertools import chain


def sum_of_digits(iterable):
    return sum(map(int, chain(*map(str, iterable))))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(sum_of_digits([13, 20, 41, 2, 2, 5]))

# TEST_2:
print('\nтест 2')
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# TEST_3:
print('\nтест 3')
print(sum_of_digits([123456789]))

# TEST_4:
print('\nтест 4')
numbers = [10]*100

iterator = iter(numbers)
print(sum_of_digits(iterator))

# TEST_5:
print('\nтест 5')
numbers = [100, 20, 30, 400, 500, 5]*100000

print(sum_of_digits(numbers))
