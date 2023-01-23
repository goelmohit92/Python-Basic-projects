# GCD= Greatest common divider
# HCF= Highest common factor

def findHCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x

    for i in range (1,smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            HCF = i
    return HCF

x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))

print("The HCF of the given two number is", findHCF(x,y))

