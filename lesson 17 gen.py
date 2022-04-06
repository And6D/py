s = []
for i in range(1,21):
    if i % 5==0:
        s.append(i)
print(s)
"""из s диапазона 1-20 выбирает числа кратные 5"""

s1 = [i for i in range(1,21) if i % 5 ==0]
print(s1)
"""тоже, но с  использованием генератора"""

s1 = [i**3 for i in range(1,21) if i % 5 ==0]
print("Сумма значений кратных 5*3 из диапазона 1-20 =", sum(s1))
"""тоже но значения i умножаются на 3 и все зачения s1 суммируются"""

s = []
for i in range(1, 21):
    for j in range(1,6):
        s.append((i, j))
print("Список S ", s)
"""создаем пустой список, в него помещаем пары из диапазона i от 1 до 20 и  j от 1 до 5"""

s1 =[(i, j)
     for i in range(1 ,7)
     for j in range(1, 9)]
print("Список S1 ", s1)

s2 = []
for i in range(-10, 11):
    if i > 0:
        s2.append(i ** 2)
    else:
        s2.append(i ** 3)
print(s2)

s3 = [ i ** 2
       if i > 0
       else i ** 3
       for i in range(-10, 11)
       if i % 2 == 0]
print(s3)

"""генератор множентва"""
s5 = [7, 8, 8 ,8, -10, 15, 3]
set_set = {i for i in s5}
print (set_set)

"""генератор словаря"""
s5 = [7, 8, 8 ,8, -10, 15, 3]
set_set = {i for i in s5}
dictionary = {i: i ** 10 for i in s5}
print(dictionary)


