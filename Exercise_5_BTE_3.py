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

#Beyond the exercise 3 (BTE_3)
'''
Consider an alternative version of Pig Latin—We don't check to see if the first letter
is a vowel, but, rather, we check to see if the word contains two different vowels.
If it does, we don't move the first letter to the end. Because the word “wine”
contains two different vowels (“i” and “e”), we'll add “way” to the end of it, giving
us “wineway.” By contrast, the word “wind” contains only one vowel, so we
would move the first letter to the end and add “ay,” rendering it “indway.” How
would you check for two different vowels in the word? (Hint: sets can come in
handy here.)
'''

def pig_latin(word):
    counter = 0
    test = set(word)
    for c in test:
        if c in "aeiou":
            counter += 1
    if counter >= 2 :
        return f"{word}way"

    return f'{word[1:]}{word[0]}ay'
    

print(pig_latin('winei'))
print(pig_latin('wind'))