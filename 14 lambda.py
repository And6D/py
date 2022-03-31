def rectangle_area(a, b):
    return a * b

print(rectangle_area(200, 200))

print((lambda a, b: a * b)(66, 66))

def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print(maximum(10,5))

print((lambda a, b: a if a > b else b )(33, 34))


"""как спарсить сайт https://www.bookvoed.ru/author?id=153717  записать в переменную"""

print("Lambda", "Λ", " or ", "λ" )
