import numpy as np

def MatrixMultiplier(matrix1, matrix2):
    n = len(matrix1)
    returnmatrix = np.zeros((n,n))
    m = n // 2
    if n == 1:
        returnmatrix[0][0] = matrix1[0][0] * matrix2[0][0]
    else:
        returnmatrix[:m, :m] = MatrixMultiplier(matrix1[:m, :m], matrix2[:m, :m]) + MatrixMultiplier(matrix1[:m, m:], matrix2[m:, :m])
        returnmatrix[:m, m:] = MatrixMultiplier(matrix1[:m, :m], matrix2[:m, m:]) + MatrixMultiplier(matrix1[:m, m:], matrix2[m:, m:])
        returnmatrix[m:, :m] = MatrixMultiplier(matrix1[m:, :m], matrix2[:m, :m]) + MatrixMultiplier(matrix1[m:, m:], matrix2[m:, :m])
        returnmatrix[m:, m:] = MatrixMultiplier(matrix1[m:, :m], matrix2[:m, m:]) + MatrixMultiplier(matrix1[m:, m:], matrix2[m:, m:])
    return returnmatrix