"""
Вам доступен список names, содержащий имена на русском языке. Дополните приведенный ниже код, чтобы он вывел все имена,
    которые начинаются на буквы А и М (независимо от регистра) и имеют длину больше 4. Имена должны быть расположены
    в лексикографическом порядке, через пробел, каждое с заглавной буквы.

Примечание 1. Начальная часть ответа выглядит так:

Аделина Айлин Александр ...

Примечание 2. В задаче удобно воспользоваться функциями map() и filter().

"""
names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита',
         'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион',
         'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей',
         'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара',
         'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья',
         'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор',
         'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина',
         'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия',
         'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана',
         'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон',
         'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']


def capitalize(arg):
    return arg[0].upper() + arg[1:].lower()


def filters(arg):
    return arg[0].upper() in 'АМ' and len(arg) > 4


print(*sorted(map(capitalize, filter(filters, names))))
