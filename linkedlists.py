class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListsAlgorithms:
    def __init__(self):
        self.stop_running = False
        self.head = None
        self.head2


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
    def algorithm_remove_from_list(self):

        # FUNC 1, PRINTS THE LIST
        self.algorithm_print_file()

        check_option = int(input("Here is the current list. Which number would you like to remove? "))

        # FUNC 2, CHECKS IF THE INPUT IS IN THE LINKED LIST
        current = self.head
        previous = None
        Value = False

        while current != None:

            if current.data == check_option:
                Value = True
                break

            previous = current
            current = current.next

        # FUNC 4, REMOVE THEN SAVE
        if Value == True:

            # If we're removing the first node
            if previous == None:
                self.head = current.next

            # If we're removing any other node
            else:
                previous.next = current.next

            print("Removed:", check_option)

            self.algorithm_print_file()

            self.save_data()

        else:
            print("That number wasn't in the list.")

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
    def algorithm_merge_and_sort_two_lists(self):
        pass

    def algorithm_reverse_list_and_sort(self):
        pass
    def algorithm_run_again(self):
        pass
        
 





        

            
linked_list = LinkedListsAlgorithms()
linked_list.read_data()

while True:

        algorithm = int(input("Which algorithm would you like to use? \n 1. Print linked list \n 2. Find whether a number is in the list \n 3. Add something to the end of the list \n 4. Remove something from the list \n 5. Sort the list low to high \n 6. Reverse list \n 7. Reverse and sort list \n press 9 to quit "))
        if algorithm == 1:
            linked_list.algorithm_print_file()
        elif algorithm == 2:
            linked_list.algorithm_find_num()
        elif algorithm == 3:
            linked_list.algorithm_add_to_end_of_list()
        elif algorithm == 4:
            linked_list.algorithm_remove_from_list()
        elif algorithm == 5:
            linked_list.algorithm_sort_list()
        elif algorithm == 6:
            linked_list.algoritm_reverse_list()
        elif algorithm == 7:
            linked_list.algorithm_reverse_list_and_sort() 
        else:
            print("That number wasn't an option... \n")
            print("BEEP BOOP, RESTARTING PROGRAM...")
            print("PLEASE BE PATIENT...")
            print("restarted program:")
            linked_list.algorithm_run_again()
            

        if algorithm == 9:
            break

    


                    

                
