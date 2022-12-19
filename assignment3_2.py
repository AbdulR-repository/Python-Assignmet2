"""
A palindrome is a number or a text phrase that reads the same backwards or
forwards. For example, each of the following five-digit integers is a palindrome: 12321,
55555, 45554 and 11611. Write a program that reads in a five-digit integer and
determines whether it is a palindrome. (Hint: Use the division and modulus operators to
separate the number into its individual digits.)
"""

number=int(input("Enter a number:"))
reverse=0
temp_num=number
while(number>0):
    digit=number%10
    print("digit checking:",digit)
    reverse=reverse*10+digit
    print("reverse checking:",reverse)
    number=number//10 #// is used for int output of divide
if temp_num==reverse:
    print("This number is palendrome:",temp_num)
else:
    print("This number is not palendrome:",temp_num)