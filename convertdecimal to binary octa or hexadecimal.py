decimal = int(input("Enter a number here: "))

print("the conversion of decimal number", decimal, "is: " )
print(bin(decimal),"in binary")
print(oct(decimal),"in octal")
print(hex(decimal),"in hexadecimal")
 

# using Recursion

def ConvertBinary(n):
    if n > 1:
        ConvertBinary(n//2)
    print(n%2, end = "")

n = int(input("Enter a number here: "))
print("the binary of the given number is: ")
ConvertBinary(n)