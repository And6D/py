# random letters
# len
import random
word = "index"
print ("В переменной word хранится слово: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(15):
 position = random.randrange(low, high)
 print ("word[", position, "]\t", word[position])
input("\n\nHaжмитe Enter. чтобы выйти.")