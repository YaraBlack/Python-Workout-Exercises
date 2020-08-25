#Run timing
'''
For this exercise, then, we’ll assume that you run 10 km each day as part of your
exercise regime. You want to know how long, on average, that run takes.
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the average time that the 10 km runs took. 
Note that the numeric inputs and outputs should all be floating-point values.
'''

#Beyond the exercise 1 (BTE_1)
'''
Write a function that takes a float and two integers (before and after). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678, 2 and
3, the return value should be 34.567.
'''

def splitFloat(basis, beforeDigits, afterDigits):
    temp = str(basis).split(".")
    bef = temp[0]
    aft = temp[1]
    print()
    q = float(bef[len(bef) - beforeDigits:] + '.' + aft[:afterDigits])
    print(q)


splitFloat(1234.5678, 3, 3)