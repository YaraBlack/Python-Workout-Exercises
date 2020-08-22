#Summing numbers
'''
Summ all numbers that is inputed in the function
'''

#Beyond the exercise 1 (BTE_1)
'''
The built-in version of sum takes an optional second argument, which is used as
the starting point for the summing. (That’s why it takes a list of numbers as its
first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns
10, because 1+2+3 is 6, which would be added to the starting value of 4. Reimplement
your mysum function such that it works in this way. If a second argument
is not provided, then it should default to 0. Note that while you can write
a function in Python 3 that defines a parameter after *args, I’d suggest avoiding
it and just taking two arguments—a list and an optional starting point.
'''


def mysum(listOfNum, startingV = 0):
    sum = 0
    for i in listOfNum:
        sum += i
    return sum + startingV


print(mysum([1, 2, 3], 5))