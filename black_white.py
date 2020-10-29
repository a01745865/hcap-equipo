#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:44:34 2020

@author: fergarcia
"""
def black_white(M, valor):
    matriz_zeros = np.zeros((M.shape[0], M.shape[1]))
    for i in range(len(M)):
        for a in range(len(M[i])):
            if M[i][a] < valor:
                matriz_zeros[i][a] = 0
            elif M[i][a] >= valor:
                matriz_zeros[i][a] = 255
    return matriz_zeros
