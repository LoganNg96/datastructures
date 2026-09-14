class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
stop_running = False
head = None
current = None

file = open("linkedlist_input.txt", "r")

reading_file = True
while reading_file:
    line = file.readline()

    if line == '':  # We've hit the end of the file
        reading_file = False
        break

    data = int(line)
    newnode = Node(data)

    if current == None:  # then this is our very first node
        head = newnode
    else:
        current.next = newnode

    current = newnode

while True:

    algorithm = int(input("Which algorithm would you like to use? \n 1.Print linked list \n 2. Find whether a number is in the list \n 3. Add something to the end of the list \n press q to quit "))


    if algorithm == "q":
        break



    if algorithm == 1:
        file = open("linkedlist_input.txt", "r")

        reading_file = True
        while reading_file:
            line = file.readline()

            if line == '':  # We've hit the end of the file
                reading_file = False
                break

            data = int(line)
            newnode = Node(data)

            if current == None:  # then this is our very first node
                head = newnode
            else:
                current.next = newnode

            current = newnode

        file.close()  # read it in, now must print it out

        current = head
        while current != None:
            print(current.data)
            current = current.next


    if algorithm == 2:
        number_to_find = int(input("Which number would you like to find?"))
        file = open("linkedlist_input.txt", "r")

        reading_file = True
        while reading_file:
            line = file.readline()

            if line == '':  # We've hit the end of the file
                reading_file = False
                break

            data = int(line)
            newnode = Node(data)

            if current == None:  # then this is our very first node
                head = newnode
            else:
                current.next = newnode

            current = newnode

        file.close()  # read it in, now must print it out

        current = head
        while current != None:
            if current.data != number_to_find:
                current = current.next
            elif current.data == number_to_find:
                print("Your number is in the linked list")
                break


    if algorithm == 3:
        number_to_add_data = int(input("Which number would you like to add to the list? (Data)"))
        # number_to_add_slot_in_list = int(input("Which number would you like to put in the linked list? (Slot)"))

        current = head
        while current.next != None:
            print(current.data)
            current = current.next

        data = int(number_to_add_data)
        newnode = Node(data)
        current.next = newnode  
        print(current.data)         
        print(current.next.data)


                

            
file.close()
