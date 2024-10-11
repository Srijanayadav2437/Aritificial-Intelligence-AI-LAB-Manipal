from collections import deque

# Function for Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    
    while queue:
        vertex = queue.popleft()  # Get the vertex from the front of the queue
        if vertex not in visited:
            print(vertex, end=' ')  # Process the current node (e.g., print it)
            visited.add(vertex)  # Mark it as visited
            # Add all unvisited neighbors to the queue
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

# Taking graph input from the user
def get_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))  # Number of vertices
    for i in range(vertices):
        vertex = input(f"Enter the vertex {i + 1}: ").strip()  # Input vertex name as string
        neighbors = input(f"Enter the neighbors of {vertex} separated by space: ").strip().split()
        graph[vertex] = neighbors  # Add neighbors for the vertex as strings
    return graph

if __name__ == "__main__":
    graph = get_graph()  # Build the graph
    start_node = input("Enter the start node: ").strip()  # Input the start node for BFS
    
    print("\nBFS traversal:")
    bfs(graph, start_node)  # Call the BFS function
