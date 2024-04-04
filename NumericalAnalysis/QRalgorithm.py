#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:10:45 2022

@author: imao
QR分解とグラムシュミットの直行化によってn*n行列の固有値を求めます。
numpy, math 使わない縛り
"""

import random

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    @classmethod
    def random_matrix(cls, n):
        return cls([[random.randint(0, 2) for _ in range(n)] for _ in range(n)])

    def inner_product(self, v1, v2):
        return sum(c1 * c2 for c1, c2 in zip(v1, v2))

    def norm(self, v):
        return sum(c ** 2 for c in v) ** 0.5

    def vector_add(self, v1, v2):
        return [c1 + c2 for c1, c2 in zip(v1, v2)]

    def vector_sub(self, v1, v2):
        return [c1 - c2 for c1, c2 in zip(v1, v2)]

    def scalar_multiplication(self, vec, scalar):
        return [scalar * c for c in vec]

    def unit_vector(self, vec):
        return self.scalar_multiplication(vec, 1 / self.norm(vec))

    def gram_schmidt(self):
        result_list = []
        for index, vector in enumerate(self.matrix):
            if index == 0:
                result = self.unit_vector(vector)
            else:
                for i in range(index):
                    unit_vector = result_list[i]
                    projection_vector = self.scalar_multiplication(unit_vector, self.inner_product(vector, unit_vector))
                    vector = self.vector_sub(vector, projection_vector)
                result = self.unit_vector(vector)
            result_list.append(result)
        return result_list

    def matrix_product(self, A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(len(A))) for j in range(len(B[0]))] for i in range(len(A))]

    def transpose(self, mat):
        return [[row[i] for row in mat] for i in range(len(mat[0]))]

    def qr_method(self, iterations=500):
        A = self.matrix
        for _ in range(iterations):
            Q = self.gram_schmidt()
            R = self.matrix_product(Q, self.transpose(A))
            A = self.matrix_product(R, self.transpose(Q))
            A = self.transpose(A)
        return A

    def round_matrix(self, matrix, n):
        return [[round(element, n) for element in row] for row in matrix]

    def extract_diagonal(self, matrix):
        return [matrix[i][i] for i in range(len(matrix))]


# テスト用のn×n行列生成
n = 100
matrix_ops = MatrixOperations.random_matrix(n)

# QR法で固有値を計算
eigenvalues = matrix_ops.qr_method()

eigenvalues_rounded = matrix_ops.round_matrix(eigenvalues, 10)
print(*eigenvalues_rounded, sep='\n')

diagonal_values = matrix_ops.extract_diagonal(eigenvalues_rounded)
for value in diagonal_values:
    print(value)
