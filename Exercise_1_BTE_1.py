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
#Beyond the exercise 1 (BTE_1)
'''
Modify this program, such that it gives the user only three chances to guess the
correct number. If they try three times without success, the program tells them
that they didn’t guess in time and then exits.
'''

import random


def GuessNumber(): 
    number = random.randint(0,100)
    tries = 0
    while tries != 3:
        tries +=1
        userInput = int(input("Guess a number: "))
        if userInput == number:
            print("Just right.")
            break

        elif userInput < number:
            print("Too low.")
            print("You have %d tries left!" % (3-tries))

        elif userInput > number:
            print("Too high.")
            print("You have %d tries left!" % (3-tries))
    else:
        print("Unfortunately, you didn't guess in time!")

GuessNumber()