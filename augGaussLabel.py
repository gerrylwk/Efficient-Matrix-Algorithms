import numpy as np
def augGaussLabel(A):               #Gaussian with row labels, to prevent
    n = len(A)                      #unnecessary changes in entries with zero pivot elements
    r = np.arange(n)
    for i in range(0,n-1):
        j = i
        while j <= n-1 and A[r[j]][i] == 0:
            j += 1
        if j == n:
            print("Error. Matrix is singular.")
        elif j != i:
            r[i] = r[j], r[j] = r[i]
        for j in range(i+1,n):
            m = A[r[j]][i]/A[r[i]][i]
            for k in range(i+1,n+1):
                A[r[j]][k] -= m*A[r[i]][k]

    x = np.zeros(n)                   # General backward substitution
    x[n - 1] = A[r[n - 1]][n] / A[r[n - 1]][n - 1]
    for i in range(n - 1, -1, -1):
        x[i] = A[r[i]][n]
        for j in range(i + 1, n):
            x[i] -= A[r[i]][j] * x[j]

        x[i] = x[i] / A[r[i]][i]
    print(x)
    return(x)


A = [[1,2,3,0],[3,4,7,2],[6,5,9,11]]         #example input
augGaussLabel(A)                    #4,1,-2