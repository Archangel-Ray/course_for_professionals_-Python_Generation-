# Вам доступен архив desktop.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит его файловую структуру и объем каждого файла.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде.
# Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.
#
# Примечание 1. Вывод на примере архива test.zip из конспекта:
#
# test
#   Картинки
#     1.jpg 88 KB
#     avatar.png 19 KB
#     certificate.png 43 KB
#     py.png 33 KB
#     World_Time_Zones_Map.png 2 MB
#     Снимок экрана.png 11 KB
#   Неравенства.djvu 5 MB
#   Программы
#     image_util.py 5 KB
#     sort.py 61 B
#   Разные файлы
#     astros.json 505 B
#
# Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.
#
# Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:
#
#     1 KB = 1024 B
#     1 MB = 1024 KB
#     1 GB = 1024 MB

from zipfile import ZipFile


def convert_kb(file_size):
    counter = 0
    while file_size > 1024:
        file_size /= 1024
        counter += 1
    return f"{round(file_size)} {['B', 'KB', 'MB', 'GB'][counter]}"


folder_list = []
with ZipFile('файлы/10/desktop.zip') as zip_file:
    for name in zip_file.namelist():
        name_list = name.split('/')
        for i in range(len(name_list)):
            if name_list[i] in folder_list:
                print(end='  ')
            else:
                if not name_list[i]:
                    folder_list.append(name_list[-2])
                else:
                    print(name_list[i], end='')
        if not zip_file.getinfo(name).is_dir():
            print('', convert_kb(zip_file.getinfo(name).file_size), end='')
        print()
