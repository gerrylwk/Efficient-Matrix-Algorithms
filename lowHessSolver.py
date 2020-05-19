import numpy as np

def lowHessSolver(A,b):                     #Ax = b
    n = len(A)
    r = np.arange(n)
    for i in range(n-1,0,-1):                #Backward Elimination, O(n)
        if A[r[i]][i] != 0:
            m = A[r[i-1]][i] / A[r[i]][i]
            for k in range(0,i):
                A[r[i-1]][k] -= m * A[r[i]][k]
            b[r[i-1]] -= m * b[r[i]]
        else:
            r[i] = r[i-1], r[i-1] = r[i]

    x = np.zeros(n)
    x[0] = b[r[0]] / A[r[0]][0]
    for i in range(1,n):                      #Forward Substitution, O(n)
        x[i] = b[r[i]]
        for j in range(0,i):
            x[i] -= A[r[i]][j] * x[j]
        x[i] /= A[r[i]][i]
    print(x)
    return(x)

Atest = np.array([[1,2,0],[2,3,5],[4,1,1]])
btest = np.array([5,23,9])
#Result is x = [1,2,3]
#Example below
lowHessSolver(Atest,btest)
