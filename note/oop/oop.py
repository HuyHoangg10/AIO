# ==============================================================================
# 1. CLASS & OBJECT INITIALIZATION (Khởi tạo Lớp và Đối tượng)
# ==============================================================================
class PlayerProfile:
    # __init__ là Constructor (Giống Constructor trong Java). 
    # Tự động kích hoạt khi object được khởi tạo để gán giá trị ban đầu.
    def __init__(self, name, role, number):
        self.name = name        # Thừa hưởng thuộc tính nội bộ từ tham số truyền vào
        self.role = role
        self.number = number

# Tạo đối tượng (Khởi tạo Object)
# Ta chỉ cần truyền dữ liệu cho name, role, number. Tham số self được Python tự động xử lý ngầm.
player1 = PlayerProfile("Bruno", "Midfielder", 8)


# ==============================================================================
# 2. OBJECT METHODS (Định nghĩa các Hàm chức năng của Đối tượng)
# ==============================================================================
class PlayerProfile:
    def __init__(self, name, role, number):
        self.name = name
        self.role = role
        self.number = number

    # QUY TẮC VÀNG: Bất kỳ hàm thông thường nào trong class đều phải có 'self' đứng đầu.
    # 'self' tương trưng cho chính object hiện tại, dùng để truy xuất biến nội bộ.
    def display_info(self):
        print(f"Player: {self.name} | Role: {self.role} | Shirt No: {self.number}")

    # Nếu hàm vừa dùng biến nội bộ (self) vừa nhận thêm tham số độc lập từ bên ngoài
    def update_stats(self, new_role, new_number):
        print(f"🧬 Updating stats for {self.name}...")
        self.role = new_role       # Cập nhật lại giá trị mới cho biến nội bộ
        self.number = new_number   # Cập nhật lại giá trị mới cho biến nội bộ

    def __call__(self, greeting):
        return f"{greeting} {self.name}"
# ==============================================================================
# 3. EXECUTION (Chạy thử nghiệm hệ thống)
# ==============================================================================
p1 = PlayerProfile("Bruno", "Midfielder", 8)

# Gọi hàm hiển thị thông tin gốc
p1.display_info()  # Result: Player: Bruno | Role: Midfielder | Shirt No: 8

# Gọi hàm cập nhật dữ liệu (Truyền tham số ngoài vào các vị trí sau self)
p1.update_stats("Captain", 18)

# Kiểm tra lại thông tin sau khi cập nhật
p1.display_info()  # Result: Player: Bruno | Role: Captain | Shirt No: 18_

print(p1("Hello"))