from queues import queue
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self): 
        self.root = None
        self.unsorted_root = None

    def read_data(self):
        file = open("linkedlist_input.txt", "r")

        while True:
            line = file.readline()

            if line == '':
                break

            if line.strip() == '':
                continue

            data = int(line)
            self.root = self.insert(self.root, data)

        file.close()

    def read_unsorted_data(self):
        file = open("Linkedlist_input.txt", "r")

        while True:
            line = file.readline()

            if line == '':
                break

            if line.strip() == '':
                continue

            data = int(line)
            self.unsorted_root = self.unsorted_insert(self.unsorted_root, data)
        file.close()

    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value > root.value:
            root.right = self.insert(root.right, value)

        elif value <= root.value:
            root.left = self.insert(root.left, value)

        return root

    def unsorted_insert(self, unsorted_root, value):
        if unsorted_root is None:
            return Node(value)

        unsorted_root.right = self.unsorted_insert(unsorted_root.right, value)
        unsorted_root.left = self.unsorted_insert(unsorted_root.left, value)

        return unsorted_root
    
    def remove(self, root, value):
        if root is None:
            return None
        # find the number
        if value < root.value:
            root.left = self.remove(root.left, value)
        elif value > root.value:
            root.right = self.remove(root.right, value)
        else:
            #THREE CASES
            # Case 1, no children, this also works with the c2 code because root.left is still none so it would replace itself with none.
            # Case 2, 1 child
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            # Case 3, 2 children
            successor = root.right  
            while successor.left:
                successor = successor.left
            root.value = successor.value
            # Finds the double guy
            root.right = self.remove(root.right, successor.value)
        return root

    def find_nearest_ancestor_recursion(self, root, value, path):

        if root is None:
            return

        path.append(root.value)

        if value < root.value:
            self.find_nearest_ancestor_recursion(root.left, value, path)

        elif value > root.value:
            self.find_nearest_ancestor_recursion(root.right, value, path)



    def find_nearest_ancestor(self, root, value, value2):

        path1 = []
        path2 = []

        self.find_nearest_ancestor_recursion(root, value, path1)
        self.find_nearest_ancestor_recursion(root, value2, path2)

        i = 0

        while i < len(path1) and i < len(path2):

            if path1[i] != path2[i]:
                return path1[i - 1]

            i += 1

        return path1[i - 1]

    def inorder_print(self, root):
        if root is None:
            return
        self.inorder_print(root.left)
        print(root.value)
        self.inorder_print(root.right)

    def find_depth_recursive(self, root):
        if root is None:
            return 0

        left_down = self.find_depth_recursive(root.left)
        right_down = self.find_depth_recursive(root.right)

        return 1 + max(left_down, right_down)
    
    def find_depth(self, root):
        print(self.find_depth_recursive(root))
        return self.find_depth_recursive(root)
    
    def DFS_recursion(self, root, value):
        if root is None:
            return False

        if root.value == value:
            return True

        if self.DFS_recursion(root.left, value):
            return True

        if self.DFS_recursion(root.right, value):
            return True

        return False


    def DFS(self, unsorted_root, value):
        if self.DFS_recursion(unsorted_root, value) == True:
            print("your number is in the tree")
        else:
            print("your number is not in the tree, try a different value?")
        return self.DFS_recursion(unsorted_root, value)
    
    def BFS(self, root):
        if root == None:
            print("nothing in tree")
            return

        value = int(input("Input a number you would like to find: "))

        q = queue()
        q.enqeue(root)

        while q.head != None:
            current = q.deqeue()

            if current.value == value:
                print("Your value is in the tree!!!!")
                return True

            if current.left != None:
                q.enqeue(current.left)

            if current.right != None:
                q.enqeue(current.right)

        print("Your value is not in the tree :(")
        return False

        
            



        

    def print_tree(self, root):
        if root is None:
            return

        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def Main_loop(self, root):
        self.print_tree(root)


tree = Binary_tree()
tree.read_unsorted_data()
tree.print_tree(tree.unsorted_root)
tree.BFS(tree.unsorted_root)