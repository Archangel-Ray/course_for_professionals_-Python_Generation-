# Вам доступен словарь data.
# Дополните приведенный ниже код, чтобы он вывел данный словарь, расположив его элементы в обратном порядке.

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

for key in list(reversed(data)):
    data.move_to_end(key)
print(data)
