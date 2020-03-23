from doubly_linked_list import DoublyLinkedList
import sys
import os
sys.path.append('../doubly_linked_list')
os.system('clear')


'''
### Queues∫
 * Should have the methods: `enqueue`, `dequeue`, and `len`.
   * `enqueue` should add an item to the back of the queue.
   * `dequeue` should remove and return an item from the front of the queue.
   * `len` returns the number of items in the queue.
 
![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)
'''


class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = len(self.storage)

    def dequeue(self):
        if len(self.storage) > 0:
            removed = self.storage.remove_from_head()
            self.size = len(self.storage)
            return removed

    def len(self):
        return len(self.storage)
