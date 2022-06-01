scores = []
choice = None
# while choise !="0":
print(""" High cores""")
# menu пока не 0
while choice != "0":
    print(
        """
    Highscores
    О - Exit
    1 - Show highscores
    2 - Add highscores
    3 - Delete highscores
    4 - Sort list 
    """
    )
    choice = input("You choice: ")
    print()
# exit
    if choice == "0":
     print("Good byе")
# вывод лучших результатов на экран
    elif choice == "1":
     print("Highscores")
     for score in scores:
        print(score)
# add record
    elif choice == "2":
     score = int(input("Write you highscores"))
     scores.append(score)
    elif choice == "3":
     score = int(input("Which highscores you want to delete?: "))
     if score in scores:
        scores.remove(score)
     else:
        print(f"Result {score} not find.")
    elif choice == "4":
      scores.sort(reverse=True)
# miss clic error
    else:
     print(f"Sorry,no what position in menu {choice}")
input("Press Enter to exit")