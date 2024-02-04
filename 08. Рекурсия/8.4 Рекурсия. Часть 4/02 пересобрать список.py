"""
Линеаризация — это процесс преобразования списка, который может содержать несколько уровней вложенных списков,
    в список, содержащий все те же элементы без какой-либо вложенности.

Например, список:

    [1, [2, 3], [4, [5, 6, [7, 8, 9]]]]

после линеаризации будет иметь вид:

    [1, 2, 3, 4, 5, 6, 7, 8, 9]

Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:

    nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
                    также являются либо целые числа, либо списки; вложенность может быть произвольной

Функция должна возвращать новый список, представляющий собой линеаризованный список nested_lists.
"""


def linear(nested_lists):
    ending_list = list()
    for next_list in nested_lists:
        if type(next_list) is list:
            ending_list.extend(linear(next_list))
        else:
            ending_list.append(next_list)
    return ending_list


# INPUT DATA:

# TEST_1:
print('\nтест 1')
my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

# TEST_2:
print('\nтест 2')
my_list = [10, 20, 30, 40, 50]

print(linear(my_list))

# TEST_3:
print('\nтест 3')
my_list = [[1], [2], [3], [4, 5], 6, 7]

print(linear(my_list))

# TEST_4:
print('\nтест 4')
my_list = [[123], 23, 43, 65, 754, 3, 1, 2]

print(linear(my_list))

# TEST_5:
print('\nтест 5')
my_list = [3123, 424, 5343, 11, 1, 23, 43, 65, 754, 3, 1, [2]]

print(linear(my_list))

# TEST_6:
print('\nтест 6')
my_list = [[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]]

print(linear(my_list))

# TEST_7:
print('\nтест 7')
my_list = [34534, [656, [7867, [[234, [123, 34534, [758, 978]]]], 667, [4546]]], [2324, [234234, [7656]], 9879, 55]]

print(linear(my_list))

# TEST_8:
print('\nтест 8')
my_list = [12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]]

print(linear(my_list))

# TEST_9:
print('\nтест 9')
my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))

my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))
