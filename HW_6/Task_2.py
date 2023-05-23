# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i, val in enumerate(lst):
        if min_val <= val <= max_val:
            indexes.append(i)
    return indexes

my_list = random.sample(range(1, 11), 10)

min_val = 3
max_val = 7

result = find_indexes(my_list, min_val, max_val)

print(result)
