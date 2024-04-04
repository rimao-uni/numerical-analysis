#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:05:02 2022

@author: imao
"""

class Gauss_Seidel():

    def calculation(self):

        coefficient_matrix = [[7,-2,1],[-1,5,-2],[-2,-1,6]]
        y =  [6,3,14]
        convergence_value = 10 ** -6
        length = len(y)
        x = [0] * length
        x_after = [0] * length
        counter = 1

        while True:

            for i in range(length):

                x_after[i] = x[i]
                x[i] = (y[i] - coefficient_matrix[i][(i+1)%length]*x[(i+1)%length] - coefficient_matrix[i][(i+2)%length]*x[(i+2)%length]) / coefficient_matrix[i][i]


            judge_counter = 0
            for i in range(length):
                if abs(x_after[i] - x[i]) < convergence_value:
                    judge_counter = judge_counter + 1
            if length == judge_counter:
                break

            print("k=" + str(counter))
            counter = counter + 1

            for i in range(length):
                print(abs(x[i]-(i+1)))


if __name__ == "__main__":
    GaussSeidel = Gauss_Seidel()
    GaussSeidel.calculation()