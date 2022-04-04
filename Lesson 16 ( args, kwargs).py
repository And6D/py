def summa(a=1, b=4 ,c=5):
    print(a, b, c)

summa(c=10, a=50, b=60)

def s(*numbers):
    print(sum(numbers))

s(5, 10 ,15 ,266, 58, 46)

def brands(**names):
    for x, y in names.items():
        print(x, ":" ,y)

brands(a="Huaway", b="Lenovo")

