import random

number = random.randint(1, 100)
guess = 0

print("Guess a number between 1 and 100!")

while guess != number:
    guess = int(input("Your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it! The number was", number)

 