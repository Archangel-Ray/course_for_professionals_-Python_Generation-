# Реализуйте функцию is_correct_json(), которая принимает один аргумент:
#
#     string — произвольная строка
#
# Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.
#
# Примечание 1. Вспомните про конструкцию try-except из урока.

import json


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except json.JSONDecodeError:
        return False


# INPUT DATA:

print('TEST_1:')
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))

print('\nTEST_2:')
print(is_correct_json('number = 17'))

print('\nTEST_3:')
data = '''{
        "beegeek": 2018,
        "stepik": 2013
       }'''

print(is_correct_json(data))

print('\nTEST_4:')
data = '''{
        "beegeek": 2018,
        ("Timur", "Guev"): 29,
        ("Artur", "Harisov"): 20,
        "stepik": 2013
       }'''

print(is_correct_json(data))

print('\nTEST_5:')
print(is_correct_json('99999'))

print('\nTEST_6:')
data = '''{
        'beegeek': 2018,
        ('Timur', 'Guev'): 29,
        ('Artur', 'Harisov'): 20,
        'stepik': 2013
       }'''

print(is_correct_json(data))

print('\nTEST_7:')
data = '''{
        'beegeek': 2018,
        'stepik': 2013
       }'''

print(is_correct_json(data))

print('\nTEST_8:')
print(is_correct_json('"beegeek"'))

print('\nTEST_9:')
print(is_correct_json('beegeek'))

print('\nTEST_10:')
print(is_correct_json('["beegeek", 1, 2, 3]'))
