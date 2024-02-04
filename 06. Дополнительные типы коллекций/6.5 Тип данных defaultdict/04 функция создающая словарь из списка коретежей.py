# В онлайн-школе BEEGEEK каждое лето проходят соревнования по шахматам, во время которых ведется статистика побед и
# поражений. Каждая партия описывается кортежем из двух элементов, где первый элемент — имя победившего ученика,
# второй элемент — имя проигравшего ученика.
#
# Реализуйте функцию wins(), которая принимает один аргумент:
#
#     pairs — итерируемый объект, элементами которого являются кортежи,
#     каждый из которых представляет собой пару имён победитель-проигравший
#
# Функция должна возвращать словарь, в котором ключом служит имя ученика,
# а значением — множество (тип set) имен учеников, которых он победил.
#
# Примечание 1. Гарантируется, что каждая партия заканчивается победой одного из учеников, то есть ничьей быть не может.
#
# Примечание 2. Элементы в возвращаемом функцией словаре могут располагаться в произвольном порядке.

from collections import defaultdict


def wins(list_data):
    result_dict = defaultdict(set)
    for key, value in list_data:
        result_dict[key].add(value)
    return result_dict


print('test 1')
result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 2')
result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 3')
result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 4')
result = wins([('Артур', 'Дима'), ('Дима', 'Тимур'),
               ('Тимур', 'Анри'), ('Анри', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 5')
result = wins([('Артур', 'Дима'), ('Дима', 'Тимур'),
               ('Тимур', 'Анри'), ('Анри', 'Алина'),
               ('Алина', 'Илья'), ('Илья', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 6')
result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'),
               ('Артур', 'Анри'), ('Артур', 'Алина'),
               ('Артур', 'Илья'), ('Артур', 'Элина')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 7')
result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'),
               ('Артур', 'Анри'), ('Артур', 'Алина'),
               ('Артур', 'Илья'), ('Элина', 'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 8')
result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'),
               ('Артур', 'Анри'), ('Артур', 'Алина'),
               ('Элина', 'Дима'), ('Элина', 'Тимур'),
               ('Элина', 'Анри'), ('Элина', 'Алина')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 9')
result = wins([('Артур', 'Дима'), ('Дима', 'Артур'),
               ('Артур', 'Алина'), ('Алина', 'Артур'),
               ('Тимур', 'Элина'), ('Элина', 'Тимур'),
               ('Элина', 'Анри'), ('Анри', 'Элина')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 10')
result = wins([('Артур', 'Дима'), ('Дима', 'Артур'),
               ('Тимур', 'Элина'), ('Элина', 'Тимур'),
               ('Алина', 'Анри'), ('Анри', 'Алина')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 11')
result = wins([('Артур', 'Дима'), ('Дима', 'Артур'),
               ('Артур', 'Тимур'), ('Тимур', 'Артур'),
               ('Тимур', 'Дима'), ('Дима', 'Тимур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 12')
result = wins([('Артур', 'Дима'), ('Дима', 'Элина'),
               ('Артур', 'Тимур'), ('Тимур', 'Анри'),
               ('Тимур', 'Элина'), ('Элина', 'Тимур'),
               ('Элина', 'Артур'), ('Анри', 'Илья'),
               ('Элина', 'Анри'), ('Анри', 'Герман')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))

print('test 13')
result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
for losers in result.values():
    print(type(losers) == set)
