# Доработайте игру «Анаграммы» так, чтобы к каждому слову полаrалась подсказка.
# Игрок может:
# 1.получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы иrроки, отгападавшие слов о без подсказки,
# получали больше тех, кто запросил подсказку.

#0
import  random
#1
WORDS = ("bullet", "sword", "turbojet", "light", "sugar", "sweet", "jet", "phone")
#2. chose random word
word = random.choice(WORDS)
# write chosen by random word in variable
correct = word
#3. jumdle word
jumble =" "
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print( """go""")
print("So, guess word:\t", jumble, "\tit", len(jumble)-1, "wide")

guess = input("\nTray to guess source word: ")
# тут условие и ветвление если после 1 попытки идем дальше, если 2 попытка предлагаем посказку,
# если берем посказку меньнише очков чем после отказа от подсказки
while guess != correct and guess != "":
    print("You wrong")
    guess = input("Tray to guess source word: ")
#сюда вставить посказки при пустом вводу
if guess == correct:
    print("Yes, its it!\n")


print("Thanks for playing.")
input("\n\nPress Enter to exit.")
