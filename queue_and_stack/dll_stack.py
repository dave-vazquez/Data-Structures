from doubly_linked_list import DoublyLinkedList
import sys
import os
sys.path.append('../doubly_linked_list')
os.system('clear')


class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = len(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if len(self.storage) > 0:
            removed = self.storage.remove_from_tail()
            self.size = len(self.storage)
            return removed

    def len(self):
        return len(self.storage)
