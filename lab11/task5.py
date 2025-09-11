from collections import deque

class Graph:
    """
    Graph represented using an adjacency list.
    Supports BFS, iterative DFS, and recursive DFS traversals.
    """
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        """
        Adds an edge from src to dest. Assumes undirected graph.
        """
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def bfs(self, start):
        """
        Breadth-First Search traversal from the start node.
        """
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Add unvisited neighbors to the queue
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs_iterative(self, start):
        """
        Depth-First Search using an explicit stack (iterative).
        """
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Add neighbors in reverse to maintain order
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def dfs_recursive(self, start):
        """
        Depth-First Search using recursion.
        """
        visited = set()
        result = []

        def _dfs(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list.get(node, []):
                    _dfs(neighbor)

        _dfs(start)
        return result

# 🔍 Test Block
g = Graph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'),
    ('C', 'E'), ('D', 'F'), ('E', 'F')
]
for src, dest in edges:
    g.add_edge(src, dest)

print("Adjacency List:", g.adj_list)
print("BFS from A:", g.bfs('A'))
print("Iterative DFS from A:", g.dfs_iterative('A'))
print("Recursive DFS from A:", g.dfs_recursive('A'))