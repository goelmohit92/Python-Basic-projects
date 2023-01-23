# solution 1 using Enumerate method
# when start indexing from 1 we can use start=1
# l = [38, 43, 32, 2, 45, 54]
# # for index, value in enumerate(l,start=1):
# for index, value in enumerate(l):
#     print(index, "-", value)

# solution using for loop not Enumerate

l = [38, 43, 32, 2, 45, 54]

for index in range(len(l)):
    value = l[index]
    print(index, "-", value)



 