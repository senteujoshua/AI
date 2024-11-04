from collections import deque

class Graph:
    def __init__(self, edges):
        self.graph = {}
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
            
            if end in self.graph:
                self.graph[end].append(start)
            else:
                self.graph[end] = [start]

    def bfs_shortest_path(self, start, end):
        if start == end:
            return [start]
        
        # Queue for BFS
        queue = deque([[start]])
        visited = set()
        
        while queue:
            # Get the first path in the queue
            path = queue.popleft()
            node = path[-1]
            
            # Check if node has been visited
            if node not in visited:
                neighbors = self.graph.get(node, [])
                
                # Explore each neighbor
                for neighbor in neighbors:
                    new_path = list(path) + [neighbor]
                    queue.append(new_path)
                    
                    # Return path if neighbor is the end
                    if neighbor == end:
                        return new_path
                
                # Mark node as visited
                visited.add(node)
        
        return None  # No path found if we reach here

if __name__ == "__main__":
    # Define edges as pairs of nodes
    edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"),
        ("D", "F"), ("E", "F"), ("F", "G")
    ]
    
    graph = Graph(edges)
    start_node = "A"
    end_node = "G"
    
    path = graph.bfs_shortest_path(start_node, end_node)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")
