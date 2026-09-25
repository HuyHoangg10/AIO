class Node:
    def __init__(
        self, point: any, left: "Node" | None = None, right: "Node" | None = None
    ) -> None:
        self.point = point
        self.left = left
        self.right = right


def build_kd_tree(point, depth=0):
    if not point:
        return
    # how dimension this kd_tree
    k = len(point[0])
    # which axis follow x or y
    axis = depth % k
    point.sort(key=lambda x: x[axis])

    median = len(point) // 2
    return Node(
        point=point[median],
        left=build_kd_tree(point[:median], depth + 1),
        right=build_kd_tree(point[median + 1 :], depth + 1),
    )


def distance_squared(point1, point2) -> int | float:
    if len(point1) != len(point2):
        return
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i]) ** 2
    return sum


def closer_point(target_point, nearest_point, node):
    if nearest_point is None:
        return node
    if node is None:
        return nearest_point
    if distance_squared(target_point, nearest_point) < distance_squared(
        target_point, node
    ):
        return nearest_point
    else:
        return node

def nearest_neighbor(node:'Node', target_point, depth=0, best=None):
    if node is None:
        return best
    k = len(target_point)
    axis = depth % k

    next_branch = None
    opposite_branch = None

    if target_point[axis] < node.point[axis]:
        next_branch = node.left
        opposite_branch = node.right
    else:
        next_branch = node.right
        opposite_branch = node.left
    best = closer_point(target_point,nearest_neighbor(next_branch,target_point,depth+1,best),node)
    if (target_point[axis] - node.point[axis])**2 < distance_squared(target_point,best):
        best = closer_point(target_point,nearest_neighbor(opposite_branch,target_point,depth+1,best),node)
    return best


points = [(1, 2), (2, 6), (3, 4), (5, 6), (7, 8), (8, 3)]
kd_tree = build_kd_tree(points)
