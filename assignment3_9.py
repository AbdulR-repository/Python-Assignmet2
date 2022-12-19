"""
Write a program that calculates how much money you’ll end up with the invested
amount of money at a fixed interest rate, compounded yearly. Have the user furnish the
initial amount, the number of years, and the yearly interest rate in percent.
At the end of the first year you have 3000 + (3000 * 0.055), which is 3165. At the end
of the second year you have 3165 + (3165 * 0.055), which is 3339.08. Do this as many
times as there are years. A for loop makes the calculation easy.
"""

initial = int(input("Enter initial amount:"))
no_years = int(input("Enter number of years:"))
intrest_rate = float(input("Enter interest rate (percent per year):"))

if(no_years>0):
    for i in range(1,no_years+1):
        intial_percent=intrest_rate / 100
        per_year=initial +(initial * intial_percent)
        initial=per_year    
        print("At the end of the ",i," year you have ",per_year)
else:
    print("Please enter a valid number of Years.")
    