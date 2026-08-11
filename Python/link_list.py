import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from shared.data_structures import LinkedList

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.display()
