# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

k = int(input('Количство долек которое хотим отломать: '))
if k <= 1 :
    print('Не можем отломать столько долек')
elif k == 5:
    print('Не можем отломать столько долек')
elif k > 6:
    print('Не можем отломать столько долек')
else:
    print("Можем отломать столько долек")