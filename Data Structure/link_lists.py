import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from shared.data_structures import LinkedList

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

center = linked_list.find_center()
print("\nCenter of linked list:")
print(center.data if center else None)
