import random

random = random.randint(1,50)
guess = 0
guesses = 0

while guess != random:
    guesses += 1
    guess = int(input('gissa ett heltal mellan 1 - 50: '))

    if guess < random:
        print (f'{guess} är för litet gissa igen')
    
    elif guess > random:
        print (f'{guess} är för stort gissa igen')
    
    else:
        print(f'{guess} är helt rätt')
        print(f'Du gissade rätt på {guesses} försök')
