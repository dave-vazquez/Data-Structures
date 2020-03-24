from doubly_linked_list import DoublyLinkedList
import os
os.system('clear')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.cache = dict()
        self.limit = limit
        self.count = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if the key is in the cache, O(n) -_- ??
        if key in self.cache:
            # move it's node to the storage head as
            # the most recently used entry
            node = self.cache[key]
            self.storage.move_to_front(node)
            # and return the value
            return node.value

        return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if the key is in the cache, O(n) -_- ??
        if key in self.cache:
            # delete the node from the storage
            cached_node = self.cache[key]
            self.storage.delete(cached_node)
            # and add the value to the storage head as
            # the most recently used entry
            self.storage.add_to_head(value)

        else:
            # or just add the value to the storage head as
            # the most recently used entry
            self.storage.add_to_head(value)
            # increment
            self.count += 1

        # update the value in the cache to the head
        self.cache[key] = self.storage.head

        # and if the size of the cache has reached it's limit
        if self.count > self.limit:
            # remove the node from the tail
            removed_node = self.storage.remove_from_tail()

            # change the value in the cache to None, O(n) -_- ??
            for k, v in self.cache.items():
                if v.value == removed_node:
                    self.cache[k].value = None

            self.count -= 1


# QUESTION: Because a dictionary (cache look-up) is not a true hash table, the RTC is O(n)
# So if we never delete entries from the dictionary (cache look-up) this cache will grow
# and grow and grow.. defeating the whole purpose of fast access to recently used data

# the tests demand that you don't delete cache entries... so like, what gives??????

# maybe I'm not understanding.
