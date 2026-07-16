A = [
    [10, 12],
    [39, 40]
]


B = [
    [51, 68],
    [73, 88]
]


product = [
    [0, 0],
    [0, 0]
]


for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            product[i][j]+=A[i][k] * B[k][j]
           


for row in product:
    print(row)