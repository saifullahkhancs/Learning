class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class   Dll:
    def __init__(self):
       self.head = None

    def append(self,data):
        new_node = Node(data)   

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current




    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Example usage:
my_list = Dll()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.print_forward()  # Output: 10 20 30
my_list.print_backward() # Output: 30 20 10