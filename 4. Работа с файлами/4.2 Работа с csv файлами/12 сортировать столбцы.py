# Вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором учебном заведении
# за период 20002000 — 20212021 г. В первом столбце записан год, в последующих столбцах записан класс и количество
# учеников в данном классе в этом году:
#
# year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
# 2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
# 2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
# ...
#
# Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv,
# располагая все столбцы в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

import csv

with open('вспомогательные файлы/student_counts.csv', encoding='utf-8') as file_in, \
        open('вспомогательные файлы/sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_out:
    rows = csv.reader(file_in)
    table_name, *column_headings = next(rows)
    dict_rows = {}
    for line in rows:
        dict_rows[line[0]] = {}
        for ind in range(len(column_headings)):
            dict_rows[line[0]][column_headings[ind]] = line[ind + 1]
    sorted_column_headings = sorted(column_headings, key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    writer = csv.writer(file_out)
    writer.writerow([table_name] + sorted_column_headings)
    for key, values in dict_rows.items():
        new_string = [key, ]
        for value_key in sorted_column_headings:
            new_string.append(dict_rows[key][value_key])
        writer.writerow(new_string)
