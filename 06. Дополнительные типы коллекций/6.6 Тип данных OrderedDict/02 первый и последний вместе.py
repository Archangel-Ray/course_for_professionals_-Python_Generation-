# Вам доступен словарь data с четным количеством элементов.
# Дополните приведенный ниже код, чтобы он вывел данный словарь, расположив его элементы по следующему правилу:
# первый, последний, второй, предпоследний, третий, и так далее.

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
                    'SeatsCount': '10'})

data_out = OrderedDict()
while data:
    key, value = data.popitem(last=bool(len(data) % 2))
    data_out[key] = value

print(data_out)
