#Summing numbers
'''
Summ all numbers that is inputed in the function
'''

#Beyond the exercise 4 (BTE_4)
'''
Write a function that takes a list of Python objects. Sum the objects that either
are integers or can be turned into integers, ignoring the others.
'''

def mysum(*args):
    sum = 0
    check = (int, float, bool)                                  #temporary solution, probably will change someday
    for i in args:
        if type(i) in check:
            sum += int(i)
    return sum

print(mysum(* [1, 'word', 3.213, True, (2, 3, 2)]))            #int(True) = 1, int(False) = 0; if the number is decimal only whole number without fractional part i.e. int(3.53) = 3