import numpy as np

#===========================1. INTRODUCTION ================================
array_a = np.array([1, 2, 3])
print(array_a.shape)


def multiply2(number:int):
    return number ** 2


# Vectorizes a scalar function for array inputs
multiply2_np = np.vectorize(multiply2)
array_b = np.array([1, 3, 4, 6])
print(multiply2_np(array_b))
# same
# array_b = array_b * 2

#============================2. COMMON FUNCTION ================================
#1.Creath a array faster:
# zeros() : create a ndarray or tensor with data full of 0, argument is a shape
#Example : shape is 4 row with 5 column , 2 dimension
data = np.zeros((4,5))
#like zeros(), ones(): data full of 1, full(): full(shape,9) : n dimension full data is 9
# arrange() : like range (list)
# random() : random data 
# np.eye(N): Creates an N x N identity matrix (1s on the main diagonal, 0s elsewhere)
# Use case: np.eye(num_classes)[labels] enables fast one-hot encoding via Fancy Indexing
identity_matrix = np.eye(4)
print(identity_matrix)

#2 Reshape:
# Note :reshape(-1, cols): -1 lets NumPy infer the dimension size automatically
# Rule: total elements must be divisible by other dimensions; only one -1 is allowed
array_c = np.arange(12)
reshape_array = np.reshape(array_c,(3,4))
print(f"Reshape array:{reshape_array}")
## arr.flatten(): Flattens multi-dimensional array into 1D (used before feeding into Dense layers)

# np.repeat(arr, repeats, axis): Duplicates each element consecutively
# Example: [1, 2] with repeats=3 -> [1, 1, 1, 2, 2, 2]
repeated_arr = np.repeat(np.array([1, 2]), 3)


#============================3. Indexing and broadcasting ================================
#1.slicing
array_d = np.arange(9).reshape(3,3)
print(f"Before slicing: {array_d}")
print(f"After slicing: {array_d[2,1:]}")

#2.indexing
A = np.array(
[[ 10,  15,  20,  25 ],
 [ 30,  35,  40,  45 ],
 [ 50,  55,  60,  65 ],
 [ 70,  75,  80,  85 ]]
 )
# Fancy Indexing (Integer Array Indexing):
# List 1: row indices [0, 1, 3]
# List 2: corresponding column indices [1, 3, 0]
# NumPy pairs them element-wise: (0,1) -> 15, (1,3) -> 45, (3,0) -> 70
# Returns a new 1D array (a deep copy, not a view): [15 45 70]
print(A[[0,1,3],[1,3,0]])

B = np.array([
    [10, 45, 80, 25],
    [95, 30, 60, 110],
    [15, 75, 50, 100]
])
print("Original array B:")
print(B)

# Create a boolean mask: condition evaluated element-wise (returns True/False)
bool_matrix = B >= 60
print("\nBoolean mask (B >= 60):")
print(bool_matrix)

# Apply boolean mask indexing to extract elements satisfying the condition
# Note: Boolean indexing always returns a 1D array as a deep copy (not a view)
result = B[bool_matrix]
print("\nFiltered result:")
print(result)

#2. Summation
C = np.arange(4).reshape(2,2)
print(C.sum(axis = 1))