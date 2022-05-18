# hero inventory
# tuple creation process
# create empty tuple

inventory = ()
if not inventory:
    print("You harmless.")
input("\n\nPress Enter, to continue.")
inventory = ("sword", "armor", "shield", "healing poison")
print("\nYou fill ", len(inventory), "slots of inventory, lets take a look closer")
print("\n Inventory:", inventory)
print("\n So, in your inventory: ")
for item in inventory:
    print(item)

