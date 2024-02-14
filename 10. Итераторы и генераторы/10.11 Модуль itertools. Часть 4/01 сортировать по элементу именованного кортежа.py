"""
Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым элементом именованного кортежа
    является имя человека, вторым — возраст, третьим — рост. Также доступен список persons, содержащий эти кортежи.

Дополните приведенный ниже код, чтобы он сгруппировал людей из данного списка по их росту и вывел полученные группы.
    Для каждой группы сначала должен быть указан рост, а затем через запятую перечислены имена людей,
    имеющих соответствующий рост. Группы должны быть расположены в порядке увеличения роста,
    каждая на отдельной строке, имена в группах — в алфавитном порядке, в следующем формате:

    <рост>: <имя>, <имя>, ...

Примечание. Начальная часть ответа выглядит так:

158: Ariana, Eva
172: Mark
...
"""
from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

persons.sort(key=lambda x: (x.height, x.name))
grouping = groupby(persons, key=lambda x: x.height)

for key, group in grouping:
    print(f"{key}: {', '.join(person.name for person in group)}")
