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
            node.value = value  # Update existing key's value
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
        self.p = 109345121  # Large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash(self, key):
        """
        Compute the hash value for the given key.

        @param key: The key to be hashed (int or str)
        @return: Hash index in the range [0, size-1]
        """
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        return ((self.a * key + self.b) % self.p) % self.size


class HashTableOpenAddressing:
    """
    Hash Table implementation using open addressing with linear probing.
    Stores key-value pairs directly in an array.
    Supports insert, delete, search, and dynamic resizing.
    """

    _deleted = object()  # Sentinel to mark deleted slots

    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        """
        Initialize the hash table.

        @param initial_capacity: Initial size of the table (default 8)
        @param load_factor_threshold: Load factor threshold to trigger resizing (default 0.75)
        """
        self.capacity = initial_capacity
        self.size = 0  # Number of active key-value pairs
        self.load_factor_threshold = load_factor_threshold
        self.table = [None] * self.capacity
        self.hash_func = UniversalHash(self.capacity)

    def _resize(self):
        """
        Resize the hash table by doubling its capacity.
        Rehash all active key-value pairs into the new table.
        """
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.hash_func = UniversalHash(self.capacity)
        self.size = 0

        for entry in old_table:
            if entry is not None and entry is not self._deleted:
                key, value = entry
                self.insert(key, value)

    def _probe(self, key):
        """
        Generator to yield indices in the table for a given key using linear probing.

        @param key: The key to find slots for
        @yield: Next index to try for insertion/search/deletion
        """
        start_idx = self.hash_func.hash(key)
        idx = start_idx

        while True:
            yield idx
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break  # Full cycle completed

    def insert(self, key, value):
        """
        Insert or update the key-value pair in the hash table.
        Resize if load factor threshold is exceeded.

        @param key: Key to insert/update
        @param value: Value to associate with the key
        """
        if (self.size + 1) / self.capacity > self.load_factor_threshold:
            self._resize()

        first_deleted_idx = None

        for idx in self._probe(key):
            slot = self.table[idx]

            if slot is None:
                # Insert here if no previous deleted slot found
                insert_idx = first_deleted_idx if first_deleted_idx is not None else idx
                self.table[insert_idx] = (key, value)
                self.size += 1
                return

            elif slot is self._deleted:
                # Remember the first deleted slot found for potential insertion
                if first_deleted_idx is None:
                    first_deleted_idx = idx

            else:
                existing_key, _ = slot
                if existing_key == key:
                    # Update existing key's value
                    self.table[idx] = (key, value)
                    return
        # If exit loop, table is full (should not happen because of resizing)
        raise RuntimeError("HashTable full, insertion failed")

    def search(self, key):
        """
        Search for the value associated with the given key.

        @param key: Key to search for
        @return: Value if found, otherwise None
        """
        for idx in self._probe(key):
            slot = self.table[idx]

            if slot is None:
                # Key not found if we hit an empty slot
                return None

            elif slot is self._deleted:
                continue

            else:
                existing_key, value = slot
                if existing_key == key:
                    return value
        return None

    def delete(self, key):
        """
        Delete the key-value pair associated with the key.

        @param key: Key to delete
        @return: True if deletion succeeded, False if key not found
        """
        for idx in self._probe(key):
            slot = self.table[idx]

            if slot is None:
                # Key not found
                return False

            elif slot is self._deleted:
                continue

            else:
                existing_key, _ = slot
                if existing_key == key:
                    self.table[idx] = self._deleted
                    self.size -= 1
                    return True
        return False


ht = HashTableOpenAddressing()

ht.insert("apple", 10)
ht.insert("banana", 20)
print(ht.search("apple"))   # Output: 10
print(ht.search("banana"))  # Output: 20

ht.delete("apple")
print(ht.search("apple"))   # Output: None
