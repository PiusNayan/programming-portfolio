# ## Exercise 4 — Number Guessing Game ⭐ (Mini Project)

# Your first game!

# Requirements:
# •Import random
# •Generate a secret number from 1–10
# •Ask the user to guess
# •Use a loop until they get it correct
# •Tell them if their guess is too high or too low
# •Display a congratulatory message when they win

import random
secret_number = random.randint(1,10)

guess = int(input("Guess any random number between 1-10. "))

atempts = 1

while guess != secret_number:
    if guess > secret_number:
        print(f'Incorrct, you guessed too high ')
    else:
        print(f'Incorrect, you guessed too low ')
    
    atempts += 1
    guess = int(input("Try again"))
print(f'Congratulations🎉, you guessed it in {atempts} attempts.')