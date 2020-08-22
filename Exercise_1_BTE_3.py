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

#Beyond the exercise 3 (BTE_3)
'''
Try the same thing, but have the program choose a random word from the dictionary,
and then ask the user to guess the word. (You might want to limit yourself
to words containing two to five letters, to avoid making it too horribly
difficult.) Instead of telling the user that they should guess a smaller or larger
number, have them choose an earlier or later word in the dict.
'''
#There is no point in creating an object of dict Class, so better just use a list.

import random


def GuessWord():
    dictionary = "apple banana orange kiwi peach".split()
    guessedWord = random.choice(dictionary)
    print("The dictionary is:{}".format(dictionary))
    while True:
        userInput = input("Guess a word: ")
        if userInput == guessedWord:
            print("Just right.")
            break

        else:
            a = 0
            b = 0
            for i, word in enumerate(dictionary):
                if word == guessedWord:
                    a = i
                if word == userInput:
                    b = i
            if b < a:
                print("The word is later in the dictionary.")
            else:           # b > a
                print("The word is earlier in the dictionary.")

GuessWord()
