"""
Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые
    пароли в порядке возрастания, составленные из цифр от 00 до 99 включительно.

Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.
"""
from itertools import product


def password_gen_():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)


def password_gen():
    yield from ("".join(map(str, x)) for x in product(range(10), repeat=3))

print(*password_gen_())
print(*password_gen())
