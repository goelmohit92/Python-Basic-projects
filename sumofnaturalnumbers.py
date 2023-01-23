num = int(input('Enter a number here: '))

if num < 0:
    print('Please enter a positive number')
else:
    sum = 0
    while num>0:
        sum +=num
        num -= 1
    print(sum)

# using recursion
# NNS = natural number sum

def NNS (n):
    if n <= 1:
        return n
    else:
        return (n) + NNS(n-1)
    
n = int(input("Enter n number here: "))

if n <= 0:
    print("Enter a  Positive number: ")
else:
    print("The sum of natural number upto given number is", NNS(n))
    