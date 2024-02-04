# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
#
# Примечание 1. Обратите внимание, что папка не считается файлом.

from zipfile import ZipFile

with ZipFile('файлы/workbook.zip') as zip_file:
    print(sum(1 for file in zip_file.infolist() if file.is_dir() is False))
