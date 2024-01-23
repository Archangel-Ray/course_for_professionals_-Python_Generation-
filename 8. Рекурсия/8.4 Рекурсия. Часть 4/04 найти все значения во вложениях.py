"""
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

    nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь,
            так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
    key — хешируемый объект

Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts и всех его вложенных
    словарях, и возвращать их в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое
    множество.

Примечание 1. Гарантируется, что все искомые значения являются хешируемыми объектами,
                т.е. могут быть элементами множества.
"""


def get_all_values(nested_dicts, key):
    return_set = set()
    for k, value in nested_dicts.items():
        if k == key:
            return_set.add(value)
        if type(value) is dict:
            go_deeper = get_all_values(value, key)
            if go_deeper is not None:
                return_set = return_set.union(go_deeper)
    return return_set


# INPUT DATA:

# TEST_1:
print('\nтест 1')
my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))

# TEST_2:
print('\nтест 2')
my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))

# TEST_3:
print('\nтест 3')
my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')

print(len(sorted(result)))

# TEST_4:
print('\nтест 4')
my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))

# TEST_5:
print('\nтест 5')
my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'age')
print(*result)

# TEST_6:
print('\nтест 6')
my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
print(type(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))
