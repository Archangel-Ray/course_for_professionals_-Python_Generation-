# Вам доступна переменная data, содержащая Counter словарь.
# Дополните приведенный ниже код, чтобы он добавил этому словарю два атрибута:
#
#     min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
#     max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение
#
# Обе функции не должны принимать никаких аргументов.
#
# Примечание 1. Элементом словаря будем считать кортеж (ключ, значение).
#
# Примечание 2. Элементы словаря в возвращаемых функциями списках должны располагаться в своем исходном порядке.
#
# Примечание 3. Функции data.min_values() и data.max_values() должны учитывать содержимое словаря.
# Например, если в словарь data будет добавлена новая пара ключ-значение, то и в возвращаемых функциями
# списках данные ключ и значение должны присутствовать.

from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: [x for x in data.items() if x[1] == min(data.values())]
data.max_values = lambda: [x for x in data.items() if x[1] == max(data.values())]

# INPUT DATA:

# TEST_1:
print(data.max_values())

# TEST_2:
print(data.min_values())

# TEST_3:
data['t'] += 1

clue = [('b', 2), ('c', 2), ('n', 2), ('t', 2)]
reply = data.min_values()

print(type(reply))
print(set(reply) == set(clue))

# TEST_4:
data.clear()

data['a'] = 1

print(data.max_values())
print(data.min_values())
