# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник
# в период с 10:00 до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих
# в это время бассейнов нужно выбрать бассейн с наибольшей длиной дорожки,
# при равных значениях — c наибольшей шириной.
#
# Вам доступен файл pools.json, содержащий список JSON-объектов,
# которые представляют данные о крытых плавательных бассейнах:
#
# Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:
#
#     ObjectName — название, будь то фитнес клуб или спортивный комплекс
#     AdmArea — административный округ
#     District — название района
#     Address — адрес
#     WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
#     DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина
#
# Напишите программу, которая определяет бассейн, подходящий Тимуру.
# Программа должна вывести его размеры и адрес в следующем формате:
#
# <длина>x<ширина>
# <адрес>
#
# Примечание 1. Пример вывода:
#
# 25x16
# Писцовая улица, дом 12, строение 1
#
# Примечание 2. Бассейн должен быть открыт во время всего периода с 10:00 до 12:00.
# Например, если бассейн работает в 10:00, но не работает в 11:30, он не подходит.

from json import load
from datetime import datetime, time


with open('вспомогательные файлы/13/pools.json', encoding='utf-8') as file:
    pools = load(file)
    pools.sort(key=lambda x: x['DimensionsSummer']['Length'] + x['DimensionsSummer']['Width'])
    for pool_object in range(1, len(pools)):
        pool = pools[-pool_object]
        work_time = pool['WorkingHoursSummer']['Понедельник'].split('-')
        open_time = datetime.strptime(work_time[0], '%H:%M').time()
        close_time = datetime.strptime(work_time[1], '%H:%M').time()
        if open_time <= time(10) and close_time >= time(12):
            print(f"{pool['DimensionsSummer']['Length']}x{pool['DimensionsSummer']['Width']}")
            print(pool['Address'])
            break
