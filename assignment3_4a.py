"""
Write a program that reads a nonnegative integer and computes and prints its
factorial.
"""

def factorial(factorial_user_input):
    fact = 1
    try:
        while factorial_user_input>0:
            fact *= factorial_user_input
            factorial_user_input -= 1
            print("Till Factorial of ",factorial_user_input,"\n")
        print("Factorial :  ", fact, "\n")
    except:
        print("An exception occurred")
        return None

n = int (input ('Enter a number for factorial: '))
factorial(n)