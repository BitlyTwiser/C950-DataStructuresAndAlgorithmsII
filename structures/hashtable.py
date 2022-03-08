# Note for avoiding collisions and curating a linked list to use for the hashtable
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self)


# Hash table with separate chaining
class HashMap:
    # Initialize hash table
    def __init__(self):
        # Capacity for internal array denoting the initial allotment of values for the delivery system
        self.capacity = 40
        self.size = 0
        self.buckets = [None] * self.capacity

    # Generate a hash for a given key
    # Input:  key - string
    # Output: Index from 0 to self.capacity
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    # Insert a key,value pair to the hashmap
    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    # Find given key value in linked list.
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    # Remove given element from linked list.
    def remove(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            # Delete  element from linked list
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            # Return the removed element
            return result
