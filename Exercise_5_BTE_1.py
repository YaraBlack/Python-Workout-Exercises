#Pig Latin
'''
The rules for translating words from English into Pig
Latin are quite simple:
- If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
- If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”
(And yes, I recognize that the rules can be made more sophisticated. Let's keep it simple
for the purposes of this exercise.)
For this exercise, write a Python function (pig_latin) that takes a string as input,
assumed to be an English word. The function should return the translation of this word
into Pig Latin. You may assume that the word contains no capital letters or punctuation.
'''

#Beyond the exercise 1 (BTE_1)
'''
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn't), then the Pig Latin translation should be
similarly capitalized.
'''

def pig_latin(word):
    if word[0].isupper():
        if word[0] in "AEIOU":
            return f"{word}way"

        return f'{word[1].upper()}{word[2:]}{word[0].lower()}ay'
    else:
        if word[0] in "aeiou":
            return f"{word}way"

        return f'{word[1:]}{word[0]}ay'

print(pig_latin('Awake'))
print(pig_latin('Pit'))