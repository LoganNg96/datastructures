class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class stacks:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next

    def push(self):
        i = int(input("input a number to place on the top of the stack"))
        newnode = Node(i)

        newnode.next = self.head
        self.head = newnode

    def pop(self):
        if self.head == None:
            print("nothing in stack")
            return

        removed = self.head.data
        self.head = self.head.next

        print("removed " + removed)