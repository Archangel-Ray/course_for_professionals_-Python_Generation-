# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит названия файлов из этого архива,
# которые были созданы или изменены позднее 2021-11-30 14:22:00.
# Названия файлов должны быть расположены в лексикографическом порядке,
# каждое на отдельной строке.
#
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.

from zipfile import ZipFile
from datetime import datetime

name_list = []
with ZipFile('файлы/workbook.zip') as zip_file:
    for file in zip_file.infolist():
        if not file.is_dir():
            if datetime(*file.date_time) > datetime(2021, 11, 30, 14, 22, 00):
                name_list.append(file.filename.split('/')[-1])

print(*sorted(name_list), sep='\n')
