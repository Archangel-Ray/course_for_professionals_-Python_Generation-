# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов,
# каждый из которых содержит информацию о каком-либо футболисте:
#
# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }
#
# У футболиста имеются следующие атрибуты:
#
#     first_name — имя
#     last_name — фамилия
#     team — название футбольного клуба
#     position — игровая позиция
#
# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
# выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен,
# а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
#
# Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным
# текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом
# в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.

from zipfile import ZipFile
import json

list_of_football_players = []
with ZipFile('файлы/09/data.zip') as zip_file:
    for file in zip_file.namelist():
        if file.split('.')[-1] == 'json':
            try:
                with zip_file.open(file) as json_file:
                    player = json.load(json_file)
                    if player['team'] == 'Arsenal':
                        list_of_football_players.append(f"{player['first_name']} {player['last_name']}")
            except json.JSONDecodeError:
                pass
            except UnicodeDecodeError:
                pass

print(*sorted(list_of_football_players), sep='\n')
