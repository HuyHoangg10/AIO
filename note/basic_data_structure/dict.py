import copy  # Required for deepcopy()

# ==============================================================================
# 1. INITIALIZATION & READ (Khởi tạo và Các cách Đọc dữ liệu)
# ==============================================================================
# Dictionary is Ordered (từ Python 3.7+), Mutable, and does NOT allow duplicate Keys.
player_profile = {"name": "Bruno", "role": "Midfielder", "number": 8}

# Standard Read -> Throws a KeyError if the key does not exist
print(player_profile["name"])  # Result: Bruno

# .get()        -> SAFE READ. Returns None (or a default value) if the key is missing
# (Giúp code Backend không bao giờ bị sập lỗi vặt khi thiếu Key dữ liệu)
print(player_profile.get("status"))  # Result: None (Không bị crash code)
print(
    player_profile.get("status", "N/A")
)  # Result: N/A (Trả về giá trị default tùy chọn)

# .setdefault() -> SAFE READ & WRITE. Returns value if key exists.
# If key does NOT exist, inserts the key with the specified default value.
current_club = player_profile.setdefault(
    "club", "Man Utd"
)  # Key "club" is new -> Inserts "club": "Man Utd"
existing_name = player_profile.setdefault(
    "name", "Harry"
)  # Key "name" exists -> Returns "Bruno", ignores "Harry"


# ==============================================================================
# 2. CREATE & UPDATE (Thêm mới và Chỉnh sửa phần tử)
# ==============================================================================
# Direct assignment -> If key exists, updates it. If key is new, creates it.
player_profile["number"] = 18  # Update existing key

# .update()     -> Merge another dictionary (or iterable of key-value pairs) into the current one
player_profile.update({"goals": 15, "role": "Captain"})


# ==============================================================================
# 3. DELETE (Các phương thức Xóa phần tử)
# ==============================================================================
# .pop()        -> Remove the specified key and return its corresponding value
# (Thường xuyên dùng để bóc tách dữ liệu JSON/API)
removed_role = player_profile.pop("role")  # Removes "role", returns "Captain"

# del           -> Keyword to delete a key-value pair, or delete the entire dict
del player_profile["number"]

# .clear()      -> Empty the entire dictionary (Deletes all elements inside)
# player_profile.clear()


# ==============================================================================
# 4. DICTIONARY LOOPS & VIEWS (Các cách Duyệt vòng lặp nâng cao)
# ==============================================================================
# .keys()       -> Return a view object containing all the keys
for key in player_profile:
    print(f"Key: {key}")

# .values()     -> Return a view object containing all the values
for value in player_profile.values():
    print(f"Value: {value}")

# .items()      -> Return a view object containing pairs of (key, value) tuples
# (Cách duyệt loop chuẩn mực và phổ biến nhất trong thực tế)
for key, value in player_profile.items():
    print(f"{key.capitalize()}: {value}")


# ==============================================================================
# 5. COPYING DICTIONARIES (Sao chép: Shallow Copy vs Deep Copy)
# ==============================================================================
# Gốc: Giả sử ta có một Nested Dictionary (Dictionary lồng nhau)
original_data = {"id": 1, "skills": ["Passing", "Shooting"]}

# .copy()      -> SHALLOW COPY (Sao chép nông)
# Chỉ copy lớp vỏ ngoài. Nếu bên trong có chứa List/Dict lồng nhau, chúng vẫn dùng chung vùng nhớ!
shallow_data = original_data.copy()
shallow_data["skills"].append(
    "Tackling"
)  # ⚠️ Thay đổi này sẽ làm thay đổi luôn cả original_data!

# copy.deepcopy() -> DEEP COPY (Sao chép sâu)
# Sao chép toàn bộ, tạo ra một bản sao độc lập hoàn toàn trong bộ nhớ (Kể cả các List/Dict lồng bên trong)
deep_data = copy.deepcopy(original_data)
deep_data["skills"].append(
    "Dribbling"
)  # ✅ Hoàn toàn an toàn, không ảnh hưởng đến bản gốc


# ==============================================================================
# 6. DICTIONARY COMPREHENSION (Cách viết ngắn gọn để tạo Dict mới)
# ==============================================================================
# Giống List/Set Comprehension nhưng trả về cặp key: value nằm trong ngoặc nhọn {}
players = ["Bruno", "Harry", "Cunha"]
base_scores = [80, 90, 85]

# Tạo một map cầu thủ và điểm số tối ưu (+ 5 điểm thưởng) cho ai có điểm >= 85
boosted_stats = {
    name: score + 5 for name, score in zip(players, base_scores) if score >= 85
}
print(f"Comprehension result: {boosted_stats}")  # Result: {'Harry': 95}
