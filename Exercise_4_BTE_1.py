#Hexadecimal output
'''
In this exercise, you’ll see how a bit of creativity, along with the built-in 'reversed'
and 'enumerate' functions, can help you to get around issues.
For this exercise, you need to write a function (hex_output) that takes a hex number
and returns the decimal equivalent. That is, if the user enters 50, you’ll assume
that it’s a hex number (equal to 0x50) and will print the value 80 to the screen. And
no, you shouldn’t convert the number all at once using the int function, although it’s
permissible to use int one digit at a time.
'''

#Beyond the exercise 1 (BTE_1)
'''
Reimplement the solution for this exercise such that it doesn't use the 'int' function
at all, but rather uses the built-in 'ord' and 'chr' functions to identify the
character. This implementation should be more robust, ignoring characters
that aren't legal for the entered number base.
'''

def hex_output():
    legal_chars = (l for l in '0123456789ABCDEF')
    result = 0
    temp = 0
    hex_num_1 = 0
    hex_num = input("Enter a hex number: 0x")
    if all((c in legal_chars) for c in hex_num):
        for ind, val in enumerate(reversed(hex_num)):
            result += (ord(val) - 48) * 16 ** ind       #chr(48) = '0' | ord('0') = 48
        print("Decimal equivalent is:", result)
        print(hex(result))                              #checking out
    else: print("Illegal character!")

hex_output()