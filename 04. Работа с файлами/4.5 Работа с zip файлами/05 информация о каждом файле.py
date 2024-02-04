# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке,
# указывая для каждого его дату изменения, а также объем до и после сжатия, в следующем формате:
#
# <название файла>
#   Дата модификации файла: <дата изменения>
#   Объем исходного файла: <объем до сжатия> байт(а)
#   Объем сжатого файла: <объем после сжатия> байт(а)
#
# Между данными о двух файлах должна располагаться пустая строка.
#
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.

from zipfile import ZipFile
from datetime import datetime

dict_info_file = {}
with ZipFile('файлы/workbook.zip') as zip_file:
    for file in zip_file.infolist():
        if not file.is_dir():
            dict_info_file[file.filename.split('/')[-1]] = (datetime(*file.date_time),
                                                            file.file_size,
                                                            file.compress_size)

for key in sorted(dict_info_file):
    print(f'''{key}
  Дата модификации файла: {dict_info_file[key][0]}
  Объем исходного файла: {dict_info_file[key][1]} байт(а)
  Объем сжатого файла: {dict_info_file[key][2]} байт(а)\n''')
