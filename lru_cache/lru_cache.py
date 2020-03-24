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
        self.cache = DoublyLinkedList()
        self.cache_lookup = dict()
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
        if key in self.cache_lookup:
            node = self.cache_lookup[key]
            self.cache.move_to_front(node)
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
        # if the key already exists in the cache_lookup O(n) -_- ??
        if key in self.cache_lookup:
            # delete the node from the cache
            cached_node = self.cache_lookup[key]
            self.cache.delete(cached_node)
            # add a new node to the head of the cache
            self.cache.add_to_head(value)
            # udate the value for the cache_lookup entry
            self.cache_lookup[key] = self.cache.head
        else:
            # add the node to the head
            self.cache.add_to_head(value)
            # create a key-value pair entry in the cache_lookup
            self.cache_lookup[key] = self.cache.head

        # and if the size of the cache has reached it's limit
        if len(self.cache) > self.limit:
            # remove the node from the tail
            self.cache.remove_from_tail()
            # TODO: should I also remove the key-value pair from the cache-lookup


cache = LRUCache()

cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.set('item2', 'z')

print(cache.get('item1'))
print(cache.get('item2'))


def test_cache_overwrite_appropriately(self):
    self.cache.set('item1', 'a')
    self.cache.set('item2', 'b')
    self.cache.set('item3', 'c')

    self.cache.set('item2', 'z')

    self.assertEqual(self.cache.get('item1'), 'a')
    self.assertEqual(self.cache.get('item2'), 'z')


def test_cache_insertion_and_retrieval(self):
    self.cache.set('item1', 'a')
    self.cache.set('item2', 'b')
    self.cache.set('item3', 'c')

    self.assertEqual(self.cache.get('item1'), 'a')
    self.cache.set('item4', 'd')

    self.assertEqual(self.cache.get('item1'), 'a')
    self.assertEqual(self.cache.get('item3'), 'c')
    self.assertEqual(self.cache.get('item4'), 'd')
    self.assertIsNone(self.cache.get('item2'))


def test_cache_nonexistent_retrieval(self):
    self.assertIsNone(self.cache.get('nonexistent'))
