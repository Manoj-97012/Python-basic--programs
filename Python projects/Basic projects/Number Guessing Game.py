#Number Guessing Game
import random
n = random.randrange(1,10)
guess = int(input('Enter a number:'))
while n != guess:
    if n > guess:
        print('To low')
        guess = int(input('Enter number again:'))
    elif n < guess:
        print('To high')
        guess = int(input('Enter number again:'))
    else:
        break
    print("You guess it right")