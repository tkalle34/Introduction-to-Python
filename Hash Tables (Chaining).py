import random


class Node:
    """
    Node for singly linked list storing a key-value pair.
    """
    def __init__(self, key, value, next=None):
        """
        Initialize a Node with key, value, and pointer to next node.

        @param key: The key of the node
        @param value: The value associated with the key
        @param next: Reference to the next node (default None)
        """
        self.key = key
        self.value = value
        self.next = next


class LinkedList:
    """
    Singly linked list to hold nodes of key-value pairs.
    Used for chaining in the hash table.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def find(self, key):
        """
        Search for a node with the given key.

        @param key: Key to search for
        @return: Node with matching key or None if not found
        """
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def insert(self, key, value):
        """
        Insert a key-value pair into the list. Update value if key exists.

        @param key: Key to insert or update
        @param value: Value associated with the key
        """
        node = self.find(key)
        if node:
            node.value = value  # update existing key
        else:
            new_node = Node(key, value, self.head)
            self.head = new_node

    def delete(self, key):
        """
        Delete the node with the specified key from the list.

        @param key: Key of the node to delete
        @return: True if node was deleted, False if key not found
        """
        prev = None
        current = self.head
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def items(self):
        """
        Generator to iterate over all key-value pairs in the list.

        @return: Yields tuples of (key, value)
        """
        current = self.head
        while current:
            yield current.key, current.value
            current = current.next


class UniversalHash:
    """
    Universal hash function for hashing keys to indices.
    Uses parameters a, b with a large prime modulus.
    """
    def __init__(self, size):
        """
        Initialize the universal hash function.

        @param size: The size of the hash table (number of buckets)
        """
        self.size = size
        self.p = 109345121  # A large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash(self, key):
        """
        Compute the hash value for the given key.

        @param key: The key to be hashed (int or str)
        @return: Hash index in the range [0, size-1]
        """
        # Convert key to an integer if it's a string
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        return ((self.a * key + self.b) % self.p) % self.size


class HashTableChaining:
    """
    Hash Table implementation using chaining for collision resolution.
    Stores key-value pairs in linked lists at each bucket.
    Supports insert, delete, search, and dynamic resizing.
    """
    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        """
        Initialize the hash table.

        @param initial_capacity: Initial number of buckets (default 8)
        @param load_factor_threshold: Load factor threshold to trigger resizing (default 0.75)
        """
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        self.table = [LinkedList() for _ in range(self.capacity)]
        self.hash_func = UniversalHash(self.capacity)

    def _resize(self):
        """
        Resize the hash table by doubling its capacity.
        Rehash all existing key-value pairs into the new table.
        """
        old_table = self.table
        self.capacity *= 2
        self.table = [LinkedList() for _ in range(self.capacity)]
        self.hash_func = UniversalHash(self.capacity)
        self.size = 0

        for bucket in old_table:
            for key, value in bucket.items():
                self.insert(key, value)

    def insert(self, key, value):
        """
        Insert or update the value associated with the key.

        @param key: Key to insert/update
        @param value: Value to associate with the key
        """
        if (self.size + 1) / self.capacity > self.load_factor_threshold:
            self._resize()

        idx = self.hash_func.hash(key)
        bucket = self.table[idx]
        node = bucket.find(key)
        if node is None:
            self.size += 1
        bucket.insert(key, value)

    def delete(self, key):
        """
        Delete the key-value pair with the given key from the table.

        @param key: Key to delete
        @return: True if deleted, False if key not found
        """
        idx = self.hash_func.hash(key)
        bucket = self.table[idx]
        deleted = bucket.delete(key)
        if deleted:
            self.size -= 1
        return deleted

    def search(self, key):
        """
        Search for the value associated with the key.

        @param key: Key to search for
        @return: The value if key found, otherwise None
        """
        idx = self.hash_func.hash(key)
        bucket = self.table[idx]
        node = bucket.find(key)
        if node:
            return node.value
        return None


ht = HashTableChaining()

ht.insert("apple", 10)
ht.insert("banana", 20)
print(ht.search("apple"))  # Output: 10
print(ht.search("banana")) # Output: 20

ht.delete("apple")
print(ht.search("apple"))  # Output: None
