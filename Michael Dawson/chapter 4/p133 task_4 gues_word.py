import random
# dictionary
WORDS = ["bullet", "sword", "turbojet",
         "light", "sugar", "sweet",
         "bicycle", "phone", "song",
         "face", "t-shirt", "smile"]
word = random.choice(WORDS)
# len word and print
print("Guess word! \t\nIt have: ", len(word), "lettres")
print("You have 5 take to guess letter in word, after try guess word")
max_tries = 5
tries =0
while tries != max_tries:
    letter = input("Choose the letter")
    tries += 1
    if letter in word:
      print("Yes, letter", letter, "in word")
    else:
      print("No,", letter, "not found")
    print("You use", tries, "take of", 5)

else:
    guess = input(" Now guess word")
    if guess == word:
        print("Yes, its it!")
    if guess != word:
        print("No, you lose!")


