#Summing numbers
'''
Summ all numbers that is inputed in the function
'''

#Beyond the exercise 2 (BTE_2)
'''
Write a function that takes a list of numbers. It should return the average (i.e.,
arithmetic mean) of those numbers.
'''

def myavg(numbers):
    sum = 0
    quantity = 0
    for i in numbers:
        quantity += 1
        sum += i
    return sum/quantity

print('{:.2f}'.format(myavg([1, 2, 5])))