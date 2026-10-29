class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree:
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value > root.value:
            root.right = self.insert(root.right, value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        
        return root

    def print_tree(self, root):
        if root is None:
            return

        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def Main_loop(self, value):
        root = None

        root = self.insert(root, 10)
        root = self.insert(root, 5)
        root = self.insert(root, 15)
        root = self.insert(root, 7)
        root = self.insert(root, 3)
        root = self.insert(root, value)
        self.print_tree(root)


tree = Binary_tree()
tree.Main_loop(12)

