"""
Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой
    трех предыдущих:
    1,  1,  1,  3,  5,  9,  17,  31,  57,  105 …

Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:

    n — натуральное число

Функция должна возвращать n-й член последовательности Трибоначчи.
"""


def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 3) + fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(n)


# INPUT DATA:

# TEST_1:
print(tribonacci(1))

# TEST_2:
print(tribonacci(7))

# TEST_3:
print(tribonacci(4))

# TEST_4:
print(tribonacci(3))

# TEST_5:
print(tribonacci(10))

# TEST_6:
print(tribonacci(2))

# TEST_7:
print(tribonacci(300))

# TEST_8:
print(tribonacci(100))
