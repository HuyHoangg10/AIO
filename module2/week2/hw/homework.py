import numpy as np 

def compute_vector_length(vector:np.ndarray):
    len_of_vector = np.sqrt(np.sum(vector ** 2))
    return len_of_vector

def compute_dot_product(vector1:np.ndarray,vector2:np.ndarray):
    result = np.sum(vector1 * vector2)
    return result

def matrix_multiply_vector(matrix:np.ndarray,vector:np.ndarray):
    result = []
    for i in range(matrix.shape[0]):
        result.append(np.sum(matrix[i]*vector))
    return np.array(result)

def inverse_matrix(matrix:np.ndarray):
    det = matrix[0,0]*matrix[1,1] - (matrix[0,1]*matrix[1,0])
    if(det == 0):
        return
    inv_matrix = np.zeros([matrix.shape[0],matrix.shape[1]])
    inv_matrix[0,0] = matrix[1,1]
    inv_matrix[0,1] = -matrix[0,1]
    inv_matrix[1,0] = -matrix[1,0]
    inv_matrix[1,1] = matrix[0,0]
    result = inv_matrix/det
    return result 

def compute_eigenvalue_eigenvector(matrix:np.ndarray):
    eigenvalues , eigenvector = np.linalg.eig(matrix)
    return eigenvalues,eigenvector

def cosine_similarity(v1,v2):
    cos_sim = compute_dot_product(v1,v2)/compute_vector_length(v1)*compute_vector_length(v2)
    return cos_sim