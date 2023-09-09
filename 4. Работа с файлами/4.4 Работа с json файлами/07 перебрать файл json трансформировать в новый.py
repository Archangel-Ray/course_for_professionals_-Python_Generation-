# Вам доступен файл data.json, содержащий список различных объектов:
#
# [
#    "nwkWXma",
#    null,
#    {
#       "ISgHT": "dIUbf"
#    },
#    "Pzt",
#    "BXcbGVTE",
#    ...
# ]
#
# Напишите программу, которая создает список, элементами которого являются объекты из списка,
# содержащегося в файле data.json, измененные по следующим правилам:
#
#     если объект является строкой, в его конец добавляется восклицательный знак
#     если объект является числом, он увеличивается на единицу
#     если объект является логическим значением, он инвертируется
#     если объект является списком, он удваивается
#     если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
#     если объект является пустым значением (null), он не добавляется
#
# Полученный список программа должна записать в файл updated_data.json.
#
# Примечание 1. Например, если бы файл data.json имел вид:
#
# ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
#
# то программа должна была бы создать файл updated_data.json со следующим содержанием:
#
# ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

import json

list_string = []
with open('вспомогательные файлы/07/data.json', encoding='utf-8') as file_in:
    for line in json.load(file_in):
        if type(line) is str:
            list_string.append(line + "!")
        elif type(line) in (int, float):
            list_string.append(line + 1)
        elif type(line) is bool:
            list_string.append(not line)
        elif type(line) is list:
            list_string.append(line * 2)
        elif type(line) is dict:
            line["newkey"] = None
            list_string.append(line)

with open('вспомогательные файлы/07/updated_data.json', 'w', encoding='utf-8') as file_out:
    json.dump(list_string, file_out)
