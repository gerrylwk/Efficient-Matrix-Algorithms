import numpy as np
def LUlowerhess(A):
    n = len(A)
    for i in range(0,n-1):
        for j in range(i+1,n):
            A[j][i] = A[j][i] / A[i][i]
            A[j][i+1] -= A[j][i] * A[i][i+1]

    print(A)
    return(A)

matA = [[1,2,0],[3,4,7],[6,5,9]]         #example input
LUlowerhess(matA)

#Example output:  matA = [[1, 2,  0],               [[1,0,0],       [[1,  2,  0],
#                        [3, -2,  7],    represents  [3,1,0],    *   [0,  -2, 7],
#                        [6,3.5,-15.5]]              [6,3.5,1]]      [0,0,-15.5]]
# With LU = matA, L would be the unit lower triangular matrix(numbers below diagonal, and diagonal values)
# are supposed to be 1), and U would be the upper triangular matrix, which includes the diagonal values.
