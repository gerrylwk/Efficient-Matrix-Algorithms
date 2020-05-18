import numpy as np
def LUupperhess(A):
    n = len(A)
    for i in range(0,n-1):
        A[i+1][i] = A[i+1][i] / A[i][i]
        for j in range(i+1,n):
            A[i+1][j] = A[i+1][j] - A[i+1][i] * A[i][j]


    print(A)

matA = [[1,2,3],[3,4,7],[0,5,9]]         #example input
LUupperhess(matA)

#Example output:  matA = [[1, 2,  3],               [[1,0, 0],       [[1,  2,  3],
#                        [3, -2, -2],    represents [3 ,1, 0],    *   [0, -2, -2],
#                        [0,-2.5, 4]]               [0,-2.5,1]]       [0,  0,  4]]
# With LU = matA, L would be the unit lower triangular matrix(numbers below diagonal, and diagonal values)
# are supposed to be 1), and U would be the upper triangular matrix, which includes the diagonal values.