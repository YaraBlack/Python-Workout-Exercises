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

#Beyond the exercise 2 (BTE_2) | I hope that I understood in right ;-;
'''
Not only should you choose a random number, but you should also choose a
random number base, from 2 to 16, in which the user should submit their
input. If the user inputs “10” as their guess, you’ll need to interpret it in the
correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16
(hexadecimal).
'''

import random


def GuessNumber():
    num_base = random.choice([i for i in range(2,17)])
    number = int(str(random.randint(0,100)), base = num_base)
    while True:
        userInput = int(input("Guess a number: "), base = num_base)
        if userInput == number:
            print("Just right.")
            break

        elif userInput < number:
            print("Too low.")

        elif userInput > number:
            print("Too high.")

GuessNumber()