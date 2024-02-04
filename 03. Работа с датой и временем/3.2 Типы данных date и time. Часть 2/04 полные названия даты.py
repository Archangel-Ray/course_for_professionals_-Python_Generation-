# Ураган Эндрю, который обрушился на Флориду 2424 августа 19921992 года, был одним из самых дорогостоящих
# и смертоносных ураганов в истории США. Дополните приведенный ниже код, чтобы он вывел дату 24 августа 1992 года
# в трех различных форматах:
#
#     в формате YYYY-MM
#     в формате month_name (YYYY), где month_name – полное название месяца на английском
#     в формате YYYY-day_number, где day_number – день года

from datetime import date

andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number
