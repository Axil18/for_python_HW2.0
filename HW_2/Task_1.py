import random

n = int(input('kolvo monet '))
orel = 0
reshka = 0

for _ in range(n):
    position = random.randint(0, 1)
    print(position)
    if position == 0:
        orel += 1
    else:
        reshka += 1
    if orel > reshka:
        print(reshka)
    else:
        print(orel)