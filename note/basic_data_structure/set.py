# ==============================================================================
# 1. READ-ONLY METHODS (Các hàm giống hệt List/Tuple áp dụng cho Set)
# ==============================================================================
# Vì Set là Unordered (không thứ tự) và Unindexed (không chỉ số), nên tất cả các hàm
# liên quan đến Index (như .index()) KHÔNG TỒN TẠI trên Set.

# len()      -> Return the total number of elements in the set
# dir()      -> Built-in function to list all valid methods of the set object


# ==============================================================================
# 2. MUTABLE METHODS (Các hàm Thêm/Xóa phần tử đặc trưng của Set)
# ==============================================================================
myset = {"Bruno", "Harry"}

# .add()     -> Add an element to the set (If the item already exists, it has no effect)
myset.add("Cunha") 
myset.add("Bruno")  # Duplicate value -> Will be ignored automatically

# .remove()  -> Remove a specified value. Throws a KeyError if the item is not found.
# myset.remove("Harry")

# .discard() -> Better than .remove(). Removes a value but DOES NOT throw an error if missing.
myset.discard("Amad")  # "Amad" is not in myset, but code continues running safely

print(f"Base set after add/discard: {myset}")


# ==============================================================================
# 3. SET OPERATIONS - RETURN NEW SET (Các phép toán trả về Set mới tinh)
# ==============================================================================
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# Union (|) -> Keep ALL elements from both sets
union_set = set1.union(set2)          # Method way
union_operator = set1 | set2          # Operator way

# Intersection (&) -> Keep ONLY the duplicate elements present in both sets
inter_set = set1.intersection(set2)   # Method way -> Result: {'apple'}
inter_operator = set1 & set2          # Operator way

# Difference (-) -> Keep elements from the first set that are NOT in the second set
diff_set = set1.difference(set2)      # Method way -> Result: {'banana', 'cherry'}
diff_operator = set1 - set2           # Operator way

# Symmetric Difference (^) -> Keep all elements EXCEPT the duplicates
sym_set = set1.symmetric_difference(set2) # Method way -> Result: {'banana', 'cherry', 'google', 'microsoft'}
sym_operator = set1 ^ set2                # Operator way


# ==============================================================================
# 4. SET OPERATIONS - IN-PLACE UPDATE (Các hàm đè dữ liệu trực tiếp, KHÔNG trả về Set mới)
# ==============================================================================
# NOTE: All these methods mutate the original set directly and return None.
base_set = {"apple", "banana", "cherry"}
target_set = {"google", "microsoft", "apple"}

# .update()                   -> Insert all items from another set into the current set
base_set.update(target_set)

# .intersection_update()      -> Keep ONLY the duplicates right inside the original set
base_set.intersection_update(target_set)

# .difference_update()        -> Remove all matched elements of target_set from base_set
base_set.difference_update(target_set)

# .symmetric_difference_update() -> Keep all items EXCEPT duplicates right inside base_set
base_set.symmetric_difference_update(target_set)


# ==============================================================================
# 5. RELATIONSHIP TESTS (Các hàm kiểm tra quan hệ giữa các tập hợp)
# ==============================================================================
# These methods return a Boolean value (True or False)
parent_set = {"Admin", "Manager", "Developer"}
child_set = {"Admin", "Manager"}
other_set = {"Tester", "Designer"}

# .issubset()   -> Check if all elements of the current set are contained in another set
print(child_set.issubset(parent_set))         # Result: True

# .issuperset() -> Check if the current set contains all elements of another set
print(parent_set.issuperset(child_set))       # Result: True

# .isdisjoint() -> Check if two sets have NO common elements (Giao nhau bằng rỗng)
print(child_set.isdisjoint(other_set))        # Result: True (Không có quyền nào chung)


# ==============================================================================
# 6. SET COMPREHENSION (Cách viết ngắn gọn để tạo một Set mới)
# ==============================================================================
# Giống List Comprehension nhưng sử dụng ngoặc nhọn {} và tự động lọc sạch trùng lặp
raw_scores = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Tạo một set bình phương của các số không trùng lặp
squared_set = {num**2 for num in raw_scores}
print(f"Set Comprehension result: {squared_set}") # Result: {1, 4, 9, 16, 25, 36}