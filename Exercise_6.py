#Pig Latin sentence
'''
Write a function
called pl_sentence that takes a string containing several words, separated by
spaces. (To make things easier, we won't actually ask for a real sentence. More specifically,
there will be no capital letters or punctuation.)
So, if someone were to call
    pl_sentence('this is a test translation')
the output would be
    histay isway away estay ranslationtay
Print the output on a single line, rather than with each word on a separate line.
'''

def pl_sentence(sentence):
    temp = ""
    for word in sentence.split():
        if word[0] in "aeiou":
            temp += f"{word}way "
        else:
            temp += f'{word[1:]}{word[0]}ay '
    return temp

print(pl_sentence('this is a test translation'))