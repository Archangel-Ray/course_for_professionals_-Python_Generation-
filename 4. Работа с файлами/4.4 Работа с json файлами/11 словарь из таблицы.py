# Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан тип площадки,
# во втором — административный округ, в третьем — название района, в четвертом — адрес:
#
# Напишите программу, создающую JSON-объект, ключом в котором является административный округ,
# а значением — JSON-объект, в котором, в свою очередь, ключом является название района,
# относящийся к этому административному округу, а значением — список адресов всех площадок в этом районе.
# Полученный JSON-объект программа должна записать в файл addresses.json.
#
# Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.

from csv import reader
from json import dump

with open('вспомогательные файлы/11/playgrounds.csv', encoding='utf-8') as file_table, \
        open('вспомогательные файлы/11/addresses.json', 'w', encoding='utf-8') as file_dict:
    table = reader(file_table, delimiter=';')
    next(table)
    dict_out = {}
    for row in table:
        dict_out.setdefault(row[1], {}).setdefault(row[2], []).append(row[3])
    dump(dict_out, file_dict, indent=3, ensure_ascii=False)
