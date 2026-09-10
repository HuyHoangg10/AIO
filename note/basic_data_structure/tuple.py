# ==============================================================================
# 1. READ-ONLY METHODS (Các hàm giống hệt List nhưng áp dụng cho Tuple)
# ==============================================================================
# Thao tác đọc dữ liệu giống List vì Tuple cũng có Index và cho phép trùng lặp.
# Thao tác ghi/sửa dữ liệu (như .append, .insert, .pop, .remove) KHÔNG TỒN TẠI.

# .index()   -> Return the index of the FIRST matched value
# .count()   -> Return the number of times a specified value appears
# len()      -> Return the total number of elements
# dir()      -> Built-in function to list all valid attributes and methods of an object


# ==============================================================================
# 2. PACKING & UNPACKING (Đóng gói và Giải nén Tuple)
# ==============================================================================
# Packing    -> Combining multiple values into a single Tuple (No brackets needed)
device_info = "Gateway_01", "192.168.1.1", "Online"

# Unpacking  -> Extracting values from a Tuple back into individual variables
name, ip, status = device_info
print(f"Device Name: {name}, IP: {ip}")

# Extended Unpacking (Using * to gather remaining items into a List)
scores = (90, 85, 78, 92, 88)
highest, second, *other_scores = scores
print(f"Top 2: {highest}, {second}. Others: {other_scores}")


# ==============================================================================
# 3. TYPE CONVERSION / CASTING (Chu trình chuyển đổi Tuple <-> List)
# ==============================================================================
# Vì Tuple là Immutable, khi cần chỉnh sửa ta phải đi đường vòng qua List.

# Step 1: Initialize an immutable tuple
immutable_config = ("Hanoi", "HoChiMinh", "DaNang")

# Step 2: Convert Tuple to List to unlock all mutable methods
mutable_list = list(immutable_config)

# Step 3: Manipulate the data freely using List methods
mutable_list.append("HaiPhong")
mutable_list[0] = "HaNoi_Capital"

# Step 4: Convert back to Tuple to freeze the data again
final_config = tuple(mutable_list)

print(f"Final safe Tuple: {final_config}")
