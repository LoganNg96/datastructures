class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



amount_of_nodes = int(input("Enter the number of nodes: "))
nodes = []
for i in range(amount_of_nodes):
    data = int(input(f"Enter data for node {i + 1}: "))
    nodes.append(Node(data))

for i in range(amount_of_nodes - 1):
    nodes[i].next = nodes[i + 1]

current = nodes[0]

while current != None:
    print(current.data)
    current = current.next