"""
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект

Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
    Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.

Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит словари с хешируемыми значениями.
"""


from collections import ChainMap


def get_all_values(chainmap, key):
    answer = set()
    for single in chainmap.maps:
        if key in single:
            answer.add(single[key])
    return answer


# INPUT DATA:

# TEST_1:
print('\nтест 1')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))

# TEST_2:
print('\nтест 2')
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)

# TEST_3:
print('\nтест 3')
chainmap = ChainMap({'name': 'Anri', 'age': 20}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
result = get_all_values(chainmap, 'name')

print(*sorted(result))

# TEST_4:
print('\nтест 4')
chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
result = get_all_values(chainmap, 'age')

print(*sorted(result))

# TEST_5:
print('\nтест 5')
chainmap = ChainMap({'name': 'Anri', 'city': 'Moscow'}, {'name': 'Arthur', 'city': 'Moscow'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})

result = get_all_values(chainmap, 'city')

print(*sorted(result))

# TEST_6:
print('\nтест 6')
chainmap = ChainMap({'name': 'Anri', 'city': 'Moscow'}, {'name': 'Arthur', 'city': 'Moscow'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})
result = get_all_values(chainmap, 'sex')

print(result)

# TEST_7:
print('\nтест 7')
chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'city': 'Almetyevsk'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})
result = get_all_values(chainmap, 'city')

print(*sorted(result))
