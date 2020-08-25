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

#Beyond the exercise 2 (BTE_2)
'''
Explore the Decimal class (http://mng.bz/oPVr), which has an alternative
floating-point representation that’s as accurate as any decimal number can be.
Write a function that takes two strings from the user, turns them into decimal
instances, and then prints the floating-point sum of the user’s two inputs. In
other words, make it possible for the user to enter 0.1 and 0.2, and for us to get
0.3 back.
'''
import decimal as dc

def sumDecimal():
    first_arg = dc.Decimal(input("First decimal: "))
    second_arg = dc.Decimal(input("Second decimal: "))
    print("The sum is:", first_arg + second_arg)



sumDecimal()