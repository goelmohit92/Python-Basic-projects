# Quadtratic equation ax**2 + bx + c = 0
# a, b and c are real numbers
# a!= 0

import cmath
import math

a = int(input("Enter number a (a!=0): "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

# formula for discriminant
d = (b**2) - (4*a*c)

root1 = (-b - cmath.sqrt(d))/(2*a)
root2 = (-b + cmath.sqrt(d))/(2*a)

print("the roots are", root1, "and", root2)
