# в коментария увидел интересный вариант решения этого задания. захотел разобраться как он работает.

import json

with open('вспомогательные файлы/07/data.json', encoding='utf-8') as file_in:
    open_file = json.load(file_in)

converter = {
    'str': lambda x: x + '!',
    'int': lambda x: x + 1,
    'bool': lambda x: not x,
    'list': lambda x: x * 2,
    'dict': lambda x: {**x, 'newkey': None},
}

new_list = []
for value in open_file:
    if value is not None:
        type_value = type(value).__name__
        new_value = converter[type_value](value)
        new_list.append(new_value)

with open('вспомогательные файлы/07/updated_data.json', 'w', encoding='utf-8') as file_out:
    json.dump(new_list, file_out)
