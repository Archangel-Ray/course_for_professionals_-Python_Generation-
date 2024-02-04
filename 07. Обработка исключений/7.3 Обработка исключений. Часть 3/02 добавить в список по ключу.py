"""
Реализуйте функцию add_to_list_in_dict() с использованием конструкции try-except,
которая принимает три аргумента в следующем порядке:

    data — словарь списков, то есть словарь, значениями в котором являются списки
    key — хешируемый объект
    element — произвольный объект

Функция должна добавлять объект element в список по ключу key в словаре data. Если ключа key в словаре data нет,
    функция должна добавить его в словарь, присвоить ему в качестве значения пустой список и
    добавить в этот список объект element.

Примечание 1. Функция должна изменять переданный словарь и возвращать значение None.

Примечание 2. Элементы в список должны добавляться в конец.
"""


def add_to_list_in_dict(data_, key, element):
    # в этом задании я не понял при чём тут отслеживание ошибок. по этому не использовал его:
    # data.setdefault(key, []).append(element)
    # а потом переделал:
    try:
        data_[key]
    except KeyError:
        data_[key] = []
    finally:
        data_[key].append(element)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 7)

print(data)

# TEST_2:
print('\nтест 2')
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'c', 7)

print(data)

# TEST_3:
print('\nтест 3')
data = {}
add_to_list_in_dict(data, 'c', 7)

print(data)

# TEST_4:
print('\nтест 4')
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': []}
add_to_list_in_dict(data, 'c', 7)

print(data)

# TEST_5:
print('\nтест 5')
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 'stepik')

print(data)

# TEST_6:
print('\nтест 6')
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
add_to_list_in_dict(data, 'a', True)
add_to_list_in_dict(data, 'a', -90)
add_to_list_in_dict(data, 'b', False)
add_to_list_in_dict(data, 'b', 'beegeek')
add_to_list_in_dict(data, 'b', None)
add_to_list_in_dict(data, 'c', [])

print(data)

# TEST_7:
print('\nтест 7')
data = {'a': [1, 2, 3]}

add_to_list_in_dict(data, 'a', 1)
add_to_list_in_dict(data, 'a', 3)
add_to_list_in_dict(data, 'b', False)

print(data)
