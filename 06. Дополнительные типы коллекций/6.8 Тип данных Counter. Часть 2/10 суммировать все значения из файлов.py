# Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год,
# разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv.
# В каждом файле в первом столбце указывается название продукта, а в последующих — количество
# проданного продукта в килограммах за определенный месяц:
#
# продукт,январь,февраль,март
# Картофель,39,61,3
# Дайкон,51,96,83
# ...
#
# Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта,
# а значением — цена за килограмм в рублях:
#
# {
#    "Картофель": 53,
#    "Дайкон": 55,
# ...
# }
#
# Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

import csv
import json
from collections import Counter

total_vegetables = Counter()

files = 'quarter1.csv quarter2.csv quarter3.csv quarter4.csv'.split()
for file in files:
    with open(f'файлы/10/{file}', encoding="utf-8") as open_csv_file:
        rows = csv.reader(open_csv_file)
        next(rows)
        for key, *values in rows:
            for value in values:
                total_vegetables[key] += int(value)

final_result = int()
with open('файлы/10/prices.json', encoding='utf-8') as open_json_file:
    price_list = json.load(open_json_file)
for key, price in price_list.items():
    final_result += total_vegetables[key] * price
print(final_result)
