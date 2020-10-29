import numpy as np

def convolucion(A,B):
    C=np.zeros((len(A)-2,len(A[0])-2))
    for i1 in range(len(C)):
        for j1 in range(len(C[0])):
            suma=0
            for i in range(len(B)):
                for j in range(len(B[0])):
                    suma+=A[i+i1][j+j1]*B[i][j]
            C[i1][j1]=suma
    return C



