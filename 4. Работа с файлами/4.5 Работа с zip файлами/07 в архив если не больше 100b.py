# Вам доступен набор различных файлов, названия которых представлены в списке file_names.
# Также вам доступен архив files.zip. Дополните приведенный ниже код, чтобы он добавил в архив files.zip
# только те файлы из списка file_names, объем которых не превышает 100 байт.
#
# Примечание 1. Получить объем файла в байтах позволяет функция getsize() из модуля os.path.
# Данная функция принимает в качестве аргумента путь к файлу и возвращает размер указанного файла в байтах.
#
# Например, вычислить объем архива files.zip в байтах и сохранить его в переменную size можно следующим образом:
#
# import os.path
#
# size = os.path.getsize('files.zip')
#
# Примечание 2. Вычислить объем файла в байтах можно и вручную, не прибегая к использованию сторонних модулей.
# Подумайте, как 😉.
#
# Примечание 3. Считайте, что файлы из списка file_names и архив files.zip находятся в папке с программой.

from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('файлы/07/files.zip', 'a') as file_in:
    for file in file_names:
        if os.path.getsize(f'файлы/07/для упаковки/{file}') < 100:
            file_in.write(f'файлы/07/для упаковки/{file}', file)
