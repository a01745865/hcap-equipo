import numpy as np
def padding(A):
    D = []
    for i in A:
        D.append([0]+i+[0])
    ceros = [0]*(len(A[0])+2)
    return [ceros]+D+[ceros]

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

matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro = [[1,0,2],[5,0,9],[6,2,1]]

A = np.array(matriz1)
B = np.array(filtro)
C = convolucion(A,B)

print(C)

matriz2 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
filtro2 = [[1,1,1],[0,0,0],[2,10,3]]
matriz2 = padding(matriz2)
print(matriz2)
A = np.array(matriz2)
B=np.array(filtro2)
C = convolucion(A,B)
print(C)

