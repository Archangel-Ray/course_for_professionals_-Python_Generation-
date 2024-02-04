# Рассмотрим следующий текстовый фрагмент:
#
# ball,color,purple
# ball,size,4
# ball,notes,it's round
# cup,color,blue
# cup,size,1
# cup,notes,none
#
# Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта,
# значение свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого
# равно purple. Также у объекта ball есть свойства size и notes, имеющие значения 4 и it's round соответственно.
# Помимо объекта ball имеется объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам
# общее название object и сгруппируем строки данного текстового фрагмента по первому столбцу:
#
# object,color,size,notes
# ball,purple,4,it's round
# cup,blue,1,none
#
# Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта,
# а в последующих — значения соответствующих свойств этого объекта.
#
# Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:
#
#     filename — название csv файла, например, data.csv; формат содержимого файла аналогичен
#                 формату текстового фрагмента, рассмотренного в условии задачи: каждая строка
#                 файла содержит три значения через запятую, а именно имя объекта, свойство этого
#                 объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
#     id_name — общее название для объектов
#
# Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу
# и назвав первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.
#
# Примечание 1. Например, если бы файл data.csv имел следующий вид:
#
# 01,Title,Ran So Hard the Sun Went Down
# 02,Title,Honky Tonk Heroes (Like Me)
#
# то вызов функции condense_csv():
#
# condense_csv('data.csv', id_name='ID')
#
# должен был бы создать файл condensed.csv со следующим содержанием:
#
# ID,Title
# 01,Ran So Hard the Sun Went Down
# 02,Honky Tonk Heroes (Like Me)
#
# Примечание 2. Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая,
# при этом кавычки не используются.
#
# Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.

import csv


def condense_csv(file_name, id_name):
    with open(file_name, encoding='utf-8') as file_in, \
            open('файлы/condensed.csv', 'w', encoding='utf-8') as file_out:
        rows = csv.reader(file_in)
        table_header = list()
        table_header.append(id_name)
        object_dict = {}
        for row in rows:
            if row[1] not in table_header:
                table_header.append(row[1])
            object_dict.setdefault(row[0], [row[0]]).append(row[2])

        writer = csv.writer(file_out)
        writer.writerow(table_header)
        writer.writerows(object_dict.values())


# INPUT DATA:

# TEST_1:
text = '''01,Title,Ran So Hard the Sun Went Down
02,Title,Honky Tonk Heroes (Like Me)'''

with open('файлы/data-11.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('файлы/data-11.csv', id_name='ID')

with open('файлы/condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())

# TEST_2:
text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''

with open('файлы/data-11.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('файлы/data-11.csv', id_name='ID')

with open('файлы/condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())

# TEST_3:
text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29
03,Artist,David Allan Coe
03,Title,Willie Waylon And Me
03,Time,3:26'''

with open('файлы/data-11.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('файлы/data-11.csv', id_name='Position')

with open('файлы/condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())

# TEST_4:
text = '''ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none'''

with open('файлы/data-11.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('файлы/data-11.csv', id_name='ID')

with open('файлы/condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())
