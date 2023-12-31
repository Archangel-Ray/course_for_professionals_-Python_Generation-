# Дана последовательность натуральных чисел от 1 до n. Напишите программу, которая сначала располагает в обратном
# порядке часть элементов этой последовательности от элемента с номером X до элемента с номером Y, а затем от элемента
# с номером A до элемента с номером B.
#
# Формат входных данных
# На вход программе подаются 5 натуральных чисел, разделенных пробелом: n, X, Y, A, B  (X<Y, A<B,  1≤X,Y,A,B≤ n).
#
# Формат выходных данных
# Программа должна сформировать последовательность чисел, согласно условию задачи, и вывести их, разделяя пробелом.
#
# Примечание 1. Нумерация членов последовательности начинается с единицы.
#
# Примечание 2. Рассмотрим первый тест, в котором n=9,X=2,Y=5,A=6,B=9. Запишем последовательность от 1 до 9:
# 1,2,3,4,5,6,7,8,9
# Перевернем в этой последовательности сначала элементы со 2 по 5 (2,3,4,5), затем с 6 по 9 (6,7,8,9).
# Получим искомую последовательность:
# 1,5,4,3,2,9,8,7,6


n, X, Y, A, B = map(int, input().split())
list_of_numbers = [i for i in range(1, n + 1)]
list_of_numbers[X - 1:Y] = list_of_numbers[X - 1:Y][::-1]
list_of_numbers[A - 1:B] = list_of_numbers[A - 1:B][::-1]
print(*list_of_numbers)
