"""
Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор,
    бесконечно генерирующий единственное значение — строку i love beegeek!.
"""
# infinite_love = iter(lambda: 'i love beegeek!', '')
infinite_love = iter('i love beegeek!'.__str__, 'и так тоже получается')
for _ in range(5):
    print(next(infinite_love))
