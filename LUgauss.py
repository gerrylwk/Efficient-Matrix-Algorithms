import numpy as np
def LUgauss(A):                             #Both L and U matrices stored together for efficient storage
    n = len(A)
    for i in range(0,n-1):
        for j in range(i+1,n):
            A[j][i] = A[j][i]/A[i][i]
            for k in range(i+1,n):
                A[j][k] -= A[j][i] * A[i][k]

    print(A)
    return(A)

matA = [[1,2,3],[3,4,7],[6,5,9]]         #example input
LUgauss(matA)

#Example output:  matA = [[1, 2,  3],               [[1,0,0],       [[1,2,3],
#                         [3,-2,,-2],    represents  [3,1,0],    *   [0,-2,-2],
#                         [6,3.5,-2]]                [6,3.5,1]]      [0,0,-2]]
# With LU = matA, L would be the unit lower triangular matrix(numbers below diagonal, and diagonal values)
# are supposed to be 1), and U would be the upper triangular matrix, which includes the diagonal values.
