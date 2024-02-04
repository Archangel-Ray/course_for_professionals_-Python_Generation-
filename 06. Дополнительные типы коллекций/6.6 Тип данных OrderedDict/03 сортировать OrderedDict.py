# Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
#
#     ordered_dict — словарь OrderedDict
#     by_values — булево значение, по умолчанию имеет значение False
#
# Функция должна сортировать словарь ordered_dict:
#
#     по ключам, если by_values имеет значение False
#     по значениям, если by_values имеет значение True
#
# Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый.
# Возвращаемым значением функции должно быть None.
#
# Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи,
# имеющие разные типы, а также значения, имеющие разные типы.
#
# Примечание 3. Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.

from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if by_values:
        values = sorted(ordered_dict.items(), key=lambda x: x[1])
        for key, _ in values:
            ordered_dict.move_to_end(key)
    else:
        keys = sorted(ordered_dict)
        for key in keys:
            ordered_dict.move_to_end(key)


# INPUT DATA:

# TEST_1:
data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data, end="")
print(data == OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)]))

# TEST_2:
data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items(), end="")
print(data == OrderedDict([('Mercury', 1), ('Venus', 2), ('Earth', 3), ('Mars', 4)]))

# TEST_3:
data = OrderedDict(a=11, b=2, c=34, d=4, e=59, f=600, g=7)
custom_sort(data, by_values=False)

print(*data.items(), end="")
print(data == OrderedDict([('a', 11), ('b', 2), ('c', 34), ('d', 4), ('e', 59), ('f', 600), ('g', 7)]))

# TEST_4:
data = OrderedDict(aq=1, qb=2, rc=3, ed=4, we=5, wf=6, ag=7)
custom_sort(data, by_values=True)

print(*data.items(), end="")
print(data == OrderedDict([('aq', 1), ('qb', 2), ('rc', 3), ('ed', 4), ('we', 5), ('wf', 6), ('ag', 7)]))

# TEST_5:
data = OrderedDict(a=11, b=2, c=34, d=4, e=59, f=600, g=7)
custom_sort(data)

print(*data.items(), end="")
print(data == OrderedDict([('a', 11), ('b', 2), ('c', 34), ('d', 4), ('e', 59), ('f', 600), ('g', 7)]))

# TEST_6:
data = OrderedDict(a=99, b=22, c=44, d=33, e=11, f=77, g=66, h=99, i=88)
custom_sort(data, by_values=True)

print(*data.items(), end="")
print(data == OrderedDict([('e', 11), ('b', 22), ('d', 33), ('c', 44), ('g', 66), ('f', 77), ('i', 88), ('a', 99),
                           ('h', 99)]))

# TEST_7:
data = OrderedDict(e=11, i=88, b=22, a=99, g=66, c=44, d=33, h=99, f=77)
custom_sort(data, by_values=False)

print(*data.items(), end="")
print(data == OrderedDict([('a', 99), ('b', 22), ('c', 44), ('d', 33), ('e', 11), ('f', 77), ('g', 66), ('h', 99),
                           ('i', 88)]))

# TEST_8:
data = OrderedDict(e=11, b=22, a=99, g=66, c=44, d=33, h=99, f=77, i=88)
custom_sort(data)

print(*data.items(), end="")
print(data == OrderedDict([('a', 99), ('b', 22), ('c', 44), ('d', 33), ('e', 11), ('f', 77), ('g', 66), ('h', 99),
                           ('i', 88)]))

# TEST_9:
data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
custom_sort(data1, by_values=True)

print(*data1.items(), end="")
print(data1 == OrderedDict([('e', 11), ('b', 22), ('g', 33), ('c', 33), ('d', 33), ('k', 44), ('f', 77), ('i', 88),
                            ('a', 99), ('h', 99)]))
