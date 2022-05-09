numbers = {232, 222, "fdfsdf", 11}
print(numbers)
print(type(numbers))

"""для создания пустого множество нужно явно указать класс"""
flag = {}
print(type(flag),"  - если явно не указать класс, по умолчанию будет словарь" )

cars = set()
print(type(cars))

"""При конвертации списка в множество дублирующие значения исключаются"""
boats = set(["red", "long", 1, 5, 5, "read", "red"])
print(boats)

for r in boats:
    print(r)

print("red" in boats)

boats.add("green")
print(boats)

boats.discard(8) #НЕ выводит ошибку при отсутствии элемента с таким именем
boats.remove(5) # выводит ошибку, KeyError при отстствии элемента

boats.pop()
print(boats, "-Удаляется первый элемент из множества" )

boats.pop()
print(boats, "Удаляется первый элемент из множества")

boats.clear()
print(boats, "метод .clear очищает множество")

plants = {1, 5, 8, 90, 34, 69}
zombie = {"dead", "undead",90}

plantsVSzombie = plants.union(zombie)
print(plantsVSzombie, ".union")

"""идентично .union можно использовать | """
garden = plants | zombie
print(garden, "|")

"""пересечение моножеств"""
warfare = plants.intersection(zombie)
print(warfare, "- значение присуствующее в множествах, метод .interselection")

warfare = plants & zombie
print(warfare, "- значение присуствующее в множествах, использовался &")

"""разница между множествами"""
fat = plants - zombie
print(fat)

hot = zombie - plants
print(hot)

"""копирование элементов из множества"""
soft = garden.copy()
print(soft)

"""измерение длинны len"""
print(len(soft))

frozen = frozenset({4, 7, 7, 8, 9, 6, 5, 4, 3, 3, 2, 23})
print(frozen)

frozen.add(15)
print(frozen)