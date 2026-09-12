class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
current = None
file = open("linkedlist_input.txt", "r")

reading_file = True
while (reading_file):
    line = file.readline()
    if (line == ''): # We've hit the end of the file
        reading_file = False
        break

    data = int(line)
    newnode = Node(data)
    if current == None: # then this is our very first node
        head = newnode
    else:
        current.next = newnode
    current = newnode
file.close() #read it in, now must print it out

current = head
while current != None:
    print(current.data)
    current = current.next


