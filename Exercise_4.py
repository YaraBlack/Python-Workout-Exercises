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
import string

def hex_output():
    result = 0
    hex_num = input("Enter a hex number: 0x")           
    if all((c in string.hexdigits) for c in hex_num):  
        for ind, val in enumerate(reversed(hex_num)):
            result += int(val, 16) * 16 ** ind
        print("Decimal equivalent is:", result)
        print(hex(result)) 
    else: print ("Wrong character!")

hex_output()