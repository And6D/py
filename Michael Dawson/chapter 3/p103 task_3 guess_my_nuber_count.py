import random
number = random.randint(1, 100)
guess = int(input('Input Number: ').replace('','0'))
tries = 1
max_tries =9
while number != guess and tries <= max_tries-1:
    if guess < number:
        print('Mine is more')
    else:
        print('Mine is less')
    guess = int(input('Input Number: ').replace('','0'))
    tries += 1
if tries >= max_tries:
    print('You POOR, bad try, noob')
else:
    print('Correct ! Number of your tries is:', tries)

