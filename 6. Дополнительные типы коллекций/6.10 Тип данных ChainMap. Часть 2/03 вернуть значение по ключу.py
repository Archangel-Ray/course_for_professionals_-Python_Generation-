"""
Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:

    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект
    from_left — булево значение, по умолчанию равное True

Функция должна возвращать значение по ключу key из chainmap, причем:

    если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
    если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому

Если ключ key отсутствует в chainmap, функция должна вернуть значение None.
"""
from collections import ChainMap


def get_value(chainmap_, key, from_left=True):
    if key in chainmap_:
        if from_left:
            return chainmap_[key]
        else:
            return chainmap_.maps[-1][key]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

# TEST_2:
print('\nтест 2')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

# TEST_3:
print('\nтест 3')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))

# TEST_4:
print('\nтест 4')
chainmap = ChainMap({'name': 'Arthur'})

print(get_value(chainmap, 'name', False))

# TEST_5:
print('\nтест 5')
chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'name'))

# TEST_6:
print('\nтест 6')
chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'age', False))
