# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях
# общественного питания:
#
# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:
#
#     Name — название
#     IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
#     OperatingCompany — название сети
#     TypeObject — вид (кафе, столовая, ресторан и т.д.)
#     AdmArea — административная зона
#     District — район
#     Address — полный адрес
#     SeatsCount — количество посадочных мест
#
# Напишите программу, которая определяет все виды заведений и для каждого вида находит самое большое заведение
# этого вида (имеет наибольшее количество посадочных мест). Программа должна вывести все виды заведений
# в лексикографическом порядке, указав для каждого самое большое заведение и количество посадочных мест в нем.
# Данные о заведениях должны быть расположены каждые на отдельной строке, в следующем формате:
#
# <вид заведения>: <название заведения>, <количество посадочных мест>
#
# Примечание 1. Начальная часть ответа выглядит так:
#
# бар: Барное объединение ПРОФСОЮЗ, 800
# буфет: СТОЛОВАЯ - КАНТИНАСИТИ, 320
# закусочная: Бургерная FARШ, 74
# ...

from json import load

with open('файлы/15/food_services.json', encoding='utf-8') as file:
    there_is_food = load(file)
    all_types = {}
    for object_with_food in there_is_food:
        if object_with_food['TypeObject'] not in all_types:
            all_types[object_with_food['TypeObject']] = object_with_food['Name'], object_with_food['SeatsCount']
        else:
            if all_types[object_with_food['TypeObject']][1] < object_with_food['SeatsCount']:
                all_types[object_with_food['TypeObject']] = object_with_food['Name'], object_with_food['SeatsCount']

for key, value in sorted(all_types.items()):
    print(f'{key}: {value[0]}, {value[1]}')
