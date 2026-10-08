import numpy as np

# ==============================================================================
# 1. INITIALIZATION & RESHAPING
# ==============================================================================
raw_vector = np.arange(12)
matrix_2d = raw_vector.reshape(3, 4)
flattened_vector = matrix_2d.ravel()

# ==============================================================================
# 2. SLICING & ARRAY MANIPULATION
# ==============================================================================
sub_matrix = matrix_2d[:, 1:3]

expanded_tensor = np.expand_dims(sub_matrix, axis=0)
squeezed_matrix = np.squeeze(expanded_tensor, axis=0)

horizontal_stacked = np.hstack((sub_matrix, sub_matrix))
vertical_stacked = np.vstack((sub_matrix, sub_matrix))
concatenated_array = np.concatenate((sub_matrix, sub_matrix), axis=1)

# ==============================================================================
# 3. CONDITIONALS & FILTERING
# ==============================================================================
mask = matrix_2d > 5
filtered_values = matrix_2d[mask]

binary_thresholded = np.where(matrix_2d >= 6, 255, 0)
clipped_matrix = np.clip(matrix_2d, a_min=3, a_max=8)

# ==============================================================================
# 4. REDUCTION & STATISTICS BY AXIS
# ==============================================================================
data_matrix = np.array([[10, 20, 5], 
                        [30,  2, 40]])

column_sum = np.sum(data_matrix, axis=0, keepdims=True)
row_mean = np.mean(data_matrix, axis=1, keepdims=True)

min_val = np.min(data_matrix)
min_idx_flattened = np.argmin(data_matrix)
max_idx_per_column = np.argmax(data_matrix, axis=0)

# ==============================================================================
# 5. LINEAR ALGEBRA & EINSUM
# ==============================================================================
matrix_a = np.array([[1.0, 2.0], 
                     [3.0, 4.0]])
matrix_b = np.array([[5.0, 6.0], 
                     [7.0, 8.0]])

matrix_product = matrix_a @ matrix_b.T

vector_u = np.array([3.0, 4.0])
vector_norm = np.linalg.norm(vector_u)
normalized_u = vector_u / vector_norm

dot_product = np.einsum('i,i->', vector_u, vector_u)
batch_mat_mul = np.einsum('bij,bjk->bik', 
                          np.random.randn(8, 4, 3), 
                          np.random.randn(8, 3, 5))