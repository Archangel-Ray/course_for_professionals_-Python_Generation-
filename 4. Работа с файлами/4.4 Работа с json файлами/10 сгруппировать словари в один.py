# Вам доступен файл countries.json, содержащий список JSON-объектов
# c информацией о странах и исповедуемых в них религиях:
#
# Каждый объект из этого списка содержит два атрибута:
#
#     country — страна
#     religion — исповедуемая религия
#
# Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии,
# а в качестве значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект
# программа должна записать в файл religion.json.
#
# Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

import json

with open('файлы/10/countries.json', encoding='utf-8') as file_in, \
        open('файлы/10/religion.json', 'w', encoding='utf-8') as file_out:
    dict_in = json.load(file_in)
    dict_out = {}
    for json_object in dict_in:
        dict_out.setdefault(json_object['religion'], []).append(json_object['country'])
    json.dump(dict_out, file_out, indent=3)
