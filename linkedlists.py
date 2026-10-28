class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListsAlgorithms:
    def __init__(self):
        self.stop_running = False
        self.head = None
        self.head2 = None
        self.head3 = None


    def read_data(self):
        file = open("linkedlist_input.txt", "r")

        current = None
        second_list = False

        while True:
            line = file.readline()

            if line == '':  # End of file
                break

            if line.strip() == '':  # Blank line = second list
                second_list = True
                current = None
                continue

            data = int(line)
            newnode = Node(data)

            if second_list == False:
                if current == None:
                    self.head = newnode
                else:
                    current.next = newnode
            else:
                if current == None:
                    self.head2 = newnode
                else:
                    current.next = newnode

            current = newnode


    def save_data(self):
        file = open("linkedlist_input.txt", "w")

        current = self.head

        while current != None:
            file.write(str(current.data) + "\n")
            current = current.next

        file.close()

    def algorithm_print_file(self, current):
        if current == None:
            return
        print(current.data)
        self.algorithm_print_file(current)

    def algorithm_find_num(self, current):
        number_to_find = int(input("Which number would you like to find?\n"))
        self.find_recursive(current, number_to_find)

    def find_recursive(self, current, number_to_find):
        if current == None:
            print("You're number is not in the file, I swear, I checked twice.")
            return
        if current.data == number_to_find:
            print("You're number was in the list, I'm pretty tuff right? Okay so I might've not really seen your number but wtv yk?")
            return
        self.find_recursive(current.next, number_to_find)

    def algorithm_add_to_end_of_list(self, current):
        number_to_add_data = int(input("Pick a number to add to the end of the list: "))
        newnode = Node(number_to_add_data)

        self.add_recursive(current, newnode)
        self.save_data()


    def add_recursive(self, current, newnode):

        if current == None:
            self.head = newnode
            self.save_data()
            return 

        if current.next == None:
            current.next = newnode
            return

        self.add_recursive(current.next, newnode)
        print(current.data)

    def algorithm_remove_from_list(self, current):

        # FUNC 1, PRINTS THE LIST
        self.algorithm_print_file(self.head)

        num_to_remove = int(input("Here is the current list. Which number would you like to remove? "))

        self.remove_recursive(current, num_to_remove)
        self.algorithm_print_file(self.head)
        self.save_data()
    def remove_recursive(self, current, num_to_remove):
        # Bug #1 - what if current == None?
        if current.next == None:
            print("Pick a different number bro, that's not in the list")
            return
        elif current == None:
            print("PICK A DIFFERENT NUMBER")
            return
        if current.next.data == num_to_remove:
            current.next = current.next.next
            return

        self.remove_recursive(current.next, num_to_remove)



    def algorithm_sort_list(self):
        current = self.head
        prev = None
        head = None

        current2 = head

        while current != None:
            prev = None
            current2 = head

            data = int(current.data)
            newnode = Node(data)
            current = current.next

            # First node
            if current2 == None:
                head = newnode

            # New node belongs at the beginning
            elif newnode.data < head.data:
                newnode.next = head
                head = newnode

            else:
                # Find where the new node belongs
                while current2 != None:
                    if newnode.data < current2.data:
                        prev.next = newnode
                        newnode.next = current2
                        break

                    prev = current2
                    current2 = current2.next

                # New node belongs at the end
                if current2 == None:
                    prev.next = newnode

        current2 = head

        while current2 != None:
            print(current2.data)
            current2 = current2.next

        yes_save = str(input("Would you like to save this sorted list? \n"))
        if yes_save == "y" or "yes" or "yea" or "Y" or "Yes" or "Yea":
            file = open("linkedlist_input.txt", "w")

            current = head

            while current != None:
                file.write(str(current.data) + "\n")
                current = current.next

            file.close()
            print("Here is the list:")
            current = head
            while current != None:
                print(current.data)
                current = current.next

    def algoritm_reverse_list(self):
        current = self.head.next
        nxt = self.head.next.next 
        prevous = self.head
        is_not_reversed = False


        while is_not_reversed == False:
            if prevous == self.head:
                prevous.next = None
            current.next = prevous


            prevous = current
            current = nxt
            if nxt != None:
                nxt = nxt.next
            if current == None:
                is_not_reversed = True
                break
        self.head = prevous
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def algorithm_merge_two_lists(self):
        current1 = self.head
        current2 = self.head2


        if current1 is None:        #BC for at the end of the list
            self.head3 = current2
            return
        if current2 is None:
            self.head3 = current1
            return

        if current1.data <= current2.data: # checks which one is bigger/ smaller
            self.head3 = current1
            current1 = current1.next
        else:
            self.head3 = current2
            current2 = current2.next

        endpoint = self.head3

        while current1 != None and current2 != None: 
            if current1.data <= current2.data: 
                endpoint.next = current1 
                current1 = current1.next 
            else:
                endpoint.next = current2 
                current2 = current2.next 

            endpoint = endpoint.next

        if current1 != None:
            endpoint.next = current1
        else:
            endpoint.next = current2

        # Print the merged list
        current = self.head3
        while current != None:
            print(current.data)
            current = current.next


    def algorithm_reverse_list_and_sort(self):
        pass
    def algorithm_run_again(self):
        pass
        
 





        

            
linked_list = LinkedListsAlgorithms()
linked_list.read_data()

while True:

        algorithm = int(input("Which algorithm would you like to use? \n 1. Print linked list \n 2. Find whether a number is in the list \n 3. Add something to the end of the list \n 4. Remove something from the list \n 5. Sort the list low to high \n 6. Reverse list \n 7. Reverse and sort list \n press 9 to quit "))
        if algorithm == 1:
            linked_list.algorithm_print_file(linked_list.head)
        elif algorithm == 2:
            linked_list.algorithm_find_num(linked_list.head)
        elif algorithm == 3:
            linked_list.algorithm_add_to_end_of_list(linked_list.head)
        elif algorithm == 4:
            linked_list.algorithm_remove_from_list(linked_list.head)
        elif algorithm == 5:
            linked_list.algorithm_sort_list()
        elif algorithm == 6:
            linked_list.algoritm_reverse_list()
        elif algorithm == 7:
            linked_list.algorithm_reverse_list_and_sort() 
        elif algorithm == 8:
            linked_list.algorithm_merge_two_lists()
        else:
            print("That number wasn't an option... \n")
            print("BEEP BOOP, RESTARTING PROGRAM...")
            print("PLEASE BE PATIENT...")
            print("restarted program:")
            linked_list.algorithm_run_again()
            

        if algorithm == 9:
            break

    


                    

                
