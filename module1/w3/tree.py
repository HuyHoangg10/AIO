class TreeNode:
    def __init__(self,data:str):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child:"TreeNode") -> None:
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self) -> None:
        space = " " * self.get_level() * 4
        prefix = space + "|___" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


data = TreeNode("Laptop")

data_a = TreeNode("Macbook")
data_b = TreeNode("Thinkpad")

data.add_child(data_a)
data.add_child(data_b)

print(data.data)
print(len(data.children))
data.print_tree()