

class Node:
    """
    Represents a node in the Binary Search Tree.

    @param value: int - The integer value stored in the node.
    """

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree implementation with common operations.
    Maintains the property: left subtree < root < right subtree.
    """

    def __init__(self):
        self.root = None

    def validateInteger(self, value):
        """
        Validate that the given value is a non-null integer.
        """
        
        if value is None or not isinstance(value, int):
            raise ValueError("Value must be a non-null integer.")

    def insert(self, value: int):
        """
        Insert a value into the BST.

        @param value: int - The value to insert.
        """
        self.validateInteger(value)

        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value == current.value:
                print("Value {0} already exists. Duplicate not "
                      "inserted.".format(value))
                return
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def search(self, value: int) -> bool:
        """
        Search for a value in the BST.

        @param value: int - The value to search.
        @return bool - True if found, else False.
        """
        self.validateInteger(value)
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value: int):
        """
        Delete a value from the BST.

        @param value: int - The value to delete.
        """
        self.validateInteger(value)
        self.root = self.deleteRecursive(self.root, value)

    def deleteRecursive(self, node, value):
        """Helper method for delete using recursion."""
        if node is None:
            return node

        if value < node.value:
            node.left = self.deleteRecursive(node.left, value)
        elif value > node.value:
            node.right = self.deleteRecursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: get inorder successor
            successorValue = self.findMin(node.right).value
            node.value = successorValue
            node.right = self.deleteRecursive(node.right, successorValue)

        return node
    
    # Traversals
    def traverseInOrder(self):
        """Print elements in in-order DFS."""
        result = []
        self.inOrder(self.root, result)
        print("In order: {0}".format(result))

    def inOrder(self, node, result):
        if node:
            self.inOrder(node.left, result)
            result.append(node.value)
            self.inOrder(node.right, result)

    def traversePreOrder(self):
        """Print elements in pre-order DFS."""
        result = []
        self.preOrder(self.root, result)
        print("Pre order: {0}".format(result))

    def preOrder(self, node, result):
        if node:
            result.append(node.value)
            self.preOrder(node.left, result)
            self.preOrder(node.right, result)

    def traversePostOrder(self):
        """Print elements in post-order DFS."""
        result = []
        self.postOrder(self.root, result)
        print("Post order: {0}".format(result))

    def postOrder(self, node, result):
        if node:
            self.postOrder(node.left, result)
            self.postOrder(node.right, result)
            result.append(node.value)

    def traverseLevelOrder(self):
        """Print elements in level-order BFS."""
        result = []
        if self.root is None:
            print("Level order: []")
            return
        queue = [self.root]  
        
        while queue:
            node = queue.pop(0)  # Remove from the front
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("Level order: {0}".format(result))


    def findMinimum(self) -> int:
        """Return the minimum value in the BST."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        return self.findMin(self.root).value


    def findMin(self, node):
        """Helper to find minimum node."""
        while node.left:
            node = node.left
        return node

    def findMaximum(self) -> int:
        """Return the maximum value in the BST."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def findSmallest(self, k: int) -> int:
        """
        Find the kth smallest element in the BST.

        @param k: int - The position (1-based).
        @return int - The kth smallest value.
        """
        if k <= 0:
            raise ValueError("k must be greater than 0.")
        elements = []
        self.inOrder(self.root, elements)
        if k > len(elements):
            raise ValueError("Tree has only {0} elements.".format(len(elements)))
        return elements[k - 1]

    def sumSmaller(self, k: int) -> int:
        """
        Sum all nodes smaller than the kth smallest element.

        @param k: int - The position (1-based).
        @return int - Sum of values smaller than kth smallest.
        """
        kth_value = self.findSmallest(k)
        elements = []
        self.inOrder(self.root, elements)
        return sum(x for x in elements if x < kth_value)


# Sample Program
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert elements
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    # Display traversals
    bst.traverseInOrder()
    bst.traversePreOrder()
    bst.traversePostOrder()
    bst.traverseLevelOrder()

    # Search elements
    print("Search 40: {0}".format(bst.search(40)))
    print("Search 90: {0}".format(bst.search(90)))

    # Find min and max
    print("Minimum: {0}".format(bst.findMinimum()))
    print("Maximum: {0}".format(bst.findMaximum()))

    # Delete elements
    bst.delete(20)
    bst.delete(50)
    bst.traverseInOrder()

    # Kth smallest and sum smaller
    print("3rd Smallest: {0}".format(bst.findSmallest(3)))
    print("Sum of elements smaller than 3rd smallest: {0}".format(bst.sumSmaller(3)))
