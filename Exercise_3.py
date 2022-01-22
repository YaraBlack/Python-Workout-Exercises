#Run timing
'''
For this exercise, then, we'll assume that you run 10 km each day as part of your
exercise regime. You want to know how long, on average, that run takes.
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the average time that the 10 km runs took. 
Note that the numeric inputs and outputs should all be floating-point values.
'''

def run_timing():
    calculating = []
    avg = 0.0
    while True:
        try:
            userInput = input("Enter 10 km run time:")
            if userInput:
                if int(userInput) > 0:
                    calculating.append(float(userInput))
                else: print ("Wrong time!")
            else: break
        except ValueError:
            print("Hey! That's not a valid number!")
    if calculating:
        for i in calculating:
            avg += i
        avg /= len(calculating)
    print("Average of {:.2f}, over {} runs".format(avg, len(calculating)))

run_timing()

'''
Solution from the book:

def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time
    and number of runs."""

    number_of_runs = 0
    total_time = 0
    
    while True:
        one_run = input('Enter 10 km run time: ')
        
        if not one_run:
            break

        number_of_runs += 1        
        total_time += float(one_run)
        
    average_time = total_time / number_of_runs
    print(f'Average of {average_time}, over {number_of_runs} runs')

run_timing()
'''