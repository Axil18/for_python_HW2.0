# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

p = int(input('Сколько Петя сделал журавликов: '))
s = p
print('Значит Серый сделал тоже', s)
k = int(p+s)*2
print('А вот Катя сделала',k ,', в два раза больше чем Петр и Сергей')
print('Выведем сколько отделно сделали журавликов Петя:',p,'; Катя:',k,'; Сережа:',s)
