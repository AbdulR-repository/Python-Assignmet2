"""
Write a program that estimates the value of the mathematical constant e by using the
formula
e = 1 + 1/1!+ 1/2!+ 1/3!+....
"""

def factorial(factorial_user_input):
    fact = 1
    try:
        while 1 <= factorial_user_input:
            fact *= factorial_user_input
            factorial_user_input -= 1
        return fact
    except:
        print("An exception occurred")
        return 1


user_input = int(input('Enter the n term in 1/n!: '))
e = 0
f = 0
while user_input > 0:
    e = e + (1 / factorial(f))
    f = f + 1
    user_input = user_input - 1
print(e)