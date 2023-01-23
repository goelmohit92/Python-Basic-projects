# # solution 1 (using Exponentiation)

num1 = float(input("Enter a number here: "))
sqr = num1**(1/2)
print("The square root of the given number is", sqr)

# solution 2 (using Math module )

import math
num = int(input("Enter a number here: "))
sr = math.sqrt(num)
print("The square root of the given number is", sr)
