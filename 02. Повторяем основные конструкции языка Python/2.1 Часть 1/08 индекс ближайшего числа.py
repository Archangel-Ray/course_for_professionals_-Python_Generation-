# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
#
#     numbers — список целых чисел
#     number — целое число
#
# Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
# Если список numbers пуст, функция должна вернуть число −1.
#
# Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к
# искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.
#
# Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3,
# имеющие индексы 1 и 2 соответственно. Наименьший из индексов равен 1.


def index_of_nearest(numbers, number):
    if numbers:
        if number in numbers:
            return numbers.index(number)
        else:
            temporary_list = numbers[:]
            temporary_list.append(number)
            temporary_list.sort()
            index_number = temporary_list.index(number)
            if index_number == 0:
                return numbers.index(temporary_list[1])
            if index_number == len(temporary_list) - 1:
                return numbers.index(temporary_list[-2])
            else:
                coming_number = temporary_list[index_number - 1]
                following_number = temporary_list[index_number + 1]
                if number - coming_number == following_number - number:
                    return min(numbers.index(coming_number), numbers.index(following_number))
                else:
                    nearest = coming_number if number - coming_number < following_number - number else following_number
                    return numbers.index(nearest)
    return -1


# INPUT DATA:

# TEST_1:
print(index_of_nearest([], 17))

# TEST_2:
print(index_of_nearest([7, 13, 3, 5, 18], 0))

# TEST_3:
print(index_of_nearest([9, 5, 3, 2, 11], 4))

# TEST_4:
print(index_of_nearest([7, 5, 4, 4, 3], 4))

# TEST_5:
print(index_of_nearest([6, 100, 101, 2], 4))

# TEST_6:
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))

# TEST_7:
print(index_of_nearest([1, 14, 100, 65, 6], 5))

# TEST_8:
print(index_of_nearest([10, 164, 100, 265, 16], 8))

# TEST_9:
print(index_of_nearest([10, 99, 0, -12, 16], -9))

# TEST_10:
print(index_of_nearest([1, 1, 1, 1, 1], 1))
