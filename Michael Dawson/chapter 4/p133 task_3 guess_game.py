# Доработайте игру «Анаграммы» так, чтобы к каждому слову полаrалась подсказка.
# Игрок может:
# 1.получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы иrроки, отгападавшие слов о без подсказки,
# получали больше тех, кто запросил подсказку.
# 0
import random
# dictionary
WORDS = ["bullet", "sword", "turbojet",
         "light", "sugar", "sweet",
         "bicycle", "phone", "song"]
PROMPT = ["a small metal object that is fired from a gun",
          "a weapon with a long metal blade",
          "a turbine engine that produces forward movement by forcing out a stream of hot air and gas behind it",
         "the energy from the sun, a lamp, etc. that makes it possible to see things",
          "a sweet substance, often in the form of white or brown crystals, made from the juices various plants, used in cooking or to make tea, coffee, etc. sweeter",
          "containing, or tasting as if it contains, a lot of sugar",
         "a road vehicle with two wheels that you ride by pushing the pedals with your feet",
         "a piece of equipment for talking to people who are not in the same place as you",
         "a short piece of music with words that you sing"]
# random choice word generator
word = random.choice(WORDS)
correct = word
# prompt variable
prompt = PROMPT[WORDS.index(correct)]
# jumble module
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
# score system
score = 100
max_score =score
mistake = -10
use_prompt = -30

print("""\n\tWat a jumble! Letter in word just going mad""")
print("\nTry guess word:\t", jumble, "\nit consists ", len(jumble), " letter at length")

guess = input("\nHere the rules:\nGuess оr Enter to take prompt"
              "\nYou can use a prompt just once, now or newer"
              "\nUse a prompt take -30 points to you score"
              "\nIf you guess at 1 try give take 100 points of score"
              "\nEvery additional try -10 points to you score"
              "\nYou will lose, when score will be 0 \t\n")
if guess =="":
    score += use_prompt
    print("Prompt: ", prompt, "\nyou lost for use a prompt", use_prompt, "\nscore for now:",
          score)

while guess != correct and score > 0:
    guess = input("Tray to guess source word: ")
    print("You wrong, in wiil be cost fot you", mistake, "points of score", score)
    score += mistake
    print("You score for now", score, "points")
if score == 0:
    print("YOU lOSE, to muсh mistakes")
if guess == correct and score > 0:
    print("Yes, you do it!", "\nYou guess word:\t", correct, "you score: ", score, "of ", max_score)
    input("\n\nHaжмитe Enter. чтобы выйти ")

