class Node:
    def __init__(self, data: int):
        """
        Represents a node in a doubly linked list with integer data.
        @param data: int. The integer value to be stored in the node.
        @raises TypeError: If the data is not an integer
        """
        # Ensure the data is an integer
        if not isinstance(data, int):
            raise TypeError("Only integers are allowed")
        self.data = data    # Data held in the node
        self.prev = None    # Pointer to the previous node
        self.next = None    # Pointer to the next node


class DoublyLinkedList:
    """
    Implements a doubly linked list that holds integers and supports
    various operations such as insertion, deletion, traversal, and
    duplicate removal.
    """
    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the linked list is empty.
        @return: bool. True if the list is empty, False otherwise.
        """
        return self.head is None

    def insertAtBeginning(self, value: int):
        """
        Inserts a node with the given value at the end of the list.
        @param value: int. The integer to insert at the end of the list.
        """
        new_node = Node(value)
        if self.is_empty(): # If list is empty, create a node
            self.head = new_node
            return
        curr = self.head
        while curr.next:    # Traverse to the last node
            curr = curr.next
        # Append the new node at the end
        curr.next = new_node
        new_node.prev = curr

    def insertAtEnd(self, value: int):
        """
        Inserts a node with the given value at the beginning of the list.
        @param value: int. The integer to insert at the beginning of the list.
        """
        new_node = Node(value)
        if self.is_empty():     # If list is empty, create a node
            self.head = new_node
            return
        # Insert new node before the current head
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertAtPosition(self, value: int, position: int):
        """
        Inserts a node with the given value at the specified position.
        @param value: int. The integer to insert.
        @param position: int. The 1-based index at which to insert the node.
        @raises IndexError: If the position is less than 1 or beyond bounds.
        """
        if position < 1:
            raise IndexError("Position must be 1 or greater")

        new_node = Node(value)

        if position == 1:
            # Delegate to insertAtEnd method to handle head insertion
            self.insertAtEnd(value)
            return

        curr = self.head
        index = 1
        # Traverse to the node before the desired position
        while curr and index < position - 1:
            curr = curr.next
            index += 1

        if curr is None:
            raise IndexError("Position out of bounds")

        # Insert the new node between curr and curr.next
        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    def deleteAtBeginning(self):
        """
        Deletes the node at the beginning of the list.
        @raises IndexError: If the list is empty.
        """
        if self.is_empty():
            raise IndexError("List is empty")

        if self.head.next is None: # If there is only one node, delete the head
            self.head = None
        else:
            # Move head to the next node
            self.head = self.head.next
            self.head.prev = None

    def deleteAtEnd(self):
        """
        Deletes the node at the end of the list.
        @raises IndexError: If the list is empty.
        """
        if self.is_empty():
            raise IndexError("List is empty")

        if self.head.next is None: # If there is only one node, delete the head
            self.head = None
        else:
            curr = self.head
            while curr.next:    # Traverse to the last node
                curr = curr.next
            curr.prev.next = None   # Remove the last node by updating the previous node's next pointer

    def deleteAtPosition(self, position: int):
        """
        Deletes the node at the specified position.
        @param position: int. The 1-based index of the node to delete.
        @raises IndexError: If the list is empty or position is invalid.
        """
        if self.is_empty():
            raise IndexError("List is empty")

        if position < 1:
            raise IndexError("Invalid position")

        curr = self.head
        index = 1

        if position == 1:   # Special case: delete head
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return

        # Traverse to the desired node
        while curr and index < position:
            curr = curr.next
            index += 1

        if curr is None:
            raise IndexError("Position out of bounds")

        # Unlink the current node
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def traverse(self):
        """
        Traverses the list and prints its values from head to tail.
        """
        curr = self.head
        print("Forward:", end=" ")
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    def length(self):
        """
        Calculates and returns the number of nodes in the list.
        @return: int. The number of nodes in the list.
        """
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count+=1
        return count

    def get(self, position: int):
        """
        Retrieves the value at the specified position in the list.
        @param position: int. The 1-based index of the value to retrieve.
        @return: int. The value at the specified position.
        @raises IndexError: If the position is out of bounds.
        """
        curr = self.head

        if position > self.length():
            raise IndexError("Position out of bounds")

        for pos in range(1, position+1):
            if pos == position:
                return curr.data
            curr = curr.next


    def find(self, value: int):
        """
        Finds the position of the first occurrence of a value in the list.
        @param value: int. The value to search for.
        @return: int. The 1-based index of the value in the list.
        @raises ValueError: If the value is not found.
        """
        curr = self.head
        position = 1
        while curr:
            if curr.data == value:
                return position
            curr = curr.next
            position += 1
        raise ValueError("Value not found in list")

    def removeDuplicates(self):
        """
        Removes all duplicate values from the list.
        Only the first occurrence of each value is retained.
        """
        if self.is_empty():
            return

        seen = set()
        current = self.head

        while current:
            if current.data in seen:
                # Save reference to the next node before removing
                next_node = current.next

                # Unlink the duplicate node
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next

                # Move to the next node
                current = next_node
            else:
                # If it is the first time seeing this value, saves it
                seen.add(current.data)
                current = current.next



# Demonstration Program

dll = DoublyLinkedList()

dll.insertAtBeginning(60)
dll.insertAtBeginning(50)
dll.insertAtBeginning(40)
dll.insertAtBeginning(30)
dll.insertAtBeginning(10)

dll.insertAtEnd(70)
dll.traverse()

dll.insertAtPosition(20, 6)
dll.traverse()

dll.deleteAtBeginning()
dll.traverse()

dll.deleteAtEnd()
dll.traverse()

dll.deleteAtPosition(2)
dll.traverse()

print("Node count is {0}".format(dll.length()))

print("Position 2 is filled by the value {0}".format(dll.get(2)))

dll.insertAtBeginning(60)
dll.insertAtPosition(60, 5)
dll.traverse()
dll.removeDuplicates()
dll.traverse()











