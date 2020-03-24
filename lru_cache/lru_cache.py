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
        # if the key is in the cache
        if key in self.cache:
            # move it's node to the front of the storage
            node = self.cache[key]
            self.storage.move_to_front(node)
            # set the value of the key to the node
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
        # if the key already exists in the cache O(n) -_- ??
        if key in self.cache:
            # delete the node from the cache
            cached_node = self.cache[key]
            self.storage.delete(cached_node)

        else:
            self.count += 1

        # add a new node to the head of the cache
        self.storage.add_to_head(value)
        # udate the value for the cache entry
        self.cache[key] = self.storage.head

        # and if the size of the cache has reached it's limit
        if self.count > self.limit:
            # remove the node from the tail
            removed_node = self.storage.remove_from_tail()

            # remove the entry from the cache
            for k, v in self.cache.items():
                if v.value == removed_node:
                    self.cache[k].value = None

# these are bad comments
