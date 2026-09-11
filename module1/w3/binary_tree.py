class BinaryTreeNode:
    def __init__(self, data: any):
        self.data = data
        self.left = None
        self.right = None

    def pre_order(self) -> None:
        print(self.data,end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self) -> None:
        if self.left:
            self.left.in_order()
        print(self.data,end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self) -> None:
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data,end=" ")

# Sửa lại tên hàm thành post_order (thêm r) rồi thêm đoạn test này vào cuối file:
if __name__ == "__main__":
    # Dựng cây kiểm chứng
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)

    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    root.left.left.left = BinaryTreeNode(7)
    root.left.left.right = BinaryTreeNode(8)

    root.left.right.right = BinaryTreeNode(9)
    root.right.left = BinaryTreeNode(6)

    print("Pre-order :", end=" ")
    root.pre_order()
    print()

    print("In-order  :", end=" ")
    root.in_order()
    print()

    print("Post-order:", end=" ")
    root.post_order()
    print()