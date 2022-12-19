"""
Write a program that computes the value of ex by using the formula [Note: Your
program can stop after summing 10 terms.]
e^x =1+ x/1! +x^2/2! + x^3/3! +...
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