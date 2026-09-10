import numpy as np

# =====================================================================
# 1. ENVIRONMENT & VERSION CHECK
# =====================================================================
print(f"NumPy Version: {np.__version__}\n")


# =====================================================================
# 2. N-DIMENSIONAL ARRAY DEFINITION & ACCESS
# =====================================================================
# Note: Initial array is already 3D, so ndmin=3 keeps it as a 3D array.
arr_3d = np.array(
    [[[1, 2, 3, 4, 6], [1, 2, 3, 4, 6]], [[1, 2, 3, 4, 6], [1, 2, 3, 4, 6]]],
    ndmin=3,
    dtype="i",
)
print("--- 3D Array Initialization ---")
print(arr_3d)
print(f"Dimensions (ndim): {arr_3d.ndim}")
print(f"Accessed Element at [0, 1, 4]: {arr_3d[0, 1, 4]}\n")


# =====================================================================
# 3. ARRAY SLICING (2D ARRAY)
# =====================================================================
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("--- 2D Array Slicing ---")
print(f"Slice 1 (Row 1, Cols 1-2): {arr_2d[1, 1:3]}")  # Output: [5, 6]
print(f"Slice 2 (Rows 0-1, Col 1): {arr_2d[0:2, 1]}")  # Output: [2, 5]
print("Slice 3 (Rows 0-1, Cols 1-2):")
print(arr_2d[0:2, 1:3])  # Output: 2D array [[2, 3], [5, 6]]
print(f"Original Data Type: {arr_2d.dtype}\n")


# =====================================================================
# 4. DATA TYPE CONVERSION (ASTYPE)
# =====================================================================
print("--- Data Type Conversion (astype) ---")
# Convert the integer array to float type ('f')
float_arr = arr_2d.astype("f")
print("Converted Float Array:")
print(float_arr)
print(f"New Data Type: {float_arr.dtype}\n")

# Practical Example: Convert numbers to boolean (0 -> False, non-zero -> True)
binary_arr = np.array([0, 1, -2])
bool_arr = binary_arr.astype(bool)
print(f"Original Array: {binary_arr}")
print(f"Converted Boolean Array: {bool_arr}\n")


# =====================================================================
# 5. MEMORY MANAGEMENT: COPY VS VIEW
# =====================================================================
print("--- Memory Management: Copy vs View ---")
original = np.array([10, 20, 30, 40])
print(f"Original Array: {original}\n")

# Case 1: Test Copy (Independent allocation)
independent_copy = original.copy()
independent_copy[0] = 99
print("--- After Modifying Copy ---")
print(f"Original Array : {original}")          # Unchanged: [10, 20, 30, 40]
print(f"Copy Array     : {independent_copy}")   # Modified:  [99, 20, 30, 40]
print(f"Copy base check: {independent_copy.base}\n")  # Returns None (Owns data)

# Case 2: Test View (Shared memory allocation)
shared_view = original.view()
shared_view[1] = 88
print("--- After Modifying View ---")
print(f"Original Array : {original}")     # Modified: [10, 88, 30, 40]
print(f"View Array     : {shared_view}")   # Modified: [10, 88, 30, 40]
print(f"View base check: {shared_view.base}")  # Returns original array object