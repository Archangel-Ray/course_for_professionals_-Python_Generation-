"""
Реализуйте функцию get_min_max(), которая принимает один аргумент:

    iterable — итерируемый объект, элементы которого сравнимы между собой

Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент
    итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable.
    Если итерируемый объект iterable пуст, функция должна вернуть значение None.
"""
import copy
import functools
import time


def timer(iters=1):
    def timer_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.perf_counter()
                value = func(*args, **kwargs)
                end = time.perf_counter()
                total += end - start
            print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
            return value
        return wrapper
    return timer_func


@timer()
def get_min_max(iterable_):
    try:
        other = copy.deepcopy(iter(iterable_))
        return min(iter(iterable_)), max(other)
    except:
        return


@timer()
def get_min_max_too(iterable_):
    try:
        min_value = max_value = next(iter(iterable_))
        for x in iterable_:
            if x < min_value:
                min_value = x
            elif x > max_value:
                max_value = x
        return min_value, max_value
    except StopIteration:
        return


# INPUT DATA:

# TEST_1:
print('\nтест 1')
iterable = iter(range(10))

print(get_min_max(iterable))

# TEST_2:
print('\nтест 2')
iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

# TEST_3:
print('\nтест 3')
iterable = iter([])

print(get_min_max(iterable))

# TEST_4:
print('\nтест 4')
data = iter((9, 9, 9, 9, 9))

print(get_min_max(data))

# TEST_5:
print('\nтест 5')
data = iter(range(1, 101))

print(get_min_max(data))

# TEST_6:
print('\nтест 6')
data = list(range(1, 101))[::-1]

print(get_min_max(data))

# TEST_7:
print('\nтест 7')
data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58,
             -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30])

print(get_min_max(data))

# TEST_8:
print('\nтест 8')
data = iter([-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5,
             75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96])

print(get_min_max(data))

# TEST_9:
print('\nтест 9')
iterable = []

print(get_min_max(iterable))

# TEST_10:
print('\nтест 10')
iterable = [69]

print(get_min_max(iterable))

# TEST_11:
print('\nтест 11')
data = iter(range(100_000_000))

print(get_min_max(data))

print('\nтест 11 ещё раз')
data = iter(range(100_000_000))

print(get_min_max_too(data))

# TEST_12:
print('\nтест 12')
data = iter(['a', 'b', 'c', 'aaa', 'abc', 'cbc', 'bbb'])

print(get_min_max(data))

# TEST_13:
print('\nтест 13')
data = iter(['bbb'])

print(get_min_max(data))
