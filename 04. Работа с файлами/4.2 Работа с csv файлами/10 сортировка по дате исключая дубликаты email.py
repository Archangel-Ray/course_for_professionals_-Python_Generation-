# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты,
# в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:
#
# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...
#
# Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя
# и записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов
# такие же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке
# названий электронных ящиков пользователей.
#
# Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать
# только ее, для некоторых пользователей есть несколько записей с разными именами.

import csv
from datetime import datetime

with open('файлы/name_log.csv', encoding='utf-8') as file_in:
    rows = csv.reader(file_in)
    header_line = next(rows)
    sorted_file = sorted(list(rows), key=lambda x: (x[1], datetime.strptime(x[2], '%d/%m/%Y %H:%M')))
    dict_users = {info[1]: info for info in sorted_file}

with open('файлы/new_name_log.csv', 'w', encoding='utf-8', newline='') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(header_line)
    writer.writerows(dict_users.values())
