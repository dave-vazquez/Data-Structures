from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
            self.head = self.tail
        elif self.tail == self.head:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def contains(self, value):
        curr_node = self.head

        while curr_node != None:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next

        return False

    # def remove(self, value):
    #     curr_node = self.head
    #     prev_node = None

    #     while curr_node != None:
    #         if curr_node.value == value:
    #             return True
    #         curr_node = curr_node.next

    #     return False

    def __str__(self):
        list_str = ""
        curr_node = self.head

        while curr_node != None:
            list_str += f"[{curr_node}] -> "
            curr_node = curr_node.next

        list_str += 'None'
        return list_str
