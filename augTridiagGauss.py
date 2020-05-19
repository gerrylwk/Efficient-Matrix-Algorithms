import numpy as np
def augTridiagGauss(A):
    n = len(A)
    r = np.arange(n)
    for i in range(0,n-1):
        j = i
        while j <= n-1 and A[r[j]][i] == 0:
            j += 1
        if j == n+1:
            print("Error. Matrix is singular.")
        elif j != i:
            r[i] = r[j], r[j] = r[i]
    for i in range(0,n-1):
        m = A[r[i+1]][i] / A[r[i]][i]
        A[r[i+1]][i+1] -= m * A[r[i]][i+1]
        A[r[i+1]][n] -= m * A[r[i]][n]

    x = np.zeros(n)
    x[n-1] = A[r[n-1]][n] / A[r[n-1]][n-1]
    for k in range(n-2,-1,-1):
        x[k] = ( A[r[k]][n] - A[r[k]][k+1]*x[k+1] )/ A[r[k]][k]

    print(x)
    return(x)

atest = [[2,3,0,0,21],[6,3,9,0,69],[0,2,5,2,34],[0,0,4,3,22]]
augTridiagGauss(atest)      #x = 3,5,4,2
