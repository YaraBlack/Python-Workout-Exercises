#Summing numbers
'''
Summ all numbers that is inputed in the function
'''

#Beyond the exercise (BTE_3)
'''
Write a function that takes a list of words (strings). It should return a tuple containing
three integers, representing the length of the shortest word, the length
of the longest word, and the average word length.
'''

def wordsFunc(words_list):
    shortLen = 0
    longLen = 0
    averLen = 0
    word_len = []
    for i in words_list:
        word_len.append((len(i), i))
        word_len.sort()
        averLen += len(i)
    shortLen = word_len[0][0]
    longLen = word_len[-1][0]
    averLen /= len(words_list)
    return (shortLen, longLen, averLen)


print(wordsFunc(['apple', 'orange', 'banana', 'watermelon', 'kiwi']))