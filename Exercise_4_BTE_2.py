#Hexadecimal output
'''
In this exercise, you'll see how a bit of creativity, along with the built-in 'reversed'
and 'enumerate' functions, can help you to get around issues.
For this exercise, you need to write a function (hex_output) that takes a hex number
and returns the decimal equivalent. That is, if the user enters 50, you'll assume
that it's a hex number (equal to 0x50) and will print the value 80 to the screen. And
no, you shouldn't convert the number all at once using the int function, although it's
permissible to use int one digit at a time.
'''

#Beyond the exercise 2 (BTE_2)
'''
Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth, until the entire name is written on the final line.
'''
def nameTriangle():
    name = input("Enter your name: ")
    v = 1
    for i in name:
        print(name[:v])
        v += 1

nameTriangle()