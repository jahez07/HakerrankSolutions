# Enter your code here. Read input from STDIN. Print output to STDOUT

# Importing necessary package
import numpy as np

# reading input fromSTDIN
n, m = map(int,input().split())

# Create an empty 2D list
array = []
for i in range(n):
    row = []
    for j in range(m):
        value = float(input(f"Enter value for row {i+1}, column {j+1}: "))
        row.append(value)
    array.append(row)

