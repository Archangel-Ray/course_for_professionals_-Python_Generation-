"""
Напишите программу с использованием рекурсии, которая выводит последовательность натуральных чисел
    от 1 до 100 включительно.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должны вывести последовательность натуральных чисел от 1 до 100 включительно, каждое на отдельной строке.
"""


def func():
    def func_in(n):
        if n <= 100:
            print(n)
            func_in(n + 1)
    func_in(1)


func()
