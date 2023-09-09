# Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении.
# В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен,
# в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:
#
# Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз
# с различной оценкой и различными датой и временем сдачи.
#
# Напишите программу, которая для каждого студента определяет его максимальную оценку,
# а также дату и время ее получения. Программа должна создать список словарей,
# каждый из которых содержит следующие пары ключ-значение:
#
#     name — имя студента
#     surname — фамилия студента
#     best_score — максимальная оценка за экзамен
#     date_and_time — дата и время получения максимальной оценки в исходном формате
#     email — адрес электронной почты
#
# Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены
# в лексикографическом порядке названий электронных почт.
#
# Примечание 1. Если при пересдаче студент получил такую же оценку,
# что и в прошлый раз, то в качестве даты следует указать дату пересдачи.

import csv
import json
from datetime import datetime

with open('вспомогательные файлы/14/exam_results.csv', encoding='utf-8') as file_in:
    _, *rows = csv.reader(file_in)
    rows = sorted(rows, key=lambda t: datetime.strptime(t[3], '%Y-%m-%d %H:%M:%S'))

students_dict = {}
for string in rows:
    in_students_dict = students_dict.get(string[4])
    if in_students_dict is None:
        students_dict[string[4]] = [*string[:2], int(string[2]), string[3]]
    else:
        if int(string[2]) >= in_students_dict[2]:
            students_dict[string[4]][2] = int(string[2])
            students_dict[string[4]][3] = string[3]

ending_list = []
for key in sorted(students_dict):
    ending_list.append(
        {
            'name': students_dict[key][0],
            'surname': students_dict[key][1],
            'best_score': students_dict[key][2],
            'date_and_time': students_dict[key][3],
            'email': key
        }
    )

with open('вспомогательные файлы/14/best_scores.json', 'w', encoding='utf-8') as file_out:
    json.dump(ending_list, file_out, indent=3)
