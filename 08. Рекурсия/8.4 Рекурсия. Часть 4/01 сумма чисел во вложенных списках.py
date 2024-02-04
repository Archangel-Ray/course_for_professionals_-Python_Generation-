"""
Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:

    nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
                    также являются либо целые числа, либо списки; вложенность может быть произвольной

Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
    Если список nested_lists пуст, функция должна вернуть число 0.
"""


def recursive_sum(nested_lists):
    sum_num = int()
    for next_list in nested_lists:
        if type(next_list) == list:
            sum_num += recursive_sum(next_list)
        else:
            sum_num += next_list
    return sum_num


# INPUT DATA:

# TEST_1:
print('\nтест 1')
my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))

# TEST_2:
print('\nтест 2')
my_list = []

print(recursive_sum(my_list))

# TEST_3:
print('\nтест 3')
my_list = [[12, 3232, 123, 24, 54, 6, 7, 28, 39, 1110]]

print(recursive_sum(my_list))

# TEST_4:
print('\nтест 4')
my_list = [[12], 13, 53, 632, 6, 2342341, 534, 76, 87, 87, 98]

print(recursive_sum(my_list))

# TEST_5:
print('\nтест 5')
my_list = [12, 13, 53, 632, 6, 2342341, [98]]

print(recursive_sum(my_list))

# TEST_6:
print('\nтест 6')
my_list = [12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]]

print(recursive_sum(my_list))

# TEST_7:
print('\nтест 7')
my_list = [12, [13, [53, 632], 6], [2342341, [98, 3123, [2432, [1, 1, 2, 3, [4, 4]], 4324]]]]

print(recursive_sum(my_list))

# TEST_8:
print('\nтест 8')
my_list = [[12], [13], [53], [632], [6], [2342341]]

print(recursive_sum(my_list))

# TEST_9:
print('\nтест 9')
my_list = [0, 0, [0, 0, 0, [0, 0], [0, 0]], 0, [0], [0, 0]]

print(recursive_sum(my_list))

# TEST_10:
print('\nтест 10')
my_list = [[[[-11, 99], -7], [35, [-50, -59, 3]], [-63, -89], 36, [0]]]

print(recursive_sum(my_list))

# TEST_11:
print('\nтест 11')
my_list = [-94, -54, 43, -67, -49, 90, -3, 0, 9, 34]

print(recursive_sum(my_list))
