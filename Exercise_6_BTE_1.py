#Pig Latin sentence
'''
Write a function
called pl_sentence that takes a string containing several words, separated by
spaces. (To make things easier, we won’t actually ask for a real sentence. More specifically,
there will be no capital letters or punctuation.)
So, if someone were to call
    pl_sentence('this is a test translation')
the output would be
    histay isway away estay ranslationtay
Print the output on a single line, rather than with each word on a separate line.
'''

#Beyond the exercise 1 (BTE_1)
'''
Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.
'''

'''
word = [
    word1 word2 word3
    word4 word5 word6
    word7 word8 word9
    ]

sentence: word1 word2 word3 word5 word6 word9
'''
def open_txt():
    with open('D:\Workspace\Python-Workout-Exercises\words.txt', 'r') as file:
        reader = file.read()
        words = reader.replace(' ', '').replace('\n','').split(',')
        return words

def pl_sentence(sentence):
    temp = ""
    for word in sentence.split():
        if word[0] in "aeiou":
            temp += f"{word}way "
        else:
            temp += f'{word[1:]}{word[0]}ay '
    return temp

# print(pl_sentence('this is a test translation'))
print(open_txt())
