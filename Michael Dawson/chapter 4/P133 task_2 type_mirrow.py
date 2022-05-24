

word = input("Type word, and take a look what reflect mirror glass\n\n")
r = len(word)
for i in range(r):
    print(word[-i-1], end='')
print("\nreflect in mirror")