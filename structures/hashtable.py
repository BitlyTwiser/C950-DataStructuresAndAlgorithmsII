"""
Note object for linked list used in hashtable
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    # Constructor hash table
    def __init__(self):
        # Static capacity value for hashing.
        self.capacity = 40
        self.size = 0
        self.buckets = [None]

    # Dynamically self adjusts the data structure to extend the quantity of "buckets" to place data within
    def _adjust_hash_table_size(self, extend_value):
        self.buckets.extend([None] * extend_value)

    """
     Private method for generating a hash for a given key using native python hashing method.
     O(N)
    """
    def _hash(self, key):
        return hash(key)

    """
     Insert a key,value pair to the hashmap OR update value found.
     The add method is self modifying as it will alter elements in the linked list if the keys of the
     input value match a key of an existing element.
     O(N)
    """
    def add(self, key, value):
        self.size += 1

        index = self._hash(key)
        if index >= len(self.buckets):
            self._adjust_hash_table_size(index+1)

        node = self.buckets[index]
        # Add to head of list of node is none
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        # Insert onto tail of linked list within bucket OR update element if found in linked list.
        while node is not None:
            # Checks if found node has same key and updates element if this is the case.
            if node.key == key:
                node.value = value
                node = node.next
            else:
                prev = node
                node = node.next
                prev.next = Node(key, value)

    """
     Find given key value in linked list.
     O(N)
    """
    def get(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    """
     Remove given element from hash
     O(N)
    """

    def delete(self, key):
        # 1. Compute hash
        index = self._hash(key)
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
