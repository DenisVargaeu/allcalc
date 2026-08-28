"""
This script check if inputed number is even or odd 
"""

def check(number):

    work = (number/2)

    if number.is_integer() and work.is_integer():
        print (f"Number {number} is even number")
    else:
        print (f"Number {number} is odd number")