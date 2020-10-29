#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:57:37 2020

@author: fergarcia
"""

import cv2

def escala(M):
    copia = []
    for i in range(len(M)):
        suma = 0
        for a in range(len(M[i])):
            for b in M[i][a]:
                suma += b
            promedio = suma/len(M[i][a])
            copia.append(promedio)
    return copia

imagen = cv2.imread("imagen.jpg")
print(imagen.shape)
print(imagen[0][0])

Matriz = [[[1,2,3]],[[4,6,10]],[[10,15,5]]]

print(escala(Matriz))

image_gray = escala(imagen)

print(image_gray.shape)