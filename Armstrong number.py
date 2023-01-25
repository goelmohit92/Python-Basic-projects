# Solution 1:
num = int(input("Enter a number here: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** order
    sum += cube
    temp //= 10

if sum == num:
    print('it is an Armstrong number')
else:
    print('it is not an Armstrong number')


# Solution 2: Armstrong number for an interval
lower = int(input("Enter the lower limit here:"))
upper = int(input("Enter the upper limit here:"))

for num in range (lower, upper +1):
    order = len(str(num))
    sum = 0
    temp= num
    while temp > 0:
        digit = temp % 10
        cube = digit ** order
        sum += cube
        temp //= 10
    if num == sum:
        print(num)
