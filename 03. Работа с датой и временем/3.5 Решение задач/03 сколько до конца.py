# Дан режим работы магазина:
# Понедельник 	9:00 - 21:00
# Вторник 	9:00 - 21:00
# Среда 	9:00 - 21:00
# Четверг 	9:00 - 21:00
# Пятница 	9:00 - 21:00
# Суббота 	10:00 - 18:00
# Воскресенье 	10:00 - 18:00
#
# Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут,
# оставшееся до закрытия магазина.
#
# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
#
# Формат выходных данных
# Программа должна вывести количество минут, которое осталось до закрытия магазина,
# или текст Магазин не работает, если он закрыт.

from datetime import datetime, time, timedelta

opening_hours = (
    (time(hour=9), time(hour=21), timedelta(hours=21)),
    (time(hour=9), time(hour=21), timedelta(hours=21)),
    (time(hour=9), time(hour=21), timedelta(hours=21)),
    (time(hour=9), time(hour=21), timedelta(hours=21)),
    (time(hour=9), time(hour=21), timedelta(hours=21)),
    (time(hour=10), time(hour=18), timedelta(hours=18)),
    (time(hour=10), time(hour=18), timedelta(hours=18))
)

current_time = datetime.strptime(input(), "%d.%m.%Y %H:%M")
current_weekdays = current_time.weekday()
if opening_hours[current_weekdays][0] <= current_time.time() < opening_hours[current_weekdays][1]:
    time_to_end = opening_hours[current_weekdays][2] - timedelta(hours=current_time.hour, minutes=current_time.minute)
    print(time_to_end.seconds // 60)
else:
    print("Магазин не работает")
