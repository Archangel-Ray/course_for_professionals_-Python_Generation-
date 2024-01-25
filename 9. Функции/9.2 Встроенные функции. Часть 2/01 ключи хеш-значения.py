"""
Реализуйте функцию hash_as_key(), которая принимает один аргумент:

    objects — список хешируемых объектов

Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects,
    а значением — сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.

Примечание 1. Элементы в возвращаемом функцией словаре, а также объекты в списке, имеющие равные хеш-значения,
                должны располагаться в своем исходном порядке.
"""


def hash_as_key(objects):
    returned_dict = {}
    for objective in objects:
        hash_object = hash(objective)
        if hash_object in returned_dict:
            if isinstance(returned_dict[hash_object], list):
                returned_dict[hash_object].append(objective)
            else:
                returned_dict[hash_object] = [returned_dict[hash_object], objective]
        else:
            returned_dict[hash_object] = objective
    return returned_dict


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))

# TEST_2:
print('\nтест 2')
data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))

# TEST_3:
print('\nтест 3')
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))

# TEST_4:
print('\nтест 4')
data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]

print(hash_as_key(data))

# TEST_5:
print('\nтест 5')
data = [frozenset((1, 2, 3, 4)), frozenset((4, 5, 6)), frozenset((1, 2, 3, 4)), frozenset((7, 8, 9, 10)), (1, 2, 3, 4), 100, 192, 221, (44, 44, 44), (44, 44, 44, 44), (44, 44, 44, 44)]

print(hash_as_key(data))

# TEST_6:
print('\nтест 6')
data = [(1, 2, 3, (100, 200, 300)), (frozenset((90, 100, 110)), 10, 222), ((100, 200, 3300), (100, 100)), 900, 999, 1000, 999999999991, (123123123, 234234234, 2342354536758578), 900, 1000000, 1000]

print(hash_as_key(data))

# TEST_7:
print('\nтест 7')
data = [5, 5, 5]

print(hash_as_key(data))
