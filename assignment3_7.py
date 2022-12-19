"""
Write a Python program which takes two digits m (row) and n (column) as input and
generates a two-dimensional array. The element value in the i-th row and j-th column of
the array should be i*j.
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

row = int(input("Enter number of rows"))
column = int(input("Enter number of columns"))
Matrix = [[0 for x in range(column)] for y in range(row)]
for i in range(0,row):
    for j in range(0,column):
            Matrix[i][j]=i*j
print("Matrix = ",Matrix)