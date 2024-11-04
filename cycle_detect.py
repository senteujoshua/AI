from collections import deque, defaultdict

class Graph:
    def __init__(self, edges):
        # Build an adjacency list
        self.graph = defaultdict(list)
        for start, end in edges:
            self.graph[start].append(end)
            self.graph[end].append(start)

    def has_cycle(self):
        visited = set()

        # Check each component of the graph (for disconnected graphs)
        for node in self.graph:
            if node not in visited:
                if self.bfs_cycle_check(node, visited):
                    return True
        return False

    def bfs_cycle_check(self, start, visited):
        # Queue for BFS; store (node, parent) tuples
        queue = deque([(start, None)])
        visited.add(start)

        while queue:
            node, parent = queue.popleft()

            # Explore neighbors
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    # Mark neighbor as visited and add to the queue
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # If neighbor is visited and not parent, we found a cycle
                    return True
        return False

if __name__ == "__main__":
    # Define edges as pairs of nodes
    edges_with_cycle = [
        ("A", "B"), ("B", "C"), ("C", "D"), ("D", "B"), ("E", "F")
    ]
    
    edges_without_cycle = [
        ("A", "B"), ("B", "C"), ("C", "D"), ("E", "F")
    ]

    graph_with_cycle = Graph(edges_with_cycle)
    graph_without_cycle = Graph(edges_without_cycle)
    
    print("Graph with cycle has a cycle:", graph_with_cycle.has_cycle())  # Expected: True
    print("Graph without cycle has a cycle:", graph_without_cycle.has_cycle())  # Expected: False
