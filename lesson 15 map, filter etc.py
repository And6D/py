with open("num text.txt") as sourse:
    n = int(sourse.readline())
    for i in range(n):
        a, b = map(int, sourse.readline().split())
        print(a, b)
"""!! в строке 5 столбце 2 0 в начале не отображется"""

print(a*b)

def f(a, b):
    return a * b
a = map(f, [5, 25, 256], [9, 2, 1]) # последовательно производить умножение элементов в списках
# №1 на №1, №2 на №2 и тд
print(list(a))

def f(a, b):
    return a * b
a = map(lambda x: x*5, (25, 26, 9, 2, 8))
print(list(a))

"""функция filter"""

def f(a):
    if a % 2 == 0:
        return a
# функция сравнивает значение а с элементами списка, выводит четные, не четные пропускает
a = filter(f,(6, 6, 800, 7, 4, 9, 4))
print(list(a))

a = filter(lambda x: (x % 2 == 0), (8, 8, 2, 9, 4, 6, 4))
print(list(a))

from functools import reduce
print(reduce(lambda a, b: a * b, (50, 48 ,96 ,30 ,80)))

z = "dfefs3"
p = [23, 32, 57, 66, 34 ,45]
resilt = zip(z, p)
print(list(resilt))
