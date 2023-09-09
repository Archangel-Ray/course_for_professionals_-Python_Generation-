# Вам доступен файл people.json, содержащий список JSON-объектов.
# Причем у различных объектов может быть различное количество ключей:
#
# Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи,
# присваивая этим ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо
# другом объекте, но отсутствует в данном. Программа должна создать список с обновленными JSON-объектами
# и записать его в файл updated_people.json.
#
# Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке.
# Порядок ключей в JSON-объектах не важен.
#
# Примечание 2. Например, если бы файл people.json имел вид:
#
# [
#    {
#       "age": 33,
#       "country": "Lesotho"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]
#
# то программа должна была создать файла updated_people.json со следующим содержанием:
#
# [
#    {
#       "age": 33,
#       "country": "Lesotho"
#       "name": null
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]

import json

with open('вспомогательные файлы/09/people.json', encoding='utf-8') as file_in:
    list_object = json.load(file_in)
    list_keys = set(keys for string in list_object for keys in string.keys())
    for json_object in list_object:
        for key in list_keys:
            json_object.setdefault(key, None)

with open('вспомогательные файлы/09/updated_people.json', 'w', encoding='utf-8') as file_out:
    json.dump(list_object, file_out, indent=3)
