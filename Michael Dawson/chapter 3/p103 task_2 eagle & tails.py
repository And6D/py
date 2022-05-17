import random
eagle = 0
tails = 0
#подкидывание монетки
for i in range(100):
    y = random.randrange(2)
    if y == 1:
        eagle += 1
    else:
        tails += 1
print("Eagle:", eagle, "Tails:", tails)