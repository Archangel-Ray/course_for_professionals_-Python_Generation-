# Рассмотрим следующий словарь:
#
# {'a': [1, 2], 'b': [3, 1], 'c': [2]}
#
# «Перевернем» его, представив ключи в виде значений, а значения — в виде ключей:
#
# {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
#
# Реализуйте функцию flip_dict(), которая принимает один аргумент:
#
#     dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк
#
# Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию),
# который представляет собой «перевернутый» словарь dict_of_lists.
#
# Примечание 1. Ключи в возвращаемом функцией словаре, а также элементы в списках должны располагаться
# в своем исходном порядке.

from collections import defaultdict


def flip_dict(dict_of_lists):
    new_dict = defaultdict(list)
    for next_key, list_value in dict_of_lists.items():
        for value in list_value:
            if value in dict_of_lists[next_key]:
                new_dict[value].append(next_key)
    return new_dict


# INPUT DATA:

TEST_1 = flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]})
print(TEST_1)
res = defaultdict(list, {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']})
print('TEST_1 - ', True if TEST_1 == res else False, '\n')

# TEST_2:
data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
res_2 = '''
cacao: Arthur
tea: Arthur, Timur
juice: Arthur, Timur, Anri
coffee: Timur, Anri
'''
for key, values in flip_dict(data).items():
    string = f'{key}: {", ".join(values)}'
    print(string, '\n', True if string in res_2 else False)
print()

# TEST_3:
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
TEST_3 = flip_dict(data)
res_3 = defaultdict(list, {1: ['a'], 2: ['a'], 3: ['a'], 4: ['b'], 5: ['b'], 6: ['b'], 7: ['c'], 8: ['c'], 9: ['c']})
print(TEST_3, '\n', 'TEST_3 - ', True if TEST_3 == res_3 else False, '\n')

# TEST_4:
data = {'a': [1, 2, 3, 5, 7], 'b': [4, 5, 6, 8, 1, 2], 'c': [7, 8, 9, 3, 2, 4], 'd': [1, 4, 6, 8, 9]}
TEST_4 = flip_dict(data)
res_4 = defaultdict(list, {1: ['a', 'b', 'd'], 2: ['a', 'b', 'c'], 3: ['a', 'c'], 5: ['a', 'b'], 7: ['a', 'c'],
                           4: ['b', 'c', 'd'], 6: ['b', 'd'], 8: ['b', 'c', 'd'], 9: ['c', 'd']})
print(TEST_4, '\n', 'TEST_4 - ', True if TEST_4 == res_4 else False, '\n')

# TEST_5:
data = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c', 'c'], 3: ['c', 'd', 'a'], 4: ['a', 'b', 'r', 'f'],
        5: ['y', 'u', 'e', 'w']}
TEST_5 = flip_dict(data)
res_5 = defaultdict(list, {'a': [1, 2, 3, 4], 'b': [1, 2, 4], 'c': [1, 2, 2, 3], 'd': [3], 'r': [4], 'f': [4],
                           'y': [5], 'u': [5], 'e': [5], 'w': [5]})
print(TEST_5, '\n', 'TEST_5 - ', True if TEST_5 == res_5 else False, '\n')

# TEST_6:
data = {6: [1, 2, 3], 88: [3, 4, 6], '99': ['a', 'f', '3', 1, 2, 3], 'a': [1, 2, 3]}
TEST_6 = flip_dict(data)
res_6 = defaultdict(list, {1: [6, '99', 'a'], 2: [6, '99', 'a'], 3: [6, 88, '99', 'a'], 4: [88], 6: [88],
                           'a': ['99'], 'f': ['99'], '3': ['99']})
print(TEST_6, '\n', 'TEST_6 - ', True if TEST_6 == res_6 else False, '\n')
