#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:58:01 2022

@author: imao
"""

class Jacobi():

    def calculation(self):

        coefficient_matrix = [[7,-2,1],[-1,5,-2],[-2,-1,6]]
        y = [6,3,14]
        convergence_value = 10 ** -6
        length = len(y)
        x = [0] * length
        x2 = [0] * length
        counter = 1;

        while True:

            for i in range(length):

                x2[i] = (y[i] - coefficient_matrix[i][(i+1)%length]*x[(i+1)%length] - coefficient_matrix[i][(i+2)%length]*x[(i+2)%length]) / coefficient_matrix[i][i]

            judge_counter = 0;
            for i in range(length):
                if abs(x2[i] - x[i]) < convergence_value:
                    judge_counter = judge_counter + 1
            if length == judge_counter:
                break

            print("k=" + str(counter) )
            counter = counter + 1

            for i in range(length):
                print(x2[i])

            for i in range(length):
                x[i] = x2[i]


if __name__ == "__main__":
    instance = Jacobi()
    instance.calculation()