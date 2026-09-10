import numpy as np

def matrix_multiply(A,B):
  A_row , A_column = len(A),len(A[0])
  B_row , B_column = len(B),len(B[0])

  if A_column != B_row:
    raise ValueError("Oi doi oi loi roi")
  
  result_matrix = [[0 for _ in range(B_column)] for _ in range(A_row)]

  for i in range(A_row):
    for j in range(B_column):
      for k in range(A_column):
        result_matrix[i][j] += A[i][k] * B[k][j]
  return result_matrix

A1 = [1,2,3]
A2 = [4,5,6]
A=[A1,A2]

B1 = [7,10]
B2 = [8,11]
B3 = [9,12]
B=[B1,B2,B3]

print(matrix_multiply(A,B))

# using numpy array
A_array = np.array([
  [1,2,3],
  [4,5,6]
])
B_array = np.array([
  [7,10],
  [8,11],
  [9,12]
])

result = np.dot(A_array,B_array)
# also can use  @ operator

print(result)