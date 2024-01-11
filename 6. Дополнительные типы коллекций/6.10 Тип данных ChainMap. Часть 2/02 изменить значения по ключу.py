"""
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

    chainmap — объект типа ChainMap, элементами которого являются словари
    key — хешируемый объект
    value — произвольный объект

Функция должна изменять все значения по ключу key во всех словарях в chainmap на value.
    Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.

Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.

Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.
"""
from collections import ChainMap


def deep_update(chainmap, key, value):
    if key in chainmap:
        for i in range(len(chainmap.maps)):
            if key in chainmap.maps[i]:
                chainmap.maps[i][key] = value
    else:
        chainmap[key] = value


# INPUT DATA:

# TEST_1:
print('\nтест 1')
chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

# TEST_2:
print('\nтест 2')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)

# TEST_3:
print('\nтест 3')
chainmap = ChainMap({})
deep_update(chainmap, 'city', 'Moscow')

print(chainmap)

# TEST_4:
print('\nтест 4')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur', 'age': 29}, {'name': 'Anri', 'age': 20}, {'name': 'Dima', 'age': 20})
deep_update(chainmap, 'age', 29)

print(chainmap)

# TEST_5:
print('\nтест 5')
chainmap = ChainMap({})

print(deep_update(chainmap, 'city', 'Moscow'))

# TEST_6:
print('\nтест 6')
chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)
