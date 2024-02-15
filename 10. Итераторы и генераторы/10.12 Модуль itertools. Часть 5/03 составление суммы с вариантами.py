"""
Тимур пришел в книжный магазин, чтобы приобрести новую книгу по математике, стоимость которой равна 100$.
    У него в кошельке имеется неограниченное количество купюр, номиналы которых представлены в списке wallet.
    Другими словами, Тимур может использовать купюру одного номинала произвольное количество раз. Например,
    он может расплатиться пятью купюрами по 20$ или десятью по 10$.

Дополните приведенный ниже код, чтобы он вывел количество способов,
    которыми Тимур может приобрести книгу стоимостью 100$.

Примечание. Способы расплатиться наборами купюр вида 50,20,20,10 и 20,10,50,20 считаются одинаковыми
            и не должны учитываться повторно.
"""
from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]

variations_all = ((combinations_with_replacement(wallet, i)) for i in range(21))
variations_our = ((x for x in i if sum(x) == 100) for i in variations_all)
print(sum(len(list(x)) for x in variations_our))
