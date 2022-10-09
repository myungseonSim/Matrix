import numpy as np
import Matrix

col = 0
row = 0
count = 0
print(Matrix.A)
print(Matrix.B)

while col != Matrix.MATRIX_SIZE:
    n = Matrix.MATRIX_SIZE
    Matrix.C = [[0]*n for _ in range(n)]
    for col in range(n):
        for row in range(n):
            for k in range(n):
                Matrix.C[col][row] += Matrix.A[col][k] * Matrix.B[k][row]
                

    row += 1
    if row == Matrix.MATRIX_SIZE:           
        col += 1
        row -= 1 
print(Matrix.C)
