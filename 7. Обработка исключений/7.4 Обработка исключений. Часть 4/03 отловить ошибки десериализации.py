"""
Напишите программу, которая принимает на вход название JSON файла,
    десериализует содержащийся в этом файле объект и выводит его.

        если файла с данным названием нет в папке с программой, программа должна вывести текст:

            Файл не найден

        если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON),
            программа должна вывести текст:

            Ошибка при десериализации

Формат входных данных
    На вход программе подается название JSON файла.

Формат выходных данных
    Программа должна десериализовать объект, содержащийся в файле с введенным названием, и вывести его.
    Если при поиске файла или десериализации его содержимого произошла ошибка,
    программа должна вывести соответствующий текст.

Примечание 1. Название подаваемого файла уже содержит расширение.
"""
import json


try:
    with open(input()) as file:
        print(json.load(file))
except FileNotFoundError as e:
    print('Файл не найден')
except:
    print('Ошибка при десериализации')
