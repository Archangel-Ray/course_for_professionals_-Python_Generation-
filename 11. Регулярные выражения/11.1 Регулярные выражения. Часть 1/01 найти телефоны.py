"""
Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd

8-ddd-dddd-dddd

где d — цифра от 0 до 9.

Формат входных данных
На вход программе подается строка произвольного содержания.

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи,
    и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.
"""
text_in = 'Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, ' \
          'Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221'  # input()
patterns = ['7-ddd-ddd-dd-dd', '8-ddd-dddd-dddd']
phone_numbers = []

for i in range(len(text_in)):
    if text_in[i] in '78':
        pattern = patterns[0]
        if text_in[i] == '8':
            pattern = patterns[1]

        if len(text_in[i:]) >= len(pattern):
            phone_number = ''
            phone_number += text_in[i]
            for ind_num in range(1, len(pattern)):
                if pattern[ind_num] == '-':
                    if text_in[i + ind_num] == '-':
                        phone_number += text_in[i + ind_num]
                elif pattern[ind_num] == 'd':
                    if text_in[i + ind_num] in '0123456789':
                        phone_number += text_in[i + ind_num]
            if len(phone_number) == len(pattern):
                phone_numbers.append(phone_number)

print(*phone_numbers, sep='\n')
