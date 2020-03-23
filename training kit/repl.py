import os
from linked_list import LinkedList
os.system('clear')


l_list = LinkedList()

l_list.push(1)
l_list.push(7)
l_list.push(3)
l_list.push(4)

print(f"l_list: {l_list}")

value = 5
print(f"l_list contains {value}: {l_list.contains(value)}")
