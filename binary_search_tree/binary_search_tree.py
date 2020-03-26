
import os
import sys
sys.path.append('../queue_and_stack')
os.system("clear")


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if the value is less than value in current leaf
        if value < self.value:
            # and if there's no leaf to the left
            if self.left == None:
                # make one with the new value
                self.left = BinarySearchTree(value)
            else:
                # else call insert on the leaf to the left
                self.left.insert(value)

        # if the value is >= value in current leaf
        else:
            # and if if there's no leaf to the right
            if self.right == None:
                # make one with the new value
                self.right = BinarySearchTree(value)
            else:
                # else call insert on the leaf to the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target matches the value in the current leaf
        # return true
        if target == self.value:
            return True

        # if the target is less than the value  in the current leaf
        if target < self.value:
            # and there is no leaf to the left, return false
            if self.left == None:
                return False
            # else call contains on the leaf to the left
            else:
                return self.left.contains(target)

        # if the target is >= to the value in the current leaf
        else:
            # and there is no leaf to the right, return false
            if self.right == None:
                return False
            # else call contains on the leaf to the right
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # just keep checking the right-most leaves until the
        # there are no more right-most leaves, and return the
        # value at the leaf you stopped at
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # USE QUEUE
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # USE STACK
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)

bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.left.right.value)  # 3
print(bst.right.left.value)  # 6

# Stretchy Stretch
# airport heap problem


# NOTE: From Lecture
# O -> worst case
# Theta --> best case?

# O traversing --> n
# Theta traversing --> ????? log(n)


# traversal has to go through all nodes
# search doesn't


# breadth --> layer by layer, or width
