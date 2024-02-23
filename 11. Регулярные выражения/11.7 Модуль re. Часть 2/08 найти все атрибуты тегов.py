"""
HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим)
    и конечным (закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента.
    Открывающий тег может содержать дополнительную информацию — атрибуты и значения атрибутов:

    <b>BeeGeek</b>
    <a href="https://stepik.org">Stepik</a>

В примере выше тег <b> не содержит никаких атрибутов, а тег <a> содержит атрибут href со значением https://stepik.org.

Напишите программу, которая находит во фрагменте HTML-страницы все атрибуты каждого тега.

Формат входных данных
    На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

Формат выходных данных
    Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их,
    указав для каждого соответствующие атрибуты. Теги вместе со всеми атрибутами должны
    быть расположены каждый на отдельной строке, в следующем формате:

    <тег>: <атрибут>, <атрибут>, ...

Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.
"""
from re import findall
from sys import stdin

# tags_dict = {}
# for row in stdin:
#     for key, value in findall(r"<(\w+)(.*?)>", row):
#         tags_dict.setdefault(key, [])
#         for tag in findall(r"([\w-]+)=", value):
#             if tag not in tags_dict[key]:
#                 tags_dict[key].append(tag)

key_value = (findall(r"<(\w+)| ([\w-]+)=\"", string) for string in stdin)
tags_dict = {}
for row in key_value:
    key, parameters, first = None, set(), True
    for element in row:
        if first:
            key, first = element[0], False
            tags_dict.setdefault(key, set())
        else:
            if element[0]:
                tags_dict[key].update(parameters)
                key, parameters = element[0], set()
                tags_dict.setdefault(key, set())
            else:
                parameters.add(element[1])
    if key:
        tags_dict[key].update(parameters)

# tags = iter(findall(r"<(\w+)| ([\w-]+)=\"", stdin.read()))
# next_teg = next(tags)
# key = ""
# tags_dict = {}
# while next_teg:
#     if next_teg[0]:
#         key = next_teg[0]
#         tags_dict.setdefault(key, set())
#         next_teg = next(tags, None)
#     else:
#         tags_dict[key].add(next_teg[1])
#         next_teg = next(tags, None)

for key in sorted(tags_dict):
    print(f"{key}: {', '.join(sorted(tags_dict[key]))}")
