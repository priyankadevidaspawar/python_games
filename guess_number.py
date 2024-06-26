# -*- coding: utf-8 -*-
"""guess_number.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NTmOxMsexwk78xp_kNLLG2STx1tTj03a

This game randomly generates a secret number between 1 and 100, and the player has to guess what it is. After each guess, the game tells the player whether their guess was too high or too low. The game continues until the player guesses the correct number.
"""

import random

def guess_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

if __name__ == "__main__":
    guess_number()