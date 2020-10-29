#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:57:37 2020

@author: fergarcia
"""

import cv2
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


def escala(M):
    matriz_zeros = np.zeros((M.shape[0], M.shape[1]))
    for i in range(len(M)):
        for a in range(len(M[i])):
            suma = 0
            for b in M[i][a]:
                suma += b
            promedio = suma/len(M[i][a])
            matriz_zeros[i][a] = promedio 
    return matriz_zeros

def black_white(M, valor):
    matriz_zeros = np.zeros((M.shape[0], M.shape[1]))
    for i in range(len(M)):
        for a in range(len(M[i])):
            if M[i][a] < valor:
                matriz_zeros[i][a] = 0
            elif M[i][a] >= valor:
                matriz_zeros[i][a] = 255
    return matriz_zeros

Filtro = [[3,4,2],[1,0,2],[2,3,1]]
imagen = cv2.imread("imagen.jpg")
imagen_gray = escala(imagen)
cv2.imwrite("GrayScale.jpg", imagen_gray)
valor = 127
imagen_black_white = black_white(imagen_gray, valor)
cv2.imwrite("Blak&White.jpg", imagen_black_white)

convolucion_sin = convolucion(imagen_gray, Filtro)
