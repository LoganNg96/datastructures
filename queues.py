class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next

    def enqeue(self, value):
        newnode = Node(value)

        if self.head == None:
            self.head = newnode
        elif self.head.next == None:
            self.tail = newnode
            self.head.next = self.tail  
        else:
            self.tail.next = newnode
            self.tail = self.tail.next 

    def deqeue(self):
        if self.head == None:
            print("nobody in queue")
            return

        removed = self.head.data
        self.head = self.head.next

        return removed

    def peek(self):
        return self.head.data

    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
        

g = queue()
g.enqeue(4)
g.enqeue(7)
g.enqeue(48)
g.enqeue(41)
g.enqeue(42)
g.enqeue(44)
g.enqeue(5)
g.enqeue(9)
g.deqeue()
g.deqeue()
g.print()
  
    