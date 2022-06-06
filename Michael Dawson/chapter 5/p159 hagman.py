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
-------------
""",
    """
    -------
    |     |
    |     0  |
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
    |     0  |  -+-
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
    |     0  |  /-+-
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
    |     0  |  /-+-/
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
    |     0  |  /-+-/
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
    |     0  |  /-+-/
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
    |     0  |  /-+-/
    |     |
    |     |
    |    |  |
    |    |  |
    |
------------
""")
# max mistake
MAX_WRONG = len(HANGMAN) -1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")
# initialise variable
word = random.choice(WORDS)  # word for gees
so_far = "-" * len(word)  # one "-" on each symbol, wat need to guess
wrong = 0  # number of wrong user choices
used = []  # symbol's what user already typed
# main circle
print("Welcome to 'HANGMAN' game, Good like.")
while wrong < MAX_WRONG and so_far !=word:
    print(f"{HANGMAN[wrong]}"
          f"\n You already use this letters:"
          f"\n {used}"
          f"\n Now you guess"
          f"\n {so_far}")

