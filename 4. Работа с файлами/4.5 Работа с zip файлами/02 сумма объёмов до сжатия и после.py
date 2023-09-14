# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом
# и не сжатом видах в байтах, в следующем формате:
#
# Объем исходных файлов: <объем до сжатия> байт(а)
# Объем сжатых файлов: <объем после сжатия> байт(а)

from zipfile import ZipFile

with ZipFile('файлы/workbook.zip') as zip_file:
    info_list = zip_file.infolist()
    print('Объем исходных файлов:', sum(file.file_size for file in info_list), 'байт(а)')
    print('Объем сжатых файлов:', sum(file.compress_size for file in info_list), 'байт(а)')
