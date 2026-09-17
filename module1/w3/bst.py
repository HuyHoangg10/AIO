class BSTNode:
    def __init__(self, data: any):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: any) -> None:
        if value is None:
            return
        if self.data is None:
            self.data = value
            return
        current = self
        while True:
            if value == current.data:
                return
            elif value < current.data:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            elif value > current.data:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right

    def in_order(self) -> None:
        if self.left:
            self.left.in_order()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order()

    def search(self, target: any) -> bool:
        current = self
        if target is None:
            return False
        while current:
            if current.data == target:
                return True
            elif target < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def _find_min(self) -> 'BSTNode':
        current = self
        while current.left is not None:
            current = current.left
        return current

    def delete(self,value:int) -> 'None | BSTNode':
        return self._delete_node(self,value)

    def _delete_node(self,root: 'BSTNode | None',value) ->'None | BSTNode':
        if root is None:
            return None
        if value < root.data:
            root.left = self._delete_node(root.left,value)
        elif value > root.data:
            root.right = self._delete_node(root.right,value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                successor = root.right._find_min()
                root.data = successor.data
                root.right = self._delete_node(root.right, successor.data)
        return root

def main() -> None:
    # 1. Khởi tạo cây chuẩn theo đúng sơ đồ bạn đã vẽ:
#         [10]
#        /    \
#      [5]    [20]
#        \    /
#        [8] [15]
#        /
#      [6]

    tree = BSTNode(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(8)
    tree.insert(15)
    tree.insert(6)

    print("Cây ban đầu (In-order):")
    tree.in_order()
    # Kết quả mong đợi: 5 6 8 10 15 20
    print()

    # 2. Thực hiện xóa node gốc 10
    # Node 15 (In-order successor) sẽ được đưa lên thế chỗ 10
    tree = tree.delete(10)

    print("\nCây sau khi xóa node 10 (In-order):")
    tree.in_order()
    # Kết quả mong đợi: 5 6 8 15 20
    print()

if __name__ == "__main__":
  main()