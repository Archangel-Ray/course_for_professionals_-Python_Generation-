# Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт,
# а также магазин, в котором он продается. Вам доступен файл prices.csv, который содержит информацию
# о ценах продуктов в различных магазинах. В первом столбце записано название магазина,
# а в последующих — цена на соответствующий товар в этом магазине:
#
# Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;
# Фарш;Вареники;Картофель;Батончик
# Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
# Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
# ...
#
# Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина,
# в котором он продается, в следующем формате:
#
# <название продукта>: <название магазина>
#
# Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название меньше
# в лексикографическом сравнении. Если один товар продается в нескольких магазинах по одной минимальной цене,
# то следует вывести тот магазин, чье название меньше в лексикографическом сравнении.

import csv

cheap_product_in_the_store = None
cheap_price = None
with open('файлы/prices.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    grocery_list = next(rows)
    for line in rows:
        the_cheapest_product_in_this_store = min(map(int, line[1:]))
        if cheap_price is not None:
            if the_cheapest_product_in_this_store > cheap_price:
                continue
        list_of_cheap_products = []
        for ind in range(1, len(line)):
            if str(the_cheapest_product_in_this_store) == line[ind]:
                list_of_cheap_products.append(grocery_list[ind])
        list_of_cheap_products.sort()
        if cheap_price is None:
            cheap_product_in_the_store = [list_of_cheap_products[0], line[0]]
            cheap_price = the_cheapest_product_in_this_store
        elif the_cheapest_product_in_this_store == cheap_price:
            if list_of_cheap_products[0] == cheap_product_in_the_store[0]:
                if line[0] < cheap_product_in_the_store[1]:
                    cheap_product_in_the_store = [list_of_cheap_products[0], line[0]]
            else:
                if list_of_cheap_products[0] < cheap_product_in_the_store[0]:
                    cheap_product_in_the_store = [list_of_cheap_products[0], line[0]]
        else:
            cheap_product_in_the_store = [list_of_cheap_products[0], line[0]]
            cheap_price = the_cheapest_product_in_this_store

print(f'{cheap_product_in_the_store[0]}: {cheap_product_in_the_store[1]}')
