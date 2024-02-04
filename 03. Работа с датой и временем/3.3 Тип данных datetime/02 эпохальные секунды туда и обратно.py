# Дополните приведенный ниже код, чтобы он преобразовал секунды seconds (прошедшие от начала эпохи) в объект datetime
# и, наоборот, объект datetime в секунды (прошедшие от начала эпохи).

from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())
