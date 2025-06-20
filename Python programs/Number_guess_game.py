import random

number_guess_game=random.randint(1,100)
while True:
    try:
        guess = int(input("Enter a number : "))
        if guess < number_guess_game:
            print("To low !")
        elif guess > number_guess_game:
            print("To high!")
        else:
            print("congrats you guess number")
            "break"
    except ValueError:
        print("Enter a vaild number")
