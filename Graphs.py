"""
Graphs Module


This program implements 8 different types of graphs using two
representations: adjacency matrices and adjacency linked lists.

All graphs are restricted to 5 nodes (0..4). Edges may be unweighted or
weighted (weights 0..10), and graphs may be directed or undirected.

Implemented Graph Types:
1. Unweighted & Undirected - Adjacency Matrix
2. Unweighted & Undirected - Adjacency Linked List
3. Weighted & Undirected   - Adjacency Matrix
4. Weighted & Undirected   - Adjacency Linked List
5. Unweighted & Directed   - Adjacency Matrix
6. Unweighted & Directed   - Adjacency Linked List
7. Weighted & Directed     - Adjacency Matrix
8. Weighted & Directed     - Adjacency Linked List

Traversal Methods:
- BFS (Breadth First Search)
- DFS (Depth First Search)


Author: <Taran Kalle>
Date: <8/31/2025>
"""


nNodes = 5
minNode, maxNode = 0, nNodes - 1
minW, maxW = 0, 10


def validNode(n):
    return minNode <= n <= maxNode


def validWeight(w):
    return minW <= w <= maxW



class Node:
    """
    Represents a single node in a singly linked list.

    @param value: any - The data stored in this node.
    @return Node - A new linked list node with value set.
    Attributes:
        value (any): The stored data.
        next (Node|None): Reference to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A minimal singly linked list used to represent adjacency lists."""

    def __init__(self):
        self.head = None

    def __iter__(self):
        """
        Iterate over all values in the linked list.

        @return Iterator - Iterator yielding values in the list.
        """
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def appendNode(self, value):
        """
        Append a new node with the given value to the end of the list.

        @param value: any - Value to append.
        @return None
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def contains(self, value):
        """
        Check if the list contains a node with the given value.

        @param value: any - Value to search for.
        @return bool - True if found, False otherwise.
        """
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def addUnique(self, value):
        """
        Add a new node only if the value is not already present.

        @param value: any - Value to add.
        @return None
        """
        if not self.contains(value):
            self.appendNode(value)

    def addOrReplace(self, matchPred, newValue):
        """
        Replace the first node value matching matchPred or append if none.

        @param matchPred: Callable - Predicate function to match values.
        @param newValue: any - Value to insert or replace.
        @return None
        """
        cur = self.head
        while cur is not None:
            if matchPred(cur.value):
                cur.value = newValue
                return
            cur = cur.next
        self.appendNode(newValue)

    def removeIf(self, matchPred):
        """
        Remove all nodes whose values satisfy the given predicate.

        @param matchPred: Callable - Predicate function to match values.
        @return None
        """
        prev = None
        cur = self.head
        while cur is not None:
            if matchPred(cur.value):
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next



class UUAdjMatrix:
    """Unweighted & Undirected graph represented with an adjacency matrix."""

    def __init__(self):
        self.mat = [[0] * nNodes for _ in range(nNodes)]

    def addEdge(self, n1, n2):
        """
        Add an undirected edge between n1 and n2.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @return bool - True if added, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.mat[n1][n2] = 1
        self.mat[n2][n1] = 1
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the undirected edge between n1 and n2.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @return bool - True if removed, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.mat[n1][n2] = 0
        self.mat[n2][n1] = 0
        return True

    def displayGraph(self):
        """
        Print the adjacency matrix in a readable format.

        @return None
        """
        header = "    " + " ".join(f"{i:>2}" for i in range(nNodes))
        print(header)
        for i in range(nNodes):
            row = " ".join(f"{self.mat[i][j]:>2}" for j in range(nNodes))
            print(f"{i:>2}: {row}")

    def bfs(self, source):
        """
        Perform a breadth-first traversal from the source node.

        @param source: int - Starting node index.
        @return list[int] - Order of nodes visited.
        """
        if not validNode(source):
            return []
        visited = [False] * nNodes
        order = []
        queue = [source]
        visited[source] = True
        while queue:
            u = queue.pop(0)  # small fixed size; OK without imports
            order.append(u)
            for v in range(nNodes):
                if self.mat[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print("BFS:", order)
        return order

    def dfs(self, source):
        """
        Perform a depth-first traversal from the source node.

        @param source: int - Starting node index.
        @return list[int] - Order of nodes visited.
        """
        if not validNode(source):
            return []
        visited = [False] * nNodes
        order = []
        stack = [source]
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                order.append(u)
                for v in range(nNodes - 1, -1, -1):
                    if self.mat[u][v] == 1 and not visited[v]:
                        stack.append(v)
        print("DFS:", order)
        return order



class UUAdjList:
    """Unweighted & Undirected graph via linked-list adjacency lists."""

    def __init__(self):
        self.adj = [LinkedList() for _ in range(nNodes)]

    def addEdge(self, n1, n2):
        """
        Add an undirected edge between n1 and n2.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @return bool - True if added, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.adj[n1].addUnique(n2)
        self.adj[n2].addUnique(n1)
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the undirected edge between n1 and n2.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @return bool - True if removed, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.adj[n1].removeIf(lambda x: x == n2)
        self.adj[n2].removeIf(lambda x: x == n1)
        return True

    def displayGraph(self):
        """
        Print adjacency lists for each node.

        @return None
        """
        for i in range(nNodes):
            neighbors = sorted(list(self.adj[i]))
            print(f"{i}: [" + ", ".join(map(str, neighbors)) + "]")

    def bfs(self, source):
        """
        Perform a breadth-first traversal from the source node.

        @param source: int - Starting node index.
        @return list[int] - Order of nodes visited.
        """
        if not validNode(source):
            return []
        visited = [False] * nNodes
        order = []
        queue = [source]
        visited[source] = True
        while queue:
            u = queue.pop(0)
            order.append(u)
            for v in sorted(list(self.adj[u])):
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print("BFS:", order)
        return order

    def dfs(self, source):
        """
        Perform a depth-first traversal from the source node.

        @param source: int - Starting node index.
        @return list[int] - Order of nodes visited.
        """
        if not validNode(source):
            return []
        visited = [False] * nNodes
        order = []
        stack = [source]
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                order.append(u)
                for v in sorted(list(self.adj[u]), reverse=True):
                    if not visited[v]:
                        stack.append(v)
        print("DFS:", order)
        return order



class WUAdjMatrix:
    """
    Weighted & Undirected graph represented with an adjacency matrix.

    Each matrix entry stores a weight (int) or None if no edge exists.
    """

    def __init__(self):
        self.mat = [[None] * nNodes for _ in range(nNodes)]

    def addEdge(self, n1, n2, w1, w2):
        """
        Add an undirected edge with weight w1 (n1→n2) and w2 (n2→n1).

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @param w1: int - Weight for n1→n2.
        @param w2: int - Weight for n2→n1.
        @return bool - True if added, False if invalid.
        """

        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        if not (validWeight(w1) and validWeight(w2)):
            return False
        self.mat[n1][n2] = w1
        self.mat[n2][n1] = w2
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the undirected edge between n1 and n2.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @return bool - True if removed, False if invalid.
        """

        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.mat[n1][n2] = None
        self.mat[n2][n1] = None
        return True

    def displayGraph(self):
        """
        Print the weighted adjacency matrix in a readable format.

        @return None
        """

        header = "    " + " ".join(f"{i:>3}" for i in range(nNodes))
        print(header)
        for i in range(nNodes):
            row = " ".join(f"{(self.mat[i][j] if self.mat[i][j] is not None else '.')!s:>3}" for j in range(nNodes))
            print(f"{i:>2}: {row}")



class WUAdjList:
    """Weighted & Undirected graph represented with linked-list adjacency.

    Each adjacency list node stores a tuple (neighbor, weight).
    """

    def __init__(self):
        self.adj = [LinkedList() for _ in range(nNodes)]

    def addEdge(self, n1, n2, w1, w2):
        """
        Add an undirected edge with given weights in both directions.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @param w1: int - Weight for n1→n2.
        @param w2: int - Weight for n2→n1.
        @return bool - True if added, False if invalid.
        """

        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        if not (validWeight(w1) and validWeight(w2)):
            return False
        self.adj[n1].addOrReplace(lambda t: t[0] == n2, (n2, w1))
        self.adj[n2].addOrReplace(lambda t: t[0] == n1, (n1, w2))
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the undirected edge between n1 and n2.

        @param n1: int - First node index.
        @param n2: int - Second node index.
        @return bool - True if removed, False if invalid.
        """

        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.adj[n1].removeIf(lambda t: t[0] == n2)
        self.adj[n2].removeIf(lambda t: t[0] == n1)
        return True

    def displayGraph(self):
        """
        Print adjacency lists with neighbors and weights.

        @return None
        """

        for i in range(nNodes):
            items = sorted(list(self.adj[i]), key=lambda t: t[0])
            parts = [f"{v}(w={w})" for (v, w) in items]
            print(f"{i}: [" + ", ".join(parts) + "]")



class UDAdjMatrix:
    """Unweighted & Directed graph via adjacency matrix (0/1 for u→v)."""

    def __init__(self):
        self.mat = [[0] * nNodes for _ in range(nNodes)]

    def addEdge(self, n1, n2):
        """
        Add a directed edge from n1 to n2.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @return bool - True if added, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.mat[n1][n2] = 1
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the directed edge from n1 to n2.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @return bool - True if removed, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.mat[n1][n2] = 0
        return True

    def displayGraph(self):
        """
        Print the adjacency matrix in a readable format.

        @return None
        """
        header = "    " + " ".join(f"{i:>2}" for i in range(nNodes))
        print(header)
        for i in range(nNodes):
            row = " ".join(f"{self.mat[i][j]:>2}" for j in range(nNodes))
            print(f"{i:>2}: {row}")



class UDAdjList:
    """
    Unweighted & Directed graph represented with linked-list adjacency.

    Each adjacency list node stores an outbound neighbor.
    """

    def __init__(self):
        self.adj = [LinkedList() for _ in range(nNodes)]

    def addEdge(self, n1, n2):
        """
        Add a directed edge from n1 to n2.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @return bool - True if added, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.adj[n1].addUnique(n2)
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the directed edge from n1 to n2.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @return bool - True if removed, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.adj[n1].removeIf(lambda x: x == n2)
        return True

    def displayGraph(self):
        """
        Print adjacency lists for each node.

        @return None
        """
        for i in range(nNodes):
            neighbors = sorted(list(self.adj[i]))
            print(f"{i} -> [" + ", ".join(map(str, neighbors)) + "]")



class WDAdjMatrix:
    """
    Weighted & Directed graph represented with an adjacency matrix.

    Each entry is either a weight (int) or None if no edge exists.
    """

    def __init__(self):
        self.mat = [[None] * nNodes for _ in range(nNodes)]

    def addEdge(self, n1, n2, w):
        """
        Add a directed edge from n1 to n2 with weight w.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @param w: int - Weight of the edge.
        @return bool - True if added, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2 or not validWeight(w):
            return False
        self.mat[n1][n2] = w
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the directed edge from n1 to n2.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @return bool - True if removed, False if invalid.
        """
        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.mat[n1][n2] = None
        return True

    def displayGraph(self):
        """
        Print the weighted adjacency matrix in a readable format.

        @return None
        """
        header = "    " + " ".join(f"{i:>3}" for i in range(nNodes))
        print(header)
        for i in range(nNodes):
            row = " ".join(f"{(self.mat[i][j] if self.mat[i][j] is not None else '.')!s:>3}" for j in range(nNodes))
            print(f"{i:>2}: {row}")



class WDAdjList:
    """
    Weighted & Directed graph represented with linked-list adjacency.

    Each adjacency list node stores a tuple (neighbor, weight).
    """

    def __init__(self):
        self.adj = [LinkedList() for _ in range(nNodes)]

    def addEdge(self, n1, n2, w):
        """
        Add a directed edge from n1 to n2 with weight w.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @param w: int - Weight of the edge.
        @return bool - True if added, False if invalid.
        """

        if not (validNode(n1) and validNode(n2)) or n1 == n2 or not validWeight(w):
            return False
        self.adj[n1].addOrReplace(lambda t: t[0] == n2, (n2, w))
        return True

    def removeEdge(self, n1, n2):
        """
        Remove the directed edge from n1 to n2.

        @param n1: int - Start node index.
        @param n2: int - End node index.
        @return bool - True if removed, False if invalid.
        """

        if not (validNode(n1) and validNode(n2)) or n1 == n2:
            return False
        self.adj[n1].removeIf(lambda t: t[0] == n2)
        return True

    def displayGraph(self):
        """
        Print adjacency lists with neighbors and weights.

        @return None
        """
        for i in range(nNodes):
            items = sorted(list(self.adj[i]), key=lambda t: t[0])
            parts = [f"{v}(w={w})" for (v, w) in items]
            print(f"{i} -> [" + ", ".join(parts) + "]")


# Demonstrations
if __name__ == "__main__":
    print("=== Unweighted Undirected (Matrix) ===")
    g1 = UUAdjMatrix()
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(3, 4)
    g1.displayGraph()
    g1.bfs(0)
    g1.dfs(0)

    print("=== Unweighted Undirected (Adjacency Linked Lists) ===")
    g2 = UUAdjList()
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    g2.addEdge(3, 4)
    g2.displayGraph()
    g2.bfs(0)
    g2.dfs(0)

    print("=== Weighted Undirected (Matrix) ===")
    g3 = WUAdjMatrix()
    g3.addEdge(0, 1, 3, 3)
    g3.addEdge(1, 2, 5, 4)
    g3.displayGraph()

    print("=== Weighted Undirected (Adjacency Linked Lists) ===")
    g4 = WUAdjList()
    g4.addEdge(0, 1, 2, 2)
    g4.addEdge(0, 2, 7, 1)
    g4.displayGraph()

    print("=== Unweighted Directed (Matrix) ===")
    g5 = UDAdjMatrix()
    g5.addEdge(0, 1)
    g5.addEdge(1, 2)
    g5.addEdge(2, 0)
    g5.displayGraph()

    print("=== Unweighted Directed (Adjacency Linked Lists) ===")
    g6 = UDAdjList()
    g6.addEdge(0, 3)
    g6.addEdge(0, 4)
    g6.addEdge(4, 1)
    g6.displayGraph()

    print("=== Weighted Directed (Matrix) ===")
    g7 = WDAdjMatrix()
    g7.addEdge(0, 4, 9)
    g7.addEdge(4, 2, 6)
    g7.displayGraph()

    print("=== Weighted Directed (Adjacency Linked Lists) ===")
    g8 = WDAdjList()
    g8.addEdge(1, 3, 8)
    g8.addEdge(1, 4, 5)
    g8.addEdge(3, 2, 1)
    g8.displayGraph()
