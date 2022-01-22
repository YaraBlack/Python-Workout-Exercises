#Summing numbers
'''
Sum all numbers that is inputed in the function
'''

def mysum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


#print(mysum(1, 2, 3))
'''
If we call mysum(*[1,2,3]), our list becomes three separate arguments, which will
then allow the function to be called in the usual way.
'''
print(mysum(* [1, 2, 3]))