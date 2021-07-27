# A program to obtain values n and s from user and print area of polygon.

# ½ n sin (360 / n ) s2

# Where n = number of sides and s = length from center to a corner.
# A program to obtain values n and s from user and print area of polygon.


import math 

s = float(input("Enter the length from center to a corner: "))
n = int(input("Enter the number of sides: "))

sin = math.sin(360 / n)

print (1/2 * n * sin * s ** 2)
