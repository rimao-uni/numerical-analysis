#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:07:58 2022

LU分解による連立方程式の解
@author: imao
"""

import numpy as np
from scipy.linalg import lu

A = np.array([[-2,1,0,0,0,0,0,0,0,0],
              [1,-2,1,0,0,0,0,0,0,0], 
              [0,1,-2,1,0,0,0,0,0,0], 
              [0,0,1,-2,1,0,0,0,0,0],
              [0,0,0,1,-2,1,0,0,0,0],
              [0,0,0,0,1,-2,1,0,0,0],
              [0,0,0,0,0,1,-2,1,0,0],
              [0,0,0,0,0,0,1,-2,1,0],
              [0,0,0,0,0,0,0,1,-2,1],
              [0,0,0,0,0,0,0,0,1,-2]])
P, L, U = lu(A)
np.set_printoptions(formatter={'float': '{:.5f}'.format})

def gaussian_elimination(A, b):
    try:
        n = len(b)
        
        for i in range(n):
           
            order = np.argmax(np.abs(A[i:, i]))  
            temp_A = A[i + order].copy()         
            temp_b = b[i + order].copy()         
            A[i + order] = A[i]                  
            A[i] = temp_A                        
            b[i + order] = b[i]                  
            b[i] = temp_b                        
            
            pivot = A[i, i]                     

            if np.abs(pivot) < 1e-19:
                print('pivot=', pivot)
                raise ZeroDivisionError
 
            A[i] = A[i] / pivot              
            b[i] = b[i] / pivot               
            for j in range(i+1, n):
                p = A[j, i]                      
                A[j] -= p * A[i]                
                b[j] -= p * b[i]             

        x = np.zeros(n)                         
        for i in reversed(range(n)):          
            x[i] = b[i] / A[i, i]               
            for j in range(i):
                b[j] -= A[j, i] * x[i]    
        print('Normal termination')
    except:
        print('Error termination : pivot too small.')
        x = np.nan
    return x
 
b = np.array([0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50], dtype=float)
 
x = gaussian_elimination(L, b)
print(x)
y = gaussian_elimination(U, x)
print(y)

