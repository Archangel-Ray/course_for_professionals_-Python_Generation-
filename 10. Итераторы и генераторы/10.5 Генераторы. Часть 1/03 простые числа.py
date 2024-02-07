"""
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:

    left — натуральное число
    right — натуральное число

Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно,
    а затем возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и
                самого себя. Единица простым числом не является.
"""


def is_this_a_prime(number):
    if number == 1:
        return False
    sum_ = set()
    for i in range(2, number):
        sum_.add(number % i != 0)
    return all(sum_)


def primes(left, right):
    for x in range(left, right + 1):
        if is_this_a_prime(x):
            yield x


# INPUT DATA:

# TEST_1:
print('\nтест 1')
generator = primes(1, 15)

print(*generator)

# TEST_2:
print('\nтест 2')
generator = primes(6, 36)

print(next(generator))
print(next(generator))

# TEST_3:
print('\nтест 3')
generator = primes(37, 37)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')

# TEST_4:
print('\nтест 4')
generator = primes(39, 83)

print(*generator)

# TEST_5:
print('\nтест 5')
generator = primes(43, 79)

print(*generator)

# TEST_6:
print('\nтест 6')
generator = primes(43, 72)

print(*generator)

# TEST_7:
print('\nтест 7')
generator = primes(1000, 2000)

print(*generator)

# TEST_8:
print('\nтест 8')
generator = primes(2000, 100000)

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
