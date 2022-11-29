""" 1. Create a program that prints a list of words in random order.
    2. The program should print all the words and not repeat any."""
import random

# dictionary
WORDS = ["bullet", "sword", "turbojet",
         "light", "sugar", "sweet",
         "bicycle", "phone", "song",
         "face", "t-shirt", "smile"]
# main
# print all word from WORDS
# while if word not duble in WORDS print word

def check_dup(l):
    newList = []
    for i in WORDS:
        if i not in newList:
            newList.append(i)
    return newList

newList = check_dup(WORDS)

random.shuffle(newList)

for i in newList:
    print(i)

# не красивое надо переделать