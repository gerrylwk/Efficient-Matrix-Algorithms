import numpy as np
def LUtridiag(A):                               #O(n) time complexity
    n = len(A)
    for i in range(0,n-1):
        A[i+1][i] /= A[i][i]
        A[i+1][i+1] -= A[i+1][i] * A[i][i+1]

    print(A)
    return(A)

matA = [[1,2,0],[3,4,7],[0,5,9]]         #example input
LUtridiag(matA)

#Example output:  matA = [[1, 2,  0],               [[1,0, 0],       [[1,  2,  0],
#                        [3, -2, -2],    represents [3 ,1, 0],    *   [0, -2,  7],
#                        [0,-2.5, 4]]               [0,-2.5,1]]       [0,  0,26.5]]
# With LU = matA, L would be the unit lower triangular matrix(numbers below diagonal, and diagonal values)
# are supposed to be 1), and U would be the upper triangular matrix, which includes the diagonal values.
