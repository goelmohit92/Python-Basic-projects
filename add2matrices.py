A = [[1,5,8],
    [4,6,7],
    [7,2,3]]

B = [[4,5,6],
    [8,9,1],
    [3,5,6]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

for r in result:
    print(r)