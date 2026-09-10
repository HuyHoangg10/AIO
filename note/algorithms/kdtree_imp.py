import math

class Node:
    def __init__(self, point, left, right):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(point, depth=0):
    if not point:
        return None
    k = len(point[0])
    axis = depth % k
    print("axis", axis)

    point.sort(key=lambda x: x[axis])
    median = len(point) // 2
    print("median", point[median])
    print("-----------------------------------")

    return Node(
        point=point[median],
        left=build_kd_tree(point[:median], depth + 1),
        right=build_kd_tree(point[median + 1:], depth + 1),
    )

# 1. Hàm tính khoảng cách chuẩn theo ảnh của thầy (Sử dụng math.sqrt và zip)
def distance_squared(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# 2. Hàm so sánh điểm gần nhất chuẩn 3 tham số theo ảnh của thầy
def closer_point(new_data, nearest_node, root_node):
    if nearest_node is None:
        return root_node
    if root_node is None:
        return nearest_node
    
    if distance_squared(new_data, nearest_node) < distance_squared(new_data, root_node):
        return nearest_node
    return root_node

# 3. Hàm tìm kiếm láng giềng gần nhất đồng bộ tham số với hệ thống của thầy
def nearest_neighbor(node, point, depth=0, best=None):
    if node is None:
        return best
    
    k = len(point)
    axis = depth % k

    if point[axis] < node.point[axis]:
        next_branch = node.left
        opposite_branch = node.right
    else:
        next_branch = node.right
        opposite_branch = node.left

    # Gọi hàm closer_point truyền vào 3 tham số theo đúng thiết kế của thầy
    best = closer_point(
        point,
        nearest_neighbor(next_branch, point, depth + 1, best), 
        node.point
    )

    # Kiểm tra xem khoảng cách hình chiếu (trên 1 trục đơn lẻ) có nhỏ hơn khoảng cách thực tế tốt nhất hiện tại không
    if abs(point[axis] - node.point[axis]) < distance_squared(point, best):
        best = closer_point(
            point,
            nearest_neighbor(opposite_branch, point, depth + 1, best), 
            best
        )

    return best

# --- Khởi tạo dữ liệu thực thi ---
point = [(1, 2), (2, 6), (3, 4), (5, 6), (7, 8), (8, 3)]
kd_tree = build_kd_tree(point)

# Điểm mục tiêu cần tìm láng giềng gần nhất
query_point = (6, 5)

# Thực thi thuật toán
result = nearest_neighbor(kd_tree, query_point)
print("Nearest Neighbor:", result)