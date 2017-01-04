"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

#ask the user for raw input
#split the input on spaces

while True:

    user_input = raw_input("Please input your math expression. Ex. + 2 2\n>")

    tokens = user_input.split()
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "-":
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "*":
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "/":
        print divide(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "square":
        print square(int(tokens[1]))
    elif tokens[0] == "cube":
        print cube(int(tokens[1]))
    elif tokens[0] == "power":
        print power(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "mod":
        print mod(int(tokens[1]), int(tokens[2]))
    else:
        print "Invalid input"
