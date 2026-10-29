

class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.newnode = None
class Binary_tree:
    def Main_loop(self, root, value):
        root = None

        root = self.insert(root, 10)
        root = self.insert(root, 5)
        root = self.insert(root, 15)
        root = self.insert(root, 7)
        root = self.insert(root, 3)

        self.print_tree(root)
        self.insert(root, value)
        self.print_tree

    def insert(root, value, self):
        if root is None:
            return Node(value)
        if value > root.data:
            root.right = value
            return root
        elif value < root.data:
            root.left = value
            return root
        self.insert(root)



    def print_tree(root, self):
        if root is None:
            return
        self.insert(root)
        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)


Binary_tree.Main_loop(Binary_tree.self, Binary_tree.value, Binary_tree.root)
