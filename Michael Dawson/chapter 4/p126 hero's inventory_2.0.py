#Арсенал героя 2.0
#Демонстрирует работу с кортежами
#создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = (
    "sword",
    "armor",
    "shield",
    "healing poison")
print("\nSo,in your inventory:")
for item in inventory:
    print(item)
# найдем длину кортежа
print("\nYou have ", len(inventory), "items in inventory")
# проверка на принадлежность кортежу с помощью in
if "healing poison" in inventory:
    print("You still can fight")
# отобразим срез
start = int(input("\nEnter start index of cut: "))
finish = int(input("Enter final index of cut: "))
print("Cut inventory[", start, ":", finish, "] - this", end=" ")
print(inventory[start:finish])

# соединим два кортежа
chest = ("gold", "gems")
print("You find chest.Look inside:")
print(chest)
print("You loot the chest")
inventory += chest
print("Now in you inventory:")
print(inventory)
input("\n\nHaжмитe Enter. чтобы выйти.")