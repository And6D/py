# Доработайте игру «Анаграммы» так, чтобы к каждому слову полаrалась подсказка.
# Игрок может:
# 1.получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы иrроки, отгападавшие слов о без подсказки,
# получали больше тех, кто запросил подсказку.

# 0
import random
# 1
WORDS = ("bullet", "sword", "turbojet",
         "light", "sugar", "sweet",
         "bicycle", "phone", "song")
PROMPT = ("a small metal object that is fired from a gun",
         "a weapon with a long metal blade",
         "a turbine engine that produces forward movement "
         "by forcing out a stream of hot air and gas behind it",
         "the energy from the sun, a lamp, etc. that makes it possible to see things",
         "a road vehicle with two wheels that you ride by pushing the pedals with your feet",
         "a piece of equipment for talking to people who are not in the same place as you",
         "a short piece of music with words that you sing")
# 2. chose random word
word = random.choice(WORDS)
# write chosen by random word in variable
correct = word
# 3. jumdle word
jumble = " "
# цикл осуществляет пермешивание исходного слова
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
# 4. set prompt
# для посказки берем индекс значения word из словаря WORDS и забирает значение с тем же индексом
# из словаря PROMPT и предаем в переменную promt

print("""go""")
print("So, guess word:\t", jumble, "\tit", len(jumble) - 1, "wide")

guess = input("\nTray to guess source word оr type 'prompt': ")
# тут условие и ветвление
#
# если введено верное слово выводим "вы угадали"  и score=max_score  "игра окончена"
# если выбрана посказка выводится jumble и посказка score=max_score - try

#    выводится до тех пор пока 1.try < max_try  2. guess  guess == correct:
# 1. print(вы исчерпли все попытки игра закончена)
# 2. print(вы угадали)
# попытки укадывается слово идем
# дальше,

#
while guess != correct and guess != "":
    print("You wrong")
    guess = input("Tray to guess source word: ")
# сюда вставить посказки при пустом вводу
if guess == correct:
    print("Yes, its it!\n")

print("Thanks for playing.")
input("\n\nPress Enter to exit.")
