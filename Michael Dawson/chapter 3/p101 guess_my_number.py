import random
number = random.randint(1, 100)
guess = int(input('Input Number: '))
tries = 1
max_tries =7
while number != guess:
    if guess < number:
        print('Mine is more')
    else:
        print('Mine is less')
        guess = int(input('Input Number: '))
        tries += 1
print("Number ", number , "is correct")
print("You ges it in: ", tries )
