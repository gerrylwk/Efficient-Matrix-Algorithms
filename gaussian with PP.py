import numpy as np

def gaussPP(A,b,scaled='pp'):                   #Ax = b
    n = len(A)
    if scaled == 'spp':                         #Setting s[k] values, which are the largest elements of
        s = np.zeros(n)                         #each row
        for k in range(0,n):
            s[k] = abs(A[k][0])
            for j in range(1,n):
                if abs(A[k][j]) > s[k]:
                    s[k] = abs(A[k][j])
            if s[k] == 0:
                print("Matrix is singular")
    elif scaled != 'pp':
        print('Argument for scaled is only either \'spp\' or \'pp\'.')

    r = np.arange(n)                                #Row Labels
    if scaled == 'spp':                             #Pivoting based on spp
        for i in range(0,n-1):
            j = i
            max = abs(A[r[j]][i]) / s[r[j]]
            for k in range(i+1,n):
                l = abs(A[r[k]][i]) / s[r[k]]
                if l > max:
                    j = k
                    max = l
            if A[r[j]][i] == 0:
                print('Matrix is singular')
            elif j != i:
                r[i],r[j] = r[j],r[i]
            for j in range(i+1,n):                  #Elimination
                m = A[r[j]][i] / A[r[i]][i]
                for k in range(i+1,n):
                    A[r[j]][k] -= m * A[r[i]][k]
                b[r[j]] -= m * b[r[i]]

    else:                                           #Pivoting based on pp
        for i in range(0, n - 1):
            j = i
            for k in range(i+1,n):
                if abs(A[r[k]][i]) > abs(A[r[j]][i]):
                    j = k
            if A[r[j]][i] == 0:
                print("Matrix is singular")
            elif j != i:
                r[i],r[j] = r[j],r[i]
            for j in range(i + 1, n):                #Elimination
                m = A[r[j]][i] / A[r[i]][i]
                for k in range(i + 1, n):
                    A[r[j]][k] -= m * A[r[i]][k]
                b[r[j]] -= m * b[r[i]]

    x = np.zeros(n)                                   #Backward Substitution
    for i in range(n-1,-1,-1):
        x[i] = b[r[i]]
        for j in range(i+1,n):
            x[i] -= A[r[i]][j] * x[j]
        x[i] /= A[r[i]][i]
        x[i] = round(x[i],7)                           #Rounding based on 7 decimal places

    print(x)
    return(x)


Atest = np.array([[2,-3,2],[-4,2,-6],[2,2,1]],dtype = float)      #Add dtype = float to prevent rounding operations
btest = np.array([-4,4,8],dtype=float)
gaussPP(Atest,btest,'pp')



