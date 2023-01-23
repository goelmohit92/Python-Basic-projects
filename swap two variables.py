# Solution 1 (using temporary variable)
x = 13
y = 15

temp = x
print("the value of temp variable is",temp)

x=y
print("the value of x is", x)

y = temp
print("the value of y is",y)

# solution 2 ( using without third variable)
x = 13
y = 15

x, y = y, x
print("the value of x is",x)
print("the value of y is",y)





