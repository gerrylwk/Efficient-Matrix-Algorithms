import numpy as np

def upperPP(A,b,scaled='pp'):
    n = len(A)
    if scaled == 'spp':                     #Check largest element of each row
        s = np.zeros(n)
        for k in range(0,n):
            j = max(0,k-1)
            s[k] = abs(A[k][j])
            for j in range(max(1,k),n):
                if s[k] < abs(A[k][j]):
                    s[k] = abs(A[k][j])
            if s[k] == 0:
                print("Matrix is singular")
    elif scaled != 'pp':
        print('Argument for scaled is only either \'spp\' or \'pp\'.')

    r = np.arange(n)
    if scaled == 'spp':
        for i in range(0,n-1):
            if abs(A[r[i]][i]) / s[r[i]] < abs(A[r[i+1]][i]) / s[r[i+1]]:
                r[i],r[i+1] = r[i+1],r[i]
            m = A[r[i+1]][i] / A[r[i]][i]
            for k in range(i+1,n):
                A[r[i+1]][k] -= m * A[r[i]][k]
            b[r[i+1]] -= m * b[r[i]]

    else:
        for i in range(0,n-1):
            if abs(A[r[i]][i]) < abs(A[r[i+1]][i]):
                r[i],r[i+1] = r[i+1],r[i]
            m = A[r[i+1]][i] / A[r[i]][i]
            for k in range(i+1,n):
                A[r[i+1]][k] -= m * A[r[i]][k]
            b[r[i+1]] -= m * b[r[i]]

    x = np.zeros(n)
    x[n-1] = b[r[n-1]] / A[r[n-1]][n-1]

    for i in range(n - 2, -1, -1):
        x[i] = b[r[i]]
        for j in range(i + 1, n):
            x[i] -= A[r[i]][j] * x[j]
        x[i] /= A[r[i]][i]
        x[i] = round(x[i], 7)  # Rounding based on 7 decimal places

    print(x)
    return(x)

Atest = np.array([[3,2,2],[2,5,1],[0,1,2]],dtype = float)      #Add dtype = float to prevent rounding operations
btest = np.array([13,15,8],dtype=float)
upperPP(Atest,btest,'spp')   #x = [1,2,3]

