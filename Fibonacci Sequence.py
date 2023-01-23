# using for loop
a =0
b = 1
num = int(input("Enter a number to obtain Fibonacci sequence: "))
if num ==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range (2, num):
        c = a + b
        a = b
        b = c
        print(c)

# using Recursion

def fibo (n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input("Enter a number here: "))

if n <= 0:
    print("Enter a positive number ")
else:
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))