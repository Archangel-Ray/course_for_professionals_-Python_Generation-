# Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения,
# разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:
#
# cant-help-myself.mp3 7 MB
# keep-yourself-alive.mp3 6 MB
# bones.mp3 5 MB
# ...
#
# Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы,
# и выводит полученные группы файлов, указывая для каждой ее общий объем.
# Группы должны быть расположены в лексикографическом порядке названий расширений,
# файлы в группах — в лексикографическом порядке их имен.
#
# Примечание 1. Например, если бы файл files.txt имел вид:
#
# input.txt 3000 B
# scratch.zip 300 MB
# output.txt 1 KB
# temp.txt 4 KB
# boy.bmp 2000 KB
# mario.bmp 1 MB
# data.zip 900 MB
#
# то программа должна была бы вывести:
#
# boy.bmp
# mario.bmp
# ----------
# Summary: 3 MB
#
# input.txt
# output.txt
# temp.txt
# ----------
# Summary: 8 KB
#
# data.zip
# scratch.zip
# ----------
# Summary: 1 GB
#
# где Summary — общий объем файлов группы.
#
# Примечание 2. Гарантируется, что все имена файлов содержат расширение.
#
# Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения
# с округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем,
# в байтах, а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения.
# Примеры перевода:
#
#     1023 B -> 1023 B
#     1300 B -> 1 KB
#     1900 B -> 2 KB
#
# Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:
#
#     1 KB = 1024 B
#     1 MB = 1024 KB
#     1 GB = 1024 MB
#
# Примечание 5. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
#
# Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.

file = open("files.txt", "r", encoding="utf-8")
string = file.readlines()
file.close()
string = [st.split() for st in string]
string_of_value_file = {}
converter = {"B": 1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}

for object_from_file in string:
    extension = object_from_file[0].split(".")[-1]
    if extension in string_of_value_file:
        string_of_value_file[extension][0] += int(object_from_file[1]) * converter[object_from_file[2]]
        string_of_value_file[extension][1].append(object_from_file[0])
    else:
        string_of_value_file.setdefault(extension, [int(object_from_file[1]) * converter[object_from_file[2]],
                                                    [object_from_file[0]]])


for key in sorted(string_of_value_file):
    for file_from_list in sorted(string_of_value_file[key][1]):
        print(file_from_list)
    print("----------")
    bytes_total = string_of_value_file[key][0]
    for value in converter.keys():
        if bytes_total < 1024:
            print(f'''Summary: {round(bytes_total)} {value}\n''')
            break
        bytes_total /= 1024
