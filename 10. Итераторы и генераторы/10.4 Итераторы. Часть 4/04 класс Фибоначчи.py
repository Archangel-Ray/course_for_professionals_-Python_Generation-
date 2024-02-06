"""
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел,
    где каждое последующее число является суммой двух предыдущих:
        1,1,2,3,5,8,13,21,34
"""


class Fibonacci:
    def __init__(self):
        self.current = (0, 1)

    def __iter__(self):
        return self

    def __next__(self):
        self.current = (self.current[1], sum(self.current))
        return self.current[0]


fibonacci = Fibonacci()

# for _ in range(100):
#     next(fibonacci)

for _ in range(10):
    print(next(fibonacci), end=' ')
