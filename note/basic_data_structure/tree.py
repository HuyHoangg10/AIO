class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child: 'TreeNode'):
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        """
        Phương thức bổ sung để in cấu trúc cây ra màn hình 
        dưới dạng phân cấp trực quan dựa trên level của từng node.
        """
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()


# ==========================================
# CHƯƠNG TRÌNH CHẠY THỬ (DEMO)
# ==========================================
if __name__ == "__main__":
    # 1. Khởi tạo các Node độc lập trong bộ nhớ
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    cellphone = TreeNode("Cell Phone")
    
    macbook = TreeNode("MacBook")
    thinkpad = TreeNode("ThinkPad")
    iphone = TreeNode("iPhone")

    # 2. Thiết lập mối quan hệ Cha - Con (Gắn các node con vào node cha)
    # Thêm con cho root
    root.add_child(laptop)
    root.add_child(cellphone)
    
    # Thêm con cho laptop
    laptop.add_child(macbook)
    laptop.add_child(thinkpad)
    
    # Thêm con cho cellphone
    cellphone.add_child(iphone)

    # 3. Kiểm tra tính toán cấp độ (get_level)
    print("--- Kiểm tra Level của từng Node ---")
    print(f"Level của '{root.data}': {root.get_level()}")         # Output: 0 (Root)
    print(f"Level của '{laptop.data}': {laptop.get_level()}")     # Output: 1
    print(f"Level của '{macbook.data}': {macbook.get_level()}")   # Output: 2
    print("-" * 35)

    # 4. In toàn bộ cấu trúc cây trực quan
    print("\n--- Cấu trúc cây toàn chỉnh ---")
    root.print_tree()