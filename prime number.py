num = int(input("enter a number here:"))

if num==1:
    print("it is not a prime number")
if num>1:
    for i in range (2,num):
        if num % i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")


# print all prime number in an interval

lower = int(input("Enter lower limit here: "))
upper = int(input("Enter upper limit here: "))

for num in range (lower, upper+1):
    if num>1:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
            print(num)



