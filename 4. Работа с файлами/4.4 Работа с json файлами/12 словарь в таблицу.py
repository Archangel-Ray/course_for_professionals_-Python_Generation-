# Вам доступен файл students.json, содержащий список JSON-объектов,
# которые представляют данные о студентах некоторого курса:
#
# Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:
#
#     name — имя
#     city — город проживания
#     age — возраст
#     progress — прогресс по курсу в процентах
#     phone— контактный номер
#
# Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
#
#     возраст 18 лет или более
#     прогресс по курсу 75% или более
#
# Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер),
# и записать в него данные выбранных студентов, расположив их в лексикографическом порядке имён.
# В качестве разделителя в файле data.csv должна быть использована запятая.
#
# Примечание 1. Гарантируется, что все студенты имеют различные имена.

from csv import writer
from json import load

with open('файлы/12/students.json', encoding='utf-8') as file_dict, \
        open('файлы/12/data.csv', 'w', encoding='utf-8', newline='') as file_table:
    dict_in = load(file_dict)
    list_out = []
    for dict_object in dict_in:
        if dict_object['age'] >= 18 and dict_object['progress'] >= 75:
            list_out.append([dict_object['name'], dict_object['phone']])
    list_out.sort(key=lambda x: x[0])
    writer = writer(file_table)
    writer.writerow(['name', 'phone'])
    writer.writerows(list_out)
