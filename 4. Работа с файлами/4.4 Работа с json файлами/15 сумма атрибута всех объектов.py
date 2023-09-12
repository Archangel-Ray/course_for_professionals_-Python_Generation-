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
#     SeatsCount — количество мест
#
# Напишите программу, которая:
#
#     определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района
#     и количество заведений в нем
#     определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
#
# Полученные значения программа должна вывести в следующем формате:
#
# <район>: <количество заведений>
# <название сети>: <количество заведений>
#
# Примечание 1. Гарантируется, что искомая сеть единственная.

from json import load

with open('файлы/15/food_services.json', encoding='utf-8') as file:
    there_is_food = load(file)
    all_district = {}
    all_operating_company = {}
    for object_with_food in there_is_food:
        all_district[object_with_food['District']] = all_district.get(object_with_food['District'], 0) + 1
        if object_with_food['OperatingCompany']:
            all_operating_company[object_with_food['OperatingCompany']] = \
                all_operating_company.get(object_with_food['OperatingCompany'], 0) + 1

all_district = max(all_district.items(), key=lambda x: x[1])
print(f'{all_district[0]}: {all_district[1]}')
all_operating_company = max(all_operating_company.items(), key=lambda x: x[1])
print(f'{all_operating_company[0]}: {all_operating_company[1]}')
