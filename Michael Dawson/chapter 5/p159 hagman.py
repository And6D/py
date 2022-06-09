import random

# constant hangman
HANGMAN = (
    """
    -------
    |     |
    |
    |
    |
    |
    |
    |
    |
-------------
""",
    """
    -------
    |     |
    |     |
    |     0
    |
    |
    |
    |
    |
-------------
""",
    """
    -------
    |     |
    |     0
    |    -+-
    |
    |
    |
    |
    |
-------------
""",
    """
    -------
    |     |
    |     0
    |   /-+-
    |
    |
    |
    |
    |
-------------
""",
    """
    -------
    |     |
    |     0
    |   /-+-/
    |     
    |
    |
    |
    |
-------------
""",
    """
    -------
    |     |
    |     0
    |   /-+-/
    |     | 
    |
    |
    |
    |
-------------
""",
    """
    -------
    |     |
    |     0
    |   /-+-/
    |     |
    |     |
    |    |
    |    |
    |
-------------
""",
    """
    -------
    |     |
    |     0  
    |   /-+-/
    |     |
    |     |
    |    |  |
    |    |  |
    |
------------
""")
# max mistake
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")
# initialise variable
word = random.choice(WORDS)  # word for gees
so_far = "-" * len(word)  # one "-" on each symbol, wat need to guess
wrong = 0  # number of wrong user choices
used = []  # symbol's what user already typed
# main circle
print("Welcome to 'HANGMAN' game, \n\tGood like.")
while wrong < MAX_WRONG and so_far != word:
    print(f"{HANGMAN[wrong]}"
          f"\n You already use this letters:"
          f"\n {used}"
          f"\n Now you guess"
          f"\n {so_far}")
    # inserted circle user input
    guess = input("\n\n Type a letter")
    guess = guess.upper()  # re-write enter in capital
    while guess in used:
        print(f"You already enter {guess} before")
        guess = input("\n\n Enter letter: ")
        guess = guess.upper()
    used.append(guess)
    # check-in is letter contained in word
    if guess in word:
        print(f"Yes! Letter {guess} is contained in word ")
        # new string so_far include this letter or letter's
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
        # in check
    else:
         print(f"\n No, {guess}, is not contained in word")
         wrong += 1
if wrong == MAX_WRONG:
    print(f"{HANGMAN[wrong]} \n you was hangman!")
else:
    print(f"You Guess {word}")
input("\n\n Press Enter to EXIT")
