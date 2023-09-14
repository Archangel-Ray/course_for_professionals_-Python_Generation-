# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит название файла из этого архива,
# который имеет наилучший показатель степени сжатия.
#
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.
#
# Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.
#
# Примечание 3. Степень сжатия файла характеризуется коэффициентом K,
# определяемым как отношение объема сжатого файла Vc​ к объему исходного файла Vo​, выраженным в процентах:
#
# K=Vc/Vo⋅100%

from zipfile import ZipFile


dict_at_most = {}
with ZipFile('файлы/workbook.zip') as zip_file:
    for file in zip_file.infolist():
        dict_at_most[file.compress_size / file.file_size if file.file_size else 'directory'] = \
            file.filename.split('/')[-1]

del dict_at_most['directory']
print(dict_at_most[min(dict_at_most)])
