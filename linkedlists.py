class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListsAlgorithms:
    def __init__(self):
        self.stop_running = False
        self.head = None


    def read_data(self):
        file = open("linkedlist_input.txt", "r")
        current = self.head
        reading_file = True
        while reading_file:
            line = file.readline()

            if line == '':  # We've hit the end of the file
                reading_file = False
                break

            data = int(line)
            newnode = Node(data)
            if current == None:  # then this is our very first node
                self.head = newnode
            else:
                current.next = newnode

            current = newnode

    def save_data(self):
        file = open("linkedlist_output.txt", "w")

        current = self.head

        while current != None:
            file.write(str(current.data) + "\n")
            current = current.next

        file.close()


    def algorithm_print_file(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next


    def algorithm_find_num(self):
        number_to_find = int(input("Which number would you like to find?\n"))
        current = self.head
        while current != None:
            if current.data != number_to_find:
                current = current.next
            elif current.data == number_to_find:
                print("Your number is in the linked list\n")
                break

    def algorithm_add_to_end_of_list(self):
        number_to_add_data = int(input("Which number would you like to add to the list? (Data)"))
        # number_to_add_slot_in_list = int(input("Which number would you like to put in the linked list? (Slot)"))

        current = self.head
        while current.next != None:
            print(current.data)
            current = current.next

        data = int(number_to_add_data)
        newnode = Node(data)
        current.next = newnode  
        print(current.data)         
        print(current.next.data)
        self.save_data()

linked_list = LinkedListsAlgorithms()
linked_list.read_data()

while True:

        algorithm = int(input("Which algorithm would you like to use? \n 1.Print linked list \n 2. Find whether a number is in the list \n 3. Add something to the end of the list \n 4. Remove something from the list \n press 9 to quit "))
        if algorithm == 1:
            linked_list.algorithm_print_file()
        elif algorithm == 2:
            linked_list.algorithm_find_num()
        elif algorithm == 3:
            linked_list.algorithm_add_to_end_of_list()

        if algorithm == 9:
            break

    


                    

                
