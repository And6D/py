# Demonstrate how to use dictionaries examples from https://encyclopedia2.thefreedictionary.com/
geek = {"404": "Not Found,not exist",
        "googling": "The act of researching things on Google.com",
        "Keyboard Plague": "trash under keyboard cups",
        "Link Rot": "The process or condition in which links on a website become irrelevant"
                    "or cease to function, as when the locations they point to are webpages that"
                    " have been modified, relocated, or no longer exist",
        "percussive maintenance": "Banging on your computer or other electronic"
                                  " device to get it working",
        "uninstalled": "about firing employees"}

# menu
choice = None
while choice != "0":
    print("""
    Highscores
    О - Exit
    1 - Find answer
    2 - Add term 
    3 - Add definition
    4 - Dell term """)
    print(f" Now in dictionary:{geek.keys()}")
    choice = input("You choice: ")
    print()
    # exit
    if choice == "0":
        print("Good byе")
    # searching of term meaning
    elif choice == "1":
        term = input("Meaning of which term you want to know? ")
        if term in geek:
            definition = geek[term]
            print(f"\n {term} meaning {definition}")
        else:
            print(f"\n Sorry, but {term} did not exist")
    elif choice == "2":
        term = input("What term do you want to add? ")
        if term not in geek:
            definition = input("\n Add you definition:")
            geek[term] = definition
            print(f"\n Term {term} was added")
        else:
            print("This term already exist, try another one.")
    elif choice == "4":
        term = input("What term do you want to del? ")
        if term in geek:
            del geek[term]
            print(f"Term {term} del")
        else:
            print(f"This {term} not found, it not in dictionary.")
# bull shit user input
    else:
        print(f"Sorry,no what position in menu {choice}")
input("Press Enter to exit")