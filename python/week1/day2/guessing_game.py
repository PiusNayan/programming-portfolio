"""
Number Guessing Game — Mini Project

The computer picks a random number between 1 and 10.
The user guesses until they get the correct answer.
After each wrong guess, the program tells them whether the guess was
too high or too low. It also counts the total number of attempts.
"""

import random

# Generate a secret number once before the loop starts
secret_number = random.randint(1, 10)

guess = int(input("Guess any random number between 1-10. "))

attempts = 1

while guess != secret_number:
    if guess > secret_number:
        print("Incorrect, you guessed too high")
    else:
        print("Incorrect, you guessed too low")

    attempts += 1
    guess = int(input("Try again"))

print(f"Congratulations🎉, you guessed it in {attempts} attempts.")