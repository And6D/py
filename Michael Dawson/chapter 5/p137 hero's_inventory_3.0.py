inventory = ["sword", "armor", "shield", "healing poison"]
print("\nIn you inventory:\n")
for item in inventory:
    print(item)
input("\npress Enter to continue")
#len
print(f"\nYou have {len(inventory)} items in inventory")
input("\npress Enter to continue")
#in
if "healing poison" in inventory:
    print("\nYou have healing poison")
#cut
start = int(input("\nSet start index of cut"))
finish = int(input("Enter final index of cut"))
print(f"Cut inventory[{start}:{finish}] -this", end=" ")
print(inventory[start:finish])
input("\npress Enter to continue")
# cluch of list
chest = ["gold", "gems"]
print(f"\nYou find chest.Watch inside in: {chest}\n You loot it")
inventory += chest
print(f"\nand now in you have: {inventory}")
input("\npress Enter to continue")
#appropriation
inventory[0] ="crossbow"
print(f"Lets check inventory: {inventory}")
input("\npress Enter to continue")
#cluch of list new meaning
print("You lost gold and gems, and earn magic gem")
inventory[4:6] = ["magic gemstone"]
print(f"Now you nave{inventory}")
input("\npress Enter to continue")
#del
print(f"You lost {inventory[2]}")
del inventory[2]
print(f"Now in you invenrory{inventory}")
input("\npress Enter to continue")
#del cut
print(f"Now you lost{inventory[:2]}")
del inventory[:2]
print(f"Now in you invenrory{inventory}")
input("\npress Enter to continue")