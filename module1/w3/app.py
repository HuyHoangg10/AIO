from binary_tree import BinaryTreeNode


def main() -> None:
    node = BinaryTreeNode(10)
    node_a = BinaryTreeNode(5)
    node_b = BinaryTreeNode(20)

    node.left = node_a
    node.right = node_b

    node.in_order()


if __name__ == "__main__":
    main()
