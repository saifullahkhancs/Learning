# Q1:- What is Data Structure?
#     A data structure is a storage thatis used to store and organize the data. It is a way 
#     of arranging the data on a computer so that it can be accessed and updated efficiently.
# A data structure is not only used for organizing the data. It is also used for processing, retrieving, and storing data

# Q2:- What are linear and Non_linear Data structure?
# Data structure in which each elemnent are arrannged sequentaially or linearly, where 
# each elemnent is attached to its previous and next adjacent elemnts, is called the 
# linear data structures
# For Example:--            Array , Stack ,Queue , Linked Lists

# Data structures that are not placed sequentaially or linearly are called non_linear data structure.
# In a non linear data structure, we can not traverse ia a single run only.
# For Example :--   Trees and Graphs


# Q3:- What is the difference between the data structure and databases?
# Data structure is a logical representation of how your data is organized, while
# database is a middleware to help you stire the data into file system.

# Q4:- What are top and rear operation?
# Top: This returns the top item from the stack.
# Rear: This returns the front-end elemeent without removing it.

# Q5:- What is the application of stack and queue?
# Stack:-
#     It acts as temporary storage during recursive operations.
#     Redo and undo operations in doc editors.
#     Reversing a string.
#     Postfix and Infix Expression
#     Function 

# Queue
#     Bredth-First search algortahim in graphs
#     Operating System: job scheduling operations, Disk Scheduling, CPU scheduling etc
#     Call management in call centers


# Link List 
# Stack , Queue , Binary trees and graphs are implememted using the link list
# Dynamic management for Operating System Memory.
# Round Robin scheduling for operating system tasks.
# Fowarad and backward operations in the browser.

# Binary data structure 
# Its widely used in computer networks for storing routing table information
# Decision Trees.
# Expression Evalution
# Database Indices.

# Binary Search trees
# It is used for indexing and multi-level indexing 
# It is used for implementing various search algorathims
# It is helpful in organizing a sorted stream of Data.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage:
linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)

print("Original linked list:")
linked_list.print_list()

linked_list.reverse()

print("Reversed linked list:")
linked_list.print_list()

Q1: - What is difference between the quick sort and merge sort what are their best cases?
Q2:- What is diferenece between the patch and put? 
Q3:- What are the Cors?
Q4:- 
