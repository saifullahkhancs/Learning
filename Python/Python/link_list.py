class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head = None

    def append(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head=new_node
            else:
                current= self.head
                while current.next != None:
                    current = current.next
                current.next = new_node
    
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

my_list = Linklist()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.print_list()