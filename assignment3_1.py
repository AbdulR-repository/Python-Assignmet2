"""
Drivers are concerned with the mileage obtained by their automobiles. One driver
has kept track of several tankfuls of gasoline by recording miles driven and gallons used
for each tankful. Develop a Python program that prompts the user to input the miles
driven and gallons used for each tank- ful. The program should calculate and display the
miles per gallon obtained for each tankful. After processing all input information, the
program should calculate and print the combined miles per gal- lon obtained for all
tankful (= total miles driven divided by total gallons used).
"""
counter = 0
total = 0
while counter<4: 
    print( "Enter the gallons used, (-1 to end): \n" )
    gallons = int(input( "Enter the gallons used, (-1 to end): \n" ))

    if gallons == -1 :
        overallAverage = total / counter
        print( "The overall average miles/gallon was %f\n", overallAverage) 
        break
    
    miles= int(input("Enter the miles driven: \n" ))
    tankAverage = miles / gallons
    print( "The miles per gallon for this tank was %f\n", tankAverage )

    total += tankAverage
    counter += 1