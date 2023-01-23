def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

n = int(input("Enter a Number here: "))
if n <=0:
    print("Factorial of number less than 1 does not exist")
else:
    print("Factorial of given number is", fact(n))

# using with loop

num = int(input("Enter a number here: "))

fact = 1

if num < 0:
    print("Factorial less than 0 is not exist")
    
if num ==0:
    print("Factorial of 0 is", 1)

if num > 0:
    for i in range(1, num+1):
        fact = fact*i
print("The factorial of a given number is: ", fact)
