import numpy as np
def augGauss(mat):                     #Gaussian for general matrix
    n = len(mat)
    for i in range(0,n-1):
        for j in range(i+1,n):
            m = mat[j][i]/mat[i][i]
            for k in range(i+1,n+1):
                mat[j][k] -= m*mat[i][k]

    x = np.zeros(n)                     #General backward substitution
    x[n-1] = mat[n-1][n]/mat[n-1][n-1]
    for i in range(n-1,-1,-1):
        x[i] = mat[i][n]
        for j in range(i+1,n):
            x[i] -= mat[i][j]*x[j]

        x[i] = x[i]/mat[i][i]
        x[i] = round(x[i],7)
    print(x)
    return(x)


matA = np.array([[1,2,3,0],[3,4,7,2],[6,5,9,11]],dtype=float)         #example input
augGauss(matA)                    #4,1,-2


