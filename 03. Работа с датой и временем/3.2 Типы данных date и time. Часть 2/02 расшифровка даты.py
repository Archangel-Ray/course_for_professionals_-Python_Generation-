# Вам доступна дата birthday. Дополните приведенный ниже код, чтобы он вывел следующие её компоненты:
#
#     полное название месяца на английском
#     полное название дня недели на английском
#     год в формате YYYY
#     номер месяца в формате MM
#     день месяца в формате DD

from datetime import date

birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))
