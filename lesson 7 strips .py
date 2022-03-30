print ("""Привет, мир!\n\tПрощай, мир!\t146%\t\nПривет, мир?\t \"_\" """)

texst0 = "'Синий'"
texst1 = '"Фил"'
print(texst0 + " " + texst1)

texst0 = "Полу"
texst1 = "рослик"
print("# " + texst0 + texst1 + " #")
# выборка по индексу начиная с конца
print (texst1[-1])
# выборка по индексу с начала начиная с 0
print(texst0.lower() + texst1[5] + texst1 [0:2] + texst1 [3:6])
print(texst0.capitalize() + texst1[5] + texst1 [0:2] + texst1 [3:6])

texst = "как пасти котов"
print(texst.split(" "))

spisok = ["a", "b", "c"]
print("|".join(spisok))

texst10 = '     чистый  код  РЕФАКТОРИНГ             '
print(texst10.strip("ч"))
print(texst10.lstrip())
print(texst10.rstrip())

print(texst10.replace("Т", 't'))
