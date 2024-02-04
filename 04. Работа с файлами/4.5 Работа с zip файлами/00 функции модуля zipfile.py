# импорт модуля
from zipfile import ZipFile

# открыть объект архива
with ZipFile('файлы/00 файлы урока/test.zip', mode='r') as zip_file:

    # таблица данных: путь - дата изменений - размер
    zip_file.printdir()
    print()

    # список объектов
    print('список объектов ZipInfo:')
    info = zip_file.infolist()
    print(*info, sep='\n')
    print()

    # атрибуты объектов
    print('атрибуты объектов:')
    print('имя файла:', info[6].filename)
    print('дата изменения файла:', info[6].date_time)  # (кортеж: год, месяц, день, час, минута, секунда)
    print('размер начального файла в байтах:', info[6].file_size)
    print('размер сжатого файла в байтах:', info[6].compress_size)
    print()

    # папка или файл
    print('проверка:')
    print('папка -', info[0].is_dir())
    print('не папка -', info[6].is_dir())
    print()

    # список имён
    print('__________список названий файлов__________')
    info = zip_file.namelist()
    print(*info, sep='\n')
    print('________________________________________\n')

    # информация объекта
    print('информация о файле по имени:')
    last_file = zip_file.getinfo('test/Программы/image_util.py')  # объект ZipInfo
    print('имя файла:', last_file.filename)
    print('дата изменения файла:', last_file.date_time)  # (кортеж: год, месяц, день, час, минута, секунда)
    print('размер начального файла в байтах:', last_file.file_size)
    print('размер сжатого файла в байтах:', last_file.compress_size)
    print()

    # открыть файл из архива
    with zip_file.open('test/Разные файлы/astros.json') as file:
        # бинарная строка
        print('бинарная строка:')
        print(file.read())

    with zip_file.open('test/Разные файлы/astros.json') as file:
        # текстовая строка
        print('декодированная строка в текст:')
        print(file.read().decode('utf-8'))
        print()

# создание нового архива
with ZipFile('файлы/00 файлы урока/archive.zip', mode='w') as new_zip_file:
    new_zip_file.write('файлы/00 файлы урока/program.py', 'program.py')
    new_zip_file.write('файлы/00 файлы урока/lse.jpeg', 'lse.jpeg')

# добавление файла в архив
with ZipFile('файлы/00 файлы урока/обновлённый test.zip') as open_old_zip_file:
    list_files = open_old_zip_file.namelist()
    if 'test/program.py' not in list_files or 'lse.jpeg' not in list_files:
        with ZipFile('файлы/00 файлы урока/обновлённый test.zip', mode='a') as open_zip_file:
            open_zip_file.write('файлы/00 файлы урока/program.py', 'test/program.py')  # в папку архива
            open_zip_file.write('файлы/00 файлы урока/lse.jpeg', 'lse.jpeg')  # в корень архива
            print('добавлено два файла:', *open_zip_file.namelist(), sep='\n')
    else:
        print('файлы уже в архиве:', *list_files, sep='\n')


# извлечение одного файла из архива
with ZipFile('файлы/00 файлы урока/обновлённый test.zip') as extract_zip_file:
    extract_zip_file.extract('test/Картинки/avatar.png', 'файлы/00 файлы урока/распакованый файл')
    extract_zip_file.extract('test/Программы/image_util.py', 'файлы/00 файлы урока/распакованый файл')
    extract_zip_file.extract('lse.jpeg', 'файлы/00 файлы урока/распакованый файл')

# извлечение всех файлов из архива
with ZipFile('файлы/00 файлы урока/обновлённый test.zip') as extractall_zip_file:
    extractall_zip_file.extractall('файлы/00 файлы урока/распакованый архив')
