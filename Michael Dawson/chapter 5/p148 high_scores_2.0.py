# high_scores 2.0
# shows nested sequences
scores = []
choice = None
# while choise !="0":
print(""" High cores""")
# menu пока не 0
while choice != "0":
    print(
        """
    Highscores 2.0
    О - Exit
    1 - Show highscores
    2 - Add highscores
    """
    )
    choice = input("You choice: ")
    print()
    # exit
    if choice == "0":
        print("Good byе")
    # вывод результатов на экран содержащихся во воложенных кортеджах
    elif choice == "1":
        print("Highscores\n"
              "NAME\t|\tSCORE")
        for entry in scores:
            score, name = entry
            print(f"{name}\t|\t{score}")
    # add record
    elif choice == "2":
        name = input("Type player's name: ")
        score = int(input("Write he's score: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # in list only 5 records
    # miss clic error
    else:
        print(f"Sorry,no what position in menu {choice}")
input("Press Enter to exit")
