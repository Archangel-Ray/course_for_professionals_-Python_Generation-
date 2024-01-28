"""
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:

    values — список чисел
    group — список, кортеж или множество чисел

Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group,
    которая должна следовать первой.
"""

# первое решение
# def sort_priority(values, group_):
#     new_sort = [x for x in sorted(group_) if x in values]
#     new_sort.extend([x for x in sorted(values) if x not in group_])
#     values[:] = new_sort


def sort_priority(values, group_):
    """второе решение"""
    values.sort(key=lambda x: (x not in group_, x))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)

# TEST_2:
print('\nтест 2')
numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)

# TEST_3:
print('\nтест 3')
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)

# TEST_4:
print('\nтест 4')
numbers = list(range(100, -100, -1))
sort_priority(numbers, (98, 97, 100, 5, -9, -34))

print(numbers)

# TEST_5:
print('\nтест 5')
data = list(range(0, 100, 5))
sort_priority(data, {1, 90, 95, 25, 55, 64})

print(data)
