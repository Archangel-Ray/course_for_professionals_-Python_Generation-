# Вам доступны словари club1, club2 и club3, содержащие данные о различных футбольных клубах.
# Дополните приведенный ниже код, чтобы он объединил данные словари в список и
# записал полученную структуру данных в файл data.json, указав в качестве отступов три символа пробела.
#
# Примечание 1. Словари в списке должны располагаться в своем исходном порядке.
#
# Примечание 2. Начальная часть файла data.json выглядит так:
#
# [
#    {
#       "name": "FC Byern Munchen",
#       "country": "Germany",
#       ...
#    },
#    ...
# ]
#
# Примечание 3. Используйте необязательный аргумент indent.

import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

with open('вспомогательные файлы/03/data0.json', 'w', encoding='utf-8') as file:
    json.dump([club1, club2, club3], file, indent=3)
