# Реализуйте функцию same_parity(), которая принимает один аргумент:
#
#     numbers — список целых чисел
#
# Функция должна возвращать новый список, элементами которого являются числа из списка numbers,
# имеющие ту же четность, что и первый элемент этого списка.


def same_parity(value):
    if not value:
        return []
    new_list = []
    if value[0] % 2 == 0:
        for num in value:
            if num % 2 == 0:
                new_list.append(num)
    if value[0] % 2 != 0:
        for num in value:
            if num % 2 != 0:
                new_list.append(num)

    return new_list


# INPUT DATA:

# TEST_1:
print(same_parity([]))

# TEST_2:
print(same_parity([6, 0, 67, -7, 10, -20]))

# TEST_3:
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))

# TEST_4:
print(same_parity([2]))

# TEST_5:
print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))

# TEST_6:
print(same_parity([-1, 1248234832443, 8]))

# TEST_7:
print(same_parity([1, 2, 4, 6, 8]))

# TEST_8:
print(same_parity([1, 3, 5, 7, 9]))
