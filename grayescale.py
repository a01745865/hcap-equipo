#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:57:37 2020

@author: fergarcia
"""

import cv2
import numpy as np

def escala(M):
    matriz_zeros = np.zeros((M.shape[0], M.shape[1]))
    for i in range(len(M)):
        suma = 0
        for a in range(len(M[i])):
            for b in M[i][a]:
                suma += b
            promedio = suma/len(M[i][a])
            matriz_zeros[i][a] = promedio 
    return matriz_zeros

imagen = cv2.imread("imagen.jpg")
print(imagen.shape)
print(imagen[0][0])


image_gray = escala(imagen)
cv2.imwrite("GrayScale.jpg", image_gray)
print(image_gray.shape)