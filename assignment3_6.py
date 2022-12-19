"""
A right triangle can have sides that are all integers. The set of
three integer values for the sides of a right triangle is called a Pythagorean triple. These
three sides must satisfy the relationship that the sum of the squares of two of the sides
is equal to the square of the hypotenuse. Find all Pythagorean triples for side1, side2
and hypotenuse all no larger than 20. Use a triple-nested for-loop that tries all
possibilities. This is an example of “brute force” comput- ing. You will learn in more
advanced computer science courses that there are many interesting prob- lems for which
there is no known algorithmic approach other than sheer brute force.
"""

limit=20
for i in range(1,limit):
    for j in range(i,limit):
        for k in range(j,limit):
            if(i*i + j*j == k*k):
                print("Pythagorean Triples (side1^2 + side2^2 = hypotenous^2 ) => {",i," , ",j," , ",k," } ")
