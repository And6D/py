
#только согласные
message = input("solid word and lower\n" + "Enter text: ")
new_message = ""
VOWELS = "aeiouаеёиоуыэюя"
# константа
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        #new_message = new_message + letter строка с увеличением
        print("New string was created: ", new_message)
print("\ntext: ", new_message)
