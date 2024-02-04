"""
Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:

    grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по ключу grades

Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing.
                Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В возвращаемом функцией словаре сначала должно следовать имя, а затем — самая высокая оценка.
"""


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


# INPUT DATA:

# TEST_1:
print('\nтест 1')
info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))

# TEST_2:
print('\nтест 2')
print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

# TEST_3:
print('\nтест 3')
annotations = top_grade.__annotations__

print(annotations['grades'])

# TEST_4:
print('\nтест 4')
info = {'name': 'Artur', 'grades': [100, 28, 3, 97, 5]}
result = top_grade(info)

print(result)

# TEST_5:
print('\nтест 5')
info = {'name': 'Dima', 'grades': [99, 99, 99, 99, 99]}

print(top_grade(info))

# TEST_6:
print('\nтест 6')
info = {'name': 'Vlad', 'grades': [22, 22, 66, 66, 5]}

print(top_grade(info))

# TEST_7:
print('\nтест 7')
info = {'name': 'Egor', 'grades': [33, 33, 33, 64, 5]}

print(top_grade(info))

# TEST_8:
print('\nтест 8')
print(*top_grade.__annotations__.values())

# TEST_9:
print('\nтест 9')
info = {'name': 'Roman', 'grades': [40]}

print(top_grade(info))
