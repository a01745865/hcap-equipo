#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:45:35 2020

@author: fergarcia
"""

import numpy as np

def padding(A):
    A = A.tolist()
    D = []
    for i in A:
        D.append([0]+i+[0])
    ceros = [0]*(len(A[0])+2)
    return np.array([ceros]+D+[ceros])
