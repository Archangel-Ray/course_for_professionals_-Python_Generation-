"""
Напишите программу, которая принимает на вход произвольное количество строк, содержащих корректные математические
    выражения, и выводит значение наибольшего из них.

Формат входных данных
    На вход программе подается произвольное количество строк,
    каждое из которых содержит корректное математическое выражение.

Формат выходных данных
    Программа должна вычислить значения введенных выражений и вывести наибольшее.

Примечание 1. Под корректным математическим выражением подразумевается выражение,
                полностью соответствующее синтаксису языка Python.
"""
from sys import stdin
list_of_answers = [eval(x) for x in stdin]
print(max(list_of_answers))
