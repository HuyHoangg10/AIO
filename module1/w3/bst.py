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
        print(self.data , end = " ")
        if self.right:
            self.right.in_order()
