class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node  = Node(data)

        if self.head == None:
            self.head = new_node
            return 
        current = self.head
        # while last_node.next == None:      it will generate the error
        while current.next:           
            current = current.next        # here it points wtoward none which will be checked up      
             
        current.next == new_node     # next complete node is the address


    def display(self):
        current = self.head
        while current != None:       # keep this in min that current is none in last
            print(current.data)       # not the current.next
            current = current.next

    
    def reverse(self):
        prev = None
        current = self.head

        while current == None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def center(self):
        current = self.head
        current_next = self.head
        while current_next != None:
            current = current.next
            current_next = current_next.next.next
        return current

        


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list:")
linked_list.display()

linked_list.reverse()

print("\nReversed linked list:")
linked_list.display()

print("\nCenter of linked list:")
linked_list.center()