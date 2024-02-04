# Найдите и исправьте ошибки, допущенные в приведенной ниже программе,
# чтобы она сериализовала словарь dogs и записала результат в файл dogs.pkl.

import pickle

dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

with open('dogs.pkl', mode='wb') as file:
    pickle.dump(dogs, file)
