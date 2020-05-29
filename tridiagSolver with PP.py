import numpy as np

def tridiagSolver(A,b,scaled='pp'):
    n = len(A)
    if scaled == 'spp':
        s = np.zeros(n)
        s[0] = max(abs(A[0][0]),abs(A[0][1]))
        for k in range(1,n-1):
            s[k] = max(abs(A[k][k-1]),abs(A[k][k]),abs(A[k][k+1]))
        s[n-1] = max(abs(A[n-1][n-2]),abs(A[n-1][n-1]))
    elif scaled != 'pp':
        print('Argument for scaled is only either \'spp\' or \'pp\'.')

    r = np.arange(n)

    if scaled == 'spp':
        for i in range(0,n-1):
            if abs(A[r[i]][i]) / s[r[i]] < abs(A[r[i+1]][i]) / s[r[i+1]]:
                r[i],r[i+1] = r[i+1],r[i]
                m = A[r[i+1]][i] / A[r[i]][i]
                if i < n-2:
                    A[r[i+1]][i+2] = -m * A[r[i]][i+2]
            else:
                m = A[r[i+1]][i] / A[r[i]][i]

            A[r[i+1]][i+1] -= m * A[r[i]][i+1]
            b[r[i+1]] -= m * b[r[i]]
    elif scaled == 'pp':
        for i in range(0, n - 1):
            if abs(A[r[i]][i]) < abs(A[r[i + 1]][i]):
                r[i], r[i + 1] = r[i + 1], r[i]
                m = A[r[i + 1]][i] / A[r[i]][i]
                if i < n - 2:
                    A[r[i+1]][i+2] = -m * A[r[i]][i+2]
            else:
                m = A[r[i + 1]][i] / A[r[i]][i]
            A[r[i + 1]][i + 1] -= m * A[r[i]][i + 1]
            b[r[i + 1]] -= m * b[r[i]]

    x = np.zeros(n)
    x[n-1] = b[r[n-1]] / A[r[n-1]][n-1]
    x[n-2] = (b[r[n-2]] - A[r[n-2]][n-1] * x[n-1]) / A[r[n-2]][n-2]

    for i in range(n-3,-1,-1):
        if r[i] == i+1:
            x[i] = (b[r[i]] - A[r[i]][i+1] * x[i+1] - A[r[i]][i+2] * x[i+2]) / A[r[i]][i]
        else:
            x[i] = (b[r[i]] - A[r[i]][i+1] * x[i+1]) / A[r[i]][i]

        x[i] = round(x[i], 7)               #Rounding based on 7 decimal places

    print(x)
    return(x)



Atest = np.array([[1,2,0],[3,-2,3],[0,1,4]],dtype = float)      #Add dtype = float to prevent rounding operations
btest = np.array([5,8,14],dtype=float)
tridiagSolver(Atest,btest,'pp')               #x=[1,2,3]

Atest = np.array([[1,2,0,0],[2,3,5,0],[0,1,-2,1],[0,0,3,6]],dtype = float)      #Add dtype = float to prevent rounding operations
btest = np.array([5,23,0,33],dtype=float)
tridiagSolver(Atest,btest,'spp')               #x=[1,2,3,4]