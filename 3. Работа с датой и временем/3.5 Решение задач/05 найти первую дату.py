# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого старшего сотрудника из данного списка.
#
# Формат входных данных
# На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации.
# В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом.
# Дата рождения указывается в формате DD.MM.YYYY.
#
# Формат выходных данных
# Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом.
# Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.
#
# Примечание 1. Гарантируется, что у всех сотрудников имена и фамилии различны.

from datetime import datetime

dict_of_coworker = {}
pattern = "%d.%m.%Y"
for _ in range(int(input())):
    string = input()
    dict_of_coworker.setdefault(datetime.strptime(string[-10:], pattern), []).append(string[:-11])
earlier = min(dict_of_coworker)
print(earlier.strftime(pattern), end=" ")
print(''.join(dict_of_coworker[earlier]) if len(dict_of_coworker[earlier]) == 1 else len(dict_of_coworker[earlier]))
