"""
Будем считать, что последовательность целых неотрицательных чисел можно преобразовать в отрезок, если разница между
    соседними элементами этой последовательности равна единице. Например, числа 3,4,5,6,7,8 можно преобразовать
    в отрезок [3;8]. Числа 1,3,5,11,15,22 в отрезок преобразовать нельзя. Одиночное число преобразуется в отрезок,
    в котором и правой, и левой границей является оно само. Например, число 1 можно преобразовать в отрезок [1;1].

Реализуйте функцию ranges(), которая принимает один аргумент:

    numbers — список различных натуральных чисел, расположенных в порядке возрастания

Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей, где первый элемент
    кортежа является левой границей отрезка, второй элемент — правой границей отрезка. Полученные кортежи-отрезки
    функция должна возвращать в виде списка.

Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.
"""


def ranges(numbers_):
    out_list = []
    temporary = []
    for number in numbers_:
        if temporary:
            if temporary[-1] == number - 1:
                temporary.append(number)
            else:
                out_list.append((temporary[0], temporary[-1]))
                temporary = [number]
        else:
            temporary.append(number)
    if temporary:
        out_list.append((temporary[0], temporary[-1]))

    return out_list


# INPUT DATA:

# TEST_1:
print("\nтест 1")
numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))

# TEST_2:
print("\nтест 2")
numbers = [1, 3, 5, 7]

print(ranges(numbers))

# TEST_3:
print("\nтест 3")
numbers = [1, 2, 3, 4, 5, 6, 7]

print(ranges(numbers))

# TEST_4:
print("\nтест 4")
numbers = list(range(5, 101))

print(ranges(numbers))

# TEST_5:
print("\nтест 5")
numbers = list(range(10, 21)) + [30] + list(range(35, 101)) + list(range(1000, 1001))

print(ranges(numbers))
