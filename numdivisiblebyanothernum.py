# soltion 1 using for loop

print("The number divisible by 13 are : ")
for i in range (1,100):
    if i % 13 == 0:
        print(i)

# solution 2 using lambda and filter

l = [30,40,52,93,78,98]

result = list(filter(lambda x : x % 13 == 0, l))
print('the numbers divisible by 13 are: ',result)