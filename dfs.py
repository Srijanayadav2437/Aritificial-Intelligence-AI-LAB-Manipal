# Function for Depth-First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize visited nodes set
    visited.add(start)
    print(start, end=' ')
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Taking graph input from the user
def get_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    for i in range(vertices):
        vertex = int(input(f"Enter vertex {i + 1}: "))  # Input vertex as an integer
        neighbors = list(map(int, input(f"Enter the neighbors of {vertex} separated by space: ").split()))  # Input neighbors as integers
        graph[vertex] = neighbors
    return graph

if __name__ == "__main__":
    graph = get_graph()
    start_node = int(input("Enter the start node: "))  # Input start node as an integer
    
    print("\nDFS traversal:")
    dfs(graph, start_node)
