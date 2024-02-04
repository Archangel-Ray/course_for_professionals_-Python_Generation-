# Дополните приведенный ниже код, чтобы он прибавил к объекту datetime(2021, 11, 4, 13, 6) одну неделю и
# 12 часов и вывел результат в формате DD.MM.YYYY HH:MM:SS.

from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))
