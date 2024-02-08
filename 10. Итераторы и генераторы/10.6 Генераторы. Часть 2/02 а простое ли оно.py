"""
Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:

    number — натуральное число

Функция должна возвращать True, если число number является простым, или False в противном случае.

Примечание 1. Простое число — натуральное число,
                имеющее ровно два различных натуральных делителя — единицу и самого себя.

Примечание 2. В задаче удобно воспользоваться функциями all() или any().
"""


def is_prime(number):
    return sum(number % x == 0 for x in range(1, number)) == 1


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(is_prime(7))

# TEST_2:
print('\nтест 2')
print(is_prime(8))

# TEST_3:
print('\nтест 3')
print(is_prime(1))

# TEST_4:
print('\nтест 4')
print(is_prime(16))

# TEST_5:
print('\nтест 5')
print(is_prime(27))

# TEST_6:
print('\nтест 6')
print(is_prime(13))

# TEST_7:
print('\nтест 7')
print(is_prime(421))

# TEST_8:
print('\nтест 8')
print(is_prime(1061))

# TEST_9:
print('\nтест 9')
print(is_prime(9973))
