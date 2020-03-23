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

    def remove(self, value):
        removed_value = None

        # if the list is empty
        if self.head == None:
            return False
        # if there's only one node in the list
        if self.head == self.tail and self.head.value == value:
            removed_value = self.tail.value
            self.head = None
            self.tail = None

        # if value is at head
        if self.head.value == value:
            removed_value = self.head.value
            self.head = self.head.next
            return removed_value

        # if the value may be past the head
        prev_node = self.head
        curr_node = self.head.next

        while curr_node != None:
            if curr_node.value == value:
                removed_value = curr_node.value
                self.head.next = self.head.next.next
                return removed_value
            prev_node = curr_node
            curr_node = curr_node.next

        return False

    def __str__(self):
        list_str = ""
        curr_node = self.head

        while curr_node != None:
            list_str += f"[{curr_node}] -> "
            curr_node = curr_node.next

        list_str += 'None'
        return list_str
