"""
Реализуйте функцию (),  которая принимает один аргумент:

    numbers — непустой список чисел

Функция должна возвращать True, если все числа в списке numbers являются четными и неотрицательными,
    или False в противном случае.

Примечание 1. В задаче удобно воспользоваться функцией all().
"""


def non_negative_even(numbers):
    return all(map(lambda x: x >= 0 and x % 2 == 0, numbers))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(non_negative_even([0, 2, 4, 8, 16]))

# TEST_2:
print('\nтест 2')
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))

# TEST_3:
print('\nтест 3')
print(non_negative_even([0, 0, 0, 0, 0]))

# TEST_4:
print('\nтест 4')
print(non_negative_even([1, 123, 42, 14, 53453, 66, 7]))

# TEST_5:
print('\nтест 5')
print(non_negative_even([-123, -4234, -5345, -56, -55, -33]))

# TEST_6:
print('\nтест 6')
print(non_negative_even([-122, -46, -78, -56]))

# TEST_7:
print('\nтест 7')
print(non_negative_even([97, 83, 91, 99, 8777, 9999, 8333, 2333123]))

# TEST_8:
print('\nтест 8')
print(non_negative_even([0]))

# TEST_9:
print('\nтест 9')
print(non_negative_even([64, 78, 4454, 234, 90, 78, 67676]))

# TEST_10:
print('\nтест 10')
print(non_negative_even([64, 78, 4454, 234, 90, 78, 0, 67676]))
