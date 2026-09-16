from collections import deque


class BinaryTreeNode:
    def __init__(self, data: any):
        self.data = data
        self.left = None
        self.right = None

    def pre_order(self) -> None:
        print(self.data, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self) -> None:
        if self.left:
            self.left.in_order()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self) -> None:
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data, end=" ")

    def level_order(self) -> list:
        if self.data is None:
            return []
        queue = deque([self])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result

    def insert(self, value: any) -> None:
        if value is None:
            return
        new_node = BinaryTreeNode(value)
        queue = deque([self])

        while queue:
            current_node = queue.popleft()
            if current_node.left is None:
                current_node.left = new_node
                return
            else:
                queue.append(current_node.left)

            if current_node.right is None:
                current_node.right = new_node
                return
            else:
                queue.append(current_node.right)

    def _delete_deepest_node(self, deepest_node: "BinaryTreeNode") -> None:
        queue = deque([self])
        while queue:
            current_node = queue.popleft()
            if current_node.left:
                if current_node.left is deepest_node:
                    current_node.left = None
                    return
                else:
                    queue.append(current_node.left)
            if current_node.right:
                if current_node.right is deepest_node:
                    current_node.right = None
                    return
                else:
                    queue.append(current_node.right)

    def delete(self, key: any) -> None:
        if self.data is None or key is None:
            return
        if self.data == key and self.left is None and self.right is None:
            self.data = None
            return

        queue = deque([self])
        target_node = None
        deepest_node = None

        while queue:
            deepest_node = queue.popleft()
            if deepest_node.data == key:
                target_node = deepest_node

            if deepest_node.left:
                queue.append(deepest_node.left)
            if deepest_node.right:
                queue.append(deepest_node.right)

        if target_node is not None:
            target_node.data = deepest_node.data
            self._delete_deepest_node(deepest_node)


def main() -> None:
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

    print("Level-order:", root.level_order())

    root.insert(10)
    print("After insert:", root.level_order())


if __name__ == "__main__":
    main()
