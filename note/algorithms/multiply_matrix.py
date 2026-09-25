import numpy as np


def multiply_matrix(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
    row_a, col_a = len(matrix_a), len(matrix_a[0])
    row_b, col_b = len(matrix_b), len(matrix_b[0])

    if col_a != row_b:
        raise ValueError("The column of matrix A must equal the row of matrix B")

    result = [[0] * col_b for _ in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(row_b):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return np.array(result)


matrix_a = np.array([[2, 1], [0, 3], [4, 5]])

matrix_b = np.array([[1, 2, 0, -1], [3, 1, 4, 2]])

print(multiply_matrix(matrix_a,matrix_b))