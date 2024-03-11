# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Cirll:
#     def __inti__(self):
#        self.head = None
    
#     def append(self,data):
#         new_node = Node(data)

#         print(self.head)

#         if self.head is None:
#             self.head = new_node
#             new_node.next = self.head
#         else:
#             current  = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head


#     def print_list(self):
#         if self.head is None:
#             print("list is empty")
#             return
        
#         current = self.head

#         while current.next != self.head:
#             print(current.data)
#             current = current.next


# my_list = Cirll()


# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# my_list.print_list()        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage:
my_list = CircularLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.print_list()  # Output: 10 20 30
