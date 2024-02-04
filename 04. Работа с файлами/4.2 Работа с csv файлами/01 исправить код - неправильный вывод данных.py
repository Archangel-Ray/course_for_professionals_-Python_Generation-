# Вам доступен csv файл grades.csv
# Ниже представлена программа, которая должна открывать данный файл и выводить содержимое каждой строки в виде списка.
# В программе допущена ошибка. Найдите её и исправьте.

import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    for row in rows:
        print(row)
