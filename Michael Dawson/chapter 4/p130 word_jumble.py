# Word jumble
# gamer must restore source word
# import random module
import  random
# set of words
WORDS = ("bullet", "sword", "turbojet", "light", "sugar", "")
# in variable 'word" set word from WORDS by random
word = random.choice(WORDS)
# in variable "correct" set chosen by random source word
correct = word
# create empty variable in wich
jumble = " "
# create condition
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

# starting greeting
print( """
                    Добро пожаловать в игру 'Анаграммы'! 
        Надо переставить буквы так. чтобы получилось осмысленное слово. 
            (Для выхода нажмите Enter. не вводя своей версии.) 
 """)
print("So it's a jumble:", jumble )

guess = input("\nTray to guess source word: ")
while guess != correct and guess != "":
    print("You wrong")
    guess = input("Tray to guess source word: ")
if guess == correct:
    print("Yes, its it!\n")

print("Thanks for playing.")
input("\n\nPress Enter to exit.")
