# Solution 1 using for loop

A = [[1,2,3],
    [4,5,6]]

B = [[0,0],
    [0,0],
    [0,0]]

for i in range (len(A)):
    for j in range(len(A[0])):
        B[j][i] = A[i][j]
for i in B:
    print(i)

print("")
# Solution using List Comprehension

A = [[1,2,3],
    [4,5,6]]

T = [[A[j][i] for j in range (len(A))] for i in range (len(A[0]))]

for i in T:
    print(i)
