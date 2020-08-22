#Number guessing game
'''
For this exercise
* Write a function (guessing_game) that takes no arguments.
* When run, the function chooses a random integer between 0 and 100 (inclusive).
* Then ask the user to guess what number has been chosen.
* Each time the user enters a guess, the program indicates one of the following:
– Too high
– Too low
– Just right
* If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
* The program only exits after the user guesses correctly.
'''

import random


def GuessNumber():
    number = random.randint(0,100)
    while True:
        userInput = int(input("Guess a number: "))
        if userInput == number:
            print("Just right.")
            break

        elif userInput < number:
            print("Too low.")

        elif userInput > number:
            print("Too high.")

GuessNumber()
