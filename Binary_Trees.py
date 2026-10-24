

class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.newnode = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value > root.value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)

    return root

def print_tree(root):
    if root is None:
        return

    print(root.value)
    print_tree(root.left)
    print_tree(root.right)


root = None

root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 7)
root = insert(root, 3)

print_tree(root)

