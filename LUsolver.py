import numpy as np
from LUgauss import LUgauss
def LUsolver(lu, b):                   # lu = b, where lu is a matrix consisting of both
    n = len(lu)                        # lower and upper entries stored in 1 matrix.
    for i in range(1,n):
        for j in range(0,i):
            b[i] -= lu[i][j] * b[j]

    x = np.zeros(n)
    x[n-1] = b[n-1] / lu[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = b[i]
        for j in range(i+1,n):
            x[i] -= lu[i][j] * x[j]
        x[i] /= lu[i][i]
    print(x)
    return(x)


Atest = np.array([[1,2,0],[2,3,5],[4,1,1]])
btest = np.array([5,23,9])
lutest = LUgauss(Atest)            #This function converts matrix Atest into LU form
LUsolver(lutest,btest)             #This function prints out the values of x, i.e. = [1,2,3]
